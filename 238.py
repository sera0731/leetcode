# Time complexity : O(N)
# Space complexity : O(N)

# 1. Solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        L = [1]*len(nums)
        R = [1]*len(nums)
        answer = [0]*len(nums)
        
        n = len(nums)
        
        for i in range(1, n) :            
            L[i] = L[i-1] * nums[i-1]
            R[n-1-i] = R[n-i] * nums[n-i]
            
        for i in range(n) :
            answer[i] = L[i] * R[i]
            
        return answer
		
# 2. O(N) space solution

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        n = len(nums)
        answer = [1]*len(nums)
        
        for i in range(1, n) :            
            answer[i] = answer[i-1]*nums[i-1]
            
        R = 1
        
        for i in range(n-1, -1, -1) :
            answer[i] *= R
            R *= nums[i]
            
        return answer


