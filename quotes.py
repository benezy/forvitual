import random
import tkinter as tk


quotes = [
    "Be the change you wish to see in the world.",
    "Don't watch the clock; do what it does. Keep going.",
    "I can accept failure, everyone fails at something. But I can't accept not trying.",
    "I have not failed. I've just found 10,000 ways that won't work.",
    "The only limit to our realization of tomorrow will be our doubts of today."
]

def generate_quote():
    return random.choice(quotes)

# create the main window
root = tk.Tk()
root.title("Random Quote Generator")

# create a label to display the quote
quote_label = tk.Label(root, text="Click the button to generate a quote.")
quote_label.pack()

# create a button to generate a new quote
button = tk.Button(root, text="New Quote", command=lambda: quote_label.configure(text=generate_quote()))
button.pack()

root.mainloop()
