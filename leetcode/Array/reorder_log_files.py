class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
    
        def order(log) :
            id, rest = log.split(' ', 1)
            return (0, rest, id) if rest[0].isalpha() else (1,)
            
        return sorted(logs, key=order)
        
