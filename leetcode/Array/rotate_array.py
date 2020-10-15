class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if not nums :
            return
        
        n = len(nums)
        k = k%n
        
        start = cnt = 0
        
        while cnt < n :
            
            curr = start
            prev = nums[start]
            
            while True :
                _next = (curr+k)%n
                nums[_next], prev = prev, nums[_next]
                curr = _next
                cnt += 1
                
                if curr == start :
                    break
                    
            start += 1

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k%len(nums)
        
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        
