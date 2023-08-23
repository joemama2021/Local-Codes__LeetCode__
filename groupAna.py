def solver(string_array):
    
    d = {}
    for i in range(len(string_array)):
        x = ''.join(sorted(string_array[i]))
        if x not in d:
            d[x] = [string_array[i]]
        else:
            d[x].append(string_array[i])

    return d.values()

array  = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(solver(array))


