# TC : O(n^2)
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        if len(nums) < 3 :
            return False
        
        n = len(nums)
        i = float('inf')
        
        for j in range(n-1) :
            
            i = min(i, nums[j])
            
            for k in range(j+1, n) :
                if i < nums[k] < nums[j] :
                    return True
        
        return False

# TC : O(n)
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        st = [(float('inf'), float('inf'))] # (low, high)
        low = float('inf')
        
        for k in nums :
            low = min(low, k)
                
            # Remove invalid elements
            while st[-1][1] <= k :
                st.pop()
                
            if st[-1][0] < k :
                return True
                
            st.append((low, k))
                
        return False
    
