## Read input as specified in the question.
## Print output as specified in the question.
def removeduplicate(S):
    u = ""
    i = 0
    while i < len(S):
        # print(i , len(S))
        u = u + S[i]
        # print(i)
        j = i +1
        while j<len(S) and S[j] == S[i]:
            j+=1
        # print(j)
        i = j
    return u

S=input()
S = removeduplicate(S)
print(S)
        
