
import tkinter as tk
from LevelSetup import LevelSetup

def start_new_game(root):
    root.withdraw()  # Hide the main window
    cs = choiceSelect(root)
    cs.generate_choices()
    cs.display_choices(root)
    root.wait_window(cs.w)  # Wait until the choice window is closed
    print("did we get here1")
    c=1
    #while cs.selected_choice is None:
    #    print(c)  # Wait until the choice window is closed
    #    c+=1
#LevelSetup.drawBoard(cs.selected_choice, root)


root = tk.Tk()
btn = tk.Button(root, text="New Game", font=("Arial", 16), command=lambda: start_new_game(root))
btn.pack(expand=True, fill=tk.BOTH, padx=40, pady=40)


from Choice import Choice
import tkinter as tk
from tkinter import Frame, Label, Button
import random
from LevelSetup import LevelSetup as setup

class choiceSelect:

    choiceList = []
    selected_choice = None
    masterWindow = None
    w=None

    def __init__(self,masterWindow):
        self.masterWindow = masterWindow


    def generate_choices(self):
        choiceNum = 3
        self.choiceList.clear()
        for i in range(choiceNum):
            newChoice = Choice(random.randint(2, 4), random.randint(1, 3),5,5)
            self.choiceList.append(newChoice)

    def topWindowClose(topWindow, masterWindow):
        topWindow.destroy()
        masterWindow.deiconify()  # Show the main window again


    def display_choices(self,masterWindow) :
        w = tk.Toplevel()
        w.title("Select a Choice")
        w.geometry("600x200")
        w.protocol("WM_DELETE_WINDOW", lambda: choiceSelect.topWindowClose(w, masterWindow))
        self.w=w

        def on_choice_click(idx):
            print("did we get here3")
            self.selected_choice = self.choiceList[idx]
            print("did we get here2")
            w.destroy()  # Close the choice window
            print("did we get here4")
            
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

        print("did we get here6")
        return


root.mainloop()