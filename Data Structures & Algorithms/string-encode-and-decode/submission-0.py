class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''

        for s in strs:
            res += (str(len(s)) + ';' + s)
        
        return res
    def decode(self, s: str) -> List[str]:
        print(s)
        curr = 0
        curr_len = ''
        res = []

        while curr < len(s):
            if s[curr] == ';':
                idx = curr + 1
                length = int(curr_len)

                res.append(s[idx:idx + length])
                curr = idx + length
                curr_len = ''
            else:
                curr_len += s[curr]
                curr += 1
        
        return res


        
