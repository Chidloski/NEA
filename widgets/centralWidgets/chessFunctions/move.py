from widgets.centralWidgets.chessFunctions.moveChecking import *
from widgets.centralWidgets.chessFunctions.movementFunctions import *
from widgets.centralWidgets.chessFunctions.checkChecking import *

# function uses a list containing whether moving is active and the object to move (pieceToMove)
def move(domain, currentPiece, moving, pieceToMove, validTiles, moveNumber, attackers, previousMove, pgn):

    # if a move isn't active, it sets moving to true and pieceToMove to the piece object
    if moving == False:

        print("\n\n<------- NEW MOVE ------->")

        # de highlights the previous move
        highlightValidTiles(previousMove, domain, True)

        # if the turn number is even (such as on turn 0) it is white to move
        if (moveNumber / 2) == int((moveNumber / 2)):
            whoseTurn = "white"
        else:
            whoseTurn = "black"

        kingPos = getattr(domain, whoseTurn + "King").pos
        highlightValidTiles([kingPos], domain, True)

        # only if first click is on a piece and the right colour piece is clicked
        if currentPiece.metaObject().className() == "piece" and currentPiece.colour == whoseTurn:
            # metaObject.className returns the class of an object
            pieceToMove = currentPiece
            moving = True

            # original postion is a valid tile
            validTiles = [pieceToMove.pos]

            # adds the rest of the valid tiles onto the end of the list to retain the original position as a valid tile
            if currentPiece.moveset == "Pawn":
                print("clicked a Pawn")
                validTiles = validTiles + checkMovePawn(currentPiece.colour, currentPiece.pos, domain, attackers, currentPiece.hasMoved, moveNumber)

            elif currentPiece.moveset == "Queen":
                print("clicked a Queen")
                validTiles = validTiles + checkMoveDiagonal(currentPiece.colour, currentPiece.pos, domain, attackers)
                validTiles = validTiles + checkMoveStraight(currentPiece.colour, currentPiece.pos, domain, attackers)

            elif currentPiece.moveset == "King":
                print("clicked a King")
                validTiles = validTiles + checkMoveKing(currentPiece.colour, currentPiece.pos, domain, attackers)

            elif currentPiece.moveset == "Knight":
                print("clicked a Knight")
                validTiles = validTiles + checkMoveKnight(currentPiece.colour, currentPiece.pos, domain, attackers)

            elif currentPiece.moveset == "Rook":
                print("clicked a Rook")
                validTiles = validTiles + checkMoveStraight(currentPiece.colour, currentPiece.pos, domain, attackers)

            elif currentPiece.moveset == "Bishop":
                print("clicked a Bishop")
                validTiles = validTiles + checkMoveDiagonal(currentPiece.colour, currentPiece.pos, domain, attackers)

            highlightValidTiles(validTiles, domain, False)

            return moving, pieceToMove, validTiles, moveNumber, attackers, previousMove, pgn
        
        # however if first click is not of parent class piece nothing happens
        else:
            print("tile piece can't move")

            return moving, pieceToMove, validTiles, moveNumber, attackers, previousMove, pgn
    
    # handles when moving is true
    elif moving == True:

        highlightValidTiles(validTiles, domain, True)

        # if a tile is clicked
        if (currentPiece.metaObject().className() in ("darkSquare", "lightSquare")):
            
            if isTileValid(currentPiece.objectName(), validTiles):
                # moves piece to new tile whilst also updating move number and attackers if move isn't nullified
                moveNumber, attackers, previousMove, pgn = movingToTile(pieceToMove, currentPiece, domain, 
                                                                   moveNumber, previousMove, pgn, attackers)

        # if a piece is clicked
        elif currentPiece.metaObject().className() == "piece":

            if isTileValid(currentPiece.pos, validTiles):
                # moves piece to new tile whilst also updating move number and attackers if move isn't nullified
                moveNumber, attackers, previousMove, pgn = movingToTile(pieceToMove, getattr(domain, str(currentPiece.pos)), 
                                                                   domain, moveNumber, previousMove, pgn, attackers)

        print("pgn:")
        print(pgn)
    
        return False, -1, [], moveNumber, attackers, previousMove, pgn

