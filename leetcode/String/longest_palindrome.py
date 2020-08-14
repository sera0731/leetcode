class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        freq = collections.defaultdict(int)
        
        for ch in s :
            freq[ch] += 1
        
        odd = 0
        
        for ch in freq :
            if freq[ch] & 1 :
                odd += 1
                
        return len(s) - odd + bool(odd)
    
