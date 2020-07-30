# First approach
import collections

class Node :
    def __init__(self, char, num) :
        self.char = char
        self.number = num

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        
        count = defaultdict(int)
        encoded = []
        
        for ch in text :
            count[ch] += 1
        
        i = ans = 0
        
        while i < len(text) :
            
            curr = text[i]
            cnt = 1
            
            while i+1 < len(text) and text[i] == text[i+1] :
                cnt += 1
                i += 1
                
            encoded.append(Node(curr, cnt))
            ans = max(ans, cnt)
            
            i += 1
            
        i = 0 
        
        while i+2 < len(encoded) :
            
            if encoded[i].char == encoded[i+2].char :
                
                target = encoded[i+1]
                noch = encoded[i].number + encoded[i+2].number
                
                if target.number == 1 :
                    plus = 1 if count[encoded[i].char] > noch else 0
                    ans = max(ans, noch + plus)
                elif target.number >= 2 :
                    ans = max(ans, encoded[i].number+1, encoded[i+2].number+1)
                        
            i += 1
                        
        return ans
            
# Enhanced version
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        
        group = collections.defaultdict(list)
        
        for i in range(len(text)) :
            group[text[i]].append(i)
            
        longest = 0
        
        for ch in group :
            
            curr = 1
            prev = 0
            curr_longest = 0
            
            g = group[ch]
            
            for i in range(1, len(g)) :
                
                if g[i] == g[i-1]+1 :
                    curr += 1
                else :
                    prev = curr if g[i] == g[i-1]+2 else 0
                    curr = 1
                    
                curr_longest = max(curr_longest, prev+curr)
                
            plus = 1 if curr_longest < len(g) else 0
            longest = max(longest, curr_longest + plus)
        
        return longest
