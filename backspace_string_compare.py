# Time complexity : O(M+N)
# Space complexity : O(M+N)

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        def backspace(A):
            
            result = []
            
            for ch in A :
                if ch != '#':
                    result.append(ch)
                elif result :
                    result.pop()
                    
            return ''.join(result)
        
        return backspace(S) == backspace(T)
