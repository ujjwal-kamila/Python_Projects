# main.py
# Simple Tic Tac Toe Game using Python 
# By Ujjwal Kamila

class TicTacToe:
    def __init__(self):
        self.xState = [0] * 9
        self.oState = [0] * 9
        self.turn = 1  # 1 for X, 0 for O
        self.wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]

    def sum(self, a, b, c):
        """Helper function for win check"""
        return a + b + c

    def printBoard(self):
        """Prints the board in console"""
        def mark(i):
            return 'X' if self.xState[i] else ('O' if self.oState[i] else i)

        print(f" ___________")
        print(f"|   |   |   |")
        print(f"| {mark(0)} | {mark(1)} | {mark(2)} |")
        print(f"|___|___|___|")
        print(f"|   |   |   |")
        print(f"| {mark(3)} | {mark(4)} | {mark(5)} |")
        print(f"|___|___|___|")
        print(f"|   |   |   |")
        print(f"| {mark(6)} | {mark(7)} | {mark(8)} |")
        print(f"|___|___|___|")

    def checkWin(self):
        """Check if X or O won. Returns 1 for X, 0 for O, -1 for no win."""
        for win in self.wins:
            if self.sum(self.xState[win[0]], self.xState[win[1]], self.xState[win[2]]) == 3:
                return 1
            if self.sum(self.oState[win[0]], self.oState[win[1]], self.oState[win[2]]) == 3:
                return 0
        return -1

    def play_turn(self, value):
        """Plays a move safely with error handling"""
        try:
            if not (0 <= value <= 8):
                raise ValueError("❌ Invalid move! Please choose between 0 and 8.")

            if self.xState[value] or self.oState[value]:
                raise ValueError("⚠️ Spot already taken! Try another position.")

            if self.turn == 1:
                self.xState[value] = 1
            else:
                self.oState[value] = 1

            # Switch turn
            self.turn = 1 - self.turn
            return True

        except ValueError as e:
            print(e)
            return False


if __name__ == "__main__":
    game = TicTacToe()
    print("🎮 Welcome to Tic Tac Toe Game | By Ujjwal Kamila 😎")

    while True:
        game.printBoard()
        try:
            move = int(input(f"Enter {'X' if game.turn == 1 else 'O'}'s chance (0-8): "))
        except ValueError:
            print("❌ Invalid input! Please enter a number between 0-8.")
            continue

        if not game.play_turn(move):
            continue  # retry if invalid move

        result = game.checkWin()
        if result != -1:
            game.printBoard()
            print("🎉 X Won the match!" if result == 1 else "🎉 O Won the match!")
            print("✅ Match Over!")
            break

# # Simple Tic Tac Toe Game using Python 
# def sum(a, b, c ):
#     return a + b + c


# def printBoard(xState, zState):
#     zero = 'X' if xState[0] else ('O' if zState[0] else 0)
#     one = 'X' if xState[1] else ('O' if zState[1] else 1)
#     two = 'X' if xState[2] else ('O' if zState[2] else 2)
#     three = 'X' if xState[3] else ('O' if zState[3] else 3)
#     four = 'X' if xState[4] else ('O' if zState[4] else 4)
#     five = 'X' if xState[5] else ('O' if zState[5] else 5)
#     six = 'X' if xState[6] else ('O' if zState[6] else 6)
#     seven = 'X' if xState[7] else ('O' if zState[7] else 7)
#     eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    
#     print(f" ___________")
#     print(f"|   |   |   |")
#     print(f"| {zero} | {one} | {two} |")
#     print(f"|___|___|___|")
#     print(f"|   |   |   |")
#     print(f"| {three} | {four} | {five} |")
#     print(f"|___|___|___|")
#     print(f"|   |   |   |")
#     print(f"| {six} | {seven} | {eight} |")
#     print(f"|___|___|___|")
    
    
    
#     # print(f"{zero} | {one} | {two} ")
#     # print(f"--|---|---")
#     # print(f"{three} | {four} | {five} ")
#     # print(f"--|---|---")
#     # print(f"{six} | {seven} | {eight} ") 

# def checkWin(xState, zState):
#     wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
#     for win in wins:
#         if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
#             print("X Won the match")
#             return 1
#         if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
#             print("O Won the match")
#             return 0
#     return -1
    
# if __name__ == "__main__":
#     xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#     zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#     turn = 1 # 1 for X and 0 for O
#     print(" Welcome to Tic Tac Toe Game 🙏️🙏️ 🎮️  👉️👉️👉️👉️ Created By Ujjwal Kamila 😎️ ")
#     while(True):
#         printBoard(xState, zState)
#         if(turn == 1):
#             print("Enter X's Chance  -> ")
#             value = int(input("Please enter a value : "))
#             xState[value] = 1
#         else:
#             print("Enter O's Chance  -> ")
#             value = int(input("Please enter a value : "))
#             zState[value] = 1
#         cwin = checkWin(xState, zState)
#         if(cwin != -1):
#             print("Match over")
#             break
        
#         turn = 1 - turn 