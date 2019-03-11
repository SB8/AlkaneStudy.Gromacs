gmxExe = ARGS[1]
edrFile = ARGS[2]
groIn = ARGS[3]
groOut = ARGS[4]

rm("box_out.txt"; force=true)

run(pipeline(`echo Box`,`$gmxExe energy -f $edrFile`, "box_out.txt"))

open("box_out.txt", "r") do fin
	for line in eachline(fin)
		if contains(line, "Box-X")
			strArr = split(strip(line))
			global boxSize = strArr[2]
		end
	end
end

boxXY = string(parse(Float64, boxSize))
boxZ = string(parse(Float64, boxShort)*3.0)


run(`$gmxExe editconf -f $groIn -pbc -box $boxXY $boxXY $boxZ -o gro_temp.gro`)

