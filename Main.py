
import tkinter as tk
from choiceSelect import choiceSelect

def start_new_game(root):
	root.withdraw()  # Hide the main window
	cs = choiceSelect()
	cs.generate_choices()
	cs.display_choices(root)


root = tk.Tk()
root.title("Chess Game Launcher")
root.geometry("300x150")
btn = tk.Button(root, text="New Game", font=("Arial", 16), command=lambda: start_new_game(root))
btn.pack(expand=True, fill=tk.BOTH, padx=40, pady=40)
root.mainloop()