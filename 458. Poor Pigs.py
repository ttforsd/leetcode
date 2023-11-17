def solver(buckets, die, test):
    if buckets == 1: 
        return 0 
    runs = test // die 