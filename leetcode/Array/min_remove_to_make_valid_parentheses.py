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
        
