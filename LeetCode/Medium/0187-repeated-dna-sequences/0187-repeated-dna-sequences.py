from collections import defaultdict, deque

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # A, C, G, T러 이루어진 문자열 DNA
        # DNA에선 특정 문자열이 반복적으로 나타난다.
        # 10자 길이로 반복적으로 나타나는 DNA 배열 전부 구하기

        # 길이 10의 슬라이딩 윈도우
        # 내부 문자열 기억 후 딕셔너리 저장
        # rolling hash 적용해보기
        if len(s) < 10:
            return []
            
        hash_table = {'A':0, 'C': 1, "G": 2, 'T': 3}
        mask = (1 << 20) - 1 # 한 글자가 2비트로 표현되고 10 글자이므로 2 * 10 = 20비트 사용
        cache = defaultdict(int)

        # 초기 해시
        window = 0
        for i in range(10):
            window = (window << 2) | hash_table[s[i]]

        # 슬라이딩 윈도우 이동
        for i in range(10, len(s)):
            cache[window] += 1
            window = ((window << 2) & mask) | hash_table[s[i]]
        cache[window] += 1 # 마지막 값도 포함하기

        answer = []
        for key in cache.keys():
            if cache[key] < 2: continue
            # 문자열로 만들기
            answer.append(self.decode_hash(key))
        
        return answer

    def decode_hash(self, target):
        unhash = ['A', 'C', 'G', 'T']
        result = []
        for _ in range(10):
            result.append(unhash[target & 3])
            target >>= 2
        return ''.join(reversed(result))