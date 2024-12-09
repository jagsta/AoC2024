def test(sequence):
	rising=0
	last=0
	safe=1
	for seq in sequence:
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
	return safe

f=open("input.txt")
total=0
for line in f.readlines():
	line_values=[int(x) for x in line.split()]
	safe=test(line_values)
	if safe==1:
		total+=1
		print("safe:",line)
	else:
		for i in range (len(line_values)):
			temp_list=list(line_values)
#			print (temp_list)
#			print ("index: ",i)
			del temp_list[i]
			safe=test(temp_list)
			if safe==1:
				total+=1
				print("safe with ",i," deleted:",line)
				break
print ("total is",total)	
