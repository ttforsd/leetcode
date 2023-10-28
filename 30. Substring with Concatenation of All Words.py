def make_table(words): 
    table = {} 
    for word in words: 
        if word not in table: 
            table[word] = 1 
        else: 
            table[word] += 1
    return table 
def solver(s, words): 
    res = []
    seeds = [] 
    word_len = len(words[0])
    num_of_words = len(words)
    words = make_table(words)
    def rm_table(table,word): 
        if word in table: 
            table[word] -= 1
        if table[word] == 0: 
            del table[word]
    for i in range(len(s) - word_len * num_of_words + 1): 
        print(s[i: i + word_len])
        if s[i: i + word_len] in words: 
            seeds.append(i)
    for index, item in enumerate(seeds): 
        working_table = words.copy()
        while len(working_table) != 0: 
            if s[item: item + word_len] not in working_table: 
                break 
            rm_table(working_table, s[item: item + word_len])
            item += word_len

        if len(working_table) == 0: 
            res.append(seeds[index])
    return res
            


s = "barfoofoobarthefoobarman"

words = ["bar","foo","the"]

print(solver(s, words))