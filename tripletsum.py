def solver(array):
    ans = []
    array.sort()

    for i in range(len(array)):
        if i > 0  and array[i] == array[i-1]:
            continue
        target = array[i]*(-1)
        l,r = i+1, len(array)-1
        while l < r:
            if array[l] + array[r] == target:
                ans.append([array[i], array[l], array[r]])
                l = l+1
                while l<r and array[l] == array[l-1]:
                    l = l+1
            elif array[l] + array[r] < target:
                l = l+1
            else:
                r = r-1
    return ans

array = [-1,0,1,2,-1,-4]
print(solver(array))