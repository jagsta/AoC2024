#This can't work by brute force for blinks = 75
# Odd length numbers > 99 need to be computed until the result is an even length
# Any even length number length 2^n will decompose into single digits in n blinks
# Any other even number will decompose to 2 odd length numbers, and will need computing
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
import math
f = open("input.txt")

digidepth=[1,3,3,3,3,5,5,5,5,5]
leaves=["1","2024","4048","6072","8096","20482880","24579456","28676032","32772608","36869184"]

def walk_tree(digit, depth, target):
    print("walking from ",digit," at depth",depth)
    nodes=0
    newdepth=depth+digidepth[digit]
    if newdepth<target:
        for d in leaves[digit]:
            nodes+=walk_tree(int(d),newdepth,target)
    else:
        steps = target - depth
        print("reached depth",depth,digit,target,steps)
        if steps == 5:
            print ("adding 8 to ",nodes)
            nodes+=8
        elif steps == 4:
            print ("adding 4 to ",nodes)
            nodes+=4
        elif steps == 3 and digit>4:
            print ("adding 2 to ",nodes)
            nodes+=2
        elif steps == 3 and digit<5:
            print ("adding 4 to ",nodes)
            nodes+=4
        elif steps == 2 and digit<5:
            nodes+=2
            print ("adding 2 to ",nodes)
        else:
            nodes+=1
            print ("adding 1 to ",nodes)
    return nodes


def process_number(n,depth,target):
    print("processing ",n," at depth",depth)
    if (depth==target):
        print(n," is at depth ",depth," adding 1 to count")
        return 1
    count=0
    if len(n)==1:
        print("single digit", n)
        count+=walk_tree(int(n),depth,target)
    elif len(n) % 2==0:
        if (len(n) & (len(n)-1) == 0) and len(n) != 0: #It's 2^log2(len n), it'll decompose into single digits in log2(len n) blinks
            print ("power of two length:",n, int(math.log2(len(n))))
            if depth+int(math.log2(len(n)))>target: #we can't decompose fully
                exp=target-depth
                count+=2**exp
            else:
                for i in n:
                     count+=walk_tree(int(i),depth+int(math.log2(len(n))),target)
        else:
            j=int(len(n)/2)
            print ("found even number of digits",n)
            num1=int(n[:j])
            num2=int(n[j:])
            count+=process_number(str(num1),depth+1,target)
            count+=process_number(str(num2),depth+1,target)
    else:
        print ("odd length: ",n)
        count+=process_number(str(int(n)*2024),depth+1,target)

    return count



stones=[]
for number in f.readline().split():
    stones.append(number.strip())
#    print (stones)

count=0
depth=0
targetblinks=6
for n in stones:
    start=timer()
    print("processing ",n, "at depth",depth)
    result=process_number(str(n),depth,targetblinks)
    count+=result
    end=timer()
    print("finished ",n," with result",result,"in ",end-start,"total",count)
print(count)
