def solver(flowers, people): 
    start = [] 
    end = [] 
    for b,w in flowers: 
        start.append(b)
        end.append(w)
    start.sort()
    print(start)
    end.sort()
    print(end)
    result = [] 
    for p in people: 
        print("p", p)
        n = binsearchstart(start,p) - binsearchend(end,p)
        result.append(n)
    return result


# given time and flower, return position
def binsearchstart(flowers, time): 
    if time < flowers[0]: 
        return 0
    if time >= flowers[-1]: 
        return len(flowers)
    # return m if flowers[m] < time and flowers[m+1] >= time 
    l = 0
    r = len(flowers) - 1
    m = (l + r) // 2 
    while True: 
        print(l, m, r, "|", flowers[l], flowers[m], flowers[r])
        if flowers[m] <= time and flowers[m + 1] > time: 
            return m + 1 
        if flowers[m] <= time: 
            l = m 
        else: 
            r = m
        m = (r + l) //2
case = [[1,6],[3,7],[9,12],[4,13], [1,7], [1,8], [3,4]]

# return flowers wilted 
def binsearchend(flowers, time):
    if time > flowers[-1]: 
        return len(flowers)
    if time <= flowers[0]: 
        return 0 
    l = 0 
    r = len(flowers) - 1
    m = (l + r) // 2
    while True: 
        print(l, m, r, "|", flowers[l], flowers[m], flowers[r])
        # return m + 1 if flowers[m] < time and flowers[m+1] >= time 
        if flowers[m] < time and flowers[m+1] >= time: 
            return m + 1 
        if flowers[m] < time: 
            l = m 
        else: 
            r = m 
        m = (r + l) // 2 


flowers = [[1,6],[3,7],[9,12],[4,13]]

people = [2,3,7,11]
