class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        st = []
        invalid = set()
        
        for i, ch in enumerate(s) :
            
            if ch == '(' :
                st.append(i)
            elif ch == ')' :
                if not st :
                    invalid.add(i)
                else :
                    st.pop()
        
        output = []
        invalid = invalid.union(set(st))
        
        for i in range(len(s)) :
            if i in invalid :
                continue
            output.append(s[i])
                
        return ''.join(output)
        
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        filtered = []
        l_total = l_extra = 0
        
        for ch in s :
            
            if ch == '(' :
                l_total += 1
                l_extra += 1
            elif ch == ')' :
                if l_extra == 0 :
                    continue
                l_extra -= 1
                
            filtered.append(ch)
            
        l_keep = l_total - l_extra
        
        for i, ch in enumerate(filtered) :
            if ch == '(' :
                l_keep -= 1
                if l_keep < 0 :
                    filtered[i] = ''
                    
        return ''.join(filtered)
        
