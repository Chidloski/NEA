from widgets.centralWidgets.chessFunctions.checkChecking import checkForCheck
from widgets.centralWidgets.chessFunctions.checkMateChecking import checkForCheckMate, checkForStaleMate
from widgets.centralWidgets.chessFunctions.moveChecking import *
from widgets.utilityWidgets.functions.playFunctions import goToStage3
from PyQt5.QtGui import QPixmap

pieceToPromote = None

# moving to tile first ensures that the targeted move doesn't go to the start position
# -> as doing so simply cancels the move
# it then removes a piece if necessary and updates the state of the board
def movingToTile(pieceToMove, tile, domain, moveNumber, previousMove, pgn, attackers):

    castling = False

    # checks whether a piece has been double clicked / move has been nullified
    if pieceToMove.pos != str(tile.objectName()):

        if pieceToMove.colour == "white":
            pgnMovePrefix = " " + str(int(moveNumber / 2) + 1) + ". "

        else:
            pgnMovePrefix = " "

        # adds the starting position to the previous move array
        previousMove = [pieceToMove.pos]

        pgnInitials = {"Pawn": "", "Knight": "N", "King": "K", "Queen": "Q", "Bishop": "B", "Rook": "R"}

        pgnCurrentMove = pgnMovePrefix + pgnInitials[pieceToMove.moveset]
        pgnCurrentMove = pgnCurrentMove + checkIfMoveIsUnique(domain, pieceToMove, tile.objectName(), moveNumber, attackers)

        # certain things must occur which are bespoke to the king when it moves
        if pieceToMove.moveset == "King":

            # prevent castling happening after king has moved
            pieceToMove.hasMoved = True

            # checks whether the king move is a castling
            if abs(ord(pieceToMove.pos[0]) - ord(str(tile.objectName()[0]))) == 2:
                castling = True

                # checks which rook also needs to be moved and to where
                if str(tile.objectName())[0] == "c":
                    rookToMove = getattr(domain, pieceToMove.colour + "ARook")
                    targetFile = "d"
                    pgnCurrentMove = pgnMovePrefix + "O-O-O"

                else:
                    rookToMove = getattr(domain, pieceToMove.colour + "HRook")
                    targetFile = "f"
                    pgnCurrentMove = pgnMovePrefix + "O-O"

                # position rook needs to move to
                rookMovesTo = targetFile + str(pieceToMove.pos[1])

                # tile which rook must move to
                tileRookMovesTo = getattr(domain, rookMovesTo)

                # move rook in UI
                rookToMove.move(int(tileRookMovesTo.x()) + 5, int(tileRookMovesTo.y()) + 5)

                # empty rook's previous position
                getattr(domain, rookToMove.pos).occupied = "False"

                # prevent further castling with this rook
                rookToMove.hasMoved = True

                # updates rook position
                rookToMove.pos = rookMovesTo

                # updates what occupies tile rook moves to
                tileRookMovesTo.occupied = rookToMove.objectName()

        elif pieceToMove.moveset == "Rook":
            # prevents castling with the rook after kt has moved
            pieceToMove.hasMoved = True

        elif pieceToMove.moveset == "Pawn":

            if abs(ord(pieceToMove.pos[1]) - ord(str(tile.objectName()[1]))) == 2:
                # explaining maths on position of tile needing en passant trigger
                # - file of moving pawn remains the same
                # - finds distance between tile and pawn relative to pawn
                # - divides distance by 2
                tileNeedingEnPassantTrigger = pieceToMove.pos[0] + str(int(pieceToMove.pos[1]) + int((int(tile.objectName()[1]) - int(pieceToMove.pos[1])) / 2))

                #print("en passant triggered on: " + tileNeedingEnPassantTrigger)
                #print("on move number: " + str(moveNumber))

                # sets en passant active to the move number of current move
                getattr(domain, tileNeedingEnPassantTrigger).enPassantActive = moveNumber

            # checking whether it performs an en passant
            if tile.objectName()[0] != pieceToMove.pos[0] and tile.occupied == "False":
                # tile containing pawn to be taken
                tileOfPawnBeingTaken = getattr(domain, tile.objectName()[0] + str(pieceToMove.pos[1]))

                # pawn being taken
                pawnBeingTaken = getattr(domain, tileOfPawnBeingTaken.occupied)

                # hides pawn being taken
                pawnBeingTaken.setHidden(True)

                # sets that pawns tile occupation to false
                tileOfPawnBeingTaken.occupied = "False"

                # pgnCurrentMove = pieceToMove.pos[0] + "x"
                pgnCurrentMove = pgnCurrentMove + "x"

            # promotes a pawn
            if ((tile.objectName()[1] == "1" and pieceToMove.colour == "black") 
                or (tile.objectName()[1] == "8" and pieceToMove.colour == "white")):

                global pieceToPromote 
                pieceToPromote = pieceToMove

                # accesses global variable in order to input the object that must be promoted

                getattr(domain, "queenButton").setHidden(False)
                getattr(domain, "knightButton").setHidden(False)
                getattr(domain, "promotionLabel").setHidden(False)
                getattr(domain, "coverScreen").setHidden(False)




        # sets the piece's original tile position to false
        getattr(domain, str(pieceToMove.pos)).occupied = "False"

        # print("occupation of tile piece is moving to: " + tile.occupied)

        # takes piece if tile was already occupied
        if tile.occupied != "False":
            getattr(domain, tile.occupied).setHidden(True)

            pgnCurrentMove = pgnCurrentMove + "x"

            # functionality can be added to keep track of taken pieces

        if castling != True:
            pgnCurrentMove = pgnCurrentMove + tile.objectName()

        # sets position to the position of tile + 5 to give correct padding
        pieceToMove.move(int(tile.x()) + 5, int(tile.y()) + 5)

        # sets the tile's occupation to the new piece that occupies it
        tile.occupied = str(pieceToMove.objectName())

        # sets the position of the new piece to the name of the tile it resides in
        pieceToMove.pos = str(tile.objectName())

        # adds the ending position to previous move array
        previousMove.append(pieceToMove.pos)

        print("previous move: ")
        print(previousMove)

        highlightValidTiles(previousMove, domain, "Previous")

        # pawn double-move, and castling depends on whether piece has moved
        # attribute for each object changes hasMoved to True when it first moves
        if pieceToMove.moveset in ("Pawn", "Rook", "King"):
            pieceToMove.hasMoved = True

        # debugging prints
        # print("updated piece info:")
        # print("     new tile occupation: " + tile.occupied)
        # print("     new piece position: " + pieceToMove.pos)

        # when a move is made, checkForCheck must be performed on the opposite colour
        if pieceToMove.colour == "white":
            defendingColour = "black"

        else:
            defendingColour = "white"

        # fetches attackers using checkForCheck
        '''attackers = checkForCheck(defendingColour, domain)

        if len(attackers) != 0:
            kingPos = getattr(domain, defendingColour + "King").pos
            highlightValidTiles([kingPos], domain, "King")

            pgnCurrentMove = pgnCurrentMove + "+"'''

        # checks whether there is a mate
        print("Checkmate: " + str(checkForCheckMate(defendingColour, domain, attackers, moveNumber)))

        # if mate, show game over label
        pgnCurrentMove, attackers = isGameOver(defendingColour, domain, attackers, moveNumber, previousMove, pgnCurrentMove)

        print("pgn of move: " + pgnCurrentMove)

        pgn = pgn + pgnCurrentMove

        # updates the moveset within the utility widget
        domain.dashboard.pvpStage2Widget.moveset.setText(pgn)

        # returns updated move number when piece isn't double clicked
        return moveNumber + 1, attackers, previousMove, pgn

    # in the case a piece is double clicked, checkForCheck is performed on the same
    # colour as a move isn't made
    attackers = checkForCheck(pieceToMove.colour, domain)

    # highlights the king in red if it is under attack
    if len(attackers) != 0:
            kingPos = getattr(domain, pieceToMove.colour + "King").pos
            highlightValidTiles([kingPos], domain, "King")

    highlightValidTiles(previousMove, domain, "Previous")

    # when piece is double clicked, move number isn't updated as move was nullified
    return moveNumber, attackers, previousMove, pgn




# checks whether tile is in valid tile
def isTileValid(tile, validTiles):

    valid = False

    for i in validTiles:
        if i == tile:
            valid = True

    return valid




def highlightValidTiles(validTiles, domain, deHighlight):
    #print("running highlight on:")
    #print(validTiles)

    # if de highlight is true, it is the end of move and thus the stylesheet must be removed
    if deHighlight == True:
        lightStyle = ""
        darkStyle = ""

    elif deHighlight == "Previous":
        lightStyle = '''
            background-color: rgb(184, 220, 184);
            color: rgb(133, 170, 133);'''
        darkStyle = '''
            background-color: rgb(133, 170, 133);
            color: rgb(184, 220, 184);'''

    elif deHighlight == "King":
        lightStyle = '''
            background-color: rgb(220, 184, 184);
            color: rgb(170, 133, 133);'''
        darkStyle = '''
            background-color: rgb(170, 133, 133);
            color: rgb(220, 184, 184);'''

    else:
        # actual colours:
        # -> light: 184, 184, 184
        # -> dark: 135, 135, 135

        lightStyle = '''
            background-color: rgb(184, 200, 220);
            color: rgb(133, 150, 170);'''
        darkStyle = '''
            background-color: rgb(133, 150, 170);
            color: rgb(184, 200, 220);'''

    # applies the style sheet for each tile
    for i in validTiles:
        if getattr(domain, i).metaObject().className() == "lightSquare":
            getattr(domain, i).setStyleSheet(lightStyle)

        else:
            getattr(domain, i).setStyleSheet(darkStyle)

    


def promotingTo(evolution, domain, alias, pgn, attackers, previousMove, moveNumber):
    pieceToPromote.moveset = evolution
    pieceToPromote.setPixmap(QPixmap("Resources/ChessIcons/" + pieceToPromote.colour.title() + evolution + ".png"))

    getattr(domain, "queenButton").setHidden(True)
    getattr(domain, "knightButton").setHidden(True)
    getattr(domain, "promotionLabel").setHidden(True)
    getattr(domain, "coverScreen").setHidden(True)

    if pieceToPromote.colour == "white":
        colour = "black"
    
    else:
        colour = "white"

    pgn = pgn[0:-1] + "=" + alias

    pgn, throwaway = isGameOver(colour, domain, attackers, moveNumber, previousMove, pgn)

    return pgn




# returns the specificity needed for the moving piece if there is an ambiguity
def checkIfMoveIsUnique(domain, pieceToMove, movingTo, moveNumber, attackers):
    similarPieces = []
    conflictingPieces = []
    alternativePiece = []

    if pieceToMove.moveset == "King":
        return ""

    elif pieceToMove.moveset in ("Rook", "Bishop"):
        alternativePiece = pieceToMove.colour + chr(ord("H") + (ord("A") - ord(pieceToMove.objectName()[5]))) + pieceToMove.moveset

        if getattr(domain, alternativePiece).isVisible() == True:
            similarPieces.append(alternativePiece)

    elif pieceToMove.moveset in ("Knight", "Queen"):
        if pieceToMove.objectName()[6:9] == "Pawn":
            if pieceToMove.moveset == "Queen":
                alternativePiece = [pieceToMove.colour + "Queen"]

            else:
                alternativePiece = [pieceToMove.colour + "BKnight", pieceToMove.colour + "GKnight"]

        elif pieceToMove.moveset == "Knight":
                
                alternativePiece = [pieceToMove.colour + chr(ord("H") + (ord("A") - ord(pieceToMove.objectName()[5]))) + pieceToMove.moveset]

        for i in alternativePiece:
            if getattr(domain, i).isVisible() == True:
                similarPieces.append(i)

        start = ord("A")

        for i in range(0, 8):
            pawn = pieceToMove.colour + chr(start + i) + "Pawn"

            if (getattr(domain, pawn).moveset == pieceToMove.moveset 
                and getattr(domain, pawn).isVisible() == True 
                and pawn != pieceToMove.objectName()):

                similarPieces.append(pawn)

    validTiles = []

    functions = {"Pawn": checkMovePawn, "Knight": checkMoveKnight, 
                         "Queen": checkMoveQueen, "Bishop": checkMoveDiagonal, "Rook": checkMoveStraight}
    
    for i in similarPieces:
        piece = getattr(domain, i)

        if piece.moveset == "Pawn":
            validTiles = functions[getattr(domain, i).moveset](piece.colour, piece.pos, domain, attackers, piece.hasMoved, moveNumber)

        for y in validTiles:
            if y == movingTo:
                conflictingPieces.append(i)

    if len(conflictingPieces) == 0:
        return ""
    
    else:
        xClash = False
        yClash = False

        for i in conflictingPieces:
            if pieceToMove.pos[0] == getattr(domain, conflictingPieces).pos[0]:
                xClash = True

            if pieceToMove.pos[1] == getattr(domain, conflictingPieces).pos[1]:
                yClash = True

        if xClash and yClash:
            return pieceToMove.pos
        
        elif xClash:
            return pieceToMove.pos[0]
        
        elif yClash:
            return pieceToMove.pos[1]
        
        else:
            return ""
        
def isGameOver(defendingColour, domain, attackers, moveNumber, previousMove, pgn):

    attackers = checkForCheck(defendingColour, domain)

    if len(attackers) != 0:
        kingPos = getattr(domain, defendingColour + "King").pos
        highlightValidTiles([kingPos], domain, "King")

        pgn = pgn + "+"

    isCheckMate = checkForCheckMate(defendingColour, domain, attackers, moveNumber - 1)
    isStaleMate = checkForStaleMate(defendingColour, domain, attackers, moveNumber - 1)

    # if mate, show game over label
    if (isCheckMate == True or isStaleMate == True):

        if isCheckMate and pgn[len(pgn) - 1] == "+":
            pgn = pgn[0: -1] + "#"

        elif isCheckMate:
            pgn = pgn + "#"  

        domain.pgn = domain.pgn + pgn

        highlightValidTiles(previousMove, domain, True)
        
        if len(attackers) != 0:
            highlightValidTiles([getattr(domain, defendingColour + "King").pos], domain, True)

        if isCheckMate == True:
            if defendingColour == "white":
                getattr(domain, "gameOverLabel").setText(f"{domain.blackPlayer} wins!")
                goToStage3(domain.dashboard, -1)

            else:
                getattr(domain, "gameOverLabel").setText(f"{domain.whitePlayer} wins!")
                goToStage3(domain.dashboard, 1)

        else:
            getattr(domain, "gameOverLabel").setText("It's a draw!")
            goToStage3(domain.dashboard, 0)

        getattr(domain, "coverScreen").setHidden(False)
        getattr(domain, "gameOverLabel").setHidden(False)
        getattr(domain, "playAgainButton").setHidden(False)

    return pgn, attackers


#### BUGFOUND
#### BUGFOUND
#### BUGFOUND
#### BUGFOUND
#### BUGFOUND
## says cant move from blocking check even if can move to another place which also blocks check


    