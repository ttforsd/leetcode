def solver(costs, k, n): 
    ans = 0 
    while k > 0: 
        k -= 1 
        if len(costs) <= k: 
            i = costs.index(min(costs))
        else:
            left = costs[:n]
            right = costs[-n:]
            left_min = min(left)
            right_min = min(right)
            if right_min < left_min: 
                i = right.index(right_min)
                i = len(costs) - (n - i) 
            else: 
                i = left.index(left_min)
        ans += costs.pop(i)
    return ans


costs = [1,2,4,1,4,2,3,4,5,6,4,3,345,34,4,5,34,23,4,3,5,3,4,5,6777,5,45,4,3]
k = 9
n = 10

print(solver(costs, k, n))