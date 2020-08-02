class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if len(word) < 2 :
            return True
        
        prev = word[1].isupper()
        
        for ch in word[2:] :
            if prev != ch.isupper() :
                return False
            
        if prev :
            return word[0].isupper()
            
        return True
                
        
