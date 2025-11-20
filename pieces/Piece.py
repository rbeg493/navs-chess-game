

class Piece:
    colour = None
    bishopMovement = False
    pawnMovement = False
    knightMovement = False
    rookMovement = False
    kingMovement = False
    isDead = False
    
    def __init__(self):
        pass

    def __str__(self):
        return f"Colour: {self.colour}, Bishop Movement: {self.bishopMovement}, Pawn Movement: {self.pawnMovement}, Knight Movement: {self.kingMovement}, Rook Movement: {self.rookMovement}, King Movement: {self.kingMovement}, Is Dead: {self.isDead}"
    


