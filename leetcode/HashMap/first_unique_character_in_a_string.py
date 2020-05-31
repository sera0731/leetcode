# Time complexity : O(N)
# Space complexity : O(N)

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        dic = {}
        
        for ch in s :
            dic[ch] = dic.get(ch, 0) + 1
        
        for i, ch in enumerate(s) :
            if dic[ch] == 1 :
                return i
        
        return -1
