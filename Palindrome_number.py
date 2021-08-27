no = int(input())
n=no
rev=0
t=0
while(no != 0):
    t = no%10
    no=no//10
    rev=(rev+t)*10

if(rev/10 == n):
    print("true")
else:
    print("false")
