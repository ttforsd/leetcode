def solver(citations): 
    while len(citations) != 0: 
        if citations[0] == 0: 
            citations.pop(0)
        else: 
            break
    if len(citations) == 0: 
        return 0
    pubs = len(citations)
    if citations[0] >= pubs: 
        return pubs
    l = 0 
    r = pubs - 1 
    m = r // 2
    while True: 
        pre = citations[m-1]
        curr = citations[m] # min cite
        if pubs - m <= curr and pubs - (m -1) > pre: 
            return pubs - m 
        if pubs - m < curr: 
            r = m
        else: 
            l = m + 1
        m = (l + r) //2


print(solver([1,1]))