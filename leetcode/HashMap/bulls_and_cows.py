class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        bull = 0
        
        secret_d = collections.defaultdict(int)
        guess_d = collections.defaultdict(int)
        
        for i in range(len(guess)) :
            if secret[i] == guess[i] :
                bull += 1
            else :
                guess_d[guess[i]] += 1
                secret_d[secret[i]] += 1
            
        cow = 0
        
        for ch in guess_d :
            cow += min(guess_d[ch], secret_d[ch])
                
        return str(bull)+"A"+str(cow)+"B"
        
