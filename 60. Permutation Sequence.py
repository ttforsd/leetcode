def gen_fac(n): 
    n -= 1
    res = [1] 
    for i in range(n - 1): 
        i += 2 
        res.append(i * res[-1])
    res.reverse()
    return res


def solver(n, k):
    factorials = gen_fac(n)
    nums = [i + 1 for i in range(n)]
    res = 0 
    for i in range(n - 1): 
        res *= 10 
        if k < factorials[i]: 
            res += nums[0] 
            del nums[0]
        else: 
            tmp = min((k -1)//factorials[i], len(nums) - 1)
            res += nums[tmp]
            del nums[tmp]
            if k % factorials[i] == 0: 
                for j in range(len(nums)): 
                    res *= 10 
                    res += nums[-1 - j]
                return res
        k = k % factorials[i] 
    res = res * 10 + nums[0]
    return res


print(solver(3, 4))