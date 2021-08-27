n =int(input())
r = 0

while n !=0:
    t = n%10
    n = n//10
    r =r*10+t
print(r)
