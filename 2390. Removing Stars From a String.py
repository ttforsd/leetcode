def solver(s): 
    s = list(s) 
    erase = 0 
    result = []
    while len(s) > 0: 
        current = s.pop()
        if current == "*": 
            erase += 1 
        else: 
            if erase > 0: 
                erase -= 1 
            else: 
                result.insert(0, current)
    return "".join(result)



while True: 
    s = input("string: ")
    print(solver(s))