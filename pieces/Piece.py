

class Piece:
    colour = None
    bishopMovement = False
    pawnMovement = False
    knightMovement = False
    rookMovement = False
    kingMovement = False
    isDead = False

    width_pos = 0
    height_pos = 0
    icon = ""
    
    def __init__(self, width_pos, height_pos, icon):
        self.width_pos = width_pos
        self.height_pos = height_pos
        self.icon = icon

    def __str__(self):
        return f"Colour: {self.colour}, Bishop Movement: {self.bishopMovement}, Pawn Movement: {self.pawnMovement}, Knight Movement: {self.kingMovement}, Rook Movement: {self.rookMovement}, King Movement: {self.kingMovement}, Is Dead: {self.isDead}"
    


