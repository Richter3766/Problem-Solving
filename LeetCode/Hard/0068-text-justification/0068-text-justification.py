class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def make_word(cur):
            if len(cur) == 1:
                return ''.join(cur).ljust(maxWidth)
            string = ''
            cur_word_len = sum(len(w) for w in cur)
            space_count = maxWidth - cur_word_len

            default_space = space_count // (len(cur) - 1)
            extra_space = space_count % (len(cur) - 1)

            for i in range(len(cur)):
                string += cur[i]
                if i < extra_space:
                    string += ' '
                if i != len(cur) - 1:
                    string += ' ' * default_space

            return string

        answer = []
        
        cur = []
        for word in words:
            # 언제 스택에 단어를 넣는가
            # 1. 넣어도 maxWidth를 넘지 않을 때
            # 2. 단어 간 패딩이 충분할 때
            total_word_len = sum(len(c) for c in cur)
            space_slot = len(cur) - 1
            word_len = len(word)
            if total_word_len + space_slot + word_len < maxWidth:
                cur.append(word)
 
            # 언제 새로운 스택을 구성하는가
            # 1. maxWidth를 넘을 때
            # 2. 단어를 넣었을 때 패딩이 충분하지 않은 경우
            else:
                sentence = make_word(cur)
                answer.append(sentence)
                cur = [word]
                
        # 마지막 단어는 ljust로 구성
        sentence = ' '.join(cur).ljust(maxWidth)
        answer.append(sentence)
        return answer