class Solution:
    def getWordCount(self, word) :
        
        cnt = []
        prev = ''
        
        for ch in word :
            if ch != prev :
                cnt.append([ch, 0])
            cnt[-1][1] += 1
            prev = ch
            
        return cnt
        
    def validate(self, stretched_word, word) :
        
        n = len(word)
        
        for i in range(n) :
            if stretched_word[i][0] != word[i][0] :
                return 0
            if stretched_word[i][1] < word[i][1] :
                return 0
            if stretched_word[i][1] < 3 and stretched_word[i][1] != word[i][1] :
                return 0
                
        return 1
        
    def expressiveWords(self, S: str, words: List[str]) -> int:
        
        output = 0
        stretched_word = self.getWordCount(S)
        
        for word in words :
            current = self.getWordCount(word)
            if len(current) != len(stretched_word) :
                continue
            output += self.validate(stretched_word, current)
            
        return output
        
