def solver(arr):
    idx = 0
    while idx <= len(arr):
        curr = arr[idx]

        if idx == len(arr)-1:
            return True
        
        if curr == 0:
            return False
        
        idx = idx + curr
    return False

arr = [2,3,1,1,4]
print(solver(arr))