using Roots
using Printf
cd(dirname(@__FILE__))
include("gmx_table_gen_exp-6_scan.jl")

# Functions for potentials, U(params..., r)
function Buck(A, B, C, r)

    return A*exp.(-B.*r) - C./(r.^6)
end

# R0 = value of r at energy minima
# ϵ = depth of potential well, which is -U(R0)

function Buck2(R0, ϵ, α, r)
    f = 1/(α-6)
    g = 6*exp.(α*(1 .- r./R0)) - α*(R0./r).^6
    return ϵ*f*g
end

function Buck2_force(R0, ϵ, α, r)
    f = 1/(α-6)
    g = -6*α*exp.(α*(1 .- r./R0)) + 6*α*(R0./r).^7
    return ϵ*f*g/R0
end

# Function whose root gives α for a Buckingham potential with parameters A, B, C
function fα(α, A, B, C)
    D = log(6*C*B^6/A)
    return 7*log(α) - α - D
end

# Compute Buck2 parameters R0, ϵ and α to match Buck(A, B, C)
function Buck2_params(A, B, C)
    # Determine interval of alpha to search (must bracket the root to avoid an error)
    a1 = 6; a2 = 20 # Approx values
    α = find_zero(α -> fα(α, A, B, C), (a1,a2), Bisection(), xatol=0, xrtol=0, maxevals=1000000)
    R0 = α/B
    ϵ = C*B^6*(α-6)/α^7
    return (R0, ϵ, α)
end

# Compute Buck1 parameters A, B and C to match Buck2(R0, ϵ, α)
function Buck1_params(R0, ϵ, α)
    A = 6*ϵ*exp(α)/(α-6)
    B = α/R0
    C = (α*ϵ*R0^6)/(α-6)
    return (A, B, C)
end

function compute_alpha2(ϵ1, ϵ2, α1)
    # Calculate a, b and c in quadratic formula
    a = ϵ2*(6-α1)
    b = ϵ1*α1*(α1-7) + 7*ϵ2*(α1-6)
    c = 6*ϵ1*α1*(7-α1)
    # Solve for higher root (α > 6)
    return α2 = (-b - sqrt(b*b - 4*a*c))/(2*a)
end

function compute_alpha2_c6_const(ϵ1, ϵ2, α1)
    return α2 = 6*α1*ϵ1/(α1*ϵ1 - ϵ2*(α1-6))
end

# Tuples of Buckingham params (A,B,C)
# Units of kJ/mol, 1/nm, (kJ/mol)*nm^6

# C-C
williamsCC4 = (3.499079E+05, 36.00, 2.376512E-03)
williamsCC7 = (2.589896E+05, 36.00, 2.112920E-03)
sjyCC = (62659.6, 30.90, 2.6811E-03)

# C-H
williamsCH4 = (3.667694E+04, 36.70, 5.230000E-04)
williamsCH7 = (4.602400E+04, 36.70, 5.355520E-04)
sjyCH = (26353.0, 34.15, 5.5441E-04)

# H-H
williamsHH4 = (1.110434E+04, 37.40, 1.142232E-04)
williamsHH7 = (1.099974E+04, 37.40, 1.351432E-04)

# Start with paramter set 7 as used in Das, Frenkel (2003)
pots = (williamsCC7, williamsCH7, williamsHH7)
#pots = (williamsCC4, williamsCH4, williamsHH4)

for shiftCC = 0.013 # 0.010:0.001:0.014
    shiftStr = @sprintf("%.3f", shiftCC)
    print("\'", shiftStr, "\'", ", ") # For use by HPC_input_gen script

    # Convert pots to R0, ϵ, α form
    pots2 = [Buck2_params(pots[i]...) for i = 1:3]
    shifts = -[shiftCC, pots2[2][2]*shiftCC/pots2[1][2], pots2[3][2]*shiftCC/pots2[1][2]]

    # Shift the potentials and recalculate α
    R0 = [pots2[i][1] for i = 1:3] # R0 unchaged
    ϵ = [pots2[i][2] + shifts[i] for i = 1:3] # ϵ shifted
    α = [compute_alpha2(pots2[i][2], ϵ[i], pots2[i][3]) for i = 1:3] # α change to maintaind 2nd deriv at R0

    new2 = [(R0[i], ϵ[i], α[i]) for i = 1:3]

    # Convert back
    newABC = [Buck1_params(new2[i]...) for i = 1:3]
    # Write tables
    write_table(newABC[1][2], joinpath("tables", "table_"*shiftStr*".xvg"))
    write_table(newABC[2][2], joinpath("tables", "table_"*shiftStr*"_C_H.xvg"))
    write_table(newABC[3][2], joinpath("tables", "table_"*shiftStr*"_H_H.xvg"))

    # Duplicate ffnonbonded_base and forcefield_base, replace parameters
    ffnonbondedIO = open("ffnonbonded_tab_base.itp", "r")
    ffnonbondedOut = open("ffnonbonded_$shiftStr.itp", "w")
    for l in eachline(ffnonbondedIO)
        l = replace(l, "CCPARAMS" => @sprintf("%-12.4E%-12.4E", newABC[1][3], newABC[1][1]))
        l = replace(l, "CHPARAMS" => @sprintf("%-12.4E%-12.4E", newABC[2][3], newABC[2][1]))
        l = replace(l, "HHPARAMS" => @sprintf("%-12.4E%-12.4E", newABC[3][3], newABC[3][1]))
        println(ffnonbondedOut,l)
    end
    close(ffnonbondedIO)
    close(ffnonbondedOut)

    topolIO = open("topol_base.top", "r")
    topolOut = open("topol_$shiftStr.top", "w")
    for l in eachline(topolIO)
        l = replace(l, "FFNONBONDED" => "ffnonbonded_$shiftStr.itp")
        println(topolOut,l)
    end
    close(topolIO)
    close(topolOut)

end
