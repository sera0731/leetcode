class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        if t < 0 :
            return False
        
        buckets = {}
        w = t+1
        
        for i, v in enumerate(nums) :
            
            bn = v//w
            
            if bn in buckets:
                return True
            if bn+1 in buckets and abs(buckets[bn+1]-v) <= t:
                return True
            if bn-1 in buckets and abs(buckets[bn-1]-v) <= t:
                return True
            
            buckets[bn] = v
            
            if i >= k :
                del buckets[nums[i-k]//w]
                
        return False
    