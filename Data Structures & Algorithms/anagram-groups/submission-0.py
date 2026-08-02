class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            key = sorted(s)
            skey = ''.join(key)

            d[skey].append(s)
        
        res = []

        for v in d.values():
            res.append(v)

        return res