

function freed_diffusion(N, T)

    a = -5.7256
    b = -212.9887
    c = -0.4636
    d = 705.1817

    return exp(-a-b/T)*N^(-0.7-c-d/T)

end

function vonMeerwall_β(T)
    return -2.72 + (T-303.15)*(2.72-1.85)/140
end

function vonMeerwall_diffusion(N, T)

    Cm = 12.011
    Hm = 1.008
    M = N*Cm + (2*N + 2)*Hm

    return M^vonMeerwall_β(T)

end
