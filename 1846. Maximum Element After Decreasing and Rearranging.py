def solver(arr): 
    arr.sort() 
    arr[0] = 1 
    for i in range(1, len(arr)): 
        prev = arr[i - 1]
        arr[i] = min(prev + 1, arr[i])
    return arr[-1]

arr = [100,1,1000,43534,23,3,4,3,5,6,7,8]

print(solver(arr))