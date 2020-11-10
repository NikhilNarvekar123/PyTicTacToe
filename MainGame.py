import tkinter as tk


class MainGame(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.board = [[''] * 3, [''] * 3, [''] * 3]
        self.playerScore = 0
        self.aiScore = 0
        self.playerTurn = True
        self.create_widgets()

    def create_widgets(self):
        buttons = tk.StringVar()

        self.label1 = tk.Label(text="Player 1: " + str(self.playerScore), font='Roboto 20 bold', bg='white', fg='black', height=1, width=8)
        self.label1.grid(row=1, column=0)


        self.label2 = tk.Label(text="AI:" + str(self.aiScore), font='Roboto 20 bold', bg='white', fg='black', height=1, width=8)
        self.label2.grid(row=2, column=0)

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
        brd = self.board

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

        filled = True
        for r in range(3):
            for c in range(3):
                if brd[r][c] == '':
                    filled = False
                    break
        return 'n' if not filled else 'f'



    def reset(self, winner):

        if winner == 'X':
            self.playerScore += 1
            print('Player won!')
        if winner == 'O':
            self.aiScore += 1
            print('AI won!')
        if winner == 'f':
            print('Draw!')

        self.board = [[''] * 3, [''] * 3, [''] * 3]
        self.create_widgets()


    def btnClick(self, btn, r, c):
        if btn['text'] == '' and self.playerTurn:
            btn['text'] = 'X'
            self.playerTurn = not self.playerTurn
            self.board[r][c] = 'X'
        elif btn['text'] == '':
            btn['text'] = 'O'
            self.playerTurn = not self.playerTurn
            self.board[r][c] = 'O'

        rez = self.checkWin()
        if rez != 'n':
            self.reset(rez)



root = tk.Tk()
app = MainGame(master=root)
app.mainloop()
