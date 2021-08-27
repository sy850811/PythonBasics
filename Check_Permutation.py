str1 = input()
str2 = input()
if(len(str1) != len(str2)):
    print("false")
else:
    for i in range(len(str1)):
        if str1[i] in str2:
            str2 = str2.replace(str1[i],"",1)
        else:
            print("false")
            break
    else:
        if(len(str2) != 0):
            print("false")
            print(str2)
        else:
            print("true")
