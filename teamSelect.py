from pieces.Piece import Piece


def generatePlayerPieces(playerReserve):
	for i in range(3):
		newPiece = Piece(0, 0, "Pawn", "blue")
		playerReserve.append(newPiece)
