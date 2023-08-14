def solver1(nums1, nums2):
    nums = []
    while len(nums1) + len(nums2) != 0: 
        if len(nums1) == 0: 
            nums += nums2
            break
        elif len(nums2) == 0: 
            nums += nums1
            break
        if nums1[0] <= nums2[0]: 
            nums.append(nums1.pop(0))
        else: 
            nums.append(nums2.pop(0))
    l = len(nums) 
    if l % 2 == 1: 
        return nums[l//2]
    return (nums[l//2] + nums[l//2 -1]) /2

def solver(nums1, nums2): 
    total = len(nums1) + len(nums2)
    half = total //2 - 1 
    l1 = 0 
    l2 = 0 
    r1 = min(len(nums1), half) - 1
    r2 = min(len(nums2), half) - 1
    while half > 0: 
        if nums1[l1] >= nums2[r2]: 
            half -= r2 + 1 
            nums2 = nums2[r2 + 1:]
            r2 = min(len(nums2), half) - 1
        elif nums2[l2] >= nums1[r1]: 
            half -= r1 + 1 
            nums1 = nums1[r1 + 1:]
            r1 = min(len(nums1), half) - 1
        elif nums1[r1] <= nums2[r2]: 
            pass

nums1 = [1,1,1]
nums2 = [3,4,6,7,8,9]
print(solver(nums1, nums2))