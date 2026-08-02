class Solution:
    def trap(self, height: List[int]) -> int:
        max_l = [0 for _ in range(len(height))]
        max_r = [0 for _ in range(len(height))]
        values = [0 for _ in range(len(height))]

        for i in range(len(height)):
            if i == 0:
                continue
            
            max_l[i] = max(max_l[i - 1], height[i - 1])

        for i in range(len(height) - 2, -1, -1):
            max_r[i] = max(max_r[i + 1], height[i + 1])
        
        res = 0

        for i in range(len(values)):
            water = min(max_l[i], max_r[i]) - height[i]

            if water > 0:
                res += water
        
        return res
        