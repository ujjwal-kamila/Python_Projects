import tkinter as tk
from tkinter import messagebox
import main  
class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(" Tic Tac Toe 🎮 | By Ujjwal Kamila ✨")
        self.root.configure(bg="#1e1e2f")
        self.root.resizable(False, False)

        # Game States
        self.xState = [0] * 9
        self.zState = [0] * 9
        self.turn = 1  # 1 for X, 0 for O

        # Scoreboard
        self.score_x = 0
        self.score_o = 0
        self.score_draw = 0

        # Title Label
        title = tk.Label(root, text="Tic Tac Toe", font=("Comic Sans MS", 28, "bold"),
                         bg="#1e1e2f", fg="#ffcc00")
        title.grid(row=0, column=0, columnspan=3, pady=10)

        # Scoreboard Label
        self.score_label = tk.Label(root, text=self.get_score_text(),
                                    font=("Arial", 14, "bold"), bg="#1e1e2f", fg="#ffffff")
        self.score_label.grid(row=1, column=0, columnspan=3, pady=5)

        # Buttons for board
        self.buttons = []
        for i in range(9):
            btn = tk.Button(root, text="", font=("Verdana", 24, "bold"),
                            width=5, height=2,
                            bg="#2e2e44", fg="white",
                            activebackground="#ffcc00",
                            activeforeground="#000000",
                            relief="flat", bd=5,
                            command=lambda i=i: self.handle_click(i))
            btn.grid(row=(i // 3) + 2, column=i % 3, padx=8, pady=8, sticky="nsew")
            self.buttons.append(btn)

        # Reset Button
        reset_btn = tk.Button(root, text="🔄 Reset Game", font=("Arial", 14, "bold"),
                              bg="#ff4444", fg="white", relief="flat",
                              padx=10, pady=5, command=self.reset_board)
        reset_btn.grid(row=5, column=0, columnspan=3, pady=10)

        # Exit Button
        exit_btn = tk.Button(root, text="❌ Exit", font=("Arial", 12, "bold"),
                             bg="#4444ff", fg="white", relief="flat",
                             padx=10, pady=5, command=root.quit)
        exit_btn.grid(row=6, column=0, columnspan=3, pady=5)

    def get_score_text(self):
        return f"⭐ X: {self.score_x}   ⭐ O: {self.score_o}   🤝 Draws: {self.score_draw}"

    def handle_click(self, index):
        if self.buttons[index]["text"] == "":
            if self.turn == 1:  # X turn
                self.buttons[index].config(text="X", fg="#ff5555")
                self.xState[index] = 1
            else:  # O turn
                self.buttons[index].config(text="O", fg="#55aaff")
                self.zState[index] = 1

            # Check Win
            result = main.checkWin(self.xState, self.zState)
            if result == 1:
                self.score_x += 1
                messagebox.showinfo("🎉 Winner", "Player X Wins! 🎉")
                self.reset_board(update_score=True)
                return
            elif result == 0:
                self.score_o += 1
                messagebox.showinfo("🎉 Winner", "Player O Wins! 🎉")
                self.reset_board(update_score=True)
                return
            elif all(self.buttons[i]["text"] != "" for i in range(9)):
                self.score_draw += 1
                messagebox.showinfo("🤝 Draw", "It's a Draw! 🤝")
                self.reset_board(update_score=True)
                return

            # Change Turn
            self.turn = 1 - self.turn

    def reset_board(self, update_score=False):
        for btn in self.buttons:
            btn.config(text="", bg="#2e2e44")
        self.xState = [0] * 9
        self.zState = [0] * 9
        self.turn = 1
        if update_score:
            self.score_label.config(text=self.get_score_text())


# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
