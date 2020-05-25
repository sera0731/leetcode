# Time complexity : O(N)
# Space complexity : O(1)

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        N = len(bin(max(nums)))-2
        bit_nums = [[(x>>i)&1 for i in range(N)][::-1] for x in nums]
        
        trie = {}
        max_xor = 0
        
        for num in bit_nums :
            curr_xor = 0
            node = trie
            xor_node = trie
            
            for bit in num :
                if bit not in node :
                    node[bit] = {}
                node = node[bit]
            
                toggled = 1-bit
                if toggled in xor_node :
                    curr_xor = (curr_xor<<1)|1
                    xor_node = xor_node[toggled]
                else :
                    curr_xor <<= 1
                    xor_node = xor_node[bit]
                    
            max_xor = max(max_xor, curr_xor)
            
        return max_xor
