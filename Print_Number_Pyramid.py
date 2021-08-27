n =int( input())

for i in range(1,n+1):
    for s in range(1,i):
        print(" ",end="")
    for n in range(i,n+1):
        print(n,end="")
    print()

for i in range(1,n):
    for s in range(1,n-i):
        print(" ",end="")
    for n in range(n-i,n+1):
        print(n,end="")
    print()
