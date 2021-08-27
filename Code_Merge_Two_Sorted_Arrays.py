from sys import stdin

def merge(arr1, n, arr2, m) :
    p1=0
    p2=0
    arr3=[]
    while p1 < n and p2 < m:
        if(arr1[p1] < arr2[p2]):
            arr3.append(arr1[p1])
            p1+=1
        else:
            arr3.append(arr2[p2])
            p2+=1
    if(p1 == n):
        arr3.extend(arr2[p2:])
        return arr3
    if(p2 == m):
        arr3.extend(arr1[p1:])
        return arr3






















#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
        
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()

    ans = merge(arr1, n, arr2, m)
    printList(ans, (n + m))

    t -= 1
