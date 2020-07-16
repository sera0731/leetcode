class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        idx = {}
        lol = start = 0
        
        for end in range(len(s)) :
            
            ch = s[end]
            
            if ch in idx and start <= idx[ch] :
                start = idx[ch]+1
            else :
                lol = max(lol, end-start+1)
                
            idx[ch] = end
                
        return lol
