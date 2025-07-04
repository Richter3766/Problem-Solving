class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        히스토그램에서 가장 큰 직사각형 찾기

        투포인터? 슬라이딩 윈도우?

        직사각형 넓이 = 포인터 사이의 값 중 최솟값 * 포인터 간 거리
        포인터 사이 중 최솟값 정보를 알고 있는 것이 좋으므로 슬라이딩 윈도우도 유효함
        -> 인 줄 알았으나 실패

        스택을 활용한 풀이
        1. 모든 막대를 순차적으로 검사 - 인덱스 i
        2. 현재 막대가 스택의 top 막대의 길이보다 길면 push
        -> 스택에 먼저 담긴 막대들이 폭의 왼쪽 경계가 됨.
        3. 현재 막대가 스택의 top 막대의 길이보다 작으면 pop
        -> 현재 막대가 스택 내부 막대로 만드는 폭의 오른쪽 경계가 됨.
        2, 3 과정을 모든 막대를 검사하고, stack이 비어있을 때까지 반복
        """
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            height = heights[i]
            while True:
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
