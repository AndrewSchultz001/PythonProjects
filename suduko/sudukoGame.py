import tkinter as tk
import boardBuilder as bb
import selectedButtons as sb
import random

class SudokuBoard:

    def __init__(self, master):
        self.master = master
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.completed_board = bb.get_board()
        self.selectedBoardButtons = {}
        self.create_board()
        self.create_buttons()
        self.selectedButtons = sb.click1()
        self.errors = 0
    
    def pickRandSpaces(self):
        for i in range(25):
            val = random.randint(0, 80)
            str_val = int(self.completed_board[val//9][val%9])
            self.selectedBoardButtons[val].config(text=str(str_val))
            self.board[val//9][val%9] = str_val
        
        for i in range(9):
            hasTrue = False
            for j in range(9):
                if (self.board[i][j] != 0):
                    hasTrue = True
            if (hasTrue == False):
                val = random.randint(0, 9)
                str_val = int(self.completed_board[i][val])
                self.selectedBoardButtons[i*9+val].config(text=str(str_val))
                self.board[i][val] = str_val


    def create_board(self):
        frame = tk.Frame(self.master)
        frame.pack(expand=True, fill='both', padx=20, pady=20)

        def restart(self, b):
            self.board = [[0 for _ in range(9)] for _ in range(9)]
            self.completed_board = bb.get_board()
            self.selectedBoardButtons = {}
            for widget in self.master.winfo_children():
                widget.destroy()
            self.create_board()
            self.create_buttons()
            self.errors = 0

        def partialBoardWipe(frame):
            for widget in frame.winfo_children():
                widget.destroy()
        
        def restartButton(frame):
            button = tk.Button(frame, text="Restart", font=("Helvetica", 12))
            button.grid(row=5, column=20)
            button.bind("<Button-1>", lambda event, b=0: restart(self, b))  
        
        def boardsEqual(self):
            for i in range(9):
                for j in range(9):
                    if (self.board[i][j] != self.completed_board[i][j]):
                        return False
            
            return True

        def change_value(self, button_id):
            value = 0
            for i in range(9):
                if (self.selectedButtons[i]):
                    value = i+1
                    break

            if (value != self.completed_board[button_id//9][button_id%9]):
                self.errors = self.errors + 1
                if (self.errors >= 4):
                    partialBoardWipe(frame)

                    game_over_label = tk.Label(frame, text="Game Over", font=("Helvetica", 20), fg="red")
                    game_over_label.grid(row=6, columnspan=9) 
                    restartButton(frame)
                else: 
                    label = tk.Label(frame, text="x", fg="red", width=4, height=2)
                    label.grid(row=5, column=12+self.errors)
            else: 
                self.selectedBoardButtons[button_id].config(text=str(value), bg='blue')
                self.board[button_id//9][button_id%9] = value
                if (boardsEqual(self)):
                    partialBoardWipe(frame)

                    win_label = tk.Label(frame, text="You Win", font=("Helvetica", 20), fg="red")
                    win_label.grid(row=6, columnspan=9) 
                    restartButton(frame)
        

        for i in range(9):
            for j in range(9):
                cell_value = self.board[i][j]
                button = tk.Button(frame, text=str(cell_value), width=4, height=2)
                button.grid(row=i, column=j)
                if ((i+1) % 3 == 0 and i != 0):
                    button.grid(pady=(0, 5))  
                if ((j+1) % 3 == 0 and j != 0):
                    button.grid(padx=(0, 5))  
                button.bind("<Button-1>", lambda event, b=(i*9+j): change_value(self, b))  
                self.selectedBoardButtons[i*9 + j] = button
        
        self.pickRandSpaces()
    
    def create_buttons(self):
        frame = tk.Frame(self.master)
        frame.pack(expand=True, fill='both', padx=20, pady=20)

        def change_color(self, button_id):
            for i in range(9):
                for j in range(9):
                    if (self.board[i][j] == button_id+1):
                        self.selectedBoardButtons[i*9+j].config(bg="blue")
                    else: 
                        self.selectedBoardButtons[i*9+j].config(bg="white")
                    
            buttons[button_id].config(bg="blue")
            
            changeSelectedButton(self, button_id)

            for b_id, button in buttons.items():
                if b_id != button_id:
                    button.config(bg="white")
            

        buttons = {}

        button = tk.Button(frame, text=str(1), width=3, bg="blue", font=("Helvetica", 14))
        button.grid(row=0, column=0)
        button.bind("<Button-1>", lambda event, b=0: change_color(self, b))  
        buttons[0] = button

        for i in range(1, 9):
            cell_value = i + 1
            button = tk.Button(frame, text=str(cell_value), width=3, font=("Helvetica", 14))
            button.grid(row=0, column=i)
            button.bind("<Button-1>", lambda event, b=i: change_color(self, b))  
            buttons[i] = button 

        def changeSelectedButton(self, button_id):
            if (button_id == 0):
                self.selectedButtons = sb.click1()
            elif (button_id == 1):
                self.selectedButtons = sb.click2()
            elif (button_id == 2):
                self.selectedButtons = sb.click3()
            elif (button_id == 3):
                self.selectedButtons = sb.click4()
            elif (button_id == 4):
                self.selectedButtons = sb.click5()
            elif (button_id == 5):
                self.selectedButtons = sb.click6()
            elif (button_id == 6):
                self.selectedButtons = sb.click7()
            elif (button_id == 7): 
                self.selectedButtons = sb.click8()
            else: 
                self.selectedButtons = sb.click9()

        
def main():
    root = tk.Tk()
    root.title("Sudoku Board")

    player_board = SudokuBoard(root)

    root.mainloop()

if __name__ == "__main__":
    main()
