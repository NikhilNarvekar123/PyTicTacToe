import copy
import random as r
# 
# class AI:
#
#     def __init__(self):
#
#
#
#





class Main:
    board = []
    def __init__(self):
        Main.board = ["1","2","3","4","5","6","7","8","9"]

    def printBoard(self):

        border = "____________"
        sep =    "------------"
        count = 0;

        print(border)
        for j in range(3):

            for i in range(11):
                if((i+1) % 4 == 0):
                    print("|",end="")
                elif((i+1) % 4 == 2):
                    print(Main.board[count],end="")
                    count += 1
                else:
                    print(" ",end="")

            if(j!=2):
                print("\n"+sep)
            else:
                print("\n"+border+"\n")

    def processMove(self, inp, player):
        Main.board[inp] = player
        x = self.checkWin(Main.board)
        return x


    def checkWin(self, boardState):

        for r in range(0, 9, 3):
            if(boardState[r] == boardState[r+1] == boardState[r+2]):
                return boardState[r]

        for c in range(0, 2):
            if(boardState[c] == boardState[c+3] == boardState[c+6]):
                return boardState[r]

        if(boardState[0] == boardState[4] == boardState[8]):
            return boardState[0]
        if(boardState[2] == boardState[4] == boardState[6]):
            return boardState[2]

        return ''




class Player(Main):


    def __init__(self, name):
        self.name = name
        print("Welcome Player ", self.name, "!")

    def handleInput(self, inp):

        validInput = False
        while not validInput:
            x = inp
            try:
                x = int(x)
                if x >= 1 and x <= 9:
                    if Main.board[x-1] != "X" or Main.board[x-1] != "O":
                        validInput = True
                        self.input = x
                        break
            except:
                validInput = False
            inp = input("Invalid input entered! Try again")

        return self.input - 1


class AI(Main):

    def __init__(self):
        print("AI client created!")
        self.moveList = []

    def makeMove(self):
        #self.generateMoves()
        self.moveList = []
        for i in range(9):
            if(Main.board[i] != 'X' and Main.board[i] != 'O'):
                 self.moveList.append(i)
        print(self.moveList)
        return self.moveList[r.randint(0, len(self.moveList) - 1)]

    #have to pass copy
    def generateMoves(self, boardState, scoreInit):

        return 1
        '''
        score = scoreInit
        winRez = self.checkWin(boardState)
        if(winRez == 'O'):
            return 10
        elif(winRez == 'X'):
            return -10
        else:
            return 0

        for i in range(9):
            if(boardState[i] == 'X' or boardState[i] == 'O'):
                continue
            boardCopy = copy.deepcopy(boardState)
            boardCopy[i] = 'O'
            score += self.generateMoves(boardCopy, score)
        '''





''' Actual Game '''

print("Welcome to AI tic-tac-toe!")
print("Meant to be a simple exploration of the minmax algorithm")
input("Press any key to begin!\n")
game = Main()
player = Player("om")
ai = AI()

# Game Loop
while True:

    print("\n**GAME STARTED! -- Every turn, enter the letter of space to fill**\n")
    game.printBoard()

    winner = "draw!"

    while(True): #game.checkWin() == ''):

        p1 = input("Enter number of square to fill in:")
        p1 = player.handleInput(p1)
        winner = game.processMove(p1, 'X')
        game.printBoard()

        print("AI making their move...")
        a1 = ai.makeMove()
        winner = game.processMove(a1, 'O')
        game.printBoard()

        if winner == 'X' or winner == 'O':
            print("Winner is ", winner, "!")
            break

    game = Main()
    ai = AI()
    input("\nEnter any key to restart!")
