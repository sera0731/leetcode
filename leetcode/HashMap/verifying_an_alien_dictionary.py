class Solution:
    def validate(self, curr, _next) :
        
        n = min(len(curr), len(_next))
            
        for j in range(n) :
            if curr[j] != _next[j] :
                if self.dictionary[curr[j]] > self.dictionary[_next[j]] :
                    return False
                break
        else :
            if len(curr) > len(_next) :
                return False
            
        return True
        
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        if len(words) < 2 :
            return True
        
        self.dictionary = collections.defaultdict(int)
        
        for i in range(len(order)) :
            self.dictionary[order[i]] = i
        
        for i in range(len(words)-1) :
            if not self.validate(words[i], words[i+1]) :
                return False
        return True
            
        
