def solver(s, wordDict): 
    wls = set([len(w) for w in wordDict])
    ws = set(wordDict)
    memo = {}
    def recur(i): 
        if i in memo: 
            return memo[i] 
        if i == 0: 
            return True 
        if i < 0: 
            return False 
        result = False
        for wl in wls: 
            if s[i - wl: i] in ws:
                result = result or recur(i - wl)
        memo[i] = result 
        return result
    return recur(len(s))


s = "a"

wordDict = ["a","code"]

s = "leetcode"
wordDict = ["leet","code"]

s ="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]


print(solver(s, wordDict))