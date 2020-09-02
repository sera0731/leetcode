class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        if t < 0 :
            return False
        
        bucket = {}
        w = t+1
        
        for i in range(len(nums)) :
            
            id = nums[i] // w
            
            if id in bucket : 
                return True
            
            if id+1 in bucket and abs(bucket[id+1]-nums[i]) <= t :
                return True
            
            if id-1 in bucket and abs(bucket[id-1]-nums[i]) <= t :
                return True
            
            bucket[id] = nums[i]
            
            if i >= k :
                del bucket[nums[i-k]//w]
                
        return False
    
