from timeit import default_timer as timer
f = open("input.txt")


def process_number(number,index):
    if number=="0":
#        print ("found 0")
        stones[index]="1"
    elif len(number) % 2 ==0:
        j=int(len(number)/2)
        if j==2:
            stones[index]=number[0]
            stones.append(number[1])
        else:
#        print ("found even number of digits",num1,num2)
#       Do we need to preserve order here? I think not, it doesn't affect the rules which are atomic
            stones[index] = number[:j]
            stones.append(number[j:])
    else:
        stones[index]=str(int(number)*2024)



stones=[]
for number in f.readline().split():
    stones.append(number.strip())
#    print (stones)

blinks=1
while (blinks<76):
    start=timer()
    for i in range(len(stones)):
#        print("processing ",stones[i], i)
        process_number(stones[i],i)
    end=timer()
    print("blinks: ",blinks, "blink took: ",end-start)
    blinks+=1

print(len(stones))
