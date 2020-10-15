import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        n = len(beginWord)
        d = defaultdict(list)
        
        for word in wordList :
            for i in range(n) :
                curr = word[:i]+'*'+word[i+1:]
                d[curr].append(word)
        
        q = deque([(beginWord, 1)])
        visited = set([beginWord])
        
        while q :
            word, cnt = q.popleft()
            for i in range(n) :
                curr = word[:i]+'*'+word[i+1:]
                
                for w in d[curr] :
                    if w == endWord :
                        return cnt + 1
                    if w not in visited :
                        visited.add(w)
                        q.append((w, cnt+1))
        
        return 0
        
