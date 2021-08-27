n = int(input())

def rev(n):
    rev = 0
    while n!=0:
        t = n%10
        rev = rev * 10 + t
        n = n//10
    return rev

if(rev(n)== n):
    print("true")
else:
    print("false")
