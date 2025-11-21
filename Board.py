class Board:
    def __init__(self, width, height, pieces):
        self.width = width
        self.height = height
        self.pieces = pieces

    # Board should store the current gamestate, including pieces and their positions
    # Pieces contain location information, so list of pieces in Board should work
