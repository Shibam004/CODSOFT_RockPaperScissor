import tkinter as tk
import random
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x400")
root.resizable(False, False)

# Global score tracking
user_score = 0
computer_score = 0

# Choices
choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    result = ""
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        user_score += 1
        result = "You Win!"
    else:
        computer_score += 1
        result = "Computer Wins!"

    # Update result and scores
    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")
    score_label.config(text=f"Score → You: {user_score}  |  Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text="Score → You: 0  |  Computer: 0")
    messagebox.showinfo("Reset", "Game has been reset!")

# Labels and Buttons
title = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 18, "bold"))
title.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

score_label = tk.Label(root, text="Score → You: 0  |  Computer: 0", font=("Arial", 12, "bold"))
score_label.pack()

reset_btn = tk.Button(root, text="Reset Game", command=reset_game)
reset_btn.pack(pady=10)

exit_btn = tk.Button(root, text="Exit", command=root.quit)
exit_btn.pack(pady=5)

# Start GUI loop
root.mainloop()
