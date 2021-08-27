from sys import stdin

def wavePrint(mat, nRows, mCols):
    for j in range(mCols):
        if(j%2==0):
            s = 0
            e = nRows
            stride = 1
        else:
            s = nRows - 1
            e = -1
            stride = -1
        for i in range(s,e,stride):
            print(mat[i][j],end=" ")



























#Taking Iput Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    wavePrint(mat, nRows, mCols)
    print()

    t -= 1
