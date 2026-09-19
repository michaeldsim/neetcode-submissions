class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        curr = n

        while curr not in seen:
            seen.add(curr)
            sum = 0
            while curr > 0:
                digit = curr % 10
                sum += digit * digit
                curr = curr // 10
                
            if sum == 1:
                return True
            else:
                curr = sum
        
        return False
            


        