class TrieNode :
    
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
    def _charToIndex(self, ch) :
        return ord(ch)-ord('a')
    
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for level in range(len(word)) :
            i = self._charToIndex(word[level])
            if not curr.children[i] :
                curr.children[i] = TrieNode()
            curr = curr.children[i]
            
        curr.isEndOfWord = True
                

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        
        for level in range(len(word)) :
            i = self._charToIndex(word[level])
            if not curr.children[i] :
                return False
            curr = curr.children[i]
            
        return curr != None and curr.isEndOfWord
            
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for level in range(len(prefix)) :
            i = self._charToIndex(prefix[level])
            if not curr.children[i] :
                return False
            curr = curr.children[i]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
