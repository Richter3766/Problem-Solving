class Solution:
    def decodeString(self, s: str) -> str:
        stack = ['']
        digit_stack = []
        cur_digit = 0
        for char in s:
            if char.isdigit():
                cur_digit = cur_digit * 10 + int(char)
            elif char == '[': 
                digit_stack.append(cur_digit)
                stack.append('')
                cur_digit = 0
            elif char == ']':
                new_char = stack.pop() * digit_stack.pop()
                stack[-1] += new_char
            else: stack[-1] += char
        print(
            stack
        )
        return stack.pop()