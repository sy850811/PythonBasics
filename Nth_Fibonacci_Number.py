a = 1
b = 1
n = int(input())
i=2
while(i<n):
    t=b
    b=a+b
    a=t
    i += 1
print(b)
