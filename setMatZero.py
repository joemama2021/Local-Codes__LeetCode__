def zeroMat(matrix, n, m):
    row = [0]*n
    col = [0]*m

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1
    
    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                matrix[i][j] = 0
    return matrix

array = [[0,1,2,0], [3,4,5,2], [1,3,1,5]]
n = len(array)
m = len(array[0])
fin = zeroMat(array, n, m)

print("Final Matrix:")
for row in fin:
    for col in row:
        print(col, end=" ")
    print()