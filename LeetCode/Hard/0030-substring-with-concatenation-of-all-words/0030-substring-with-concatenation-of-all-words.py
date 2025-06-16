from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
            words로 만들 수 있는 모든 단어 조합을 만들면 
            최악의 경우 30!의 시간복잡도 생김.
            그러니 조합 만들지 않고 단어 조합을 만드는게 핵심 같음.

            문자열 탐색 시 길이가 최대 1만자리이므로 N^2만 되어도
            최악의 경우 시간이 오래 걸리게 될 것이므로
            N 탐색으로 끝내는 게 좋음

            즉, 문자열을 한 번만 읽고, 단어들의 조합인지 판단할 수 있는 알고리즘 고민이 필요

            슬라이딩 윈도우!
        """
        word_len = len(words[0])            # 단어 길이
        window_size = len(words) * word_len # 윈도우 크기(단어 길이 * 단어 수)
        words_counter = Counter(words)      # words에 등장하는 단어 수
        word_count = len(words)
        s_len = len(s)
        answer = [] # 정답 리스트

        for offset in range(word_len):
            left = offset   # 윈도우 왼쪽(조건에 맞으면 정답에 추가됨) 
            right = offset  # 윈도우 오른쪽(핵심 포인터)
            window_counter = defaultdict(int)   # 현재 윈도우 단어 카운팅 역할
            words_in_window = 0 # 윈도우 내 단어 수
            
            while right + word_len <= s_len:    # 윈도우가 단어 범위를 벗어나지 않았을 때
                word = s[right:right + word_len]
                right += word_len

                if word in words_counter:
                    window_counter[word] += 1
                    words_in_window += 1
                
                    # 단어 수가 words를 초과한다면 왼쪽을 당겨서 조정함
                    while window_counter[word] > words_counter[word]:
                        left_word = s[left:left + word_len]
                        window_counter[left_word] -= 1
                        left += word_len
                        words_in_window -= 1
                    
                    # 윈도우 내 단어수가 실제 단어 수와 같으면 정답 처리
                    if words_in_window == word_count:
                        answer.append(left)
                else:
                    window_counter.clear()
                    words_in_window = 0
                    left = right

        return answer
