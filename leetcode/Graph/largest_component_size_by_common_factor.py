class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        
        uf = UnionFind(max(A))
        map = {}
        
        for num in A :
            prime_factors = list(set(self.getPrimeFactors(num)))
            map[num] = prime_factors[0]
            for i in range(len(prime_factors)-1) :
                uf.union(prime_factors[i], prime_factors[i+1])
                
        ans = 0
        count = collections.defaultdict(int)
        
        for num in A :
            id = uf.find(map[num])
            count[id] += 1
            ans = max(ans, count[id])
            
        return ans
    
    def getPrimeFactors(self, num) :
        
        factor = 2
        prime_factors = []
        
        while num >= factor * factor:
            if num % factor == 0 :
                prime_factors.append(factor)
                num = num // factor
            else :
                factor += 1
        
        prime_factors.append(num)
        return prime_factors
            
        
class UnionFind :
    def __init__(self, size) :
        self.parent = list(range(size+1))
        self.size = [1]*(size+1)
        
    def find(self, x) :
        if self.parent[x] != x :
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y) :
        px, py = self.find(x), self.find(y)
        
        if px == py :
            return
        
        if self.size[px] > self.size[py] :
            px, py = py, px
        
        self.parent[px] = py
        self.size[py] += self.parent[px]
        
