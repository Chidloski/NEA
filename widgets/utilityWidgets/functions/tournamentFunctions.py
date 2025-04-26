from PyQt5 import QtCore, QtGui, QtWidgets
from playerDB.passwordFunctions import passwordHashing, verifyPassword
from playerDB.jsonFunctions import *
from widgets.utilityWidgets.functions.playFunctions import createMatch, ratingChange
import random
from datetime import datetime

# handles the loggging in of a secondary user for pvp
def tournamentSecondaryLogIn(widget, index):
    # print(widget.opponentUser)

    loginSuccess = False

    # if no-one is already logged in
    if widget.logInButton.text() == "Log In":

        username = widget.usernameInput.text()
        password = widget.passwordInput.text()

        if widget.usernameInput.isVisible():
            # ensures both inputs are filled
            if len(username) == 0 or len(password) == 0:
                widget.errorLabel.setText("Fields must be filled")
                widget.errorLabel.setHidden(False)

            else:
                # gets data
                data = getData("users", username = username)
                
                # if no record is found
                if len(data) == 0:
                    widget.errorLabel.setText("Incorrect username/password")
                    widget.errorLabel.setHidden(False)

                else:
                    clash = False

                    for i in widget.userDetails:
                        if data[0]["id"] == i[0]:
                            clash = True

                    if clash == True:
                        widget.errorLabel.setText("Players must be unique")
                        widget.errorLabel.setHidden(False)

                    else:

                        # fetches hashed password
                        id = data[0]["id"]

                        query = {"id": id}

                        passwordData = getData("passwords", **query)
                        hashedPassword = passwordData[0]["hash"]

                        # if password doesn't match
                        if not verifyPassword(hashedPassword, password):
                            widget.errorLabel.setText("Incorrect username/password")
                            widget.errorLabel.setHidden(False)

                        # populates all necessary elements with new logged in user
                        else:
                            widget.userDetails[index][0] = id
                            widget.userDetails[index][1] = data[0]["username"]
                            widget.userDetails[index][2] = data[0]["rating"]

                            widget.usernameInput.setHidden(True)
                            widget.passwordInput.setHidden(True)

                            widget.userTypeLabel.setText("User:")

                            widget.logInButton.setText("Log Out")

                            widget.errorLabel.setHidden(True)

                            loginSuccess = True

        else: # handles when logging in a guest
            guestName = widget.guestNameInput.text()

            # dont allow login if name is not filled
            if len(guestName) == 0:
                widget.errorLabel.setText("Name must be filled")
                widget.errorLabel.setHidden(False)

            else:
                clash = False

                # check if name is already being used
                for i in widget.userDetails:
                    if guestName == i[1]:
                        clash = True

                if clash == True:
                    widget.errorLabel.setText("Name must be unique")
                    widget.errorLabel.setHidden(False)

                # add guest to user details
                else:
                    widget.userDetails[index][0] = "guest"
                    widget.userDetails[index][1] = guestName
                    widget.userDetails[index][2] = 800

                    widget.guestNameInput.setHidden(True)
                    widget.userTypeLabel.setText("Guest:")

                    widget.logInButton.setText("Log Out")

                    widget.errorLabel.setHidden(True)

                    loginSuccess = True
 
    else:
        # handles when secondary user logs out
        widget.errorLabel.setHidden(True)
        widget.userTypeLabel.setHidden(True)
        widget.userLabel.setHidden(True)

        widget.secondaryUserRadioButton.setHidden(False)
        widget.guestRadioButton.setHidden(False)

        widget.userElements[index][1].setText(f"Player {index + 1}")
        widget.userValues[index][1] = False
        widget.userDetails[index] = [-1, "", -1]

        widget.secondaryUserRadioButton.setChecked(True)
        widget.usernameInput.setHidden(False)
        widget.passwordInput.setHidden(False)

        widget.logInButton.setText("Log In")

    # if user logged in succesfully populate the corresponding label
    if loginSuccess == True:
        widget.userTypeLabel.setHidden(False)
        widget.userLabel.setHidden(False)

        widget.userLabel.setText(widget.userDetails[index][1])

        widget.secondaryUserRadioButton.setHidden(True)
        widget.guestRadioButton.setHidden(True)

        widget.userElements[index][1].setText(widget.userDetails[index][1])
        widget.userValues[index][1] = True



# populate tournament stage 2
def goToTournamentStage2(dashboard, widget, capacity):
    dashboard.tournamentStage2Widget.resetUi()

    valid = False

    # ensure capacity is a digit
    if capacity.isdigit():
        capacity = int(capacity)

        if widget.tournamentTypeGroup.checkedButton().objectName() == "knockoutRadioButton":
            if capacity <= 8 and capacity > 1: # knockout must be less than 9 people
                dashboard.tournamentStage2Widget.titleLabel.setText("Knockout")

                dashboard.tournamentStage2Widget.tournamentType = "Knockout"

                valid = True

            else:
                widget.tournamentErrorLabel.setHidden(False)
                widget.tournamentErrorLabel.setText("Knockout capacity must be 8 or smaller")
        
        else:
            if capacity > 7 and capacity > 1:
                widget.tournamentErrorLabel.setHidden(False)
                widget.tournamentErrorLabel.setText("A round robin must have 6 or less people")

            else:
                dashboard.tournamentStage2Widget.titleLabel.setText("Round Robin")

                dashboard.tournamentStage2Widget.tournamentType = "Round Robin"

                valid = True

    else:
        widget.tournamentErrorLabel.setHidden(False)
        widget.tournamentErrorLabel.setText("Capacity must be an integer")

    # if all checks are passed populate the widget
    if valid == True:
        dashboard.tournamentStage2Widget.capacity = capacity
        dashboard.tournamentStage2Widget.setActivePlayers(capacity)
        widget.tournamentErrorLabel.setHidden(True)

        dashboard.tournamentChessBoard.resetUi()

        dashboard.pvpStackedWidget.setCurrentIndex(3)
        dashboard.centralStackedWidget.setCurrentIndex(3)



# quit out of tournament so reset all widgets
def goToStage1FromTournaments(dashboard):
    dashboard.playWidget.resetUi(dashboard.baseWindow.userId)
    dashboard.tournamentStage2Widget.resetUi()
    dashboard.tournamentStage3Widget.resetUi()
    dashboard.tournamentStage4Widget.resetUi()
    dashboard.tournamentChessBoard.resetUi()
    dashboard.pvpStackedWidget.setCurrentIndex(0)
    dashboard.centralStackedWidget.setCurrentIndex(3)


# populate tournament stage 3
def goToTournamentStage3(dashboard, type, userDetails, capacity):

    inputtedCapacity = 0

    # if there is a valid record in user details add one to the capacity
    for i in userDetails:
        if i[0] != -1:
            inputtedCapacity += 1

    # if all players are logged in
    if inputtedCapacity == capacity:
        dashboard.tournamentStage3Widget.resetUi()

        dashboard.tournamentStage3Widget.typeLabel.setText(type)

        dashboard.tournamentStage3Widget.tournamentType = type
        dashboard.tournamentStage3Widget.userDetails = userDetails

        users = []
        userIds = []

        # append necessary info from userDetails
        for i in userDetails:
            if i[0] != -1:
                users.append(i[1])
                userIds.append(i[0])

        # create the corresponding bracket and create the correct scrollable widget
        if type == "Knockout":
            print(f"users to put in the bracket: {users}")
            bracket = createBracket(users)
            print(f"final bracket: {bracket}")

            dashboard.tournamentStage3Widget.knockoutDetails = bracket

            dashboard.tournamentStage3Widget.scrollableMatplotlibWidget.drawTournamentBracket(bracket)

            match = nextMatch("Knockout", bracket, 0)

        # create the corresponding league table
        elif type == "Round Robin":
            print(f"users to put in the table: {users}")
            matches = createRobin(users)
            table = createRobinTable(userDetails)

            dashboard.tournamentStage3Widget.roundRobinMatches = matches
            dashboard.tournamentStage3Widget.roundRobinDetails = table

            dashboard.tournamentStage3Widget.scrollableMatplotlibWidget.drawRoundRobin(table)

            match = nextMatch("Robin", matches, 0)

        dashboard.tournamentStage3Widget.matchIndex = 0
        dashboard.tournamentStage3Widget.currentMatch = match

        dashboard.tournamentStage3Widget.tournamentId = makeTournamentRecord(type, capacity)

        # add all user ids to competitors.json
        for i in userIds:
            makeCompetitorsRecord(i, dashboard.tournamentStage3Widget.tournamentId)

        # create a populate function which takes the match array and populates all necessary elements of stage 3
        dashboard.tournamentStage3Widget.populateNextMatch(match, userDetails)

        dashboard.pvpStackedWidget.setCurrentIndex(4)
    
    else:
        dashboard.tournamentStage2Widget.errorLabel.setText("Please log in all players")
        dashboard.tournamentStage2Widget.errorLabel.setHidden(False)

        

# function to dynamically create all matches for a bracket based on the users inputted
def createBracket(users):
    start = 1
    size = 1 # contains the number of rounds of the bracket
    found = False

    random.shuffle(users)

    # gets the number of tiers for the bracket
    while found == False:
        if len(users) > start:
            size += 1

        else:
            found = True

        start = start * 2

    bracket = {}

    # pads the bracket with the necessary matches
    for i in range(1, size + 1):
        bracket[i] = []

        if i == size:
            bracket[i].append(["Winner"])

        else:
            for y in range(0, 2**(size - i - 1)):
                bracket[i].append(["", ""])

    usersToAdd = []

    # the first half of the bracket can always be populated otherwise a bracket of one less tiers would be made
    # add the users corresponding to the size of half of the bracket to usersToAdd
    for i in range(0, 2**(size - 2)):
        usersToAdd.append(users.pop(0))

    # add users to the correct matches
    for i in range(0, len(usersToAdd) // 2):
        bracket[1][i] = [usersToAdd[i * 2], usersToAdd[(i * 2) + 1]]

    remainingChanges = int(len(usersToAdd) / 2)
    index = 2

    # cascade up the list padding with winners
    while remainingChanges >= 0.5:

        for i in range(0, int(remainingChanges)):
            bracket[index][(i - (i % 2)) // 2][i % 2] = f'W{i + 1}'

        if remainingChanges == 0.5:
            bracket[index][0][0] = 'W1'

        index += 1
        remainingChanges = remainingChanges / 2

    editingRound = 1
    fractionLeft = 0.5 # half of the bracket left to add
    sectorsFilled = 0
    
    # whilst there are still unadded users
    while len(users) > 0:
        # if amount of unadded users is a power of 2 equal to the remaining portion
        if len(users) == 2**(size - editingRound - 1 - sectorsFilled):
            usersToAdd = []

            # add all remaining users to usersToAdd
            for i in range(0, len(users)):
                usersToAdd.append(users.pop(0))

            # start at the correct index
            # left-hand half of the list has already been created so must index half way through
            index = int(2**(size - editingRound) - (2**(size - editingRound) * fractionLeft))

            # add to first tier
            for i in usersToAdd:
                bracket[editingRound][index // 2][index % 2] = i

                index += 1

            remainingChanges = len(usersToAdd) // 2
            remainingChangesRound = editingRound + 1

            startIndex = int(2**(size - editingRound) - (2**(size - editingRound) * fractionLeft)) // 2

            # cascade up the tiers padding with winners
            while remainingChanges >= 0.5:

                for i in range(startIndex, startIndex + int(remainingChanges)):
                    bracket[remainingChangesRound][((i - (i % 2)) // 2)][i % 2] = f'W{i + 1}'

                if remainingChanges == 0.5:
                    if remainingChangesRound != size:
                        bracket[remainingChangesRound][startIndex // 2][startIndex % 2] = f'W{startIndex + 1}'

                remainingChanges = remainingChanges / 2
                remainingChangesRound += 1
                startIndex = startIndex // 2
        

        # if there are more users than a power of 2, users must be added through multiple tiers
        elif len(users) > 2**(size - editingRound - 2):

            # this portion populates a left over part of the bracket if there are enough
            # remaining users to do so
            usersToAdd = []

            # add the necessary amount of users
            for i in range(0, int(2**(size - editingRound - 2))):
                usersToAdd.append(users.pop(0))

            # if amount is decimal add a singular user
            if 2**(size - editingRound - 2) < 1:
                usersToAdd.append(users.pop(0))

            # find the correct index, explained elsewhere
            index = int(2**(size - editingRound) - (2**(size - editingRound) * fractionLeft))

            # add users to correct matches
            for i in usersToAdd:
                bracket[editingRound][index // 2][index % 2] = i

                index += 1
            
            remainingChanges = int(len(usersToAdd) // 2)

            remainingChangesRound = editingRound + 1

            startIndex = int(2**(size - editingRound) - (2**(size - editingRound) * fractionLeft)) // 2

            # cascade up tiers with winners
            while remainingChanges >= 0.5:
                # find the first index to change
                roundCapacity = 2**(size - remainingChangesRound)

                for i in range(startIndex, startIndex + int(remainingChanges)):
                    bracket[remainingChangesRound][((i - (i % 2)) // 2)][i % 2] = f'W{i + 1}'

                if remainingChanges == 0.5:
                    bracket[remainingChangesRound][startIndex // 2][startIndex % 2] = f'W{startIndex + 1}'

                remainingChanges = remainingChanges / 2
                remainingChangesRound += 1
                startIndex = startIndex // 2

            fractionLeft = fractionLeft / 2
            editingRound += 1
            sectorsFilled += 1

        else:
            editingRound += 1


    return bracket



# create all the necessary matches for users
def createRobin(users):
    matches = [] # will contain a 2d array of every matchup needed

    # each user will play each other user only once
    for i in range(0, len(users)):
        poppedUser = users.pop(0)

        for y in users:
            match = [poppedUser, y]
            
            # shuffle order of match
            random.shuffle(match)

            matches.append(match)

    # shuffle all matches
    random.shuffle(matches)

    return matches



# initialise round robin table
def createRobinTable(userDetails):
    table = []

    # pad each record with zeroes
    for i in userDetails:
        if i[0] != -1:
            record = [i[0], i[1], 0, 0, 0, 0, 0]
            table.append(record)

    return table



# find the next match given the current match index
# -> will return -1 if that match was the last match
def nextMatch(type, matches, index):
    if type == "Knockout":
        round = 1
        maxRound = len(matches)
        currentIndex = 0

        for i in range(0, index):
            if round == maxRound: # catches if index is far too large
                return -1
            
            elif currentIndex == len(matches[round]) - 1: # if current index is last in the tier
                currentIndex = 0
                round += 1

            elif matches[round][currentIndex + 1] == ["", ""]: # if current index is the last actual match in a tier
                currentIndex = 0
                round += 1

            else:
                currentIndex += 1

        if round == maxRound:
            return -1
        
        else:
            return matches[round][currentIndex]
    
    else:
        if index < len(matches):
            return matches[index]
        
        else:
            return -1


# handles when resign button is clicked
def resign(dashboard):

    if dashboard.tournamentChessBoard.offerLabel.isVisible() == False:

        dashboard.tournamentChessBoard.coverScreen.setHidden(False)

        dashboard.tournamentChessBoard.offerLabel.setText("Are you sure?")
        dashboard.tournamentChessBoard.offerLabel.setHidden(False)

        dashboard.tournamentChessBoard.acceptOfferButton.setText("Resign")
        dashboard.tournamentChessBoard.acceptOfferButton.setHidden(False)

        dashboard.tournamentChessBoard.rejectOfferButton.setText("Cancel")
        dashboard.tournamentChessBoard.rejectOfferButton.setHidden(False)



# populate stage 4
def goToTournamentStage4(dashboard, match, userDetails):
    dashboard.tournamentStage4Widget.resetUi()

    dashboard.tournamentChessBoard.resetUi()
    dashboard.tournamentChessBoard.coverScreen.setHidden(True)

    dashboard.tournamentStage4Widget.player1Username = match[0]

    # add the correct details for player 1
    for i in userDetails:
        if match[0] == i[1]:
            dashboard.tournamentStage4Widget.player1Id = i[0]
            dashboard.tournamentStage4Widget.player1Rating = i[2]

    dashboard.tournamentStage4Widget.player2Username = match[1]

    # add the correct details for player 2
    for i in userDetails:
        if match[1] == i[1]:
            dashboard.tournamentStage4Widget.player2Id = i[0]
            dashboard.tournamentStage4Widget.player2Rating = i[2]

    # randomly picks which player is black and the other white
    if random.randint(0, 1) == 1:
        dashboard.tournamentChessBoard.whitePlayer = dashboard.tournamentStage4Widget.player1Username
        dashboard.tournamentChessBoard.whitePlayerId = dashboard.tournamentStage4Widget.player1Id
        dashboard.tournamentStage4Widget.currentUserLabel.setText("White: " + dashboard.tournamentStage4Widget.player1Username)

        dashboard.tournamentChessBoard.blackPlayer = dashboard.tournamentStage4Widget.player2Username
        dashboard.chessBoard.blackPlayerId = dashboard.tournamentStage4Widget.player2Id
        dashboard.tournamentStage4Widget.opponentUserLabel.setText("Black: " + dashboard.tournamentStage4Widget.player2Username)

    else:
        dashboard.tournamentChessBoard.whitePlayer = dashboard.tournamentStage4Widget.player2Username
        dashboard.tournamentChessBoard.whitePlayerId = dashboard.tournamentStage4Widget.player2Id
        dashboard.tournamentStage4Widget.currentUserLabel.setText("Black: " + dashboard.tournamentStage4Widget.player1Username)

        dashboard.tournamentChessBoard.blackPlayer = dashboard.tournamentStage4Widget.player1Username
        dashboard.tournamentChessBoard.blackPlayerId = dashboard.tournamentStage4Widget.player1Id
        dashboard.tournamentStage4Widget.opponentUserLabel.setText("White: " + dashboard.tournamentStage4Widget.player2Username)

    # creates the necessary records
    dashboard.tournamentChessBoard.currentMatchId = createMatch(dashboard.tournamentChessBoard.whitePlayerId, dashboard.tournamentChessBoard.blackPlayerId)
    makeCompMatchRecord(dashboard.tournamentStage3Widget.tournamentId, dashboard.tournamentChessBoard.whitePlayerId, dashboard.tournamentChessBoard.blackPlayerId,
                        dashboard.tournamentChessBoard.currentMatchId, dashboard.tournamentStage3Widget.tournamentType)

    # populates rating labels
    dashboard.tournamentStage4Widget.currentUserRatingLabel.setText(f"Rating: {str(dashboard.tournamentStage4Widget.player1Rating)}")
    dashboard.tournamentStage4Widget.opponentUserRatingLabel.setText(f"Rating: {str(dashboard.tournamentStage4Widget.player2Rating)}")

    # calculates rating deltas
    currentWin = ratingChange(dashboard.tournamentStage4Widget.player1Rating, dashboard.tournamentStage4Widget.player2Rating, 1, 50)
    currentDraw = ratingChange(dashboard.tournamentStage4Widget.player1Rating, dashboard.tournamentStage4Widget.player2Rating, 0.5, 50)
    currentLoss = ratingChange(dashboard.tournamentStage4Widget.player1Rating, dashboard.tournamentStage4Widget.player2Rating, 0, 50)

    opponentWin = ratingChange(dashboard.tournamentStage4Widget.player1Rating, dashboard.tournamentStage4Widget.player2Rating, 1, 50)
    opponentDraw = ratingChange(dashboard.tournamentStage4Widget.player1Rating, dashboard.tournamentStage4Widget.player2Rating, 0.5, 50)
    opponentLoss = ratingChange(dashboard.tournamentStage4Widget.player1Rating, dashboard.tournamentStage4Widget.player2Rating, 0, 50)

    # populates rating deltas
    dashboard.tournamentStage4Widget.currentUserRatingDelta.setText(f"Win {'+' if currentWin >= 0 else ''}{currentWin} / Draw {'+' if currentDraw >= 0 else ''}{currentDraw} / Loss {'+' if currentLoss >= 0 else ''}{currentLoss}")
    dashboard.tournamentStage4Widget.opponentUserRatingDelta.setText(f"Win {'+' if opponentWin >= 0 else ''}{opponentWin} / Draw {'+' if opponentDraw >= 0 else ''}{opponentDraw} / Loss {'+' if opponentLoss >= 0 else ''}{opponentLoss}")

    dashboard.tournamentStage4Widget.currentUserRatingDeltaArray = [currentWin, currentDraw, currentLoss]
    dashboard.tournamentStage4Widget.opponentUserRatingDeltaArray = [opponentWin, opponentDraw, opponentLoss]

    dashboard.tournamentChessBoard.coverScreen.setHidden(True)

    dashboard.pvpStackedWidget.setCurrentIndex(5)



# populate stage 3 after a match has been completed
def goBackToTournamentStage3(dashboard, outcome):
    tournamentStage3 = dashboard.tournamentStage3Widget
    tournamentStage4 = dashboard.tournamentStage4Widget
    tournamentChessBoard = dashboard.tournamentChessBoard

    # changes the ratings of the players based upon the outcome
    if dashboard.tournamentChessBoard.whitePlayer == tournamentStage4.player1Id:
        player1Rating = dashboard.tournamentStage4Widget.player1Rating + dashboard.tournamentStage4Widget.currentUserRatingDeltaArray[(outcome * -1) + 1]
        player2Rating = dashboard.tournamentStage4Widget.player2Rating + dashboard.tournamentStage4Widget.opponentUserRatingDeltaArray[(outcome) + 1]

    else:
        player1Rating = dashboard.tournamentStage4Widget.player1Rating + dashboard.tournamentStage4Widget.currentUserRatingDeltaArray[(outcome) + 1]
        player2Rating = dashboard.tournamentStage4Widget.player2Rating + dashboard.tournamentStage4Widget.opponentUserRatingDeltaArray[(outcome * -1) + 1]

    # update player ratings in the userDetails array
    for i in tournamentStage3.userDetails:
        if i[1] == tournamentStage4.player1Username:
            i[2] = player1Rating

        elif i[1] == tournamentStage4.player2Username:
            i[2] = player2Rating

    finaliseMatch(dashboard, dashboard.tournamentChessBoard.currentMatchId, outcome, dashboard.tournamentChessBoard.pgn, player1Rating, player2Rating)

    # update bracket and get next match
    if tournamentStage3.tournamentType == "Knockout":
        previousMatchRound, previousMatchIndex = getCurrentTournamentMatch(tournamentStage3.knockoutDetails, tournamentStage3.matchIndex)

        # get the winner from the match
        if outcome == 1:
            successor = tournamentChessBoard.whitePlayer

        else:
            successor = tournamentChessBoard.blackPlayer

        # update the bracket replacing "Wx" with player name
        if previousMatchRound == len(tournamentStage3.knockoutDetails) - 1:
            tournamentStage3.knockoutDetails[previousMatchRound + 1][0] = [successor]

        else:
            tournamentStage3.knockoutDetails[previousMatchRound + 1][previousMatchIndex // 2][previousMatchIndex % 2] = successor

        # get next match
        match = nextMatch("Knockout", tournamentStage3.knockoutDetails, tournamentStage3.matchIndex + 1)
        tournamentStage3.scrollableMatplotlibWidget.drawTournamentBracket(tournamentStage3.knockoutDetails)


    else:
        match = nextMatch("Round Robin", tournamentStage3.roundRobinMatches, tournamentStage3.matchIndex + 1)

        # update the league table
        for i in tournamentStage3.roundRobinDetails:
            if i[1] == tournamentChessBoard.whitePlayer:
                if outcome == 1:
                    i[2] += 1
                    i[3] += 1
                    i[6] += 1

                elif outcome == 0:
                    i[2] += 1
                    i[4] += 1
                    i[6] += 0.5

                else:
                    i[2] += 1
                    i[5] += 1

            if i[1] == tournamentChessBoard.blackPlayer:
                if outcome == -1:
                    i[2] += 1
                    i[3] += 1
                    i[6] += 1

                elif outcome == 0:
                    i[2] += 1
                    i[4] += 1
                    i[6] += 0.5

                else:
                    i[2] += 1
                    i[5] += 1

        tournamentStage3.scrollableMatplotlibWidget.drawRoundRobin(tournamentStage3.roundRobinDetails)


    tournamentStage3.matchIndex += 1
    tournamentStage3.currentMatch = match

    # populate for next match
    tournamentStage3.populateNextMatch(match, tournamentStage3.userDetails)

    dashboard.pvpStackedWidget.setCurrentIndex(4)



# handles when a draw button is clicked
def requestDraw(dashboard):

    if dashboard.tournamentChessBoard.offerLabel.isVisible() == False:

        dashboard.tournamentChessBoard.coverScreen.setHidden(False)

        dashboard.tournamentChessBoard.offerLabel.setText("Draw offered")
        dashboard.tournamentChessBoard.offerLabel.setHidden(False)

        dashboard.tournamentChessBoard.acceptOfferButton.setText("Accept")
        dashboard.tournamentChessBoard.acceptOfferButton.setHidden(False)

        dashboard.tournamentChessBoard.rejectOfferButton.setText("Decline")
        dashboard.tournamentChessBoard.rejectOfferButton.setHidden(False)



# finds the match from an index
def getCurrentTournamentMatch(bracket, matchIndex):
    round = 1
    index = 0

    for i in range(0, matchIndex):
        if index == len(bracket[round]) - 1: # if match is last in tier
            index = 0
            round += 1

        elif bracket[round][index + 1] == ['', '']: # if match is last actual match in tier
            print("found a blank")
            round += 1
            index = 0

        else:
            index += 1

    return round, index



# finalises match record and alters users' ratings
def finaliseMatch(dashboard, matchId, outcome, pgn, player1Rating, player2Rating):
    query = {"id": matchId}

    match = getData("matches", **query)

    match = match[0]

    # set winner
    if outcome == 1:
        match["winner"] = match["whitePlayer"]

    elif outcome == -1:
        match["winner"] = match["blackPlayer"]

    else:
        match["winner"] = "draw"

    match["pgn"] = pgn

    match["finished"] = True

    update("matches", match, matchId)

    # update user record unless player is guest
    if dashboard.tournamentStage4Widget.player1Id != "guest":
        currentUser = getData("users", id = dashboard.tournamentStage4Widget.player1Id)
        currentUser = currentUser[0]

        currentUser["rating"] = player1Rating
        currentUser["match3"] = currentUser["match2"]
        currentUser["match2"] = currentUser["match1"]
        currentUser["match1"] = matchId

        update("users", currentUser, dashboard.tournamentStage4Widget.player1Id)

        currentUserId = currentUser["id"]
        currentUserRating = player1Rating
        timeInfo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        currentUserProgressRecord = {
            "userId": currentUserId,
            "matchRating": currentUserRating,
            "datetime": timeInfo
        }

        _ = insert("matchProgress", currentUserProgressRecord)

    # both players must be checked for guests as tournament may have guest vs guest
    if dashboard.tournamentStage4Widget.player2Id != "guest":
        opponentUser = getData("users", id = dashboard.tournamentStage4Widget.player2Id)
        opponentUser = opponentUser[0]

        opponentUser["rating"] = player2Rating
        opponentUser["match3"] = opponentUser["match2"]
        opponentUser["match2"] = opponentUser["match1"]
        opponentUser["match1"] = matchId

        update("users", opponentUser, dashboard.tournamentStage4Widget.player2Id)

        opponentUserId = opponentUser["id"]
        opponentUserRating = player2Rating
        timeInfo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        opponentUserProgressRecord = {
            "userId": opponentUserId,
            "matchRating": opponentUserRating,
            "datetime": timeInfo
        }

        _ = insert("matchProgress", opponentUserProgressRecord)



# finalises unifinished matches when program is exited
def finaliseMatchAndTournamentOnExit(dashboard):
    if dashboard.pvpStackedWidget.currentIndex() == 5:
        matchId = dashboard.tournamentChessBoard.currentMatchId

        query = {"id": matchId}

        match = getData("matches", **query)

        match = match[0]

        match["pgn"] = dashboard.tournamentChessBoard.pgn

        match["winner"] = "Unfinished match"

        update("matches", match, matchId)



# add record to tournaments.json
def makeTournamentRecord(type, capacity):
    record = {"type": type,
              "capacity": capacity,
              "winnerId": "unfinished"}
    
    tournamentId = insert("tournaments", record)

    return tournamentId



# add record to competitors.json
def makeCompetitorsRecord(userId, tournamentId):
    record = {"userId": userId,
              "tournamentId": tournamentId}
    
    _ = insert("competitors", record)



# add record to compMatch.json
def makeCompMatchRecord(tournamentId, whitePlayerId, blackPlayerId, matchId, type):
    record = {"tournamentId": tournamentId,
              "white": whitePlayerId,
              "black": blackPlayerId,
              "matchId": matchId,
              "type": type}
    
    _ = insert("compMatch", record)



# finalise tournament
def finaliseTournament(tournamentId, winnerId):
    query = {"id": tournamentId}

    tournamentRecord = getData("tournaments", **query)

    tournamentRecord = tournamentRecord[0]

    tournamentRecord["winnerId"] = winnerId

    update("tournaments", tournamentRecord, tournamentId)




    
        



