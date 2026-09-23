class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            letters = list(word)
            letters.sort()

            groups[tuple(letters)].append(word)
        
        res = []

        for value in groups.values():
            res.append(value)
        
        return res
