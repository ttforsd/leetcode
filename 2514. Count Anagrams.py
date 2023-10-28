def solver(s): 
    s = s.split()
    for i in range(len(s)): 
        s[i] = sorted(s[i])



def word_freq(words): 
    dic = {} 
    for word in words: 
        if word not in dic: 
            dic[word] = 1 
        else: 
            dic[word] += 1 
    return dic 