n = int(input())

def arm(n,m):
    armNo = 0
    while n!=0:
        t = n%10
        armNo+=t**m
        n = n//10
    return armNo

def countDigit(n):
    count = 0
    while n!=0:
        n=n//10
        count+=1
    return count


if(n == arm(n,countDigit(n))):
    print("true")
else:
    print("false")
