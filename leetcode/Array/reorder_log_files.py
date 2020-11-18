class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        def sort(log) :
            
            identifier, rest = log.split(' ', 1)
            
            if rest[0].isnumeric() :
                return (1, '')
            
            return (0, rest, identifier)

        return sorted(logs, key=sort)
        
