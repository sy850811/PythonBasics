def fToC(f):
    return int((f-32)/1.8)

s = int(input())
e = int(input())
w = int(input())

for i in range(s,e+1,w):
    print(i,end = '\t')
    print(fToC(i))



