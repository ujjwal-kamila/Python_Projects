from tkinter import *
import random

# New fun messages and relationship tips
MESSAGES_AND_TIPS = {
    "high": {
        "message": [
            "🔥 Love is on fire! You two are inseparable!",
            "💖 A fairytale couple in the making!",
            "🌟 Your hearts beat in perfect harmony!",
            "💍 This could be eternal love!",
            "🎶 Every love song was written for you!"
        ],
        "tips": [
            "Surprise each other with handwritten notes.",
            "Dance together—even if there’s no music.",
            "Travel somewhere new and make memories.",
            "Cook a special dinner together.",
            "Always celebrate the little milestones."
        ]
    },
    "medium": {
        "message": [
            "😊 A sweet bond is growing stronger!",
            "🌈 You’re on the way to something beautiful!",
            "💌 A lovely connection is blooming!",
            "🌹 Romance is in the air!",
            "✨ You two bring out the best in each other!"
        ],
        "tips": [
            "Find new hobbies to enjoy together.",
            "Make each other laugh every day.",
            "Give compliments often, they mean a lot.",
            "Plan weekly ‘us-time’ away from phones.",
            "Listen more, talk deeper."
        ]
    },
    "low": {
        "message": [
            "🤔 Some work needed, but don’t give up!",
            "🌱 Small seeds can grow into strong love.",
            "💡 Focus on building trust first.",
            "💬 Honest talks can make wonders happen.",
            "🕰️ Give it time, love grows slowly."
        ],
        "tips": [
            "Communicate without judgment.",
            "Respect each other’s space.",
            "Share dreams and future plans.",
            "Practice patience and kindness.",
            "Start with strong friendship."
        ]
    }
}

# Function to calculate love percentage
def calculate_love():
    name1_text = name1.get().strip()
    name2_text = name2.get().strip()

    if not name1_text or not name2_text:
        result.config(text="⚠️ Please enter both names!", fg="red")
        return

    # Simple algorithm based on ASCII values
    combined_names = name1_text.lower() + name2_text.lower()
    love_score = sum(ord(char) for char in combined_names) % 100

    if love_score > 80:
        category = "high"
    elif love_score > 50:
        category = "medium"
    else:
        category = "low"

    message = random.choice(MESSAGES_AND_TIPS[category]["message"])
    tip = random.choice(MESSAGES_AND_TIPS[category]["tips"])

    result.config(
        text=f"💘 Love Percentage: {love_score}%\n\n{message}\n\n💡 Tip: {tip}",
        fg="white",
        bg="#222244"
    )

def reset_fields():
    name1.delete(0, END)
    name2.delete(0, END)
    result.config(
        text="💘 Love Percentage between both of You:",
        fg="white",
        bg="#222244"
    )

# Creating GUI window
root = Tk()
root.geometry('600x500')
root.title('Love Calculator ❤️')
root.configure(bg="#222244")  # Dark background

# Center heading
heading = Label(
    root, 
    text='💖 The Love Calculator 💖', 
    font=("Helvetica", 18, "bold"),  
    fg="pink", 
    bg="#222244"
)
heading.pack(pady=20)

# Input fields
slot1 = Label(root, text="💁 Enter Your Name:", font=("Arial", 12, "bold"), fg="white", bg="#222244")
slot1.pack()
name1 = Entry(root, border=3, font=("Arial", 12))
name1.pack(pady=5)

slot2 = Label(root, text="💃 Enter Partner's Name:", font=("Arial", 12, "bold"), fg="white", bg="#222244")
slot2.pack()
name2 = Entry(root, border=3, font=("Arial", 12))
name2.pack(pady=5)

# Buttons
bt = Button(root, text="💘 Calculate", height=2, width=15, command=calculate_love, bg="lightgreen", font=("Arial", 12, "bold"))
bt.pack(pady=15)

reset_btn = Button(root, text="🔄 Reset", height=2, width=15, command=reset_fields, bg="tomato", font=("Arial", 12, "bold"))
reset_btn.pack(pady=5)

# Result area
result = Label(
    root, 
    text='💘 Love Percentage between both of You:', 
    font=("Arial", 12, "italic"), 
    wraplength=500, 
    justify="center",
    fg="white",
    bg="#222244"
)
result.pack(pady=20)

root.mainloop()
