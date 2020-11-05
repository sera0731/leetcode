class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        output = max_cnt = start = 0
        count = collections.defaultdict(int)
        
        for end in range(len(s)) :
            
            count[s[end]] += 1
            max_cnt = max(max_cnt, count[s[end]]) 
            
            # Replace 해야 하는 글자 수가 k보다 클 경우 start를 오른쪽으로 이동.
            if (end - start + 1) - max_cnt > k  :
                count[s[start]] -= 1
                start += 1
            
            output = max(output, end - start + 1)
                
        return output
                
