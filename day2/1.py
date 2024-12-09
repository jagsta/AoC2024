f=open("input.txt")
total=0
for line in f.readlines():
	rising=0
	last=0
	safe=1
	line_values=[int(x) for x in line.split()]
	for seq in line_values:
		if last:
			diff=last-seq
			if rising!=0:
				if (diff<0 and rising>0) or (diff>0 and rising<0) or (diff==0) or (abs(diff)>3):
					safe=0
					break
				
			else:
				if abs(diff)>3:
					safe=0
					break
				if diff<0:
					rising=-1
				elif diff>0:
					rising=1
				else:
					safe=0
					break
		last=seq
	if safe==1:
		total+=1
		print("safe:",line)
print ("total is",total)	
