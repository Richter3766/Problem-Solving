class Solution:
    def intToRoman(self, num: int) -> str:
        # 각 자릿수를 로마 문자로 바꾸기
        answer = ''

        # 1000
        q, num = divmod(num, 1000)
        answer += 'M' * q
        # 500
        q, r = divmod(num, 500)
        if q > 0 and r >= 400:
            answer += 'CM'
            num = num % 900
        else: 
            answer += 'D' * q
            num = r
        # 100
        q, num = divmod(num, 100)
        if q == 4:
            answer += 'CD'
        else: 
            answer += 'C' * q

        # 50
        q, r = divmod(num, 50)
        if q > 0 and r >= 40:
            answer += 'XC'
            num = num % 90
        else:
            answer += 'L'* q
            num = r
        
        # 10
        q, num = divmod(num, 10)
        if q == 4:
            answer += 'XL'
        else:
            answer += 'X' * q

        # 5
        q, r = divmod(num, 5)
        if q > 0 and r >= 4:
            answer += 'IX'
            num = num % 9
        else:
            answer += 'V' * q
            num = r

        # 1
        if num == 4:
            answer += 'IV'
        else: answer += 'I' * num          

        return answer
    