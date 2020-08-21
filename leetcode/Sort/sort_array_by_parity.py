class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        q = collections.deque([])
        
        for n in A :
            if n & 1 :
                q.append(n)
            else :
                q.appendleft(n)
        
        return list(q)
        
  class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        n = len(A)
        l, r = 0, n-1
        
        while l < r :
            if A[l] & 1 :
                A[l], A[r] = A[r], A[l]
                r -= 1
            else :
                l += 1
        
        return A
            
