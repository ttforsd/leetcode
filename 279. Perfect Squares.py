from collections import deque

primes = [10000, 9801, 9604, 9409, 9216, 9025, 8836, 8649, 8464, 8281, 8100, 7921, 7744, 7569, 7396, 7225, 7056, 6889, 6724, 6561, 6400, 6241, 6084, 5929, 5776, 5625, 5476, 5329, 5184, 5041, 4900, 4761, 4624, 4489, 4356, 4225, 4096, 3969, 3844, 3721, 3600, 3481, 3364, 3249, 3136, 3025, 2916, 2809, 2704, 2601, 2500, 2401, 2304, 2209, 2116, 2025, 1936, 1849, 1764, 1681, 1600, 1521, 1444, 1369, 1296, 1225, 1156, 1089, 1024, 961, 900, 841, 784, 729, 676, 625, 576, 529, 484, 441, 400, 361, 324, 289, 256, 225, 196, 169, 144, 121, 100, 81, 64, 49, 36, 25, 16, 9, 4, 1]


def solver(n): 
    queue = deque()
    # in queue, store: n_left, steps 
    queue.append((n, 0))
    visited = set()
    while len(queue) != 0: 
        val, steps = queue.popleft()
        if val in visited or val < 0: 
            continue 
        visited.add(val)
        if val == 0: 
            return steps 
        for prime in primes: 
            if val - prime >= 0: 
                queue.append((val - prime, steps + 1))
    return -1 



