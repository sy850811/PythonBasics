def find(li,i):
    count=0
    for e in li:
        if e == i:
            li.remove(e)
            return True
    return False

for i in range(int(input())):
    n = int(input())
    if n!=0:
    	li1 = [int(x) for x in input().split()]
    else:
        li1=[]
    m = int(input())
    if m!=0:
    	li2 = [int(x) for x in input().split()]
    else:
        li2=[]
    i = 0
    e = len(li1)
    while i < e:
        if((find(li2,li1[i]))):
            print(li1[i],end=" ")
            li1.remove(li1[i])
            i-=1
            e-=1
        i+=1
    print()
