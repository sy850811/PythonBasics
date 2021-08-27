no = int(input())
even=0
odd=0
while(no != 0):
    t = no%10
    if(t%2 == 0):
        even+=t
    else:
        odd+=t
    no=no//10
print(even," ",odd)
