row = int(input())
n = (row//2)+1
for i in range (1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for d in range(1,2*i):
        print("*",end="")
    print()
    
n = row//2

for i in range(1,n+1):
    for s in range(1,i+1):
        print(" ",end="")
    for d in range(1,row-2*i + 1):
        print("*",end="")
    print()
    
