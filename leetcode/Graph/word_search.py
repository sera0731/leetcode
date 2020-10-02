class Solution:
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        if not word :
            return True
        
        self.board = board
        self.word = word
        
        for i in range(len(board)) :
            for j in range(len(board[0])) :
                if self.dfs(i, j, 0) :
                    return True
        
        return False
    
    def dfs(self, i, j, ci) :
        
        if ci == len(self.word) :
            return True
            
        if i < 0 or j < 0 or i >= len(self.board) or j >= len(self.board[0]) or self.word[ci] != self.board[i][j]:
            return False
                    
        self.board[i][j] = '0'
            
        for dx, dy in [(0,1), (-1,0), (0,-1), (1,0)] :
            if self.dfs(i + dx, j + dy, ci+1) :
                return True
            
        self.board[i][j] = self.word[ci]
        return False
                
