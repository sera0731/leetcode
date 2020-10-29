class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = [0]*26
        for ch in tasks :
            freq[ord(ch)-ord('A')] += 1
        
        freq.sort()
        
        f_max = freq.pop()
        idle_time = (f_max-1)*n
        
        while freq and idle_time > 0 :
            idle_time -= min(freq.pop(), f_max-1)
        
        if idle_time < 0 :
            idle_time = 0
        
        return len(tasks) + idle_time
        
