def solver(s, t): 
    s = list(s)
    t = list(t) 
    while len(s) + len(t) != 0: 
        s_last, s = get_last(s)
        t_last, t = get_last(t)
        if s_last != t_last: 
            return False
    return True




# return last string and position
def get_last(s): 
    if len(s) == 0:
        return '', []
    if s[-1] != "#": 
        return s[-1] , s[:-1]
    back = 0 
    while len(s) != 0:
        current = s.pop()
        if current == "#": 
            back += 1 
        else: 
            if back > 0: 
                back -= 1 
            else: 
                return current, s
    return '', []
            


while True: 
    s = input("s: ")
    t = input("t: ")
    print(solver(s,t))