# <------ SUMMARY ------>
# These functions enable the board to see whether the king is in danger 
# or whether a piece is blocking a check

'''
def isBlockingCheck(colour, domain, currentPosition):

    # returns False if the function is called upon the king piece
    if str(getattr(domain, str(currentPosition)).occupied) == (str(colour) + "King"):
        return False

    #print("checking pin on: " + currentPosition)
    # temporarily sets the current position's tile to false
    # -> allows check for check to see if moving the piece would cause a check on its own king
    temp = getattr(domain, str(currentPosition)).occupied
    #print("contents of current position: " + temp)

    getattr(domain, str(currentPosition)).occupied = "False"

    # position contains the value of the King's position for the blockableCheck function
    kingPosition = getattr(domain, (str(colour) + "King")).pos

    # only uses the first two positions within direction array as distance is only used to 
    # finds the direction between current position and king
    direction = onSameLine(currentPosition, kingPosition)

    # if onSameLine returns false, it means the two pieces do not share a line
    # thus the piece cannot block / be pinned to the king
    if direction == False:
        # resets the value of occupied back to original
        getattr(domain, str(currentPosition)).occupied = temp
        #print("reset occupation: " + getattr(domain, str(currentPosition)).occupied)

        return False
        
    # calls blockableCheck to see whether the king is in danger
    attackers = blockableChecks(kingPosition, colour, domain, direction[0], direction[1])

    # resets the value of occupied back to original
    getattr(domain, str(currentPosition)).occupied = temp
    #print("reset occupation: " + getattr(domain, str(currentPosition)).occupied)

    #print("direction from piece to king: ")
    #print(direction)

    # if there is no attackers on the king then false can be returned
    if len(attackers) == 0:
        return False
    
    else:
        if len(attackers) == 1:
            directionToAttacker = onSameLine(currentPosition, attackers[0][1])
            #print("direction from piece to attacker: ")
            #print(directionToAttacker)

            if directionToAttacker == False:
                return True
            
            elif directionToAttacker[0] * -1 == direction[0] and directionToAttacker[1] * -1 == direction[1]:
                return True
            
            return False
        blocks = []

        for i in attackers:
            directionToAttacker = onSameLine(currentPosition, attackers[i][1])

            if directionToAttacker == False:
                blocks.append(False)

            elif directionToAttacker[0] * -1 == direction[0] and directionToAttacker[1] * -1 == direction[1]:
                pass'''




# check for check gets the position of the king and returns a list of all attacking pieces
def checkForCheck(colour, domain, *args):
    # for checking valid king moves, kingpos values other than the true values must be inputted
    # therefore the position would be submitted as an extra argument
    if len(args) == 0:
        # when no extra argument is submitted, true king position is used
        position = getattr(domain, (str(colour) + "King")).pos

    else:
        position = list(args)[0]
        #print("checking king validation for: " + position)

    attackers = []
    
    #print("<------- blockable checks ------->")

    # calls the blockable check function in all compass directions
    for x in range(-1, 2):
        for y in range(-1, 2):
            if not (x == 0 and y == 0):
                attackers = attackers + blockableChecks(position, colour, domain, x, y)

    #print("attackers:")
    #print(attackers)

    #print("<------- finish blockable checks ------->")

    # adds attackers that are either pawns or knights
    attackers = attackers + nonBlockableChecks(position, colour, domain)

    return attackers





def addToAttackers(attackers, blockingPiece, validPieces, colour):
    if blockingPiece.moveset in validPieces and blockingPiece.colour != colour:
        # if so it adds it to the attackers list
        attackers.append([blockingPiece.moveset, blockingPiece.pos])
        
    return attackers




# <--------- New Function --------->

# checks all regular / blockable checks
def blockableChecks(position, colour, domain, xDirection, yDirection):
    blocked = False
    attackers = []
    currentPos = position


    # sets starting co-ordinate
    currentPos = str(chr(ord(position[0]) + xDirection)) + str(int(position[1]) + yDirection)

    # print("checking direction: " + str(xDirection) + " " + str(yDirection))

    # loops until blockable piece is found
    # or co-ordinate is out of bound
    while blocked == False and not((currentPos[0] < 'a') or (currentPos[0] > "h") or 
        (int(currentPos[1]) < 1) or (int(currentPos[1]) > 8)):

        # re-assigns position to x and y variables
        letterPos = currentPos[0]
        numPos = currentPos[1]

        # print("current position:" + currentPos)

        # checks whether the tile of corresponding coordinate is occupied
        if getattr(domain, currentPos).occupied != "False":
            blocked = True
            blockingPiece = getattr(domain, getattr(domain, currentPos).occupied)
            # print(getattr(domain, currentPos).occupied)

            # if either is true, the current move-check is for a straight line
            if xDirection == 0 or yDirection == 0:
                # checks if blocking piece has capability to take in straight line
                attackers = addToAttackers(attackers, blockingPiece, ("Rook", "Queen"), colour)
                # print(attackers)
            
            # checks diagonal
            else:
                # checks for corresponding pieces
                attackers = addToAttackers(attackers, blockingPiece, ("Bishop", "Queen"), colour)
                # print(attackers)

        currentPos = str(chr(ord(letterPos) + xDirection)) + str(int(numPos) + yDirection)

    return attackers




# <--------- New Function --------->

# checks all irregular checks (knight, pawn)
def nonBlockableChecks(position, colour, domain):
    attackers = []
    currentPos = position

    # sets up the currentPos as the first knight check position
    # check works by looping through the circle of possible knight positions
    currentPos = str(chr(ord(position[0]) + 1)) + str(int(position[1]) + 2)

    for i in range(0, 8):
        letterPos = currentPos[0]

        # ensures that if the number is two digits, both digits are shown in the numPos
        if len(currentPos) == 3:
            numPos = currentPos[1] + currentPos[2]

        else:
            numPos = currentPos[1]

        if not (int(numPos) > 8 or int(numPos) < 1 or letterPos < "a" or letterPos > "h"):
            # checks the current position for a piece within the tile
            if getattr(domain, currentPos).occupied != "False":

                # if so it gets the piece and checks whether it is of the attacking colour and is the right type of piece
                # -> if so it is added to the atackers list
                blockingPiece = getattr(domain, getattr(domain, currentPos).occupied)
                attackers = addToAttackers(attackers, blockingPiece, ("Knight"), colour)

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

    # <--- next block checks for a pawn check --->
    
    # declares the y direction of checking depending on the colour
    # -> as pawns can only move in a singular direction
    if colour == "white":
        numMovement = 1
    
    else:
        numMovement = -1
    
    # loops through two possbilites, a check to the left and right of a pawn
    for i in range(-1, 2, +2):
        currentPos = str(chr(ord(position[0]) + i)) + str(int(position[1]) + numMovement)

        if not (int(currentPos[1]) > 8 or int(currentPos[1]) < 1 or currentPos[0] < "a" or currentPos[0] > "h"):
            if getattr(domain, currentPos).occupied != "False":
                # if so it gets the piece and checks whether it is of the attacking colour and is the right type of piece
                # -> if so it is added to the atackers list
                blockingPiece = getattr(domain, getattr(domain, currentPos).occupied)
                attackers = addToAttackers(attackers, blockingPiece, ("Pawn"), colour)

    return attackers




def onSameLine(piecePosition, kingPosition):
    # checking whether they are on the same straight line
    # -> entails either both the numPos or both the letterPos are the same

    # calculates the distance between the piece and king in both x and y
    xDifference = ord(piecePosition[0]) - ord(kingPosition[0])
    # print("calculatinx xdifference: piece and king pos: " + piecePosition[0] + kingPosition[0] + " result: " +  str(ord(piecePosition[0]) - ord(kingPosition[0])))
    yDifference = int(piecePosition[1]) - int(kingPosition[1])

    if abs(xDifference) > abs(yDifference):
        distance = abs(xDifference)

    else:
        distance = abs(yDifference)

    # if either distance is 0, they are on the same line
    # if the absolute value of each is equal to eachother they are on the same line
    # -> output of this function is plugged into blockable check
    # -> therefore, ouputted direction must be eithe -1, 0, 1
    # ---> therefore, when distance isn't 0, its divided by its absolute value

    if xDifference == 0:
        return [xDifference, int((yDifference / abs(yDifference))), distance]
    
    elif yDifference == 0:
        return [int((xDifference / abs(xDifference))), yDifference, distance]
    
    elif abs(xDifference) == abs(yDifference):
        return [int((xDifference / abs(xDifference))), int((yDifference / abs(yDifference))), distance]
    
    else:
        return False




# the purpose of check against check is to compare all possible moves of a piece
# with the legitimate moves when the king is in check
def movesStoppingCheck(pieceValidTiles, kingPos, position, domain):
    tilesToBlock = []
    validTiles = []

    occupiedTile = getattr(domain, position)
    occupant = occupiedTile.occupied

    occupiedTile.occupied = "False"

    attackers = checkForCheck(getattr(domain, occupant).colour, domain)

    # if there is more than one attacker, a non-king piece cannot move to stop the check
    if len(attackers) > 1:
        #print("multiple attackers")
        occupiedTile.occupied = occupant
        return []
    
    # if there is no attackers, all valid moves are possible
    # (this is because if the piece is pinned to the king, earlier logic prevents the
    # call from getting this far)
    elif len(attackers) == 0:
        occupiedTile.occupied = occupant
        return pieceValidTiles

    # a non-king piece cannot block either of these checks and thus can only take the piece
    elif attackers[0][0] in ("Knight", "Pawn"):
        tilesToBlock = [attackers[0][1]]

    # is called when there is one attacker which is blockable
    else:
        # fetches list of all tiles which can block check
        tilesToBlock = movesBlockingCheck(attackers, kingPos)

    # print("tiles blocking check")
    # print(tilesToBlock)

    # if there is a move in both lists, it is added to validTiles
    for i in pieceValidTiles:
        for y in tilesToBlock:
            if i == y:
                validTiles.append(i)

    occupiedTile.occupied = occupant
    return validTiles




# function fetches all tiles on which a piece can be placed to block the check
def movesBlockingCheck(attackers, kingPos):
    blockingTiles = []

    # holds the direction of the piece to the king as well as the distance
    direction = onSameLine(attackers[0][1], kingPos)
    # print("direction content: ")
    # print(direction)

    # assigned to the position on the board of the attacking piece
    position = attackers[0][1]

    # loops through each tile in the line between attacker (including) and king (excluding)
    for i in range(0, direction[2]):
        #print("adding position " + position + " to blocking pieces")
        blockingTiles.append(position)

        # adds the inverse number of direction as the direction array holds the direction of piece relative to king
        # and we need king relative to piece
        position = chr(ord(position[0]) + direction[0] * -1) + str(int(position[1]) + direction[1] * -1)

    return blockingTiles




# checks whether king moves are valid when the king is in check
def movesStoppingCheckForKing(pieceValidTiles, domain, colour, kingPos):
    # sets the king's tile occupation to false to allow for checkChecking to pass through the tile
    getattr(domain, kingPos).occupied = "False"
    validTiles = []

    # for each valid move it calls the checkForCheck function
    for i in pieceValidTiles:
        # if this function returns no attackers, the move is valid
        if len(checkForCheck(colour, domain, i)) == 0:
            # print("check for check value of position " + i)
            # print(checkForCheck(colour, domain, i))
            validTiles.append(i)

    # resets the king's tile occupation to the object name of the king
    getattr(domain, kingPos).occupied = colour + "King"

    return validTiles



