n = int(input())
isEven = n%2 == 0
if(isEven):
    upTwo = n//2-1
    downTwo = upTwo
    one = 1
else:
    upTwo = n//2
    downTwo = upTwo -1
    one = -1
s=1
for j in range(upTwo+1):
    for k in range(n):
        print(s+k,end=" ")
    print()
    s+=n*2
s-=n*2
s+=n*one
for k in range(n):
    print(s+k,end=" ")
print()

s-=n*2
for j in range(downTwo):
    for k in range(n):
        print(s+k,end=" ")
    print()
    s-=n*2
