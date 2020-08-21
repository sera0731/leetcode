class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def dfs(i=0, curr=[]) :
            
            if len(curr) == n :
                output.append("".join(curr))
                return
                
            for ch in m[digits[i]] :
                dfs(i+1, curr+[ch])
        
        m = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        n = len(digits)
        
        output = []
        
        if digits :
            dfs()
            
        return output
            
            
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits :
            return []
        
        m = ["", "", "abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        n = len(digits)
        
        output = [""]
        
        for i in digits :
            curr = []
            num = int(i)
            for ch in m[num] :
                for x in output :
                    curr.append(x+ch)
                    
            output = curr
        
        return output
    
