
# 🛠️ Python Mini Projects for Beginners
Welcome\! This repository contains a set of small, polished Python projects created by Ujjwal Kamila. Each project is easy to run, beginner-friendly, and demonstrates GUI or console skills using standard Python libraries.

### Projects included

  * **Clock** (Analog + Digital variations)
  * **Love Calculator**
  * **Number Guessing Game**
  * **Rent Calculator**
  * **Rock Paper Scissor Game**
  * **Tic Tac Toe Game**
  * **UPI TO QR** (UPI QR code generator)

-----


## About

This repository groups small, fun Python projects—mostly GUI apps made with Tkinter and a couple of console utilities. They are great for learning GUI programming, event handling, and basic Python logic.

## Projects

### 1\. Clock

**Description**: Beautiful analog and digital clocks with dark themes.
**Files**: `analog.py`, `Digital_clock.py`
**Features**:

  * Analog clock with hour/minute/second hands
  * Clean digital clock display
  * Dark, modern themes
    **Run**:

<!-- end list -->

```bash
python Clock/analog.py
# or
python Clock/Digital_clock.py
```

### 2\. Love Calculator

**Description**: A playful GUI app that calculates a “compatibility percentage” for two names.
**Files**: `love_calculator.py`
**Features**:

  * Simple, friendly UI
  * Calculates a fun compatibility score
    **Run**:

<!-- end list -->

```bash
python "Love Calculator/love_calculator.py"
```

### 3\. Number Guessing Game

**Description**: Console-based classic game where the user guesses a randomly chosen number.
**Files**: `main.py`
**Features**:

  * Random number generation
  * Hints for the user (higher/lower)
    **Run**:

<!-- end list -->

```bash
python "Number guessing Game/main.py"
```

### 4\. Rent Calculator

**Description**: A small console calculator to help compute rent breakdowns.
**Files**: `main.py`
**Features**:

  * Input rent, duration, etc.
  * Clear output and formatting
    **Run**:

<!-- end list -->

```bash
python "Rent Calculator/main.py"
```

### 5\. Rock Paper Scissor Game

**Description**: A polished GUI for the classic Rock-Paper-Scissors game.
**Files**: `main.py` (logic), `gui.py` (UI)
**Features**:

  * Play against a random computer move
  * Interactive buttons and UI
  * Clear result display
    **Run**:

<!-- end list -->

```bash
python "Rock Paper Game/gui.py"
```

### 6\. Tic Tac Toe Game

**Description**: Two-player Tic Tac Toe GUI with a scoreboard and reset functionality.
**Files**: `main.py` (logic), `gui.py` (UI)
**Features**:

  * Clickable grid for placing X and O
  * Win detection and score tracking
  * Reset board and exit options
    **Run**:

<!-- end list -->

```bash
python "Tic Tac Toe Game/gui.py"
```

### 7\. UPI TO QR

**Description**: Generate a UPI payment QR code image from a UPI ID and amount.
**Files**: `main.py`
**Requirements**: `qrcode[pil]`
**Features**:

  * Input UPI ID and amount
  * Saves a scannable `upi.png` image
    **Run**:

<!-- end list -->

```bash
python "UPI TO QR/main.py"
```

-----

## Requirements & Installation

Recommended Python: 3.8+

Most projects use only the Python standard library (**Tkinter**). For the UPI QR project, you need to install a library:

```bash
# Install the qrcode library with image support
pip install "qrcode[pil]"
```



-----

## How to Run

1.  Clone the repository:
    ```bash
    git clone https://github.com/ujjwal-kamila/Python_Projects.git
    cd your-repo
    ```
2.  Navigate to the project folder you want and run the corresponding Python script:
    ```bash
    # Example for Rock Paper Game (use quotes for names with spaces)
    python "Rock Paper Game/gui.py"

    # Example for Clock
    python Clock/analog.py
    ```

-----

## Project Structure

```

├─ .gitignore
├─ LICENSE
├─ README.md
├─ Clock/
│  ├─ Digital_clock.py
│  └─ analog.py
├─ Love Calculator/
│  └─ love_calculator.py
├─ Number guessing Game/
│  └─ main.py
├─ Rent Calculator/
│  └─ main.py
├─ Rock Paper Game/
│  ├─ gui.py
│  └─ main.py
├─ Tic Tac Toe Game/
│  ├─ images/
│  ├─ README.md
│  ├─ gui.py
│  └─ main.py
└─ UPI TO QR/
   ├─ README.md
   ├─ main.py
   └─ upi.png
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome\! Feel free to check the issues page.



## 📄 License

This project is licensed under the MIT License.

<br>

---

<h3 align="center">
  <b>Happy Coding 👨‍💻 | Keep Practicing 💡</b>
</h3>

---

<h3 align="center">
  <b>Let's Connect!! </b>
  <img src="https://user-images.githubusercontent.com/74038190/214644145-264f4759-7633-441e-9d67-d8dda9d50d26.gif" width=95px>
</h3>

<p align="center">
  <a href="https://ujjwal-kamila.vercel.app/"><img src="https://img.shields.io/badge/Portfolio-Visit-blue?logo=Firefox&logoColor=white"></a>
  <a href="https://www.linkedin.com/in/ujjwal-kamila-8a12a4262/"><img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white"></a>
  <a href="https://leetcode.com/ujjwalkamila86/"><img src="https://img.shields.io/badge/LeetCode-FFA116.svg?logo=LeetCode&logoColor=black"></a>
</p>