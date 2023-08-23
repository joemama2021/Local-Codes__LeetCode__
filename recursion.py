def recur1(stri, cnt):
    if cnt == 6:
        return 1
    
    print(stri,end="\n")
    return recur1(stri, cnt+1)

def reverse_arr(arr, i = 0):

    n = len(arr)
    if i >= n/2:
        return arr
    
    temp = arr[i]
    arr[i] = arr[n-i-1]
    arr[n-i-1] = temp
    return reverse_arr(arr, i+1)

def check_palind(word,i):
    n = len(word)

    if len(word) == 0:
        return "Empty string"
    
    if len(word) == 1:
        return "Length only 1"

    if i >= n/2:
        return True

    if word[i] != word[n-i-1]:
        return False
    
    else:
        return check_palind(word, i+1)
    
def fibonacci(n):
    if n <= 1:
        return n
    return print(fibonacci(n-1) + fibonacci(n-2)) 
    
def subsequences(arr, subarr, idx=0):
    if idx == len(arr):
        if len(subarr) != 0:
            print(subarr)

    else:
        subsequences(arr, subarr, idx+1)
        subsequences(arr, subarr+[arr[idx]], idx+1)
    
    return

def dec_bin(decimal, res = ""):
    if decimal == 0:
        return res
    
    res = str(decimal % 2) + res
    return dec_bin(decimal//2, res)

arr = [1,2,3]
word = ""
print(dec_bin(128))
