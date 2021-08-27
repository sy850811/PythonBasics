## Read input as specified in the question.
## Print output as specified in the question.
s=input()[:-1]
index = -1
arr = [0]*26
for i in s:
    # print(i,ord(i))
    arr[ord(i) - 97]+=1
max = -1
for i in range(26):
   if arr[i] > max:
    max = arr[i]
    index = i

print(chr(97+index))
