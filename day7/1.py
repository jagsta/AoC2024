f = open("input.txt")
import re

class Node:
    def __init__(self, value = None, depth = None):
        self.left  = None
        self.right = None
        self.value = value
        self.depth = depth

def addNodes(node,number,depth):
    #multiply left, add right, concat middle
    if node.left:
        addNodes(node.left,number,depth)
    if node.right:
        addNodes(node.right,number,depth)
    else:
        node.left=Node(node.value * number)
        node.left.depth=depth
        node.right=Node(node.value + number)
        node.right.depth=depth
 #       print (node.left.value,node.right.value,depth)

def findNode(node,target,depth):
#    print ("finding ",target,depth," at:", node.depth,node.value)
    #if node.value==target and node.depth==depth:
    if node.value==target and node.depth==depth:
        print ("found match for ",target)
        return 1
    else:
        if node.depth == depth:
            return 0
        result=findNode(node.left,target,depth)
        if result:
            return 1
        result=findNode(node.right,target,depth)
        if result:
            return 1
        return 0
sums={}
total=0
for line in f.readlines():
    temp=line.split(":")
    target=int(temp[0])
    numbers=list(map(int, temp[1].split()))
    sums[target]=numbers
#    print (target,numbers,line.strip())
#   print (len(sums))

#   print (target, sums[target])
    depth=len(numbers)
    tree=Node(numbers[0])
    curdepth=1
#    left,right = addNode(tree,sums[line][level],level)
    for i in numbers:
#        print(curdepth,i)
        if curdepth==1:
            tree.depth=curdepth
        else:
            addNodes(tree,i,curdepth)
        curdepth+=1
    #print("finding ",target," at depth ",depth)
    if findNode(tree,target,depth):
        total+=target

print("total: ",total)
