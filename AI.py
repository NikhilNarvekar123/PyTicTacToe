import math as m

class AI:

    def __init__(self, boardState):
        self.boardState = boardState




    def updateBoard(self, boardState):
        self.boardState = boardState
        return self.boardState


    def minmax(self, player, move = None):

        if move != None:
            self.boardState[move[0]][move[1]] = 'O'

        res = self.gameOver()
        if res != 'n':
            if res == 'X':
                return -1
            elif res == 'O':
                return 1
            else:
                return 0

        if player == 'AI':
            max = -m.inf
            for r in range(3):
                for c in range(3):
                    if(self.boardState[r][c] == ''):
                        self.boardState[r][c] = 'O'
                        val = self.minmax('Human')
                        max = max(max, val)
                        self.boardState[r][c] = ''
            return max

        elif player == 'Human':
            min = m.inf
            for r in range(3):
                for c in range(3):
                    if(self.boardState[r][c] == ''):
                        self.boardState[r][c] = 'X'
                        val = self.minmax('AI')
                        min = min(min, val)
                        self.boardState[r][c] = ''
            return min


    def makeMove(self, boardState):

        board = self.updateBoard(boardState)

        initMoves = []
        for r in range(3):
            for c in range(3):
                if(self.boardState[r][c] == ''):
                    initMoves.append((r,c))

        maxMove = None
        for move in initMoves:
            val = self.minmax('Human', move)
            self.boardState[move[0]][move[1]] = ''
            if (not maxMove) or maxMove[1] < val:
                maxMove = (move, val)

        print(maxMove)
        self.boardState[maxMove[0][0]][maxMove[0][1]] = 'O'




        return board






    def isMoveValid(self, r, c, board) -> bool:
        if r < 0 or r > 2:
            return False
        if c < 0 or c > 2:
            return False
        if board[r][c] == '':
            return False
        return True





    def gameOver(self):
        brd = self.boardState

        if brd[0][0] == brd[0][1] == brd[0][2] and (brd[0][0] != ''):
            return brd[0][0]
        if brd[1][0] == brd[1][1] == brd[1][2] and (brd[1][0] != ''):
            return brd[1][0]
        if brd[2][0] == brd[2][1] == brd[2][2] and (brd[2][0] != ''):
            return brd[2][0]

        if brd[0][0] == brd[1][0] == brd[2][0] and (brd[0][0] != ''):
            return brd[0][0]
        if brd[0][1] == brd[1][1] == brd[2][1] and (brd[0][1] != ''):
            return brd[0][1]
        if brd[0][2] == brd[1][2] == brd[2][2] and (brd[0][2] != ''):
            return brd[0][2]

        if brd[0][0] == brd[1][1] == brd[2][2] and (brd[0][0] != ''):
            return brd[0][0]
        if brd[0][2] == brd[1][1] == brd[2][0] and (brd[0][2] != ''):
            return brd[0][2]

        for r in range(3):
            for c in range(3):
                if brd[r][c] == '':
                    return 't'

        return 'n'
