from sys import stdin

'''def sortZeroesAndOne(arr, n) :
    #Your code goes here 
    trr =[]
    for i in range(n):
        if(arr[i]==0):
            trr.insert(0,0)
        else:
            trr.append(1)
    return tr'''

def sort012(arr , n): 
    z=o=t=0
    for ele in arr:
        if ele == 0:
            z = z+1
        elif ele == 1:
            o = o+1
        else:
            t = t+1
    for i in range(z):
        arr[i]=0
    for i in range(z,z+o):
        arr[i]=1
    for i in range(z+o,z+o+t):
        arr[i]=2
    return arr
            






def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0:
        return list(), 0
   
    arr = list(map(int, stdin.readline().rstrip().split()))
    return arr, n
 

#to print the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")

    print()


#main
t = int(stdin.readline().strip())

while t > 0 :

    arr, n = takeInput()

    sort012(arr, n)
    printList(arr, n)

    t -= 1
