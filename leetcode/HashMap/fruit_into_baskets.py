class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        
        start = output = 0
        bsk = collections.defaultdict(int)
        
        for end in range(len(tree)) :
            
            bsk[tree[end]] += 1
            
            while len(bsk) > 2 :
                
                bsk[tree[start]] -= 1
                
                if bsk[tree[start]] == 0 :
                    del bsk[tree[start]]
                    
                start += 1
            
            output = max(output, end-start+1)
            
        return output
                
