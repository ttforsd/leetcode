def solver(strs): 
    dic = dict()
    for s in strs: 
        tmp = letter_freq(s)
        if tmp not in dic: 
            dic[tmp] = []
        dic[tmp].append(s)
    return dic.values()

def letter_freq(word): 
    freq = [0] * 26
    for s in word: 
        index = ord(s) - ord("a")
        freq[index] += 1 
    return tuple(freq)