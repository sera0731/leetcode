class Solution:
    def __init__(self, rects):
        
        self.rects = rects
        self.ranges = [0]
        sm = 0
        
        for x1, y1, x2, y2 in rects:
            sm += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.ranges.append(sm)

    def pick(self):
        
        n = random.randint(0, self.ranges[-1] - 1)
        i = bisect.bisect(self.ranges, n) - 1
        
        x1, y1, x2, y2 = self.rects[i]
        w = x2 - x1 + 1
        
        n -= self.ranges[i]
        return [x1 + n % w, y1 + n // w]
        
