maxx = 99999999999
def solver(arr, amnt):
    if arr[0] != amnt and len(arr) == 1:
        return -1
    
    def usingRecursion(arr_coins, amnt):
        if amnt == 0:
            return 0
        
        if amnt < 0:
            return maxx
        
        coins = maxx

        for c in arr_coins:
            result = usingRecursion(arr_coins, amnt-c)

            if result != maxx:
                coins = min(coins, result+1)

        return coins
    
    def usingDP(arr, amnt):
        

arr = [1,2,3,4,5]
print(solver(arr, 16))
        
        