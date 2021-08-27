from sys import stdin 

def sort012(arr, n) :
    one = 0
    two = 0
    arr3 = []
    for i in arr:
        if i == 0:
            arr3.append(0)
        elif i == 1:
            one+=1
        else:
            two+=1
    for i in range(one):
        arr3.append(1)
    for i in range(two):
        arr3.append(2)
    return arr3

























#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()

    arr = sort012(arr, n)
    printList(arr, n)
    
    t -= 1
