# when take index i out
# nums from i + 1 onwards: odd become even, even become odd 

def solver(nums): 
    start_odd = 0 
    start_even = 0 
    after_odd = 0 
    after_even = 0 
    count = 0 
    for i in range(len(nums)): 
        if (i + 1) % 2 == 0: 
            after_odd += nums[i] 
        else: 
            after_even += nums[i] 
    for i in range(len(nums)): 
        index = i + 1 
        if index % 2 == 1: 
            after_even -= nums[i] 
        else: 
            after_odd -= nums[i] 
        current_even = after_even + start_even
        current_odd = after_odd + start_odd 
        if current_even == current_odd: 
            count += 1 
        if index % 2 == 1: 
            start_odd += nums[i] 
        else: 
            start_even += nums[i]
    return count 

nums = [2,1,6,4]



def ans(nums): 
	even, odd = [0], [0]
	for i in range(len(nums)):
		if(i % 2):
			odd.append(odd[-1] + nums[i])
			even.append(even[-1])
		else:
			even.append(even[-1] + nums[i])
			odd.append(odd[-1])
	ans = 0
	for i in range(1, len(nums)+1):
		e_l, o_l = even[i-1], odd[i-1]
		e_r, o_r = even[-1]-even[i], odd[-1]-odd[i]
		if(e_l + o_r == e_r + o_l):
			ans += 1
	return ans

solver(nums)