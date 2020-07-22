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
        
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        nums = [0]*10
        bull = cow = 0
        
        for i in range(len(secret)) :
            
            s = secret[i]
            g = guess[i]
            
            if s == g :
                bull += 1
            else :
                if nums[int(s)] < 0 :
                    cow += 1
                if nums[int(g)] > 0 :
                    cow += 1
                    
                nums[int(s)] += 1
                nums[int(g)] -= 1
                
        return '{}A{}B'.format(bull, cow)
                
