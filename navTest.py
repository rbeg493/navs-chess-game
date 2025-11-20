import tkinter as tk
from pieces.Piece import Piece
from pieces.Rook import Rook

rook = Rook("Black", True)
print(rook)
window = tk.Tk()
greeting = tk.Label(window, text="Hello, Tkinter")
greeting.pack()
window.mainloop()