class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = Counter(s1)
        size = len(s1)
        l, r = 0, 0

        window_count = defaultdict(int)
        
        while r < len(s2):
            if r - l + 1 > size:
                window_count[s2[l]] -= 1
                l += 1
            window_count[s2[r]] += 1
            print(window_count, l, r)

            if r - l + 1 == size:
                match = True

                for letter, count in counts.items():
                    if window_count[letter] != count:
                        match = False
                
                if match:
                    return True

            r += 1

        return False