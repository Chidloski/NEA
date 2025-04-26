from widgets.centralWidgets.chessFunctions.moveChecking import checkMoveKing, checkMovePawn, checkMoveKnight, checkMoveDiagonal, checkMoveStraight, checkMoveQueen
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QLabel, QApplication
import time
import re


# pgn standards are as follows
# first portion: piece mnemonic
# -> a file/rank can be added to this if two pieces can make the same move
# second portion: x if a piece has been taken
# tile target
# mnemonic denoting check/mate
def parsePGN(pgn):
    moveset = []
    
    # define typical pattern for pgn
    moveNumberPattern = r'^\d{1,3}\.$'

    # split move list into pgn
    newPgn = [item for item in pgn if not re.match(moveNumberPattern, item)]

    solutionPattern = r'^[a-z]\d[a-z]\d$'
    otherSolutionPattern = r'^[a-z]\d[a-z]\d[a-z]$'

    for index, move in enumerate(newPgn):

        promotionInfo = ""

        # find move colour
        if int(index / 2) == index / 2:
            colour = "white"

        else:
            colour = "black"

        # remove any move numbers if move number is connected to move
        if len(move) > 2 and move[1] == ".":
            move = move[2:]

        elif len(move) > 3 and move[2] == ".":
            move = move[3:]

        elif len(move) > 4 and move[3] == ".":
            move = move[4:]


        # solution patterns may follow non-pgn standards such as e4e5 rather than any piece info
        if re.match(otherSolutionPattern, move):
            endPosition = move[-3:-1]
            piece = move[:2]
            middleInfo = ""
            promotionInfo = str(move[-1]).upper()

        elif re.match(solutionPattern, move):
            endPosition = move[-2:]
            piece = move[:2]
            middleInfo = ""
            promotionInfo = ""

        # check for castling king side
        elif move == "O-O":
            if colour == "white":
                endPosition = "g1"

            else:
                endPosition = "g8"

            piece = "K"
            middleInfo = ""

        # check for castling queen side
        elif move == "O-O-O":
            if colour == "white":
                endPosition = "c1"

            else:
                endPosition = "c8"

            piece = "K"
            middleInfo = ""
        
        else:
            
            # check for promotion
            if move[-2:] in ("=Q", "=N"):
                endPosition = move[-4:-2]

                promotionInfo = move[-1]

                move = move[:-2]

            # check for promotion and check or checkmate
            elif move[-3:] in ("=Q+", "=N+", "=Q#", "=N#"):
                endPosition = move[-5:-3]

                promotionInfo = move[-2]

                move = move[:-3]

            # check for check or checkmate
            elif move[-1] in ("+", "#"):
                endPosition = move[-3:-1]

                move = move[:-1]

            else:
                endPosition = move[-2:]

            if move[0] == move[0].upper():
                piece = move[0]
                middleInfo = move[1: -2]

            # if there is no piece in the pgn, it relates to a pawn
            else:
                piece = "P"
                middleInfo = move[:-2]

            if len(middleInfo) != 0 and middleInfo[-1] == "x":
                middleInfo = middleInfo[:-1]

        moveNumberPattern = r'^\d{1,3}\.$'

        # append to moveset unless the move relates to end of game message
        if not move in ("1-0", "0-1", "1/2-1/2") and not re.match(moveNumberPattern, move):

            moveset.append([colour, piece, middleInfo, endPosition, promotionInfo])

    return moveset
        


# this function focusses on getting the correct piece from the information gathered in parsepGN
def getPiece(domain, colour, pieceType, piecePosition, endPosition):
    tileFormat = r'^[a-z]\d$'

    # solutions which do not follow pgn will pass through a tile as the piece type
    if re.match(tileFormat, pieceType):
        return getattr(domain, pieceType).occupied

    pieceAcronym = {"P": "Pawn", "R": "Rook", "N": "Knight", "B": "Bishop", "Q": "Queen", "K": "King"}

    piece = pieceAcronym[pieceType]

    possiblePieces = []

    # part of the function loops through to find all the possible pieces that could relate to the piece acronym
    # -> for knights and queens, pawns must also be checked just in case they have been promoted
    if piece == "Pawn":
        for i in range(65, 73):
            pieceToCheck = getattr(domain, colour + chr(i) + "Pawn")

            if pieceToCheck.moveset == "Pawn" and pieceToCheck.isVisible() == True and abs(ord(pieceToCheck.pos[0]) - ord(endPosition[0])) <= 1:
                possiblePieces.append(colour + chr(i) + "Pawn")

    elif piece in ("Queen", "Knight"):
        if piece == "Knight":
            if getattr(domain, colour + "BKnight").isVisible():
                possiblePieces.append(colour + "BKnight")

            if getattr(domain, colour + "GKnight").isVisible():
                possiblePieces.append(colour + "GKnight")

        else:
            if getattr(domain, colour + "Queen").isVisible():
                possiblePieces.append(colour + "Queen")

        for i in range(65, 73):
            pieceToCheck = getattr(domain, colour + chr(i) + "Pawn")

            if pieceToCheck.moveset == piece and pieceToCheck.isVisible() == True:
                possiblePieces.append(colour + chr(i) + "Pawn")

    elif piece == "Bishop":
        if getattr(domain, colour + "CBishop").isVisible():
            possiblePieces.append(colour + "CBishop")

        if getattr(domain, colour + "FBishop").isVisible():
            possiblePieces.append(colour + "FBishop")

    elif piece == "Rook":
        if getattr(domain, colour + "ARook").isVisible():
            possiblePieces.append(colour + "ARook")

        if getattr(domain, colour + "HRook").isVisible():
            possiblePieces.append(colour + "HRook")

    else:
        possiblePieces.append(colour + "King")

    refinedPossiblePieces = []

    # refine the possible pieces for whether a disambiguation has been passed through in piecePosition
    for possiblePiece in possiblePieces:
        pieceObject = getattr(domain, possiblePiece)

        if len(piecePosition) == 0 or piecePosition in (pieceObject.pos, pieceObject.pos[0], pieceObject.pos[1]):
            refinedPossiblePieces.append(possiblePiece)

    functions = {"Pawn": checkMovePawn, "Knight": checkMoveKnight, "King": checkMoveKing,
                    "Queen": checkMoveQueen, "Bishop": checkMoveDiagonal, "Rook": checkMoveStraight}

    # check whether each piece in the refined set is able to make the move to the target position
    # -> by this point, only one piece can and it is thus returned
    for refinedPiece in refinedPossiblePieces:
        refinedPieceObject = getattr(domain, refinedPiece)

        if refinedPieceObject.moveset == "Pawn":
            validTiles = functions["Pawn"](colour, refinedPieceObject.pos, domain, domain.attackers, refinedPieceObject.hasMoved, domain.moveNumber)

        else:
            validTiles = functions[refinedPieceObject.moveset](colour, refinedPieceObject.pos, domain, domain.attackers)

        for position in validTiles:
            if position == endPosition:
                return refinedPiece



# simulates the clicks needed to move a piece from the pgn
def makeMove(domain, piece, target, promotionInfo):
    print(f"piece: {piece}")
    print(f"target: {target}")

    pieceObject = getattr(domain, piece)
    targetObject = getattr(domain, target)

    piecePressEvent = QMouseEvent(QMouseEvent.MouseButtonPress, pieceObject.rect().center(), Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
    pieceObject.mousePressEvent(piecePressEvent)

    pieceReleaseEvent = QMouseEvent(QMouseEvent.MouseButtonRelease, pieceObject.rect().center(), Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
    pieceObject.mouseReleaseEvent(pieceReleaseEvent)

    targetPressEvent = QMouseEvent(QMouseEvent.MouseButtonPress, targetObject.rect().center(), Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
    targetObject.mousePressEvent(targetPressEvent)

    targetReleaseEvent = QMouseEvent(QMouseEvent.MouseButtonRelease, targetObject.rect().center(), Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
    targetObject.mouseReleaseEvent(targetReleaseEvent)

    # necessary for if a pawn needs to be promoted
    if pieceObject.moveset == "Pawn" and ((pieceObject.colour == "white" and target[1] == "8") or (pieceObject.colour == "black" and target[1] == "1")):
        if promotionInfo == "N":
            buttonObject = getattr(domain, "knightButton")

        else:
            buttonObject = getattr(domain, "queenButton")

        buttonPressEvent = QMouseEvent(QMouseEvent.MouseButtonPress, buttonObject.rect().center(), Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
        buttonObject.mousePressEvent(buttonPressEvent)

        buttonReleaseEvent = QMouseEvent(QMouseEvent.MouseButtonRelease, buttonObject.rect().center(), Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
        buttonObject.mouseReleaseEvent(buttonReleaseEvent)



