def solver(matrix): 
    n = len(matrix)
    m = len(matrix[0])
    total = n * m 
    counter = 0 
    l = 0 
    r = m - 1
    top = 0 
    bottom = n - 1
    horizontal = True 
    order = True
    result = []
    x, y = 0, 0
    while True: 
        result.append(matrix[x][y])
        counter += 1 
        if counter == total: 
            return result
        if horizontal and order: 
            if r == y: 
                horizontal = False 
                top += 1 
                x += 1 
            else: 
                y += 1 
        elif not horizontal and order: 
            if x == bottom: 
                horizontal = True
                order = False 
                y -= 1 
                r -= 1
            else: 
                x += 1
        elif horizontal and not order: 
            if l == y: 
                horizontal = False
                order = False 
                x -= 1 
                bottom -= 1 
            else: 
                y -= 1 
        else: 
            if x == top: 
                horizontal = True
                order = True
                l += 1
                y += 1 
            else: 
                x -= 1 