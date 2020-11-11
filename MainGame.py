import tkinter as tk
from AI import AI

# Class for Tkinter game frame. Contains code for player to make moves and display the board. Uses
# the AI helper class to let the AI agent make moves.
class MainGame(tk.Frame):

    def __init__(self, master=None):

        # tkinter boilerplate
        super().__init__(master)
        self.master = master

        # class variables
        self.board = [[''] * 3, [''] * 3, [''] * 3]
        self.playerScore = 0
        self.aiScore = 0
        self.ai = AI(self.board)

        # spawn game board
        self.create_widgets()

    def create_widgets(self):

        # text for player score
        self.label1 = tk.Label(text="Player 1: " + str(self.playerScore), font='Roboto 20 bold', bg='white', fg='black', height=1, width=8)
        self.label1.grid(row=1, column=0)

        # text for AI score
        self.label2 = tk.Label(text="AI:" + str(self.aiScore), font='Roboto 20 bold', bg='white', fg='black', height=1, width=8)
        self.label2.grid(row=2, column=0)

        # represent 9 grid buttons for tictactoe board
        button1 = tk.Button(text=self.board[0][0], font='Roboto 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: self.btnClick(button1, 0, 0))
        button1.grid(row=3, column=0)

        button2 = tk.Button( text=self.board[0][1], font='Roboto 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: self.btnClick(button2, 0, 1))
        button2.grid(row=3, column=1)

        button3 = tk.Button( text=self.board[0][2],font='Roboto 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: self.btnClick(button3, 0, 2))
        button3.grid(row=3, column=2)

        button4 = tk.Button(text=self.board[1][0], font='Roboto 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: self.btnClick(button4, 1, 0))
        button4.grid(row=4, column=0)

        button5 = tk.Button(text=self.board[1][1], font='Roboto 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: self.btnClick(button5, 1, 1))
        button5.grid(row=4, column=1)

        button6 = tk.Button(text=self.board[1][2], font='Roboto 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: self.btnClick(button6, 1, 2))
        button6.grid(row=4, column=2)

        button7 = tk.Button(text=self.board[2][0], font='Roboto 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: self.btnClick(button7, 2, 0))
        button7.grid(row=5, column=0)

        button8 = tk.Button(text=self.board[2][1], font='Roboto 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: self.btnClick(button8, 2, 1))
        button8.grid(row=5, column=1)

        button9 = tk.Button(text=self.board[2][2], font='Roboto 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: self.btnClick(button9, 2, 2))
        button9.grid(row=5, column=2)

    def checkWin(self):
        """Checks if either the AI or player has won the game (or if board is all full)
           'f' represents a full board, 'X' represents player win, 'O' represents AI win,
           'n' represents no win yet
        """

        # create temp copy for ease
        brd = self.board

        # row check
        if brd[0][0] == brd[0][1] == brd[0][2] and (brd[0][0] != ''):
            return brd[0][0]
        if brd[1][0] == brd[1][1] == brd[1][2] and (brd[1][0] != ''):
            return brd[1][0]
        if brd[2][0] == brd[2][1] == brd[2][2] and (brd[2][0] != ''):
            return brd[2][0]

        # column check
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

        # checks if board is all full
        filled = True
        for r in range(3):
            for c in range(3):
                if brd[r][c] == '':
                    filled = False
                    break

        return 'n' if not filled else 'f'

    def reset(self, winner):
        """Changes the player/ai score and resets the board for a new game"""

        if winner == 'X':
            self.playerScore += 1
            print('Player won!')
        if winner == 'O':
            self.aiScore += 1
            print('AI won!')
        if winner == 'f':
            print('Draw!')

        # reset/redraw board
        self.board = [[''] * 3, [''] * 3, [''] * 3]
        self.create_widgets()

    def btnClick(self, btn, r, c):
        """Makes the player move based on clicked square, also conducts subsequent AI move"""

        # if space not occupied (otherwise exit)
        if btn['text'] == '':
            btn['text'] = 'X'
            self.board[r][c] = 'X'
        else:
            return

        # check win for player and reset if game over
        rez = self.checkWin()
        if rez != 'n':
            self.reset(rez)

        # make AI move and update board
        newBoard = self.ai.makeMove(self.board)
        self.board = newBoard
        self.create_widgets()

        # check win for AI and reset if game over
        rez = self.checkWin()
        if rez != 'n':
            self.reset(rez)


# Launch game via tkinter
root = tk.Tk()
app = MainGame(master=root)
app.mainloop()
