def solver(string1, string2):
    letters1 = {}
    letters2 = {}

    for i in range(len(string1)):

        if string1[i] in letters1:
            letters1[string1[i]] += 1
        else:
            letters1[string1[i]] = 1
        
        if string2[i] in letters2:
            letters2[string2[i]] += 1
        
        else: 
            letters2[string2[i]] = 1
    
    for i in range(len(string1)):
        if letters1[string1[i]] != letters2[string1[i]]:
            return -1
    
    return 1

string1 = 'nalesmas'
string2 = 'salesman'

print(solver(string1, string2))
        
