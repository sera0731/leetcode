class Solution:
    def __init__(self) :
        self.s = ''
        self.memo = {}
        self.set = set()
        
    def helper(self, start=0) :
        
        if start == len(self.s) :
            return True
        if start in self.memo :
            return self.memo[start]
        
        for i in range(start+1, len(self.s)+1) :
            if self.s[start:i] in self.set and self.helper(i) :
                self.memo[start] = True
                return True
        
        self.memo[start] = False
        return False
        
        
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.s = s
        self.set = set(wordDict)
        
        return self.helper()
        
