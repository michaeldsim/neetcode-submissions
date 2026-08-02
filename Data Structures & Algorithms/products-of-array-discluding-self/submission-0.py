class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1 for _ in range(len(nums))]
        post = [1 for _ in range(len(nums))]

        # pre 
        curr_prod = 1
        for i in range(len(nums)):
            if i == 0:
                continue
            
            curr_prod *= nums[i - 1]
            pre[i] = curr_prod
        
        curr_prod = 1
        for i in reversed(range(len(nums))):
            if i == len(nums) - 1:
                continue
            
            curr_prod *= nums[i + 1]
            post[i] = curr_prod
        
        res = [1 for _ in range(len(nums))]

        for i in range(len(res)):
            res[i] = pre[i] * post[i]
        
        return res