class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        
        if val in self.dict :
            return False
        
        self.dict[val] = len(self.arr)
        self.arr.append(val)
        
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dict :
            return False
        
        i = self.dict[val]
        last = self.arr[-1]
        
        self.dict[last] = i
        self.arr[i] = last
        
        self.arr.pop()
        del self.dict[val]
        
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.arr)
