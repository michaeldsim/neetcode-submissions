class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(path, index, total):
            if total == target:
                result.append(path[:])
                return

            for i in range(index, len(nums)):
                number = nums[i]
                if number + total > target:
                    continue
                
                path.append(number)
                backtrack(path, i, total + number)
                path.pop()
        
        backtrack([], 0, 0)
        return result