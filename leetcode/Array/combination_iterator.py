class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combs = collections.deque()
        self.getAllCombs(characters, combinationLength)
        
    def getAllCombs(self, target, n, curr=[], start=0) :
        
        if len(curr) == n :
            self.combs.append(''.join(curr[:]))
            return
        
        for i in range(start, len(target)) :
            self.getAllCombs(target, n, curr+[target[i]], i+1)
    
    def next(self) -> str:
        if self.hasNext() :
            return self.combs.popleft()

    def hasNext(self) -> bool:
        return len(self.combs) > 0
    
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.n = len(characters)
        self.k = combinationLength
        self.b = (1<<self.n)-(1<<self.n-self.k)
        
    def next(self) -> str:
        
        curr = []
        
        for i in range(self.n):
            if self.b & (1 << self.n-1-i) :
                curr.append(self.chars[i])
        
        self.b -= 1
        
        while self.b > 0 and bin(self.b).count('1') != self.k :
            self.b -= 1
        
        return ''.join(curr)

    def hasNext(self) -> bool:
        return self.b > 0
