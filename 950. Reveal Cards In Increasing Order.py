from math import ceil, floor

def solver(deck): 
    deck.sort() 
    l = len(deck)
    def recur(start: int, use_next: bool):
        if len(deck) - start <= 2 and use_next: 
            return deck[start:]
        elif len(deck) - start <= 2: 
            res = deck[start:]
            res = res[::-1]
            return res 
        
        if use_next: 
            mid_pt = ceil((start + l) / 2)
            first_half = deck[start:mid_pt] 
            second_half = recur(mid_pt, (l - start) % 2 == 0)
        else: 
            mid_pt = floor((start + l) / 2)
            second_half = deck[start:mid_pt]
            first_half = recur(mid_pt,  (l - start) % 2 == 1)

        # merge 
        res = [] 
        for i in range(len(first_half)): 
            res.append(first_half[i])
            if i < len(second_half): 
                res.append(second_half[i])
        return res
    
    return recur(0, True)


deck = [1,2,3]

deck = [2,11,3,17,5,13,7]

deck = [i for i in range(10000)]

print(solver(deck))