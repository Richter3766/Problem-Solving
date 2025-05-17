class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0: return True
        if x < 0: return False # 음수는 불가능 - 때문에
        if x % 10 == 0: return False # 10의 배수는 뒤집으면 1이 나오므로 False
        
        left = x
        right = 0
        while True:
            left, r = divmod(left, 10)
            right = right * 10 + r
            if right >= left: break
        
        if right == left: return True
        if right // 10 == left: return True
        return False
        