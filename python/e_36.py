class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Check for duplicates in row
        #Check for duplicates in column
        n = len(board)

        for i in range(n):
            row, column = set(), set() #could have also just used {}
            #Difference would be keys are positions in the board [i,j]
            #Values are the values
            for j in range(n):
                if board[i][j] != ".": 
                    if board[i][j] in row:  
                        return False
                    else:
                        row.add(board[i][j])
        
                if board[j][i] != ".":
                    if board[j][i] in column:
                        return False
                    else:
                        column.add(board[j][i])
        
        #Check for duplicates in a 3x3 array
        #Keys: [i,j]
        #Values board[i][j]
    
        squares_set = {}
        for i in range(n):
            for j in range(n): 
                if board[i][j] != ".":
                    grid_key = (i // 3, j // 3)

                    if grid_key not in squares_set:
                        squares_set[grid_key] = set()

                    if board[i][j] in squares_set[grid_key]:
                        return False
                    
                    squares_set[grid_key].add(board[i][j])
        return True