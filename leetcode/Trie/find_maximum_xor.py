class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        n = len(bin(max(nums)))-2
        bits = []
        
        for i in nums :
            bits.append([ (i>>j)&1 for j in reversed(range(n))])
        
        trie = {}
        output = 0
        
        for bit in bits :
            
            current = 0
            
            xor_node = trie
            node = trie
            
            for i in bit :
                if i not in node :
                    node[i] = {}
                node = node[i]
                
                opps = i^1
                if opps in xor_node :
                    current = current << 1 | 1
                    xor_node = xor_node[opps]
                else :
                    current = current << 1
                    xor_node = xor_node[i]
            
            output = max(output, current)
                
        return output
            
            
