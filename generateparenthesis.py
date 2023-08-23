def solver(n):
    ans = []

    if n == 0:
        return "Nothing to return!"

    if n == 1:
        return "()"
    
    def helper(s, open = 0, close = 0):
        if open == n and close == n:
            ans.append(s)
            return
        
        if open < n:
            helper(s + "(", open+1, close)
        
        if close < open:
            helper(s + ")", open, close+1)

    helper("")
    return ans

print(solver(3))