f = open("input.txt")

field=[]
for line in f.readlines():
    field.append(line.strip())

#print (len(field),len(field[0]))

antinodes=set()
# for each antenna, add an antinode for each antenna of the same type (twice the offset to the antenna)
for y in range(len(field)):
    for x in range(len(field[0])):
        if not field[y][x]==".":
            antenna=field[y][x]
            print("checking antenna ",antenna)
            for dy in range(len(field)):
                for dx in range(len(field[0])):
                    if field[dy][dx]==antenna and (dy!=y or dx!=x):
                        ax=(x-dx)
                        ay=(y-dy)
                        antix=x+ax
                        antiy=y+ay
                        print(x,y,dx,dy,antix,antiy)
                        if antix>=0 and antix<len(field[0]) and antiy>=0 and antiy<len(field):
                            print("antinode at ",antix,antiy)
                            antinodes.add("0"+str(antix)+"0"+str(antiy))

print(antinodes)
print(len(antinodes))
