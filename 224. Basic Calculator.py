def solver(s): 
    # if minus before bracket, - to +, + to - 
    s = s.replace(" ", "")
    sign = 1
    op = set(["-", "+"])
    # after - sign, check for (
    digits = [str(i) for i in range(10)]
    digits = set(digits)
    num = ""
    res = 0 
    ptr = 0 
    track = []
    addition = 1
    while ptr < len(s):
        if s[ptr] in digits: 
            num += s[ptr]
            ptr += 1
            continue 
        elif num: 
            num = int(num)
            num = num * sign * addition
            res += num
            num = ""
        if s[ptr] == "-" and s[ptr + 1] == "(": 
            sign *= -1 
            track.append(True)
            ptr += 1
            addition = True 
        elif s[ptr] == "-": 
            addition = -1
        elif s[ptr] == "+": 
            addition = 1
        elif s[ptr] == "(": 
            track.append(False)
        elif s[ptr] == ")": 
            tmp = track.pop()
            if tmp: 
                sign *= -1 
        ptr += 1
    if len(num) != 0: 
        num = int(num)
        num = num * addition * sign
        res += num
    return res 




s = "1-(     -2)"

print(solver(s))