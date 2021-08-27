from sys import stdin

# def pushZerosAtEnd(arr, n) :
#     #Your code goes here
#     for i in range(n):
#         j=i-1
#         temp = arr[i]
#         if(arr[i] != 0):
#             while j>=0 and arr[j] == 0:
#                 arr[j+1] = arr[j]
#                 j-=1
#             arr[j+1] = temp
#     return arr

# def pushZerosAtEnd(arr, n) :
#     for i in range(n):
#         if arr[i] == 0:
#             arr.pop(i)
#             arr.append(0)
#     return arr

def pushZerosAtEnd(arr, n) :
    count = 0
    for i in range(n):
        if(arr[i] != 0):
            arr[count] = arr[i]
            count+=1
    for i in range(count,n):
        arr[i] = 0


























#Taking Input Using Fast I/O
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

    pushZerosAtEnd(arr, n)
    printList(arr, n)

    t -= 1
