def parse(s): 
    s = s.split(".")
    for i in range(len(s)): 
        s[i] = int(s[i])
    ptr = len(s) - 1 
    while s[ptr] == 0 and ptr > 0: 
        ptr -= 1 
    return s[:ptr + 1]

def solver(version1, version2): 
    version1 = parse(version1)
    version2 = parse(version2)
    for i in range(len(version1)):
        if i < len(version2): 
            if version1[i] > version2[i]: 
                return 1
            elif version1[i] < version2[i]: 
                return -1

    if len(version1) > len(version2): 
        return 1 
    elif len(version1) < len(version2): 
        return -1 
    return 0 
        




version1 = "0.0"
version2 = "1.001"
print(solver(version1, version2))