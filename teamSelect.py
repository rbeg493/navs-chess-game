from pieces.Piece import Piece


def generatePlayerPieces(numOfPieces, playerReserve):
	for i in range(3):
		newPiece = Piece(numOfPieces, 0, 0, "Pawn", "blue")
		playerReserve.append(newPiece)
		numOfPieces += 1
