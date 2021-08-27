from sys import stdin


# def rotate(arr, n, d):
#     #Your code goes here
#     for j in range(d):
#         first = arr[0]
#         for i in range(n-1):
#             arr[i] = arr [i+1]
#         arr[n-1] = first
            
# def rotate(arr, n, d):
#     #Your code goes here
#     for j in range(d):
#         arr.append(arr.pop(0))


# def rotate(arr, n, d):
#     #Your code goes here
#     if d == n:
#         return
#     for j in range(d):
#         t = arr[0]
#         arr[:-1] = arr[1:]
#         arr[-1] = t
#     return arr

def rotate(arr, n, d):
    #Your code goes here
    if n==0 or d == 0:
        return arr
    t = arr[:d]
    arr[:n-d] = arr[d:]
    arr[-d:] = t
    # print(arr)
    return arr





















#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
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
    d = int(stdin.readline().rstrip())
    arr = rotate(arr, n, d)
    printList(arr, n)
    
    t -= 1
