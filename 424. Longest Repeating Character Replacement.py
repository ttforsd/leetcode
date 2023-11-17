from collections import defaultdict

def solver(s, k): 
    l = 0 
    r = 0 
    ft = defaultdict(int)
    res = 0 
    while r < len(s): 
        ft[s[r]] += 1 
        while len(ft) > k + 1 or sum(ft.values()) - max(ft.values()) > k: 
            ft[s[l]] -= 1
            if ft[s[l]] == 0: 
                del ft[s[l]]
            l += 1
        res = max(res, r - l + 1)
        r += 1 
    return res


s = "KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"
k = 4

s = "AABABBA"

k = 1

print(solver(s,k))