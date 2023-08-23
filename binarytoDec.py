def solver(binary):
    def reverse(arr):
        for i in range(len(arr)//2):
            temp = arr[i]
            arr[i] = arr[len(arr)-i-1]
            arr[len(arr)-i-1] = temp
        return arr
    
    def pow(a, b):
        if b == 0:
            return 1
        
        return a*pow(a, b-1)
    
    arr = []
    binary = str(binary)
    for i in binary:
        arr.append(int(i))
    reverse(arr)

    ans = 0

    for i in range(len(arr)):

        ans = ans + arr[i]*pow(2, i)
    return ans

print(solver(101101100011))
