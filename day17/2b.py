import sys
import re

target=[2,4,1,7,7,5,4,1,1,4,5,5,0,3,3,0]
binA=[0b0]

def findlowest(b,a):
    result=[]
    b=b^4
    for i in range(8):
        tempA=a<<3 #shift A 3 bits right
        b1=i # try for b 0-7
        b2=b1^7 # b2 is inverse of b1
        tempA+=b2 # new A is A+b2
        c=b^b1 # C needs to be this
        tempA2=tempA>>b1
        print("i",i,"b",bin(b),"tempA",bin(tempA),"b1",bin(b1),"b2",bin(b2),"c",bin(c),"tempA2",bin(tempA2))
        if c^(tempA2%8)==0: #c matches in the required spot of A
            print("found match for c in",tempA2,"A would be",bin(tempA))
            result.append(tempA)
    return result

for i in reversed(target):
    A=[]
    for b in binA:
        print("trying",i,bin(b))
        result=findlowest(i,b)
        if len(result)>0:
            for r in result:
                A.append(r)
        else:
            print("no valid answer")
            continue
    binA=A.copy()

for i in sorted(binA):
    print(int(i))
