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

        else:
            guestName = widget.guestNameInput.text()

            if len(guestName) == 0:
                widget.errorLabel.setText("Name must be filled")
                widget.errorLabel.setHidden(False)

            else:
                clash = False

                for i in widget.userDetails:
                    if guestName == i[1]:
                        clash = True

                if clash == True:
                    widget.errorLabel.setText("Name must be unique")
                    widget.errorLabel.setHidden(False)

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

    if loginSuccess == True:
        widget.userTypeLabel.setHidden(False)
        widget.userLabel.setHidden(False)

        widget.userLabel.setText(widget.userDetails[index][1])

        widget.secondaryUserRadioButton.setHidden(True)
        widget.guestRadioButton.setHidden(True)

        widget.userElements[index][1].setText(widget.userDetails[index][1])
        widget.userValues[index][1] = True



def goToTournamentStage2(dashboard, widget, capacity):
    dashboard.tournamentStage2Widget.resetUi()

    valid = False

    if capacity.isdigit():
        capacity = int(capacity)
        print(capacity)


        if widget.tournamentTypeGroup.checkedButton().objectName() == "knockoutRadioButton":
            if capacity <= 8 and capacity > 0:
                dashboard.tournamentStage2Widget.titleLabel.setText("Knockout")

                dashboard.tournamentStage2Widget.tournamentType = "Knockout"

                valid = True

            else:
                widget.tournamentErrorLabel.setHidden(False)
                widget.tournamentErrorLabel.setText("Knockout capacity must be 8 or smaller")
        
        else:
            if capacity > 7:
                widget.tournamentErrorLabel.setHidden(False)
                widget.tournamentErrorLabel.setText("A round robin must have 6 or less people")

            else:
                dashboard.tournamentStage2Widget.titleLabel.setText("Round Robin")

                dashboard.tournamentStage2Widget.tournamentType = "Round Robin"

                valid = True

    else:
        widget.tournamentErrorLabel.setHidden(False)
        widget.tournamentErrorLabel.setText("Capacity must be an integer")

    if valid == True:
        dashboard.tournamentStage2Widget.capacity = capacity
        dashboard.tournamentStage2Widget.setActivePlayers(capacity)
        widget.tournamentErrorLabel.setHidden(True)

        dashboard.tournamentChessBoard.resetUi()

        dashboard.pvpStackedWidget.setCurrentIndex(3)
        dashboard.centralStackedWidget.setCurrentIndex(3)



def goToStage1FromTournaments(dashboard):
    dashboard.playWidget.resetUi(dashboard.baseWindow.userId)
    dashboard.tournamentStage2Widget.resetUi()
    dashboard.tournamentStage3Widget.resetUi()
    dashboard.tournamentStage4Widget.resetUi()
    dashboard.tournamentChessBoard.resetUi()
    dashboard.pvpStackedWidget.setCurrentIndex(0)
    dashboard.centralStackedWidget.setCurrentIndex(3)



def goToTournamentStage3(dashboard, type, userDetails, capacity):

    inputtedCapacity = 0

    for i in userDetails:
        if i[0] != -1:
            inputtedCapacity += 1

    if inputtedCapacity == capacity:
        dashboard.tournamentStage3Widget.resetUi()

        dashboard.tournamentStage3Widget.typeLabel.setText(type)

        dashboard.tournamentStage3Widget.tournamentType = type
        dashboard.tournamentStage3Widget.userDetails = userDetails

        users = []
        userIds = []

        for i in userDetails:
            if i[0] != -1:
                users.append(i[1])
                userIds.append(i[0])

        if type == "Knockout":
            print(f"users to put in the bracket: {users}")
            bracket = createBracket(users)
            print(f"final bracket: {bracket}")

            dashboard.tournamentStage3Widget.knockoutDetails = bracket

            dashboard.tournamentStage3Widget.scrollable_matplotlib_widget.draw_tournament_bracket(bracket)

            match = nextMatch("Knockout", bracket, 0)

        elif type == "Round Robin":
            print(f"users to put in the table: {users}")
            matches = createRobin(users)
            table = createRobinTable(userDetails)

            dashboard.tournamentStage3Widget.roundRobinMatches = matches
            dashboard.tournamentStage3Widget.roundRobinDetails = table

            dashboard.tournamentStage3Widget.scrollable_matplotlib_widget.draw_round_robin(table)

            match = nextMatch("Robin", matches, 0)

        dashboard.tournamentStage3Widget.matchIndex = 0
        dashboard.tournamentStage3Widget.currentMatch = match

        dashboard.tournamentStage3Widget.tournamentId = makeTournamentRecord(type, capacity)

        for i in userIds:
            makeCompetitorsRecord(i, dashboard.tournamentStage3Widget.tournamentId)

        # create a populate function which takes the match array and populates all necessary elements of stage 3
        dashboard.tournamentStage3Widget.populateNextMatch(match, userDetails)

        dashboard.pvpStackedWidget.setCurrentIndex(4)
    
    else:
        dashboard.tournamentStage2Widget.errorLabel.setText("Please log in all players")
        dashboard.tournamentStage2Widget.errorLabel.setHidden(False)

        


def createBracket(users):
    start = 1
    size = 1 # contains the number of rounds of the bracket
    found = False

    random.shuffle(users)

    while found == False:
        if len(users) > start:
            size += 1

        else:
            found = True

        start = start * 2

    bracket = {}

    for i in range(1, size + 1):
        bracket[i] = []

        if i == size:
            bracket[i].append(["Winner"])

        else:
            for y in range(0, 2**(size - i - 1)):
                bracket[i].append(["", ""])

    usersToAdd = []

    for i in range(0, 2**(size - 2)):
        usersToAdd.append(users.pop(0))

    for i in range(0, len(usersToAdd) // 2):
        bracket[1][i] = [usersToAdd[i * 2], usersToAdd[(i * 2) + 1]]

    remainingChanges = int(len(usersToAdd) / 2)
    index = 2

    while remainingChanges >= 0.5:

        for i in range(0, int(remainingChanges)):
            bracket[index][(i - (i % 2)) // 2][i % 2] = f'W{i + 1}'

        if remainingChanges == 0.5:
            bracket[index][0][0] = 'W1'

        index += 1
        remainingChanges = remainingChanges / 2

    editingRound = 1
    fractionLeft = 0.5
    sectorsFilled = 0
    
    while len(users) > 0:
        if len(users) == 2**(size - editingRound - 1 - sectorsFilled):
            usersToAdd = []

            for i in range(0, len(users)):
                usersToAdd.append(users.pop(0))

            index = int(2**(size - editingRound) - (2**(size - editingRound) * fractionLeft))

            for i in usersToAdd:
                bracket[editingRound][index // 2][index % 2] = i

                index += 1

            remainingChanges = len(usersToAdd) // 2
            remainingChangesRound = editingRound + 1

            startIndex = int(2**(size - editingRound) - (2**(size - editingRound) * fractionLeft)) // 2

            while remainingChanges >= 0.5:
                # find the first index to change
                roundCapacity = 2**(size - remainingChangesRound)
                #startIndex = roundCapacity - int(roundCapacity * 2**(-editingRound))

                for i in range(startIndex, startIndex + int(remainingChanges)):
                    bracket[remainingChangesRound][((i - (i % 2)) // 2)][i % 2] = f'W{i + 1}'

                if remainingChanges == 0.5:
                    if remainingChangesRound != size:
                        bracket[remainingChangesRound][startIndex // 2][startIndex % 2] = f'W{startIndex + 1}'

                remainingChanges = remainingChanges / 2
                remainingChangesRound += 1
                startIndex = startIndex // 2
        

        elif len(users) > 2**(size - editingRound - 2):

            # this portion populates a left over part of the bracket if there are enough
            # remaining users to do so
            usersToAdd = []


            for i in range(0, int(2**(size - editingRound - 2))):
                usersToAdd.append(users.pop(0))

            if 2**(size - editingRound - 2) < 1:
                usersToAdd.append(users.pop(0))

            index = int(2**(size - editingRound) - (2**(size - editingRound) * fractionLeft))

            for i in usersToAdd:
            
                print(index)
                bracket[editingRound][index // 2][index % 2] = i

                index += 1
            
            remainingChanges = int(len(usersToAdd) // 2)

            remainingChangesRound = editingRound + 1

            startIndex = int(2**(size - editingRound) - (2**(size - editingRound) * fractionLeft)) // 2

            while remainingChanges >= 0.5:
                # find the first index to change
                roundCapacity = 2**(size - remainingChangesRound)
                # startIndex = roundCapacity - int(roundCapacity * 2**(-editingRound))

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


def createRobin(users):
    matches = [] # will contain a 2d array of every matchup needed

    for i in range(0, len(users)):
        poppedUser = users.pop(0)

        for y in users:
            match = [poppedUser, y]
            
            random.shuffle(match)

            matches.append(match)

    random.shuffle(matches)

    return matches



def createRobinTable(userDetails):
    table = []

    for i in userDetails:
        if i[0] != -1:
            record = [i[0], i[1], 0, 0, 0, 0, 0]
            table.append(record)

    return table



def nextMatch(type, matches, index):
    if type == "Knockout":
        round = 1
        maxRound = len(matches)
        currentIndex = 0

        for i in range(0, index):
            if round == maxRound: # catches if index is far too large
                return -1
            
            elif currentIndex == len(matches[round]) - 1:
                currentIndex = 0
                round += 1

            elif matches[round][currentIndex + 1] == ["", ""]:
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


def goToTournamentStage4(dashboard, match, userDetails):
    dashboard.tournamentStage4Widget.resetUi()

    dashboard.tournamentChessBoard.resetUi()
    dashboard.tournamentChessBoard.coverScreen.setHidden(True)

    dashboard.tournamentStage4Widget.player1Username = match[0]

    for i in userDetails:
        if match[0] == i[1]:
            dashboard.tournamentStage4Widget.player1Id = i[0]
            dashboard.tournamentStage4Widget.player1Rating = i[2]

    dashboard.tournamentStage4Widget.player2Username = match[1]

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

    dashboard.tournamentChessBoard.currentMatchId = createMatch(dashboard.tournamentChessBoard.whitePlayerId, dashboard.tournamentChessBoard.blackPlayerId)
    makeCompMatchRecord(dashboard.tournamentStage3Widget.tournamentId, dashboard.tournamentChessBoard.whitePlayerId, dashboard.tournamentChessBoard.blackPlayerId,
                        dashboard.tournamentChessBoard.currentMatchId, dashboard.tournamentStage3Widget.tournamentType)

    dashboard.tournamentStage4Widget.currentUserRatingLabel.setText(f"Rating: {str(dashboard.tournamentStage4Widget.player1Rating)}")

    dashboard.tournamentStage4Widget.opponentUserRatingLabel.setText(f"Rating: {str(dashboard.tournamentStage4Widget.player2Rating)}")

    currentWin = ratingChange(dashboard.tournamentStage4Widget.player1Rating, dashboard.tournamentStage4Widget.player2Rating, 1, 50)
    currentDraw = ratingChange(dashboard.tournamentStage4Widget.player1Rating, dashboard.tournamentStage4Widget.player2Rating, 0.5, 50)
    currentLoss = ratingChange(dashboard.tournamentStage4Widget.player1Rating, dashboard.tournamentStage4Widget.player2Rating, 0, 50)

    opponentWin = ratingChange(dashboard.tournamentStage4Widget.player1Rating, dashboard.tournamentStage4Widget.player2Rating, 1, 50)
    opponentDraw = ratingChange(dashboard.tournamentStage4Widget.player1Rating, dashboard.tournamentStage4Widget.player2Rating, 0.5, 50)
    opponentLoss = ratingChange(dashboard.tournamentStage4Widget.player1Rating, dashboard.tournamentStage4Widget.player2Rating, 0, 50)

    dashboard.tournamentStage4Widget.currentUserRatingDelta.setText(f"Win {'+' if currentWin >= 0 else ''}{currentWin} / Draw {'+' if currentDraw >= 0 else ''}{currentDraw} / Loss {'+' if currentLoss >= 0 else ''}{currentLoss}")

    dashboard.tournamentStage4Widget.opponentUserRatingDelta.setText(f"Win {'+' if opponentWin >= 0 else ''}{opponentWin} / Draw {'+' if opponentDraw >= 0 else ''}{opponentDraw} / Loss {'+' if opponentLoss >= 0 else ''}{opponentLoss}")

    dashboard.tournamentStage4Widget.currentUserRatingDeltaArray = [currentWin, currentDraw, currentLoss]
    dashboard.tournamentStage4Widget.opponentUserRatingDeltaArray = [opponentWin, opponentDraw, opponentLoss]

    dashboard.tournamentChessBoard.coverScreen.setHidden(True)

    dashboard.pvpStackedWidget.setCurrentIndex(5)



def goBackToTournamentStage3(dashboard, outcome):
    tournamentStage3 = dashboard.tournamentStage3Widget
    tournamentStage4 = dashboard.tournamentStage4Widget
    tournamentChessBoard = dashboard.tournamentChessBoard

    if dashboard.tournamentChessBoard.whitePlayer == tournamentStage4.player1Id:
        player1Rating = dashboard.tournamentStage4Widget.player1Rating + dashboard.tournamentStage4Widget.currentUserRatingDeltaArray[(outcome * -1) + 1]
        player2Rating = dashboard.tournamentStage4Widget.player2Rating + dashboard.tournamentStage4Widget.opponentUserRatingDeltaArray[(outcome) + 1]

    else:
        player1Rating = dashboard.tournamentStage4Widget.player1Rating + dashboard.tournamentStage4Widget.currentUserRatingDeltaArray[(outcome) + 1]
        player2Rating = dashboard.tournamentStage4Widget.player2Rating + dashboard.tournamentStage4Widget.opponentUserRatingDeltaArray[(outcome * -1) + 1]

    for i in tournamentStage3.userDetails:
        if i[1] == tournamentStage4.player1Username:
            i[2] = player1Rating

        elif i[1] == tournamentStage4.player2Username:
            i[2] = player2Rating

    finaliseMatch(dashboard, dashboard.tournamentChessBoard.currentMatchId, outcome, dashboard.tournamentChessBoard.pgn, player1Rating, player2Rating)

    if tournamentStage3.tournamentType == "Knockout":
        previousMatchRound, previousMatchIndex = getCurrentTournamentMatch(tournamentStage3.knockoutDetails, tournamentStage3.matchIndex)
        if outcome == 1:
            successor = tournamentChessBoard.whitePlayer

        else:
            successor = tournamentChessBoard.blackPlayer


        if previousMatchRound == len(tournamentStage3.knockoutDetails) - 1:
            tournamentStage3.knockoutDetails[previousMatchRound + 1][0] = [successor]
            print("tourney finished")
            print(f"new bracket: {tournamentStage3.knockoutDetails}")

        else:
            tournamentStage3.knockoutDetails[previousMatchRound + 1][previousMatchIndex // 2][previousMatchIndex % 2] = successor
            print(f"new bracket: {tournamentStage3.knockoutDetails}")

        match = nextMatch("Knockout", tournamentStage3.knockoutDetails, tournamentStage3.matchIndex + 1)
        tournamentStage3.scrollable_matplotlib_widget.draw_tournament_bracket(tournamentStage3.knockoutDetails)


    else:
        match = nextMatch("Round Robin", tournamentStage3.roundRobinMatches, tournamentStage3.matchIndex + 1)

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

        tournamentStage3.scrollable_matplotlib_widget.draw_round_robin(tournamentStage3.roundRobinDetails)


    tournamentStage3.matchIndex += 1
    tournamentStage3.currentMatch = match
    print(match)
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



def getCurrentTournamentMatch(bracket, matchIndex):
    round = 1
    index = 0

    for i in range(0, matchIndex):
        if index == len(bracket[round]) - 1:
            index = 0
            round += 1

        elif bracket[round][index + 1] == ['', '']:
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

    print(matchId)
    print(match)

    match = match[0]

    if outcome == 1:
        match["winner"] = match["whitePlayer"]

    elif outcome == -1:
        match["winner"] = match["blackPlayer"]

    else:
        match["winner"] = "draw"

    match["pgn"] = pgn

    match["finished"] = True

    update("matches", match, matchId)

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



def makeTournamentRecord(type, capacity):
    record = {"type": type,
              "capacity": capacity,
              "winnerId": "unfinished"}
    
    tournamentId = insert("tournaments", record)

    return tournamentId


def makeCompetitorsRecord(userId, tournamentId):
    record = {"userId": userId,
              "tournamentId": tournamentId}
    
    _ = insert("competitors", record)


def makeCompMatchRecord(tournamentId, whitePlayerId, blackPlayerId, matchId, type):
    record = {"tournamentId": tournamentId,
              "white": whitePlayerId,
              "black": blackPlayerId,
              "matchId": matchId,
              "type": type}
    
    _ = insert("compMatch", record)


def finaliseTournament(tournamentId, winnerId):
    query = {"id": tournamentId}

    tournamentRecord = getData("tournaments", **query)

    tournamentRecord = tournamentRecord[0]

    tournamentRecord["winnerId"] = winnerId

    update("tournaments", tournamentRecord, tournamentId)


'''users = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
bracket = createBracket(users)
print(f"final bracket: {bracket}")

for i in range(0, 5):
    print(nextMatch("Knockout", bracket, i))'''



    
        



