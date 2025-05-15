class Solution:
    def reverse(self, x: int) -> int:
        revered_x = self.calculate_reverse(x)
        if self.check_range_outside(revered_x):
            return 0
        return revered_x
    
    def check_range_outside(self, x):
        if x > 2 ** 31 - 1:
            return True
        elif x < - (2 ** 31):
            return True
        return False

    def calculate_reverse(self, x):
        sign = 1 if x > 0 else -1
        cur = abs(x)
        reversed_x = 0

        while True:
            if cur == 0:
                return reversed_x * sign
            cur, r = divmod(cur, 10)
            reversed_x = reversed_x * 10 + r
