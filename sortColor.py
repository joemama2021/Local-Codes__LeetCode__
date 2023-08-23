def solver(arr):
    aux1 = []
    
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.pop(i)
            arr.insert(0, 0)
            i += 1
            continue
        
        if arr[i] == 2:
            arr.pop(i)
            arr.append(2)
            i += 1
            continue

        if arr[i] == 1:
            i += 1
            continue

    return arr

arr = [2,0,1]
print(solver(arr))