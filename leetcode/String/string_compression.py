class Solution:
    def compress(self, chars: List[str]) -> int:
        
        if len(chars) < 2 :
            return len(chars)
        
        start = end = 0
        
        while end < len(chars) :
            
            current = chars[end]
            count = 0
            
            while end < len(chars) and current == chars[end] :
                count += 1
                end += 1
            
            chars[start] = current
            start += 1
            
            if count != 1 :
                for ch in str(count) :
                    chars[start] = ch
                    start += 1
                    
        return start
        
