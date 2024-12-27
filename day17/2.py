import sys
import re

def combo(operand,a,b,c):
    if operand<4:
        return operand
    match operand:
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c

def execute(A,B,C,program):
    output=[]
    halted=False
    i=0
    while not halted:
        if i>=len(program)-1:
            halted=True
            break
        opcode=program[i]
        operand=program[i+1]
 #       print(i,opcode,operand,A,B,C)
        match opcode:
            case 0:
                #adv num A den 2^combo op
                num=A
                den=2**combo(operand,A,B,C)
                A=num//den
 #               print("adv",num,den,A)
            case 1:
                #bxl bitwise XOR B lit op
                a=B
                b=operand
                B=int(a^b)
 #               print("bxl",a,b,B)
            case 2:
                #bst
                a=combo(operand,A,B,C)
                B=int(a%8)
 #               print("bst",a,B)
            case 3:
                #jnz
                if A!=0:
                    i=operand
 #                   print("jnz",i)
                    continue
            case 4:
                #bxc
                B=int(B^C)
 #               print ("bxc",B,C)
            case 5:
                res=combo(operand,A,B,C)
                output.append(int(res%8))
 #               print("out",res,int(res%8))
            case 6:
                num=A
                den=2**combo(operand,A,B,C)
                B=num//den
 #               print("bdv",num,den,A)
            case 7:
                num=A
                den=2**combo(operand,A,B,C)
                C=num//den
 #               print("cdv",num,den,A)
        i+=2
    line=""
    for out in output:
        line+=str(out)+","

    result = line[:-1]
    return result

file="input.txt"

if len(sys.argv)>1:
    file=sys.argv[1]

f = open(file)

A,B,C=0,0,0
program=[]
for line in f.readlines():
    match=re.match(r'Register (\w): (\d+)',line)
    if match:
        if match.group(1)=="A":
            A=int(match.group(2))
        elif match.group(1)=="B":
            B=int(match.group(2))
        elif match.group(1)=="C":
            C=int(match.group(2))
    match=re.match(r'Program:',line)
    if match:
        match=re.finditer(r'(\d+)\,(\d+)',line)
        for m in match:
            program.append(int(m.group(1)))
            program.append(int(m.group(2)))

print (A,B,C)
print (program)

programstring=""
for i in program:
    programstring+=str(i)+","
programstring=programstring[:-1]
print(programstring)
found=False
i=53340000000000
while not found:
    a=i
    b=B
    c=C
    p=program.copy()
    result=execute(a,b,c,p)
    print(i,result)
    if result==programstring:
        found=True
        break
    i+=1
print(i)
