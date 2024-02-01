from tkinter import *
from time import strftime

# creating tkinter window
digital_clock = Tk()
digital_clock.geometry("500x250")
digital_clock.title('Unique Digital Clock By, Ujjwal Kamila')

# Function to display time on the label
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# Increase the user experience by designing the label widget
label = Label(digital_clock, font=('calibri', 40, 'bold'),
              background='#AA0000',
              foreground='white')

# Add a custom welcome message
welcome_message = Label(digital_clock, text="Welcome to Digital Clock :) ",
                       font=('calibri', 16),
                       background='#AA0000',
                       foreground='white')
welcome_message.pack(side=BOTTOM)

# Add a button to change the clock color
def change_color():
    colors = ['#AA0000', '#00AA00', '#0000AA', '#AA00AA', '#AAAA00']
    current_color = label.cget("background")
    new_color = colors[(colors.index(current_color) + 1) % len(colors)]
    label.config(background=new_color)
    welcome_message.config(background=new_color)
    
color_button = Button(digital_clock, text="Change Color", command=change_color)
color_button.pack(side=TOP)

# Clock at the center of the tkinter window
label.pack(anchor='center')
time()  # function calling

digital_clock.mainloop()
