def n_meet(start, end):
    ans = [1]
    length = len(start)
    i = 1
    j = 0

    while i < length:
        if start[i] > end[j]:
            ans.append(i+1)
            j = i
            i += 1
        
        else:
            i += 1

    return ans

start = [10,12,20]
end =   [20,25,30]

print(n_meet(start, end))