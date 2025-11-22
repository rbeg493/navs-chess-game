

class Piece:
    color = None

    # Width and height positions = col and row positions on the board
    width_pos = 0
    height_pos = 0
    icon = ""
    for_vertical = 1
    down = 0
    left = 0
    right = 0
    id = [height_pos, width_pos]

    
    def __init__(self, width_pos, height_pos, icon):
        self.width_pos = width_pos
        self.height_pos = height_pos
        self.icon = icon

    def __str__(self):
        return f"Color: {self.color},id: {self.id},icon: {self.icon}"
    
    def isValidMove(self, newRow, newCol, board):
        # Unfinished
        if not(1 <= newRow <= board.height and 1 <= newCol <= board.width):
            return False
        for piece in board.pieces:
            if piece.color == self.color and piece.width_pos == newCol and piece.height_pos == newRow:
                return False

        return True
    


