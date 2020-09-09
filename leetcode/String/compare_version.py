class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        v1 = [int(i) for i in version1.split(".")]
        v2 = [int(i) for i in version2.split(".")]
        
        n, m = len(v1), len(v2)
        i = j = 0
        
        for i in range(max(n, m)) :
            vv1 = v1[i] if i < n else 0
            vv2 = v2[i] if i < m else 0
            
            if vv1 != vv2 :
                return -1 if vv1 < vv2 else 1
            
        return 0
    
