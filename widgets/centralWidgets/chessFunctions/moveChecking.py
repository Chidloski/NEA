from widgets.centralWidgets.chessFunctions.checkChecking import movesStoppingCheck, movesStoppingCheckForKing, checkForCheck

# <------ SUMMARY ------>
# All of these functions are used to check whether
# moving to tiles on the board is valid
# return a list full of all tiles which are valid to move to




def checkMoveDiagonal(colour, position, domain, attackers):
    # checks whether tiles in diagonals are valid to move to

    # list contains all valid tiles for all diagonal directions
    validTiles = []

    # for each diagonal direction, the same function is run with different direction args
    # returned list is then added to the current valid list
    leftDownValid = moveValidityLong(colour, position, domain, -1, -1)
    validTiles = validTiles + leftDownValid

    rightDownValid = moveValidityLong(colour, position, domain, 1, -1)
    validTiles = validTiles + rightDownValid

    leftUpValid = moveValidityLong(colour, position, domain, -1, 1)
    validTiles = validTiles + leftUpValid

    rightUpValid = moveValidityLong(colour, position, domain, 1, 1)
    validTiles = validTiles + rightUpValid

    kingPos = getattr(domain, colour + "King").pos
    validTiles = movesStoppingCheck(validTiles, attackers, kingPos)

    return validTiles




def checkMoveStraight(colour, position, domain, attackers):
    # checks whether tiles in diagonals are valid to move to

    # list contains all valid tiles for all diagonal directions
    validTiles = []

    # for each diagonal direction, the same function is run with different direction args
    # returned list is then added to the current valid list
    leftValid = moveValidityLong(colour, position, domain, -1, 0)
    validTiles = validTiles + leftValid

    rightValid = moveValidityLong(colour, position, domain, 1, 0)
    validTiles = validTiles + rightValid

    upValid = moveValidityLong(colour, position, domain, 0, 1)
    validTiles = validTiles + upValid

    downValid = moveValidityLong(colour, position, domain, 0, -1)
    validTiles = validTiles + downValid

    kingPos = getattr(domain, colour + "King").pos
    validTiles = movesStoppingCheck(validTiles, attackers, kingPos)

    return validTiles




def checkMoveQueen(colour, position, domain, attackers):
    validTiles = []

    validTiles = validTiles + checkMoveDiagonal(colour, position, domain, attackers)
    validTiles = validTiles + checkMoveStraight(colour, position, domain, attackers)

    return validTiles




# moveValidity function passes in the colour of the moving piece, its current position,
# the object class, and the direction in which it should move

# it then splits the current position e.g a1 into two variables a, 1 which are then manipulated as needed
# then it checks whether the tile corresponding to the new coordinate is open
# if not it checks whether the piece on the tile is of the same colour or different
def moveValidityLong(colour, position, domain, letterDirection, numDirection):
    validTiles = []

    currentPos = str(position)

    blocked = False

    # loops continuously until an occupated tile is found
    while blocked == False:
        letterPos = currentPos[0]
        numPos = currentPos[1]

        currentPos = str(chr(ord(letterPos) + letterDirection)) + str(int(numPos) + numDirection)
        #print(currentPos)

        # 4 statements check whether the co-ordinate is out of bounds
        if ((currentPos[0] < 'a') or
            (currentPos[0] > "h") or 
            (int(currentPos[1]) < 1) or
            (int(currentPos[1]) > 8)):

            blocked = True

        # checks whether the tile of corresponding coordinate is occupied
        elif getattr(domain, currentPos).occupied == "False":
            # if clear, tile is added to valid list
            validTiles.append(str(currentPos))
        
        else:
            # if not, checks whether it is of the same colour
            # if not this tile becomes the last valid tile
            if getattr(domain, currentPos).occupied[0] == colour[0]:
                blocked = True
            
            else:
                validTiles.append(str(currentPos))
                blocked = True

    return validTiles




def checkMoveKnight(colour, position, domain, attackers):
    validTiles = []

    currentPos = str(position)

    letterPos = currentPos[0]
    numPos = currentPos[1]

    currentPos = str(chr(ord(letterPos) + 1)) + str(int(numPos) + 2)

    for i in range(0, 8):
        letterPos = currentPos[0]

        # ensures that if the number is two digits, both digits are shown in the numPos
        if len(currentPos) == 3:
            numPos = currentPos[1] + currentPos[2]

        else:
            numPos = currentPos[1]

        validTiles = validTiles + checkTile(colour, currentPos, domain)

        # moves currentPos in a grid pattern with movement depending on i value
        if (i - 1) % 2 == 0:
            # when one more than a multiple of 2, it must two tiles in one direction
            if (i - 1) % 4 == 0:
                numPos = str(int(numPos) + (i - 3))

            else:
                letterPos = str(chr(ord(letterPos) + (i - 5)))

        else:
            # when even, it must move diagonally
            if i % 4 == 0:
                # when it is a multiple of 4, diagonal is one positive, one negative
                # due to the size of i, i // -2 allows the result to be positive or negative
                letterPos = str(chr(int(ord(letterPos) + (i // - 2) + 1)))
                numPos = str(int(numPos) + (i // 2) - 1)

            else:
                # diagonal movement either positive positive, or negative negative
                letterPos = str(chr(int(ord(letterPos) + ((i - 2) // 2) - 1)))
                numPos = str(int(numPos) + ((i - 2) // 2) - 1)

        currentPos = letterPos + numPos

    kingPos = getattr(domain, colour + "King").pos
    validTiles = movesStoppingCheck(validTiles, attackers, kingPos)

    return validTiles




def checkMoveKing(colour, position, domain, attackers):
    validTiles = []

    currentPos = str(position)

    letterPos = currentPos[0]
    numPos = currentPos[1]

    currentPos = str(letterPos) + str(int(numPos) + 1)

    for i in range(0, 8):
        letterPos = currentPos[0]
        numPos = currentPos[1]

        # checks validity of tile
        validTiles = validTiles + checkTile(colour, currentPos, domain)

        # moves currentPos differently depending on value of i
        if i > 0 and i < 3:
            numPos = str(int(numPos) - 1)
        
        elif i > 2 and i < 5:
            letterPos = chr(int(ord(letterPos) - 1))

        elif i > 4 and i < 7:
            numPos = str(int(numPos) + 1)

        else:
            letterPos = chr(int(ord(letterPos) + 1))

        currentPos = letterPos + numPos

    # you cannot castle out of check so this must be checked
    if len(attackers) == 0:
        # if one of the pieces has moved, castling is not possible
        if getattr(domain, colour + "King").hasMoved == False:
            if getattr(domain, colour + "ARook").hasMoved == False:
                # print("running castling on ARook")
                # calling castling
                validTiles = validTiles + castling(getattr(domain, colour + "King"), 
                                                   getattr(domain, colour + "ARook"), domain, colour)

            if getattr(domain, colour + "HRook").hasMoved == False:
                # print("running castling on HRook")
                # calling castling
                validTiles = validTiles + castling(getattr(domain, colour + "King"), 
                                                   getattr(domain, colour + "HRook"), domain, colour)
    
    #print("all possible king moves:")
    #print(validTiles)

    validTiles = movesStoppingCheckForKing(validTiles, domain, colour, position)

    #print("valid king tiles:")
    #print(validTiles)

    return validTiles




def castling(king, rook, domain, colour):
    # declares attackers as a list
    attackers = []

    # calculates the distance between the king and rook
    difference = ord(rook.pos[0]) - ord(king.pos[0])

    # print("difference calculation: " + str(ord(rook.pos[0])) + " - " + str(ord(king.pos[0])))
    # print("castling difference" + str(difference))
    # print("direction calclulation: " + str(difference) + "/" + str(abs(difference)))

    # calculates the direction of the castle
    direction = int(difference / abs(difference))
    # print("castling direction:" + str(direction))

    # loops between all positions between the king and castle
    for i in range(1, abs(difference)):
        # if direction is negative, so is i
        i = i * direction

        currentPos = chr(ord(king.pos[0]) + i) + king.pos[1]
        # print("checkin castle block at " + currentPos)

        # if there is a piece in position between, castle is not possible
        if getattr(domain, currentPos).occupied != "False":
            # print("piece blocking castling")
            return []
        
    # checks all position the king moves through within the castle
    # -> checks whether if any of the moving through tiles causes a check on the king
    # --> if so, the castle is not possible
    for i in range(2, abs(difference)):
        kingMovesThrough = chr(ord(king.pos[0]) + direction) + king.pos[1]

        getattr(domain, king.pos).occupied = "False"
        getattr(domain, kingMovesThrough).occupied = colour + "King"

        attackers = attackers + checkForCheck(colour, domain)

        getattr(domain, king.pos).occupied = colour + "King"
        getattr(domain, kingMovesThrough).occupied = "False"

    # if previous for loop returns any attackers, it returns no valid tiles
    if len(attackers) == 0:
        return [chr(ord(king.pos[0]) + (2 * direction)) + king.pos[1]]
    
    else:
        return []




# checks the validity of a pawn move
# -> pawn move caveats include:
#       - able to move two squares on first fo
#       - move diagonally if it can take a piece
#       - move diagonally due to en passant
#       - only ever moves towards opponent's home row
def checkMovePawn(colour, position, domain, attackers, *args):
    hasMoved, currentMove = args

    # checks the colour to decide the direction of movement
    if colour == "white":
        direction = 1

    else:
        direction = -1

    validTiles = []

    currentPos = str(position)

    letterPos = currentPos[0]
    numPos = currentPos[1]

    currentPos = str(chr(ord(letterPos) - 1)) + str(int(numPos) + direction)

    # for loop checks both diagonal directions
    for i in range(0, 2):
        #print("current move number: " + str(currentMove))
        
        if ((currentPos[0] < 'a') or
            (currentPos[0] > "h") or 
            (int(currentPos[1]) < 1) or
            (int(currentPos[1]) > 8)):

            pass

        # checks whether the tile of corresponding coordinate is occupied by a rival piece
        # or if the tile has en passant activated the previous move
        elif (getattr(domain, currentPos).enPassantActive + 1 == currentMove 
              or (getattr(domain, currentPos).occupied[0] != colour[0] 
                  and getattr(domain, currentPos).occupied != "False")):
            validTiles.append(str(currentPos))

        # switches to other diagonal direction
        currentPos = str(chr(ord(letterPos) + 1)) + str(int(numPos) + direction)

    # switches position to directly in front
    currentPos = str(chr(ord(letterPos))) + str(int(numPos) + direction)

    # checks whether it is out of bounds
    if ((currentPos[0] < 'a') or
            (currentPos[0] > "h") or 
            (int(currentPos[1]) < 1) or
            (int(currentPos[1]) > 8)):

            pass
    
    # checks whether positions in front are not occupied
    elif getattr(domain, currentPos).occupied == "False":
        validTiles.append(str(currentPos))

        currentPos = str(chr(ord(letterPos))) + str(int(numPos) + (direction * 2))

        # checks position two in front if never moved before
        if hasMoved == False and getattr(domain, currentPos).occupied == "False":
            validTiles.append(str(currentPos))


    kingPos = getattr(domain, colour + "King").pos
    validTiles = movesStoppingCheck(validTiles, attackers, kingPos)

    return validTiles




# holds the generic function for checking moves for both King, and Knight
# checking long, and pawn check both have caveats
# -> blocked by piece (long), en passant (pawn)
def checkTile(colour, position, domain):
    validTiles = []

    # ensures that if the number is two digits, both digits are shown in the numPos
    if len(position) == 3:
        numPos = position[1] + position[2]
    
    else:
        numPos = position[1]

    # checks whether position is out of bounds
    if ((position[0] < 'a') or
            (position[0] > 'h') or 
            (int(numPos) < 1) or
            (int(numPos) > 8)):

            pass

    # checks whether the tile of corresponding coordinate is occupied
    elif getattr(domain, position).occupied == "False":
        # if clear, tile is added to valid list
        validTiles.append(str(position))
        
    else:
        # if not, checks whether it is of the same colour
        # if not this tile becomes the last valid tile
        if getattr(domain, position).occupied[0] == colour[0]:
            pass
        
        else:
            validTiles.append(str(position))

    #print(position)
    #print(validTiles)
    return validTiles

