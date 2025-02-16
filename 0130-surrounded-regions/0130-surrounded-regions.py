class Solution:
    def dfs(self,board, visited, source):
        rows, cols = len(board), len(board[0])
        i, j = source
        visited.append((i,j))
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        for nr, nc in directions:
            fr, fc = nr + i, nc + j
            if 0 <= fr < rows and 0 <=fc < cols and (fr,fc) not in visited and board[fr][fc] == 'O':
                self.dfs(board, visited, (fr,fc))

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #If someone is on the boundary that is where he cannot be covered. 
        visited = [] #List that stores the visited nodes
        for i in range(len(board[0])):
            if board[0][i] == 'O' and (0,i) not in visited:
                self.dfs(board, visited, (0,i))   
            if board[len(board) - 1][i] == 'O' and (len(board) - 1,i) not in visited: 
                self.dfs(board, visited, (len(board) - 1, i))
        for j in range(len(board)):
            if board[j][0] == 'O' and (j, 0) not in visited:
                self.dfs(board, visited, (j, 0)) 
            if board[j][len(board[0]) - 1] == 'O' and (j, len(board[0]) - 1) not in visited:
                self.dfs(board, visited, (j, len(board[0]) - 1) )

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i,j) not in visited:
                    board[i][j] = 'X'

                #Last row



        