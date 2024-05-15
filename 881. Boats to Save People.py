from collections import Counter
from bisect import bisect_right


def solver(people, limit): 
    res = 0 
    people.sort() 
    while people: 
        total = people[-1]
        people.pop(-1)
        res += 1
        if people and total + people[0] <= limit: 
            index = bisect_right(people, limit - total) 
            total += people[index - 1] 
            people.pop(index - 1) 
    return res 


people = [3,5,3,4]
limit = 5

people = [3,2,2,1]
limit = 3 

people = [2,2]
limit = 6

people = [1,2,3,4,5,4,9]
limit = 12

print(solver(people, limit))