# Time complexity : O(N)
# Space complexity : O(N)

class TrieNode:

    def __init__(self):
        self.value = 0
        self.children = {}

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.keys = {}

    def insert(self, key: str, val: int) -> None:
        
        delta = val - self.keys.get(key, 0)
        self.keys[key] = val
        
        curr = self.root
        curr.value += delta
        
        for ch in key :
            node = TrieNode()
            if ch not in curr.children :
                curr.children[ch] = node
            curr = curr.children[ch]
            curr.value += delta
        

    def sum(self, prefix: str) -> int:
        
        ans = 0
        curr = self.root
        
        for ch in prefix :
            if ch not in curr.children :
                return 0
            curr = curr.children[ch]
        
        return curr.value
