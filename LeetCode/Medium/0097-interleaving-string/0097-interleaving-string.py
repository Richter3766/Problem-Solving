class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        문자열 엮기

        s1, s2, s3에 대한 포인터를 각각 관리하기
        s3를 하나씩 읽으면서 s1, s2에 있는 문자열인지 검사?

        포인터 읽는 순서에 따라 가능한데 불가능하게 보일수도 있음
        이 경우 해당 경우의 수를 전부 탐색하는 게 맞아 보임
        -> DFS 활용
        -> 불필요한 탐색 줄이기 위해 메모이제이션 적용
        """
        if len(s1) + len(s2) != len(s3):
            return False

        cache = {}

        def interleave(p1, p2):
            # 이미 탐색한 경우 리턴
            if (p1, p2) in cache:
                return cache[(p1, p2)]
            
            # 끝에 다다랐으면 종료
            p3 = p1 + p2
            if p3 == len(s3):
                return True

            # p1의 값이 같을 때
            if p1 < len(s1) and s1[p1] == s3[p3]:
                if interleave(p1 + 1, p2):
                    return True
        
            # p2의 값이 값을 때
            if p2 < len(s2) and s2[p2] == s3[p3]:
                if interleave(p1, p2 + 1):
                    return True
            
            # 캐시에 결과 저장
            cache[(p1, p2)] = False
            return False

        return interleave(0, 0)

