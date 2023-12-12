from collections import defaultdict, deque 

def solver(nums, k): 
    res = 0 
    l = 0 
    r = 0 
    count = defaultdict(deque)
    while r < len(nums): 
        count[nums[r]].append(r)
        while count[nums[r]][0] < l: 
            count[nums[r]].popleft()
        if len(count[nums[r]]) > k: 
            res = max(res, count[nums[r]][-2] - l + 1)
            l = max(l, count[nums[r]][0] + 1)
            count[nums[r]].popleft()
        else: 
            res = max(res, r - l + 1)
        r += 1 
    res = max(res, len(nums) - l)
    return res




nums = [1,2,3,1,2,3,1,2]
k = 2
nums = [1,2,1,2,1,2,1,2]
k = 1

nums = [5,5,5,5,5,5,5]
k = 4

nums = [1,2,2,1,3]
k = 1

nums = [8,94,6,67,61,99,52,20,39,12,93,67,96,18,79,68,92,75,29,83,67,14,74,60,30,1,87,20,8,72,54,32,36,26,47,73,93,50,57,21,12,89,73,12,65,58,10,5,57,85,22,16,39,47,20,48,83,21,6,53,76,61,69,81,13,84,11,33,86,19,79,84,4,9,96,62,30,54,77,40,4,97,42,58,70,71,38,31,13,37,26,89,13,71,78,50,70,26,41,67,59,74,9,48,48,61,78,21,81,3,95,54,88,37,65,39,100,34,65,31,25,96,34,83,65,15,23,97,95,98,38,29,69,18,36,76,74,47,66,43,30,84,68,53,37,4,50,73,99,59,33,58,82,28,13,50,82,52,14,39,69,44,72,54,44,61,66,45,72,98,54,62,46,52,40,21,63,88,75,32,4,62,1,27,41,19,61,32,94,65,74,33,96,41,78,12,79,73,86,98,50,57,19,11,63,97,81,80,37,2,98,6,48,76,72,95,87,34,27,64,86,21,4,67,74,89,14,17,99,100,95,44,89,51,41,12,1,31,44,28,18,82,32,98,31,45,34,69,65,94,81,10,98,62,20,74,11,45,53,11,79,40,92,61,99,11,9,73,55,12,33,100,35,15,25,55,41,99,93,19,45,35,52,29,12,25,2,1,89,50,63,26,100,63,47,47,61,75,95,21,26,17,58,10,65,65,96,88,56,29,13,18,82,6,45,48,23,61,75,74,21,77,42,79,98,20,12,7,24,70,88,30,86,65,2,18,94,72,75,83,96,58,19,72,16,1,6,69,84,30,45,81,47,90,50,27,51,23,49,38,79,63,30,82,51,91,88,26,15,14,95,61,63,45,87,3,28,23,42,9,69,12,22,6,37,1,63,94,66,56,42,5,24,49,85,49,7,70,64,72,84,9,95,31,34,36,24,63,67,94,16,87,15,63,67,51,48,26,14,73,46,9,71,44,45,99,16,81,65,9,24,9,8,55,74,88,81,62,48,61,94,96,50,87,82,61,97,65,64,65,56,51,36,37,89,72,62,68,21,1,21,26,16,43,26,75,49,35,40,1,89,12,25,87,87,100,57,38,25,2,36,33,73,39,86,39,42,61,77,59,72,29,40,73,85,20,62,4,10,51,72,1,42,3,41,17,50,48,5,95,50,45,73,61,64,57,91,14,23,46,18,42,35,22,24,85,83,24,78,73,59,80,82,82,80,100,41,40,39,34,54,52,2,78,65,27,10,41,18,71,66,24,40,22,78,59,59,62,71,43,26,85,97,39,92,19,71,10,8,92,44,8,30,82,95,64,82,52,72,39,58,14,89,99,100,22,14,58,32,85,53,4,87,14,76,36,38,97,3,8,67,62,40,83,56,100,12,4,15,85,37,58,22,14,65,78,76,69,12,67,20,31,57,94,85,52,68,23,84,82,13,63,25,2,99,28,7,36,95,81,15,4,1,34,89,3,77,94,12,78,9,98,33,1,63,71,67,17,52,70,28,27,87,23,86,29,7,72,69,72,77,71,82,46,95,89,49,62,52,39,74,63,87,47,90,15,37,17,84,36,10,14,75,100,46,81,98,13,15,56,20,72,42,42,51,24,92,8,94,19,7,36,46,19,7,11,43,99,34,21,78,9,72,6,93,23,22,5,67,22,51,47,54,100,31,29,65,58,74,16,91,11,3,20,90,21,11,68,43,55,40,32,11,88,41,6,51,85,97,40,85,29,87,28,32,92,91,93,84,66,2,93,11,28,89,61,58,45,99,25,4,25,97,65,21,19,97,26,76,14,34,13,56,1,78,51,98,67,6,65,74,41,50,63,91,99,81,91,33,86,5,28,18,77,74,70,10,46,13,18,66,84,59,17,13,11,95,95,25,72,74,70,50,85,23,100,6,82,29,57,53,25,39,40,41,50,60,83,78,23,22,20,18,22,21,50,22,7,21,79,59,83,48,23,61,15,25,37,59,27,63,62,33,61,45,68,24,14,68,27,69,90,65,30,45,68,81,10,46,9,58,36,59,67,85,61,6,32,19,88,35,25,26,5,70,47,65,38,23,13,75,81,70,91,39,63,43,84,6,53,64,14,83,5,37,28,69,33,17,20,6,77,61,79,68,42,58,75,20,38,41,3,30,96,69,81,71,64,65,15,17,37,60,100,72,98,23,63,38,36,39,4,33,62,5,12,88,80,14,18,61,97,17,74,87,70,36,29,95,3,13,50,45,48,61,72,68,60,69,62,46,41,46,5,80,90,29,95,15,4]
k = 4


print(solver(nums, k))