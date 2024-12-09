#!/usr/bin/python3

f=open("input.txt")
l=[]
r=[]
for line in f.readlines():
	line_values=[int(x) for x in line.split()]
	l.append(line_values[0])
	r.append(line_values[1])	
l.sort()
r.sort()
total=0
for i in range (len(l)):
	diff=abs(l[i]-r[i])
	total=total+diff
print("total is",total)
