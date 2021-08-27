'''
    In order to print two or more integers in a line separated by a single 
    space then you may consider printing it with the statement, 

    print(str(num1) + " " + str(num2))

'''

from sys import stdin

def findLargestRow(arr, nRows, mCols):
    index = 0
    maxSum = -2147483648
    for i in range(len(arr)):
        sum = 0
        for ele in arr[i]:
            sum += ele
        if sum > maxSum:
            maxSum = sum
            index = i
    return maxSum,index

def findLargestColumn(arr, nRows, mCols):
    index = 0
    maxSum = -2147483648
    for j in range(mCols):
        sum = 0
        for i in range(len(arr)):
            sum += arr[i][j]
        if sum > maxSum:
            maxSum = sum
            index = j
    return maxSum,index

def findLargest(arr, nRows, mCols):
    rSum,rIndex = findLargestRow(arr, nRows, mCols)
    cSum,cIndex = findLargestColumn(arr, nRows, mCols)
    # print(rSum,rIndex,cSum,cIndex)
    if(rSum>=cSum):
        print("row "+str(rIndex)+" "+str(rSum))
    else:
        print("column "+str(cIndex)+" "+str(cSum))
























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

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1
