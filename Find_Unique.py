def find(li,i):
    count=0
    for e in li:
        if e == i:
            count+=1
    return count == 2

for i in range(int(input())):
    n = int(input())
    li = [int(x) for x in input().split()]
    for i in range(n):
        if(not(find(li,li[i]))):
            print(li[i])
            break
