def solver(array):
    def checker(m,n,o):
        if m<n<o:
            return True
    
    for i in range(len(array)-2):
        m = array[i]
        n = array[i+1]
        o = array[i+2]
        if checker(m,n,o):
            return True
    return False

array = [1,2,3,4,5]
print(solver(array))