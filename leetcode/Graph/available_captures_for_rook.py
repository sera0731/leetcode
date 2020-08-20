# Time complexity : O(1)
# Space complexity : O(1)

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        row, col = 0, 0
        num = 0
        
        for i in range(8) :
            for j in range(8) :
                if board[i][j] == 'R' :
                    row, col = i, j
                    break
        
        for i, j in [(0,-1),(0,1),(1,0),(-1,0)] :
            
            ci, cj = row+i, col+j
            
            while 0<=ci<8 and 0<=cj<8 :
                
                if board[ci][cj] == 'p' :
                    num += 1
                if board[ci][cj] != '.' :
                    break
                
                ci += i
                cj += j
                
        return num
        
