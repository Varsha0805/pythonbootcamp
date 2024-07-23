def diagonalDifference(arr):
    s1,s2=0,0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                s1=s1+arr[i][j]
            if i+j==len(arr)-1:
                s2=s2+arr[i][j]
    return abs(s1-s2)