from Choice import Choice
import tkinter as tk
from tkinter import Frame, Label, Button
import random
from LevelSetup import LevelSetup as setup
from pieces.Piece import Piece

class choiceSelect:

    choiceList = []
    selected_choice = None
    masterWindow = None
    childWindow=None

    def __init__(self,masterWindow):
        self.masterWindow = masterWindow


    def generate_choices(self):
        choiceNum = 3
        self.choiceList.clear()
        for i in range(choiceNum):
            newChoice = Choice(random.randint(2, 4), random.randint(1, 3),5,5)
            self.choiceList.append(newChoice)


    def display_choices(self,masterWindow) :
        w = tk.Toplevel()
        self.childWindow=w
        w.title("Select a Choice")
        w.geometry("600x200")
        w.protocol("WM_DELETE_WINDOW", lambda: choiceSelect.topWindowClose(w, masterWindow))


        def on_choice_click(idx):
            self.selected_choice = self.choiceList[idx]
            w.destroy()  # Close the choice window
            
            #setup.drawBoard(setup, self.selected_choice, masterWindow)

        # Create a frame for each choice
        for idx, choice in enumerate(self.choiceList):
            frame = Frame(w, borderwidth=2, relief="groove", width=200, height=200)
            frame.grid(row=0, column=idx, padx=10, pady=10, sticky="nsew")
            # Make the whole frame clickable
            frame.bind("<Button-1>", lambda e, i=idx: on_choice_click(i))
            # Display choice attributes (customize as needed)
            Label(frame, text=f"Choice {idx+1}", font=("Arial", 14, "bold")).pack(pady=10)
            Label(frame, text=f"Number of Enemies: {getattr(choice, 'enemyNumber', '')}").pack()
            Label(frame, text=f"Reward ID: {getattr(choice, 'reward', '')}").pack()
            # Make labels clickable too
            for child in frame.winfo_children():
                child.bind("<Button-1>", lambda e, i=idx: on_choice_click(i))

        # Make columns expand equally
        for i in range(3):
            w.grid_columnconfigure(i, weight=1)
        #w.mainloop()


    def generateEnemies(self, selectedChoice, badArmy):
        # Clear existing enemies
        badArmy.clear()

        # Generate enemies
        for i in range(selectedChoice.enemyNumber):
            newPiece = Piece(0, 0, "Pawn", "red")
            badArmy.append(newPiece)

        