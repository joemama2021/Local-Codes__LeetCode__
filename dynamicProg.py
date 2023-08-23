def fibo(n):
    ans = [1,1]
    i = 2

    if n == 0:
        return 1
    
    if n == 1:
        return 1
    
    while i <= n:
        ans.append(ans[i-1] + ans[i-2])
        i += 1
    return ans[len(ans)-2]

def gridtrlist1elRecur(m,n):
    return

def gridtrlist1el(m, n):
    arr = [[0]*n for i in range(m)]
    arr[0][0] = 1
    
    i = 0
    j = 0

    for i in range(m):
        for j in range(n):
            if i+1 < m:
                arr[i+1][j] = arr[i+1][j] + arr[i][j]
            if j+1 < n:
                arr[i][j+1] = arr[i][j+1] + arr[i][j]
                
    return arr[m-1][n-1]

def longestSubsequence(arr):
    n = len(arr)
    max_ans = 1

    lis = [0]*n
    lis[0] = 1
    for i in range(1, n):
        for j in range(0, i):
            if arr[j] < arr[i]:
                lis[i] = max(lis[i], lis[j]+1)
    
    for i in range(n):
        max_ans = max(max_ans, lis[i])
    
    return max_ans

    

arr = [10,9,2,5,3,7,101,18]
print(longestSubsequence(arr))