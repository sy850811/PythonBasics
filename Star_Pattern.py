n = int(input())
i = 1
while i<=n:
    j = 1
    while j <= n-i:
        print(" ",end="")
        j+=1
    j=1
    while j <= i:
        print("*",end="")
        j+=1
    j=1
    while j <= i-1:
        print("*",end="")
        j+=1
    print()
    i+=1
