class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        
        m = {}
        splited = str.split(' ')
        
        if len(pattern) != len(splited) :
            return False
        
        for i in range(len(pattern)) :
            
            p = pattern[i]
            s = splited[i]
            
            p_key = 'pattern_{}'.format(p)
            s_key = 'word_{}'.format(s)
            
            if p_key not in m :
                m[p_key] = i
            
            if s_key not in m :
                m[s_key] = i
                
            if m[p_key] != m[s_key] :
                return False
                
        return True
    
