class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        s = set(nums)
        largest = 1

        for num in nums:
            if num - 1 not in s:
                length = 1
                curr = num + 1

                while curr in s:
                    curr = curr + 1
                    length += 1
                    largest = max(largest, length)
        
        return largest