def solver(arr):
    i = 0
    while i < len(arr)//2:
        temp = arr[i]
        arr[i] = arr[len(arr)-i -1]
        arr[len(arr)-i -1] = temp

        i += 1

    return arr

def reverse_string(string):
    n = len(string)
    ans = ""
    for c in string:
        ans = c + ans
    
    return ans

string = "Hello"
print(reverse_string(string))
