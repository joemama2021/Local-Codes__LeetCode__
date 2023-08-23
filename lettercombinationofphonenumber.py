def solver(arr):
    ans = []
    letters = {
        "1" : "%@#",
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",
        "5" : "jkl",
        "6" : "mno",
        "7" : "pqrs",
        "8" : "tuv",
        "9" : "wxyz",
    }
    if len(arr) == 0:
        return []

    def dfsKeypad(path, idx = 0):
        if len(path) == len(arr):
            ans.append("".join(path))
            return
        
        for val in letters[str(arr[idx])]:
            path.append(val)
            dfsKeypad(path, idx+1)
            path.pop()
    
    dfsKeypad([])
    return ans

arr = "23"
print(solver(arr))

