class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = subsum = 0
        
        m = collections.defaultdict(int)
        m[0] = 1
        
        for v in nums :
            
            subsum += v
            
            if subsum-k in m :
                count += m[subsum-k]
                
            m[subsum] += 1
        
        return count
    
