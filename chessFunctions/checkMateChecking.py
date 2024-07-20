from chessFunctions.moveChecking import checkMoveKing, checkMovePawn, checkMoveKnight, checkMoveDiagonal, checkMoveStraight, checkMoveQueen
from chessFunctions.checkChecking import movesBlockingCheck, isBlockingCheck

# check mate function goes through all different cases for the attackers list and checks whether it will result in a checkmate
# colours in this case represents the defending team's colour
def checkForCheckMate(colour, domain, attackers, moveNumber):
    #print("<------- checkmate function ------->")
    kingPos = getattr(domain, colour + "King").pos

    #print("attackers: ")
    #print(attackers)

    # if there are no attackers, checkamte is impossible
    if len(attackers) == 0:
        return False
    
    # multiple attackers
    elif len(attackers) > 1:
        # the only thing stopping a mate would be a valid king move to escape
        if len(checkMoveKing(colour, kingPos, domain, attackers)) != 0:
            return False
        
        else:
            return True
        
    else:
        # if king has a valid move -> checkmate = false
        if len(checkMoveKing(colour, kingPos, domain, attackers)) != 0:
            return False
        
        else:
            # if the attacker cannot be blocked, only valid block move is the tile of the attacker
            if attackers[0][0] in ("Knight", "Pawn"):
                movesAvoidingCheck = [attackers[0][1]]
            
            else:
                # calls function to return a list containing all tiles in between king and attacker
                movesAvoidingCheck = movesBlockingCheck(attackers, kingPos)

            validTiles = allPieceMoves(colour, domain, attackers, moveNumber)

            #print("moves avoiding check:")
            #print(movesAvoidingCheck)

            # if any piece has a move which is also in movesAvoidingCheck, checkmate can be avoided
            for i in validTiles:
                for y in movesAvoidingCheck:
                    if i == y:
                        return False
                    
            return True
        
def checkForStaleMate(colour, domain, attackers, moveNumber):
    kingPos = getattr(domain, colour + "King").pos

    if len(attackers) != 0:
        return False
    
    elif len(checkMoveKing(colour, kingPos, domain, attackers)) != 0:
        return False
    
    else:
        validTiles = allPieceMoves(colour, domain, attackers, moveNumber)
        #print("ALL PIECE MOVES:")
        #print(validTiles)

        if len(validTiles) == 0:
            return True
        
        else:
            return False




def allPieceMoves(colour, domain, attackers, moveNumber):
    functions = {"Pawn": checkMovePawn, "Knight": checkMoveKnight, 
                         "Queen": checkMoveQueen, "Bishop": checkMoveDiagonal, "Rook": checkMoveStraight}
            
    pieces = ["ARook", "BKnight", "CBishop", "Queen", "FBishop", "GKnight", "HRook", "APawn",
                "BPawn", "CPawn", "DPawn", "EPawn", "FPawn", "GPawn", "HPawn"]
    
    validTiles = []

    # loops through all pieces and adds their moves to a list
    for i in pieces:
        # finding the object corresponding to the piece name
        piece = getattr(domain, colour + i)

        # debugging prints
        # print("current piece: " + (colour + i))
        # print("current piece position: " + piece.pos)
        # print(piece.isVisible())

        # if the piece has not been taken
        if piece.isVisible():
            # if the piece is not pinned
            if not isBlockingCheck(colour, domain, piece.pos):
                # extra args 
                if piece.moveset == "Pawn":
                    validTiles = validTiles + functions[piece.moveset](colour, piece.pos, domain, attackers, piece.hasMoved, moveNumber)

                else:
                    validTiles = validTiles + functions[piece.moveset](colour, piece.pos, domain, attackers)

    
    return validTiles




def remainingPieces(domain):
    pieces = ["ARook", "BKnight", "CBishop", "Queen", "FBishop", "GKnight", "HRook", "APawn",
                "BPawn", "CPawn", "DPawn", "EPawn", "FPawn", "GPawn", "HPawn"]
    
    colour = "white"

    piecesLeft = []

    for i in range(0, 2):
        for i in pieces:
            piece = getattr(domain, colour + i)

            if piece.isVisible() == True:
                piecesLeft = piecesLeft + piece

        colour = "black"

    return remainingPieces