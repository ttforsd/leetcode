def solver(s): 
    if len(s) == 0: 
        return ""
    odd_seed = [(i, i) for i in range(len(s))] 
    odd_longest = s[0]
    even_longest = ""
    even_seed = [] 
    for i in range(len(s) - 1): 
        if s[i] == s[i + 1]: 
            even_seed.append((i, i + 1))
    if len(even_seed) != 0: 
        start, end = even_seed[0]
        even_longest = s[start: end + 1]
    while len(odd_seed) + len(even_seed) != 0: 
        tmp = []
        for i in range(len(odd_seed)): 
            start, end = odd_seed[i] 
            start -= 1 
            end += 1 
            if start < 0 or end >= len(s) or s[start] != s[end]: 
                continue 
            tmp.append((start, end))
            odd_longest = s[start: end + 1]
        odd_seed = tmp.copy()
        
        tmp = [] 
        for i in range(len(even_seed)): 
            start, end = even_seed[i] 
            start -= 1 
            end +=1
            if start < 0 or end >= len(s) or s[start] != s[end]: 
                continue 
            tmp.append((start, end))
            even_longest = s[start: end + 1]
        even_seed = tmp.copy()
    return max(even_longest, odd_longest, key=len)
    
            
        
        

        
s = "babad"


print(solver("cbbd"))


s = "crbidxnkyieminyzchamldzjzglygkfbbyggagwdqdqamzpguppqjfrcewfduwvcmhliahovcwoupwxwhaoiiiguahuqxiqndwxqxweppcbeoasgtucyqlxnxpvtepwretywgjigjjuxsrbwucatffkrqyfkesakglyhpmtewfknevopxljgcttoqonxpdtzbccpyvttuaisrhdauyjyxgquinvqvfvzgusyxuqkyoklwslljbimbgznpvkdxmakqwwveqrpoiabmiegoyzuyoignfcgmqxvpcmldivknulqbpyxjuvyhrzcsgiusdhsogftokekbdynmksyebsnzbxjxfvwamccphzzlzuvotvubqvhmusdtwvlsnbqwqhqcigmlfoupnqcxdyflpgodnoqaqfekhcyxythaiqxzkahfnblyiznlqkbithmhhytzpcbkwicstapygjpjzvrjcombyrmhcusqtslzdyiiyvujnrxvkrwffwxtmdqqrawtvayiskcnpyociwkeopardpjeyuymipekbefbdfuybfvgzfkjtvurfkopatvusticwbtxdtfifgklpmjamiocalcocqwdivyulupammxhdbeazrrktxiyothnvbwwrsocxzxaxmoenigbhvxffddexrwsioqoyovaqvtmkwzupstkgkmvrddzolmuzjnsj"

print(solver(s))