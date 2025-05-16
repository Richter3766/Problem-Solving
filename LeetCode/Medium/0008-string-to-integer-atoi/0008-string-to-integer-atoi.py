class Solution:
    def myAtoi(self, s: str) -> int:
        converted_i = self.atoi(s)
        answer = self.check_boundary(converted_i)

        return answer

    def atoi(self, s: str):
        s = s.lstrip()
        result = 0
        sign = 1
        digit_start = False

        for i in range(len(s)):
            cur = s[i]

            # if digit_start and not cur.isdecimal():
            #     break
            # # 1번 조건: whitespace 무시
            # if cur.isspace(): 
            #     continue
            # 2번 조건: 부호 결정
            if not digit_start and (cur == '+' or cur == '-'):
                sign = 1 if cur == '+' else -1
                digit_start = True
                continue
            elif not cur.isdigit():
                break

            # 해당되지 않는 실제 수라면 계산해주기
            result = result * 10 + int(cur)
            digit_start = True

        return result * sign

    def check_boundary(self, number):
        if number < -(2 ** 31):
            return -(2 ** 31)
        elif number > (2 ** 31) - 1:
            return (2 ** 31) - 1
        else: return number

    def atoi_refactor(self, s: str ,left_bound = -(2 ** 31), right_bound = (2 ** 31) - 1):
        # 1. 공백 제거
        s = s.lstrip()
        sign = 1 # 기본은 양수
        state = ParseState.START
        result = 0

        i = 0
        while i < len(s):
            cur_str = s[i]
            i += 1

            if state == ParseState.START and (cur_str == '+' or cur_str == '-'):
                sign = 1 if cur_str == '+' else -1
                continue
            if not cur_str.isdigit():
                break
            result = result * 10 + int(cur_str)

        return result * sign

from enum import Enum

class ParseState(Enum):
    START = 0
    SIGN = 1
    NUMBER = 2
    END = 3
