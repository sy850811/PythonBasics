n = int(input())

a = 0
b = 1

while a<=n:
    # print(a)
    if (a == n):
        print("true")
        break
    a,b =b,a+b
else:
    print("false")
