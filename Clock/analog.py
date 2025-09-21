import tkinter as tk
from time import localtime
import math

# --- Configuration ---
WINDOW_SIZE = 450
CLOCK_RADIUS = 180
CENTER = WINDOW_SIZE // 2

# Colors
BG_COLOR = "#1e1e2f"
CLOCK_BG = "#222244"
TICK_COLOR = "#ffcc00"
HOUR_HAND_COLOR = "#ff5555"
MIN_HAND_COLOR = "#55ff55"
SEC_HAND_COLOR = "#55aaff"
NUMBER_COLOR = "#ffffff"

# Create tkinter window
root = tk.Tk()
root.title("✨ Analog Clock with Numbers | By Ujjwal Kamila ✨")
root.geometry(f"{WINDOW_SIZE}x{WINDOW_SIZE+60}")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# Create Canvas
canvas = tk.Canvas(root, width=WINDOW_SIZE, height=WINDOW_SIZE, bg=BG_COLOR, highlightthickness=0)
canvas.pack()

# Draw clock circle
canvas.create_oval(CENTER-CLOCK_RADIUS, CENTER-CLOCK_RADIUS,
                   CENTER+CLOCK_RADIUS, CENTER+CLOCK_RADIUS,
                   fill=CLOCK_BG, outline=TICK_COLOR, width=6)

# Draw tick marks
for i in range(60):
    angle = math.radians(i * 6)  # 360 / 60 = 6 degrees
    length = 20 if i % 5 == 0 else 10  # Longer ticks for hours
    width = 3 if i % 5 == 0 else 1
    x_start = CENTER + (CLOCK_RADIUS - length) * math.sin(angle)
    y_start = CENTER - (CLOCK_RADIUS - length) * math.cos(angle)
    x_end = CENTER + CLOCK_RADIUS * math.sin(angle)
    y_end = CENTER - CLOCK_RADIUS * math.cos(angle)
    canvas.create_line(x_start, y_start, x_end, y_end, fill=TICK_COLOR, width=width)

# Draw numbers 1 to 12
for i in range(1, 13):
    angle = math.radians(i * 30)  # 360 / 12
    x = CENTER + (CLOCK_RADIUS - 40) * math.sin(angle)
    y = CENTER - (CLOCK_RADIUS - 40) * math.cos(angle)
    canvas.create_text(x, y, text=str(i), fill=NUMBER_COLOR, font=("Verdana", 16, "bold"))

# Welcome label
welcome_label = tk.Label(root, text="Welcome to Analog Clock 🙂",
                         font=("Verdana", 14, "bold"), bg=BG_COLOR, fg=TICK_COLOR)
welcome_label.pack(pady=5)

# Function to update clock hands
def update_clock():
    t = localtime()
    seconds = t.tm_sec
    minutes = t.tm_min
    hours = t.tm_hour % 12

    # Clear previous hands
    canvas.delete("hands")

    # Calculate angles
    sec_angle = math.radians(seconds * 6)
    min_angle = math.radians(minutes * 6 + seconds * 0.1)
    hour_angle = math.radians(hours * 30 + minutes * 0.5)

    # Second hand
    x_sec = CENTER + (CLOCK_RADIUS - 30) * math.sin(sec_angle)
    y_sec = CENTER - (CLOCK_RADIUS - 30) * math.cos(sec_angle)
    canvas.create_line(CENTER, CENTER, x_sec, y_sec, fill=SEC_HAND_COLOR, width=2, tag="hands")

    # Minute hand
    x_min = CENTER + (CLOCK_RADIUS - 60) * math.sin(min_angle)
    y_min = CENTER - (CLOCK_RADIUS - 60) * math.cos(min_angle)
    canvas.create_line(CENTER, CENTER, x_min, y_min, fill=MIN_HAND_COLOR, width=4, tag="hands")

    # Hour hand
    x_hour = CENTER + (CLOCK_RADIUS - 90) * math.sin(hour_angle)
    y_hour = CENTER - (CLOCK_RADIUS - 90) * math.cos(hour_angle)
    canvas.create_line(CENTER, CENTER, x_hour, y_hour, fill=HOUR_HAND_COLOR, width=6, tag="hands")

    # Center dot
    canvas.create_oval(CENTER-8, CENTER-8, CENTER+8, CENTER+8, fill="#ffffff", tag="hands")

    # Update every 1000ms
    root.after(1000, update_clock)

# Start the clock
update_clock()
root.mainloop()
