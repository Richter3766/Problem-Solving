class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        1로된 가장 큰 직사각형 찾기
        이전의 히스토그램 방식과 유사함이 느껴짐

        행 단위로 이전의 해결 방식 활용 가능
        이전 행의 계산을 재사용할 수 있을까?
        """
        # heigths 계산
        # 공간복잡도 최소화를 위해 이전 행만 기억하여 활용
        row_len = len(matrix)
        col_len = len(matrix[0])
        before = [0] * col_len
        max_area = 0
        for r in range(row_len):
            heights = [0] * col_len
            for c in range(col_len):
                # 현재 값이 0이면 셀 필요 없음
                if matrix[r][c] == "0":
                    continue

                # 이전 값이 0이 아니면 이전값 - 1
                if before[c] != 0:
                    heights[c] = before[c] - 1
                    continue

                # 이전 값이 0이면 새롭게 세기
                count = 1
                for nr in range(r + 1, row_len):
                    if matrix[nr][c] == "0":
                        break
                    count += 1
                heights[c] = count
            cur_area = self.find_max_area(heights)
            max_area = max(max_area, cur_area)
            # print(heights)
            before = heights    # 현재 높이를 이전 높이로 설정

        return max_area

    def find_max_area(self, heights):
        # 여기서 hegiths는 해당 행 기준으로 아래 행에 있는 1의 개수를 센 것
        # 이전 문제와 비슷하게 stack을 활용해 최대 넓이 계산
        stack = [-1]
        max_area = 0
                
        for i in range(len(heights)):
            # 스택이 비어있거나 오른쪽 경계가 아닌 경우
            height = heights[i]
            if len(stack) == 1 or height >= heights[stack[-1]]:
                stack.append(i)
                continue
            
            # 현재 막대가 오른쪽 경계가 될 때
            # stack의 마지막 막대를 꺼내어 넓이 계산    
            while True:
                # 현재 막대가 오른쪽 경계가 아니게 되면 스택에 추가 후 넘어가기
                if len(stack) == 1 or height >= heights[stack[-1]]:
                    stack.append(i)
                    break

                cur_stick = stack.pop()
                width = i - (stack[-1] + 1)
                max_area = max(max_area, width * heights[cur_stick])

        while len(stack) > 1:
            cur_stick = stack.pop()
            width = len(heights) - (stack[-1] + 1)
            max_area = max(max_area, width * heights[cur_stick])

        return max_area
