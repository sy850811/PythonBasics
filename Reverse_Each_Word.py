S = input()
def revEachWord(S):
    RS = ""
    for i in S.split():
        RS = RS + i[::-1] + " "
    return RS[:-1]
S = revEachWord(S)
print(S,end = "")
