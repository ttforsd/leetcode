import numpy as np 

def solver(s, shifts): 
    l = len(s) 
    arr = np.zeros(l, dtype=int)
    for shift in shifts: 
        if shift[-1] == 0: 
            change = 25 
        else: 
            change = 1 
        c_array = np.zeros(l, dtype=int)
        c_array[shift[0]: shift[1] + 1] = change 
        arr += c_array
    res = ""
    print(arr)
    for i in range(l): 
        c = ord(s[i]) - ord('a') 
        c = (c + arr[i]) % 26
        res += chr(c + ord("a"))
    return res


s = "abc"

shifts = [[0,1,0],[1,2,1],[0,2,1]]

s = "dztz"
shifts = [[0,0,0],[1,1,1]]

print(solver(s, shifts))