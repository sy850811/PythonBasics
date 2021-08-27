

while True:
    i = int(input())
    if i==6:
        break
    else:
        a = int(input())
        b = int(input())
        if i==1:
            print(a + b)
        elif i==2:
            print(a - b)
        elif i==3:
            print(a * b)
        elif i==4:
            print(a / b)
        elif i==5:
            print(a % b)
        elif i==6:
            break
        else:
            print("Invalid Operation")
    
