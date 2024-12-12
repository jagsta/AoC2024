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
                        antix=x
                        antiy=y
                        ax=(x-dx)
                        ay=(y-dy)
                        while (antix>=0 and antix<len(field[0]) and antiy>=0 and antiy<len(field)):
                            print(x,y,dx,dy,antix,antiy)
                            if antix>=0 and antix<len(field[0]) and antiy>=0 and antiy<len(field):
                                print("antinode at ",antix,antiy)
                                antinodes.add(str(antix)+","+str(antiy))
                            antix+=ax
                            antiy+=ay

print(antinodes)
print(len(antinodes))
