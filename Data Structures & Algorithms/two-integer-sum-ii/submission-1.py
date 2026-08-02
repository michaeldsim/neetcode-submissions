class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # naive solution is to just grab every possible pair in the list
        # O(n^2)

        # two pointer approach
        front, end = 0, len(numbers) - 1

        while front < end:
            if numbers[front] + numbers[end] == target:
                return [front + 1, end + 1]
            elif numbers[front] + numbers[end] > target:
                end -= 1
            else:
                front += 1
