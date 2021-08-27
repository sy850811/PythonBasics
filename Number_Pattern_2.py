n = int(input())
i = 1
print("1")
while i<n:
    j = 1
    print(i,end="")
    while j<i:
        print("0",end="")
        j+=1
    print(i,end="")
    print()
    i+=1
