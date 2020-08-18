# DFS
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        
        def dfs(curr, i) :
            
            if i == N :
                output.append(curr)
                return
            
            last = curr % 10
            
            for _next in set([last + K, last - K]) :
                if 0 <= _next < 10 :
                    dfs(curr*10 + _next, i+1)
            
        output = []
        
        if N == 1 :
            output.append(0)
        
        for i in range(1, 10) :
            dfs(i,1)
            
        return output
   
# BFS
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        
        if N == 1 :
            return [i for i in range(10)]
        
        queue = collections.deque([i for i in range(1,10)])
        
        for _ in range(N-1) :
            
            n = len(queue)
            for i in range(n) :
                
                j = queue.popleft()
                last = j % 10
                
                for curr in set([last + K, last - K]) :
                    if 0 <= curr < 10 :
                        queue.append(j*10 + curr)
        
        return queue
        
