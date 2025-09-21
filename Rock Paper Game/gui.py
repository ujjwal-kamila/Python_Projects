import tkinter as tk
from main import play_rps

# Dark theme colors
BG_COLOR = "#0f0f1f"
BTN_COLOR = "#1f1f3f"
BTN_HOVER = "#ffcc00"
TEXT_COLOR = "#ffffff"
RESULT_COLOR = "#ff9900"

class RPSDarkGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors 🎮")
        self.root.configure(bg=BG_COLOR)
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # Title
        title = tk.Label(root, text="Rock Paper Scissors", font=("Verdana", 24, "bold"),
                         bg=BG_COLOR, fg=BTN_HOVER)
        title.pack(pady=20)

        # Instruction
        instr = tk.Label(root, text="Choose your move:", font=("Arial", 14),
                         bg=BG_COLOR, fg=TEXT_COLOR)
        instr.pack(pady=5)

        # Button Frame
        btn_frame = tk.Frame(root, bg=BG_COLOR)
        btn_frame.pack(pady=10)

        # Rock, Paper, Scissor Buttons
        self.buttons = {}
        for choice in ["Rock", "Paper", "Scissor"]:
            btn = tk.Button(btn_frame, text=choice, font=("Arial", 14, "bold"),
                            bg=BTN_COLOR, fg=TEXT_COLOR, width=12, height=2,
                            bd=0, relief="ridge",
                            command=lambda ch=choice: self.make_move(ch))
            btn.pack(side="left", padx=10)
            self.buttons[choice] = btn
            # Hover effect
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=BTN_HOVER, fg=BG_COLOR))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=BTN_COLOR, fg=TEXT_COLOR))

        # Result Label
        self.result_label = tk.Label(root, text="", font=("Arial", 16, "bold"),
                                     bg=BG_COLOR, fg=RESULT_COLOR, wraplength=450, justify="center")
        self.result_label.pack(pady=30)

        # Exit Button
        exit_btn = tk.Button(root, text="❌ Exit", font=("Arial", 12, "bold"),
                             bg="#ff4444", fg=TEXT_COLOR, width=10, command=root.quit)
        exit_btn.pack(pady=10)

    def make_move(self, user_choice):
        comp_choice, result = play_rps(user_choice)
        self.result_label.config(
            text=f"Your Choice: {user_choice}  |  Computer Choice: {comp_choice}\n\nResult: {result}"
        )

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = RPSDarkGUI(root)
    root.mainloop()
