class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        total_prod = math.prod(nums)
        is_total_prod_zero = total_prod == 0
        last_zero_seen = -1
        nums_zero = 0
        if is_total_prod_zero:
            for ind, i in enumerate(nums):
                if i == 0:
                    nums_zero +=1
                    last_zero_seen = ind
        
        if nums_zero > 1:
            return [0 for i in range(len(nums))]
        
        elif nums_zero == 1:
            total_prod_without_zero = math.prod(nums[:last_zero_seen] + nums[last_zero_seen+1:])
            for i,val in enumerate(nums):
                nums[i] = 0
            nums[last_zero_seen] = total_prod_without_zero
            return nums
            
        for i, val in enumerate(nums):
            nums[i] = total_prod//val

        return nums
        