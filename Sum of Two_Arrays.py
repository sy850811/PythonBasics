
from sys import stdin

def sumoftwoarrays(arr1, n, arr2, m):
    
    op1 = 0
    for i in arr1:
        op1 = op1 * 10 + i
    op2 = 0
    for i in arr2:
        op2 = op2 * 10 + i
    op3 = op2 + op1
    # print(op2,op1)
    arr3=[]
    while op3!=0:
        arr3.append(op3%10)
        op3 = op3 // 10
    if len(arr3) < n+1 or len(arr3) < m+1:
        arr3.append(0)
    return arr3[::-1]
        
        


















def printlist(arr3):
    for ele in arr3:
        print(ele,end=" ")
















def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list([0]), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()
    arr3= sumoftwoarrays(arr1, n, arr2, m)
    printlist(arr3)

    t -= 1
