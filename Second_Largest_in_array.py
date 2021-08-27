
from sys import stdin

def arrayRotateCheck(arr, n):
    #Your code goes here
    i=0
    while i < n-1:
        if arr[i] > arr[i+1]:
            return n - i -1
        i += 1
    else:
        return 0
    
            
            
        













#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print(arrayRotateCheck(arr, n))

    t -= 1
