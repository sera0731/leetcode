class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        h = collections.defaultdict(list)
        
        for s in strs :
            
            cnt = [0]*26
            for ch in s :
                cnt[ord(ch)-ord('a')] += 1
            
            h[tuple(cnt)].append(s)
            
        return h.values()
        
