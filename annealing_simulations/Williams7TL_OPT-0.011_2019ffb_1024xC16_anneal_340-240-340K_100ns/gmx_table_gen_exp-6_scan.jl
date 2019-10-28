
# Tables provide
# f(r), which has r dependence of Coulomb term (should usually be 1/r)
# g(f), for r dependence of attractive/dispersion term (e.g. -1/r^6)
# h(f), for r dependence of repulsive term (e.g. exp(-B*r) or 1/r^12)

# Each line has the format
# r, f, -f", g, -g", h, -h" <-- note the minus sign for derivatives

# Exponent of attractive terms
att = 6

step = 0.002 # nm
r_start = 0.04
r_cut = 1.5
r_ext = 1.0

function write_table(b, filename)
	n_switch = trunc(Int, r_start/step)
	n_end = trunc(Int, ((r_cut+r_ext)/step) + 1) # +1 just to add extra point

	r_zero = [x*step for x in 0:(n_switch-1)]
	r_range = [x*step for x in n_switch:n_end] # Adds one extra point after r_cut+r_ext

	tfile = open(filename, "w")

	# Write comment line
	@printf(tfile, "# %s%-.2f\n", "Buckingham (exp-6) potential, B=", b)

	# Write r = 0 line (all zeros)
	for r in r_zero
		@printf(tfile, "%15.6e %15.6e %15.6e %15.6e %15.6e %15.6e %15.6e\n", r, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
	end

	for r in r_range
		@printf(tfile, "%15.6e ", r)
		@printf(tfile, "%15.6e %15.6e ", 1.0/r, 1.0/r^2)
		@printf(tfile, "%15.6e %15.6e ", -1.0/r^att, -6.0/r^(att+1))
		@printf(tfile, "%15.6e %15.6e\n", exp(-b*r), b*exp(-b*r))
	end

	close(tfile)
end
