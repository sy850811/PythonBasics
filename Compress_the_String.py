## Read input as specified in the question.
## Print output as specified in the question.
def compress_str(s):
    u = ""
    i=0
    while i < len(str(s)):
        u += s[i]
        j = i + 1
        count = 1
        while j < len(s) and s[j] == s[i]:
            count += 1
            j += 1
        if(count > 1):
            u += str(count)
        # print(i,j)
        i = j
    return u

s=input()
s=compress_str(s)
print(s)
