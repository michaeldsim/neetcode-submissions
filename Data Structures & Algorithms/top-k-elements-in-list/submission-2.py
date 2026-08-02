class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        h = []
        
        for num, count in c.items():
            heapq.heappush(h, (count, num))

            if len(h) > k:
                heapq.heappop(h)
        
        return [num for count, num in h]