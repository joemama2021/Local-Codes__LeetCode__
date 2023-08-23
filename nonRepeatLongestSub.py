def solver(str):
    ans = ['$']
    fin=''
    if len(str) == 0:
        return 0
    if len(str) == 1:
        return 1
    for i in range(len(str)-1):
        visited = []
        j = i
        while str[j] not in visited and j < len(str):
            visited.append(str[j])
            j = j+1
            if j >= len(str):
                break

        if len(visited) > len(ans[0]):
            ans[0] = visited
    fin = ''.join(ans[0])
    return fin

str = "pwwkew"
print(solver(str))
