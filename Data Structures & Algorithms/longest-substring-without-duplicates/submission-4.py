class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        longest = 0
        l, r = 0, 0

        for r in range(len(s)):
            while s[r] in letters:
                letters.remove(s[l])
                l += 1
            
            letters.add(s[r])
            longest = max(longest, r - l + 1)

        return longest