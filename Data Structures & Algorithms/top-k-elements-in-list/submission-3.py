class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in c.items():
            buckets[count].append(num)
        
        res = []
        for bucket in reversed(buckets):
            if bucket:
                for num in bucket:
                    res.append(num)

                    if len(res) == k:
                        return res
        
        return -1
