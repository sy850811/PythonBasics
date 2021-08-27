n = int(input())
m = 2*n-1
for i in range(1,2*n):
    for j in range(1,2*n):
       for k in range(1,n+1):
        if(i==k or j==k or j==m-k+1 or i == m-k+1):
            print(n-k+1,end="")
            break
    print()
