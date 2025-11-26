
import tkinter as tk
from choiceSelect import choiceSelect
from LevelSetup import LevelSetup
from teamSelect import generatePlayerPieces


def start_new_game(root):
	playerReserve = []
	badArmy = []
	playerArmy = []
	cs = choiceSelect(root)

	# Hide the main window
	root.withdraw()  

	# Select team composition
	generatePlayerPieces(playerReserve) 

	# Select Level 
	cs.generate_choices() 
	cs.display_choices(root)

	# Wait until the choice window is closed
	root.wait_window(cs.childWindow)  

	# Generate enemies based on selected choice
	cs.generateEnemies(cs.selected_choice, badArmy)

	# Draw game board
	LevelSetup.drawBoard(LevelSetup,cs.selected_choice, root, playerReserve, badArmy)




root = tk.Tk()
root.title("Chess Game Launcher")
root.geometry("300x150")
btn = tk.Button(root, text="New Game", font=("Arial", 16), command=lambda: start_new_game(root))
btn.pack(expand=True, fill=tk.BOTH, padx=40, pady=40)
root.mainloop()


