class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            base = nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                val = base + nums[left] + nums[right]
                print(left, right)
                if val == 0:
                    res.append([base, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif val > 0:
                    right -= 1
                else:
                    left += 1
            
        return res
 