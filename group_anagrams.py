# Time complexity : O(NK), where N is the lenght of strs. K is the maximum length of a string in strs.
# Space complexity : O(NK)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = collections.defaultdict(list)
        
        for i in strs :
            count = [0]*26
            for ch in i :
                count[ord(ch)-ord('a')] += 1
            result[tuple(alpha)].append(i)
                
        return result.values()
