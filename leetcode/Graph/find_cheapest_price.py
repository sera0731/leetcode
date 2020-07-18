class Node:
    def __init__(self, val) :
        self.val = val
        self.next = []
        
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        if not flights :
            return -1
        
        nodes = {}
        weight = {}
        
        for s, d, v in flights :
            if s not in nodes :
                nodes[s] = Node(s)
            if d not in nodes :
                nodes[d] = Node(d)
            nodes[s].next.append(nodes[d])
            weight[(s, d)] = v
            
        queue = collections.deque([(nodes[src], 0)])
        price = float('inf')
        stops = -2 # start, end
        
        while queue and stops < K :
            
            n = len(queue)
            
            for _ in range(n) :
                curr, curr_sum = queue.popleft()
                
                # found
                if curr.val == dst :
                    price = min(price, curr_sum)
                    continue
                    
                for i in curr.next :
                    next_sum = weight[(curr.val, i.val)] + curr_sum
                    if next_sum < price :
                        queue.append((i, next_sum))
                    
            stops += 1
            
        return price if price != float('inf') else -1
    
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        if not flights :
            return -1
        
        f = collections.defaultdict(dict)
        
        for s,d,w in flights :
            f[s][d] = w
        
        h = [(0, 0, src)]
        
        while h :
            
            price, stop, node = heapq.heappop(h)
            
            if node == dst :
                return price
            
            for i in f[node] :
                if stop < K+1 :
                    heapq.heappush(h, (price+f[node][i], stop+1, i))
                
        return -1
    
