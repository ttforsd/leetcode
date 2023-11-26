def solver(ideas): 
    # compute swaps for first char of word on the fly 
    # dictionary group work by first char 
    # 2 layer dictionary 1: first char c1, set of word begin with c2 that can swap c1 
    count = 0 
    first_char = {} 
    for idea in ideas: 
        if idea[0] not in first_char: 
            first_char[idea[0]] = set() 
        first_char[idea[0]].add(idea[1:])
    two_layer = {} 
    chars = list(first_char)
    ideas = set(ideas)
    for i in range(len(chars)): 
        a = chars[i] 
        two_layer[chars[i]] = {}
        for j in range(i + 1, len(chars)):
            b = chars[j]
            common = len(first_char[a] & first_char[b])
            two_layer[a][b] = len(first_char[b]) - common
    for idea in ideas: 
        c0 = idea[0] 
        for char in chars: 
            if char == c0: 
                continue 
            if char + idea[1:] not in ideas and char in two_layer[c0]: 
                count += two_layer[c0][char]
    return count * 2


ideas = ["coffee","donuts","time","toffee"]

ideas = ["lack","back"]

print(solver(ideas))