class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        s_values = sorted(c.items(), key=lambda item:item[1], reverse=True)

        res = []

        for v in s_values:
            res.append(v[0])

            if len(res) == k:
                break

        return res