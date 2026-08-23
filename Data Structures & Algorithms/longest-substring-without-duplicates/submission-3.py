class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        longest = 0
        l, r = 0, 0

        for r in range(len(s)):
            if s[r] in letters:
                while s[l] != s[r]:
                    letters.remove(s[l])
                    l += 1
            
                letters.remove(s[l])
                l += 1
            letters.add(s[r])
            longest = max(longest, r - l + 1)

        return longest