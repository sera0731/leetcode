class Codec:
    
    def len_to_str(self, x) :
        
        x = len(x)
        bytes = []
        
        for i in range(4) :
            target = chr(x>>i*8 & 0xff)
            bytes.append(target)
        
        bytes.reverse()
        str_bytes = ''.join(bytes)
        return str_bytes
        
    def str_to_int(self, x) :
        
        result = 0
        
        for ch in x :
            result = result * 256 + ord(ch)
        
        return result
    
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        
        return ''.join([self.len_to_str(s) + s for s in strs])

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        
        i, n = 0, len(s)
        output = []
        
        while i < n :
            length = self.str_to_int(s[i:i+4])
            i += 4
            output.append(s[i:i+length])
            i += length
        
        return output
    
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
