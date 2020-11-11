import math as m

# Helper class for MainGame class. Runs the AI agent required.
# Contains functionality to make moves (primarily based on minmax alg.)
class AI:

    def __init__(self, boardState):
        self.boardState = boardState

    def updateBoard(self, boardState):
        """Meant to update the AI agent's board variable whenever called"""
        self.boardState = boardState
        return self.boardState

    def minmax(self, player, move = None):
        """ Runs the recursive algorithm which maximizes the AI score while minimizing the user score
            Highest valuation means best moveset for AI to make to win
            Lowest valuation means best moveset for player to make to win
            Given a player move, runs minmax and determines its valuation
        """

        # entry-case -> given a particular move, evaluate highest potential value for it
        if move != None:
            self.boardState[move[0]][move[1]] = 'O'

        # checks if given boardstate results in a game over
        # negative valution is bad (since boardstate has resulted in player winning)
        # positive valuation is good (since boardstate has resulted in AI winning)
        res = self.gameOver()
        if res == 'X':
            return -1
        elif res == 'O':
            return 1
        elif res == 't':
            return 0

        # simulates the AI making a move on current boardstate (tries to get highest valuation)
        if player == 'AI':
            maxVal = -m.inf

            for r in range(3):
                for c in range(3):

                    # makes a move on every existing empty space
                    if(self.boardState[r][c] == ''):
                        self.boardState[r][c] = 'O'

                        # makes recursive call to simulate player move (with updated boardstate)
                        val = self.minmax('Human')

                        # if valuation is higher than valuation for other potential move, set this valuation to max
                        maxVal = max(maxVal, val)
                        #maxVal += val

                        # reset board
                        self.boardState[r][c] = ''

            return maxVal

        # simulates the player making a move on current boardstate (tries to get lowest valuation)
        elif player == 'Human':
            minVal = m.inf

            for r in range(3):
                for c in range(3):

                    # makes a move on every existing empty space
                    if(self.boardState[r][c] == ''):
                        self.boardState[r][c] = 'X'

                        # makes recursive call to simulate AI move (with updated boardstate)
                        val = self.minmax('AI')

                        # if valuation is smaller than valuation for other potential move, set this valuation to min
                        minVal = min(minVal, val)
                        #minVal -= val

                        # reset board
                        self.boardState[r][c] = ''

            return minVal

    def makeMove(self, boardState):
        """ Called from outside classes. Makes the AI move based on current boardstate """

        # tempcopy for ease
        board = self.updateBoard(boardState)

        # finds all potential moves for AI based on given boardstate
        initMoves = []
        for r in range(3):
            for c in range(3):
                if(self.boardState[r][c] == ''):
                    initMoves.append((r,c))

        # calculates valuation for each potential move and finds the best move
        maxMove = None
        for move in initMoves:
            val = self.minmax('Human', move)
            self.boardState[move[0]][move[1]] = ''
            if (not maxMove) or maxMove[1] < val:
                maxMove = (move, val)

        # Makes optimal move
        self.boardState[maxMove[0][0]][maxMove[0][1]] = 'O'
        return board

    def gameOver(self):
        """ Checks if a game with the given board state has a winner """

        # local copy for ease
        brd = self.boardState

        # row check
        if brd[0][0] == brd[0][1] == brd[0][2] and (brd[0][0] != ''):
            return brd[0][0]
        if brd[1][0] == brd[1][1] == brd[1][2] and (brd[1][0] != ''):
            return brd[1][0]
        if brd[2][0] == brd[2][1] == brd[2][2] and (brd[2][0] != ''):
            return brd[2][0]

        # col check
        if brd[0][0] == brd[1][0] == brd[2][0] and (brd[0][0] != ''):
            return brd[0][0]
        if brd[0][1] == brd[1][1] == brd[2][1] and (brd[0][1] != ''):
            return brd[0][1]
        if brd[0][2] == brd[1][2] == brd[2][2] and (brd[0][2] != ''):
            return brd[0][2]

        # diagonal check
        if brd[0][0] == brd[1][1] == brd[2][2] and (brd[0][0] != ''):
            return brd[0][0]
        if brd[0][2] == brd[1][1] == brd[2][0] and (brd[0][2] != ''):
            return brd[0][2]

        # checks if tie has been reached (board full)
        full = True
        for r in range(3):
            for c in range(3):
                if brd[r][c] == '':
                    full = False

        return 'n' if not full else 't'
