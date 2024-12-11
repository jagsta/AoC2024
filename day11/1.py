from timeit import default_timer as timer
f = open("input.txt")


def process_number(number,index):
    if number==0:
#        print ("found 0")
        stones[index]=1
    elif len(str(number)) % 2 ==0:
        if len(str(number))==2:
           num1=int(str(number)[0])
           num2=int(str(number)[1])
        else:
            num1 = int(str(number)[:(int(len(str(number))/2))])
            num2 = int(str(number)[int(len(str(number))/2):])
#        print ("found even number of digits",num1,num2)
        stones.insert(index,num1)
        stones[index+1]=num2
    else:
        number*=2024
        stones[index]=number



stones=[]
for number in f.readline().split():
    stones.append(int(number.strip()))
#    print (stones)

blinks=1
while (blinks<26):
    start=timer()
    for i in reversed(range(len(stones))):
#        print("processing ",stones[i], i)
        process_number(stones[i],i)
    end=timer()
    print("blinks: ",blinks, "blink took: ",end-start," total is ",len(stones))
    blinks+=1

print(len(stones))
