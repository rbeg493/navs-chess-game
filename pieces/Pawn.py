from pieces.Piece import Piece

class Pawn(Piece):

    def __init__(self, colour, pawnMovement):
       self.colour = colour
       self.pawnMovement = pawnMovement
