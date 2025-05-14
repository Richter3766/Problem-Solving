class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag = ['' for _ in range(numRows)]

        cur = 0
        di = 1
        
        if numRows == 1:
            return s

        for i in range(len(s)):
            zigzag[cur] += s[i]
            if cur == 0 and di < 0:
                di = 1
            elif cur == numRows - 1 and di > 0:
                di = -1 
            cur += di
        
        return ''.join(zigzag)
