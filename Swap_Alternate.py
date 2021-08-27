testCases = int(input())
for t in range(testCases):
    n = int(input())
    li = [int(x) for x in input().split()]
    for i in range(0,n-1,2):        
        li[i],li[i+1]=li[i+1],li[i]
        print(li[i],li[i+1],end=" ")
    if(n % 2 != 0):
        print(li[n-1],end=" ")
    print()
        
