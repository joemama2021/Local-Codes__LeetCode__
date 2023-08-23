def solver(arr, k):
    ans  = []
    dict_util = {}
    
    if len(arr) == 1 and k == 1:
        return [arr[0]]
    
    for i in range(len(arr)):
        if arr[i] not in dict_util:
            dict_util[arr[i]] = 1
            continue

        if arr[i] in dict_util:
            dict_util[arr[i]] += 1

    
    for keys in dict_util:
        if dict_util[keys] >= k:
            ans.append(keys)
    return ans

arr = [1,1,1,2,2,3]
print(solver(arr, 2))