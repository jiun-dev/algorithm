# 링크 : https://leetcode.com/problems/reverse-integer/submissions/

class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            x = int(str(x)[::-1])
        else:
            x =  -1 * int(str(x*-1)[::-1])
        
        if x not in range(-2**31,2**31):
            x = 0
            
        return x
        
