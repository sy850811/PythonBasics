from sys import stdin

def spiralPrint(mat, nRows, mCols):
    #Your code goes here
    k=0
    l=0
    while (k < nRows and l < mCols) : 
           for i in range(l, mCols) : 
               mat1.append(mat[k][i])
              
           k += 1
  
           for i in range(k, nRows) : 
               mat1.append(mat [i][mCols - 1])
              
           mCols -= 1
   
           if ( k < nRows) : 
              
              for i in range(mCols - 1, (l - 1), -1) : 
                  mat1.append(mat[nRows - 1][i]) 
              
              nRows -= 1
           
           if (l < mCols) : 
            
              for i in range(nRows - 1, k - 1, -1) : 
                  mat1.append(mat[i][l]) 
              
              l += 1
    return mat1



def printList(mat1):
    for ele in mat1:
        print(ele, end=" ")
    print()























#Taking Input Using Fast I/O
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

    mat1=[]
    mat, nRows, mCols = take2DInput()
    spiralPrint(mat, nRows, mCols)
    printList(mat1)

    t -= 1
