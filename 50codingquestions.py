def reverse_num(num):
    reverse = 0
    while num > 0:
        rem = num%10
        reverse = (reverse*10) + rem
        num = num//10
    
    return reverse

def fibo_series(n):
    ans = [0,1]
    i = 0
    while i < n-2:
        ans.append(ans[i] + ans[i+1])
        i += 1
    for i in ans:
        print(i, end=' ')

def gcd(num1, num2):
    lim = min(num1, num2)

    i = 1
    ans = 0
    while i <= lim:
        if num1%i == 0 and num2%i == 0 and i > ans:
            ans = i
        i += 1
    return ans

def perfect_num(num):
    arr_of_div = []
    for i in range(1, (num//2)+1):
        if num%i == 0:
            arr_of_div.append(i)
    
    sum = 0
    for i in arr_of_div:
        sum = sum + i

    if sum == num:
        return 1
    else:
        return 0

def anagram_check(string1, string2):
    aux_dict = {}

    for i in range(len(string1)):
        if string1[i] not in aux_dict:
            aux_dict[string1[i]] = 1
        else:
            aux_dict[string1[i]] += 1
    
    for i in range(len(string2)):
        if string2[i] in aux_dict:
            aux_dict[string2[i]] -= 1
        
        else:
            aux_dict[string2[i]] = 1
    
    for i in aux_dict:
        if aux_dict[i] != 0:
            return -1
    return 1

def palin_check(string1, i = 0):
    n = len(string1)
    if i > n/2:
        return 1
    
    if string1[i] != string1[n-i-1]:
        return -1
    return palin_check(string1, i + 1)

def char_freq(string1):
    aux_dict = {}
    for i in range(len(string1)):
        if string1[i] not in aux_dict:
            aux_dict[string1[i]] = 1
        else:
            aux_dict[string1[i]] += 1
    
    for i in aux_dict:
        print("The frequency of " +i+ " is "+str(aux_dict[i]), end="\n")
    
    return ""

def replace_substring(string1, to_rep, rep_with):
    n = len(string1)
    m = len(to_rep)
    return

def reverse_string(string):
    ans = ''
    i = 0
    while i < len(string):
        ans = string[i] + ans
        i += 1
    return ans

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = 0
        j = 0
        k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def sort_digits(num):
    num = str(num)
    arr = []
    for i in range(len(num)):
        arr.append(int(num[i]))
    
    mergeSort(arr)
    ans = ''
    for i in arr:
        ans = ans + str(i)
    return int(ans)

def lowest_ele(arr):
    mergeSort(arr)
    return arr[0]

string1 = 'racecars'
string2 = 'salesman'
arr = [5,8,7,2,4,3]

print(lowest_ele(arr))


