# bfs but biased towards greater height



def solver(heightMap): 
    pass




def solver1(heightMap): 
    hor, vert = bounds(heightMap)
    volume = 0 
    for v in range(1, len(heightMap) - 1): 
        for h in range(1, len(heightMap[0]) - 1): 
            h_bound = hor[v][h]
            h_bound = min(h_bound)
            v_bound = vert[h][v]
            v_bound = min(v_bound)
            bound = min(v_bound, h_bound)
            volume += bound - heightMap[v][h]
    return volume


def bounds(map): 
    width = len(map[0])
    height = len(map)
    horizontal = [[[0,0] for _ in range(width)] for _ in range(height)]
    vertical = [[[0,0] for _ in range(height)] for _ in range(width)]
    for i in range(len(horizontal)): 
        for j in range(len(horizontal[0])): 
            if j == 0: 
                horizontal[i][j][0] = map[i][j]
                horizontal[i][-j-1][-1] = map[i][-j-1]
            else: 
                horizontal[i][j][0] = max(horizontal[i][j-1][0], map[i][j])
                horizontal[i][-j-1][-1] = max(horizontal[i][-j][-1], map[i][-j-1])
    for i in range(len(vertical)): 
        for j in range(len(vertical[0])): 
            if j == 0: 
                vertical[i][j][0] = map[j][i]
                vertical[i][-j-1][-1] = map[-1][i]
            else: 
                vertical[i][j][0] = max(vertical[i][j-1][0], map[j][i])
                vertical[i][-j-1][-1] = max(vertical[i][-j][-1], map[-j-1][i])
    return horizontal, vertical