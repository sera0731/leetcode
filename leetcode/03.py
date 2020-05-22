class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        D = {}
        start, ans = 0, 0
        
        for i in range(len(s)) :
            
            if s[i] in D and D[s[i]] >= start :
                start = D[s[i]]+1
            else :
                ans = max(i-start+1, ans)
                
            D[s[i]] = i
            
        return ans