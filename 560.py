# Time complexity : O(N)
# Space complexity : O(N)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        dic = collections.defaultdict(int)
        dic[0] = 1
        
        subsum = 0
        count = 0
        
        for n in nums :
            subsum += n
            target = subsum-k
            
            if target in dic :
                count += dic[target]
                
            dic[subsum] += 1
            
        return count
        
