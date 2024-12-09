import re

f=open("input.txt")
total=0
for line in f.readlines():
#    sums=re.findall("mul\((\d{1,3}),(\d{1,3})\)",line)
#    for sum in sums:
    for sum in re.finditer("mul\((\d{1,3}),(\d{1,3})\)",line):
        num1 = int(sum.group(1))
        num2 = int(sum.group(2))
        total+= (num1 * num2)
print ("total: ",total)
