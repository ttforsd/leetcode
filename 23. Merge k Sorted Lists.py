import heapq 

def solver(lists): 
    if len(lists) == 1: 
        return lists[0]
    for i in range(len(lists)): 
        lists[i] = (len(lists[i]), lists[i])
    heapq.heapify(lists)
    while len(lists) > 1:
        print(lists)
        l1 = heapq.heappop(lists)[-1]
        l2 = heapq.heappop(lists)[-1]
        new_list = [] 
        i = 0 
        j = 0 
        while i < len(l1) or j < len(l2): 
            if i < len(l1) and (j >= len(l2) or l1[i] < l2[j]):
                new_list.append(l1[i])
                i += 1
            else: 
                new_list.append(l2[j])
                j += 1 
        heapq.heappush(lists, (len(new_list), new_list.copy()))
    return lists[0][-1]


lists = [[],[]]

print(solver(lists))