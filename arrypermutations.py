def solver(arr):
    ans = []
    if len(arr) == 1:
        return [arr[:]]
    
    for i in range(len(arr)):
        popped = arr.pop(0)
        perms = solver(arr)

        for perm in perms:
            perm.append(popped)
        
        ans.extend(perms)
        arr.append(popped)

    return ans

arr = [1,2,3]
print(solver(arr))