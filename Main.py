
import tkinter as tk
from choiceSelect import choiceSelect
from LevelSetup import *
from teamSelect import generatePlayerPieces
from Gameplay import *


def start_new_game(root):
	playerReserve = {}
	badArmy = {}
	playerArmy = {}
	numOfPieces = 0
	
	# Hide the main window
	root.withdraw()  

	# Select team composition
	generatePlayerPieces(numOfPieces, playerReserve) 

	while (True):
		cs = choiceSelect(root)
		ls = LevelSetup()


		# Select Level 
		cs.generate_choices() 
		cs.display_choices(root)

		# Wait until the choice window is closed
		root.wait_window(cs.childWindow)  

		# Catch for if the choice window is closed without choice made
		if(cs.selected_choice is None):
			break
		
		# Generate enemies based on selected choice
		cs.generateEnemies(cs.selected_choice, badArmy, numOfPieces)

		# Draw game board
		gameBoard, m, w, rectangles, colours = ls.drawBoard(cs.selected_choice, root, playerReserve, badArmy, playerArmy)
		root.wait_variable(ls.setupComplete)

		# Catch for if the level setup window is closed without setup complete
		if not ls.setupComplete.get():
			break
	
		# Play the game
		game = Gameplay(playerArmy, gameBoard, badArmy)
		ls.game = game
		game.playGame(m, w, rectangles, colours, cs.selected_choice)
		root.wait_variable(game.levelComplete)
		#root.wait_window()

		if badArmy:
			print("Player loses")
			break
		else:
			print("player wins")
			while playerArmy:
				pieceID, piece = playerArmy.popitem()
				playerReserve[pieceID] = piece
			
		
		# Level complete screen
		print("Congratulations you won!!!!")
		
	





root = tk.Tk()
root.title("Chess Game Launcher")
root.geometry("300x150")
btn = tk.Button(root, text="New Game", font=("Arial", 16), command=lambda: start_new_game(root))
btn.pack(expand=True, fill=tk.BOTH, padx=40, pady=40)
root.mainloop()
