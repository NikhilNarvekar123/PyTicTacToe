import tkinter as tk


class MainGame(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.board = [[''] * 3, [''] * 3, [''] * 3]
        self.create_widgets()

    def create_widgets(self):
        buttons = tk.StringVar()

        label = tk.Label(text="Player 1:", font='Roboto 20 bold', bg='white', fg='black', height=1, width=8)
        label.grid(row=1, column=0)


        label = tk.Label(text="AI:", font='Roboto 20 bold', bg='white', fg='black', height=1, width=8)
        label.grid(row=2, column=0)

        button1 = tk.Button(text=" ", font='Roboto 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: self.btnClick(button1, 0, 0))
        button1.grid(row=3, column=0)

        button2 = tk.Button( text=' ', font='Roboto 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: self.btnClick(button2, 0, 1))
        button2.grid(row=3, column=1)

        button3 = tk.Button( text=' ',font='Roboto 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: self.btnClick(button3, 0, 2))
        button3.grid(row=3, column=2)

        button4 = tk.Button(text=' ', font='Roboto 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: self.btnClick(button4, 1, 0))
        button4.grid(row=4, column=0)

        button5 = tk.Button(text=' ', font='Roboto 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: self.btnClick(button5, 1, 1))
        button5.grid(row=4, column=1)

        button6 = tk.Button(text=' ', font='Roboto 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: self.btnClick(button6, 1, 2))
        button6.grid(row=4, column=2)

        button7 = tk.Button(text=' ', font='Roboto 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: self.btnClick(button7, 2, 0))
        button7.grid(row=5, column=0)

        button8 = tk.Button(text=' ', font='Roboto 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: self.btnClick(button8, 2, 1))
        button8.grid(row=5, column=1)

        button9 = tk.Button(text=' ', font='Roboto 20 bold', bg='black', fg='white', height=4, width=8, command=lambda: self.btnClick(button9, 2, 2))
        button9.grid(row=5, column=2)

    def btnClick(self, btn, r, c):
        if btn['text'] == ' ':
            btn['text'] = 'X'
        self.board[r][c] = 'X'
        print(self.board)





root = tk.Tk()
app = MainGame(master=root)
app.mainloop()
