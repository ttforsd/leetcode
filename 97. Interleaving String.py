def solver(s1, s2, s3): 
    target_len = len(s3)
    memo = {}
    def recur(i, j, k): 
        if k == target_len: 
            return True 
        if (i, j, k) in memo: 
            return memo[(i,j,k)]
        if i == len(s1) and j == len(s2): 
            return False 
        if i == len(s1): 
            if s3[k] != s2[j]: 
                return False 
            memo[(i,j,k)] = recur(i, j + 1, k + 1)
            return memo[(i,j,k)]
        if j == len(s2): 
            if s3[k] != s1[i]: 
                return False 
            memo[(i,j,k)] = recur(i + 1, j, k + 1)
            return memo[(i,j,k)]
        if i < len(s1) and s1[i] == s3[k] and s2[j] != s3[k]: 
            memo[(i,j,k)] = recur(i + 1, j, k + 1)
            return memo[(i,j,k)]
        if j < len(s2) and s2[j] == s3[k] and s1[i] != s3[k]: 
            memo[(i,j,k)] = recur(i, j + 1, k + 1)
            return memo[(i,j,k)]
        result = False 
        if s1[i] == s2[j] == s3[k]: 
            if i < len(s1): 
                result = result or recur(i + 1, j, k + 1)
            if j < len(s2):
                result = result or recur(i, j+1, k + 1) 
        memo[(i,j,k)] = result
        return result
    return recur(0,0,0)
    
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"

s1 = "aabccabc"
s2 = "dbbabc"
s3 = "aabdbbccababcc"

print(solver(s1, s2, s3))