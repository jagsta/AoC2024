#This can't work by brute force for blinks = 75
# Odd length numbers > 99 need to be computed until the result is an even length
# Any even length number will decompose into single digits in (length)/2 blinks
# Any single digit will decompose to a set of single digits in a fixed number of blinks - 0(1), 1,2,3,4(3), 5,6,7,8,9(5)
# precompute the trees for 0 - 9, these can replace any instances of a single digit
# We don't care about intermediates, we only care about the number of nodes at depth = blinks
# We can skip any calculations until we exceed the target blinks on a given tree, then back track to the right number of blinks
#
# For each starting stone, traverse the tree, skipping, until blinks>target
# We'll need to do this recursively, depth first?
# When we exceed the target, we'll add the number of nodes at the correct depth to a count of nodes, then carry on
# Iterate over the initial stones tallying up the nodes


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
    print("blinks: ",blinks, "blink took: ",end-start," length is now: ",len(stones))
    blinks+=1

print(len(stones))
