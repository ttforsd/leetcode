def solver(n): 
    def recur(i, occupied): 
        count = 0 
        visited = set()
        for j in range(len(occupied)): 
            diff = i - j
            if occupied[j] + diff < n: 
                visited.add(occupied[j] + diff)
            if occupied[j] - diff >= 0: 
                visited.add(occupied[j] - diff)
            visited.add(occupied[j])
        for pos in range(n): 
            if pos not in visited and i == n - 1: 
                return 1
            if pos not in visited: 
                occupied.append(pos)
                count += recur(i + 1, occupied.copy())
                occupied.pop()
        return count 
    return recur(0, [])


while True: 
    n = int(input("Number: "))
    print(solver(n))