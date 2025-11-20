Navs Chess Game

Board:
  Height
  Width
  
Piece:
  Colour,
  BishopMovement = False, 
  PawnMovement = False, 
  KnightMovement = False, 
  RookMovement = False, 
  KingMovement = False, 
  IsDead = False

Rook inherits Piece:
  RookMovement = True

Knight inherits Piece:
  KnightMovement = True

Bishop inherits Piece:
  BishopMovement = True

Queen inherits Piece:
  RookMovement = True, 
  BishopMovement = True

King inherits Piece:
  KingMovement = True

Pawn inherits Piece:
  PawnMovement = True


Tech:
	Python:
    	Tkinter
	Github:
	VSCode:
