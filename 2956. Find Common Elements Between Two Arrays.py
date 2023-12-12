def solver(nums1, nums2): 
    a = 0 
    b = 0 
    n1 = set(nums1)
    n2 = set(nums2)
    for num in nums1: 
        if num in n2: 
            a += 1 
    for num in nums2: 
        if num in n1: 
            b += 1 
    return [a, b]