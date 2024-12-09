#!/usr/bin/python3

f=open("input.txt")
l=[]
#r=[]
counts={}
for line in f.readlines():
	line_values=[int(x) for x in line.split()]
	l.append(line_values[0])
#	r.append(line_values[1])	
	if line_values[1] in counts:
		counts[line_values[1]]+=1
	else:
		counts[line_values[1]]=1
#l.sort()
#r.sort()
total=0
for i in range (len(l)):
#	diff=abs(l[i]-r[i])
#	total=total+diff
	if l[i] in counts:
		sim=l[i] * counts[l[i]]
	else:
		sim=0
	total+=sim
print("total is",total)
