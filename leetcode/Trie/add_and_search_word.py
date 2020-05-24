class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root
        for ch in word:
            if ch not in curr.items:
                curr.items[ch] = Node()
            curr = curr.items[ch]
            
        curr.isEnd = True
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        stack = [(self.root, word)]
        
        while stack :
            node, w = stack.pop()
            if not w:
                if node.isEnd :
                    return True
            elif w[0] == '.':
                for ch in node.items.values():
                    stack.append((ch, w[1:]))
            else :
                if w[0] in node.items :
                    stack.append((node.items[w[0]], w[1:]))
                
        return False
            
