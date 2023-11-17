def solver(ratings): 
    res = 1
    ptr = 0 # start of most recent descend 
    number = 1 
    for i in range(1, len(ratings)): 
        if ratings[i] > ratings[i - 1]: 
            number += 1
            res += number 
            ptr = i 
        elif ratings[i] == ratings[i-1]: 
            ptr = i 
            number = 1 
            res += number 
        else: 
            res += i - ptr 
            res += 1 
    return res


print(solver([1,2,2,3,2,1]))