# BFS
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
          
# BFS (HashMap)
import collections
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = defaultdict(dict)

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root
        
        for ch in word:
            if ch not in curr :
                curr[ch] = {}
            curr = curr[ch]
        
        curr['#'] = True
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        stack = [(self.root, word)]
        
        while stack :
            
            node, target = stack.pop()
            
            if node == True :
                continue
                
            if not target :
                if '#' in node :
                    return True
                else :
                    continue
                
            first = target[0]
            
            if first == '.':
                for ch in node:
                    stack.append((node[ch], target[1:]))
            elif first in node :
                stack.append((node[first], target[1:]))
                
        return False

 
# DFS
import collections

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = defaultdict(dict)

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root
        
        for ch in word:
            if ch not in curr :
                curr[ch] = {}
            curr = curr[ch]
        
        curr['#'] = True
        
    def helper(self, node, word) :
        
        for i, ch in enumerate(word) :
            if ch not in node :
                if ch == '.' :
                    for child in node :
                        if child != '#' and self.helper(node[child], word[i+1:]) :
                            return True
                return False
            else :
                node = node[ch]
                
        return '#' in node
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.helper(self.root, word)
            
