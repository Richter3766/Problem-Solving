class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ''
        
        index_range = min(len(s) for s in strs)
        for i in range(index_range):
            cur_prefix = strs[0][i]
            is_common = True
            for string in strs:
                if string[i] != cur_prefix:
                    is_common = False
                    break
            if is_common: answer += cur_prefix
            else: break
        
        return answer