from PyQt5 import QtCore, QtGui, QtWidgets
from playerDB.passwordFunctions import passwordHashing, verifyPassword
from playerDB.jsonFunctions import *
import random

# handles the loggging in of a secondary user for pvp
def secondaryLogIn(widget, username, password, state, baseWindow):
    # print(widget.opponentUser)

    # if no-one is already logged in
    if state is False:
        # ensures both inputs are filled
        if len(username) == 0 or len(password) == 0:
            widget.errorLabel.setText("Both fields must be filled")
            widget.errorLabel.setHidden(False)

        else:
            # gets data
            data = getData("users", username = username)
            
            # if no record is found
            if len(data) == 0:
                widget.errorLabel.setText("Incorrect username or password")
                widget.errorLabel.setHidden(False)

            # if base user tries to login
            elif data[0]["id"] == baseWindow.userId:
                widget.errorLabel.setText("User cannot play themselves")
                widget.errorLabel.setHidden(False)

            else:
                # fetches hashed password
                id = data[0]["id"]

                query = {"id": id}

                passwordData = getData("passwords", **query)
                hashedPassword = passwordData[0]["hash"]

                # if password doesn't match
                if not verifyPassword(hashedPassword, password):
                    widget.errorLabel.setText("Incorrect username or password")
                    widget.errorLabel.setHidden(False)

                # populates all necessary elements with new logged in user
                else:
                    widget.opponentUser = id

                    widget.secondaryUsernameInput.setHidden(True)
                    widget.secondaryPasswordInput.setHidden(True)

                    widget.secondaryUserLabel.setText("User: " + data[0]["username"])
                    widget.secondaryUserLabel.setHidden(False)

                    widget.secondaryUserRatingLabel.setText("Rating: " + str(data[0]["rating"]))
                    widget.secondaryUserLabel.setHidden(False)

                    widget.loginButton.setText("Log Out")

                    widget.errorLabel.setHidden(True)

    else:
        # handles when secondary user logs out
        widget.errorLabel.setHidden(True)
        widget.secondaryUserLabel.setHidden(True)
        widget.secondaryUserLabel.setHidden(True)

        widget.secondaryUsernameInput.setHidden(False)
        widget.secondaryPasswordInput.setHidden(False)

        widget.loginButton.setText("Log In")

        widget.opponentUser = False



# handles the event that the play button is clicked
def Play(baseWindow, dashboard, widget, radioButtonStatus, opponentUser):
    # handles when no selection is made
    if radioButtonStatus == None:
        widget.errorLabel.setText("Pick opponent option")
        widget.errorLabel.setHidden(False)

    # if secondary user selected but no logged in secondary user
    elif radioButtonStatus.text() == "Secondary User" and opponentUser is False:
        widget.errorLabel.setText("Log in other user")
        widget.errorLabel.setHidden(False)

    # passes id of secondary user if secondary user is selected
    elif radioButtonStatus.text() == "Secondary User":
        # transition to pvp stage 2
        # pass the id of secondary user
        print("passing opponent id")
        goToStage2(dashboard, baseWindow.userId, opponentUser)

    # passes guest as id if guest option is picked
    else:
        # transition to pvp stage 2
        # pass the id of guest
        print("passing guest")
        goToStage2(dashboard, baseWindow.userId, "guest")



# whenever the utility widget must switch to stage 2
def goToStage2(dashboard, userId, opponentId):
    # resets stage 2 ui
    dashboard.pvpStage2Widget.resetUi()

    # resets chessboard Ui
    dashboard.chessBoard.resetUi()

    # gets user data
    userQuery = {"id": userId}
    userData = getData("users", **userQuery)
    userUsername = userData[0]["username"]
    userRating = userData[0]["rating"]

    # gets opponent data based on whether opponent is secondary user
    if opponentId == "guest":
        opponentUsername = "guest"
        opponentRating = 800
    
    else:
        opponentQuery = {"id": opponentId}
        opponentData = getData("users", **opponentQuery)

        opponentUsername = opponentData[0]["username"]
        opponentRating = opponentData[0]["rating"]

    # declares data within the widget so it can be accessed
    dashboard.pvpStage2Widget.userId = userId
    dashboard.pvpStage2Widget.opponentId = opponentId

    dashboard.pvpStage2Widget.userRating = userRating
    dashboard.pvpStage2Widget.opponentRating = opponentRating

    dashboard.pvpStage2Widget.userUsername = userUsername
    dashboard.pvpStage2Widget.opponentUsername = opponentUsername

    # randomly picks which player is black and the other white
    if random.randint(0, 1) == 1:
        dashboard.chessBoard.whitePlayer = userUsername
        dashboard.chessBoard.whitePlayerId = userId
        dashboard.pvpStage2Widget.currentUserLabel.setText("White: " + userUsername)

        dashboard.chessBoard.blackPlayer = opponentUsername
        dashboard.chessBoard.blackPlayerId = opponentId
        dashboard.pvpStage2Widget.opponentUserLabel.setText("Black: " + opponentUsername)

    else:
        dashboard.chessBoard.whitePlayer = opponentUsername
        dashboard.chessBoard.whitePlayerId = opponentId
        dashboard.pvpStage2Widget.currentUserLabel.setText("Black: " + userUsername)

        dashboard.chessBoard.blackPlayer = userUsername
        dashboard.chessBoard.blackPlayerId = userId
        dashboard.pvpStage2Widget.opponentUserLabel.setText("White: " + opponentUsername)

    # gives chessBoard the current match id whilst also creating a match record
    dashboard.chessBoard.currentMatchId = createMatch(dashboard.chessBoard.whitePlayerId, dashboard.chessBoard.blackPlayerId)

    # populate widget
    dashboard.pvpStage2Widget.currentUserRatingLabel.setText("Rating: " + str(userRating))

    dashboard.pvpStage2Widget.opponentUserRatingLabel.setText("Rating: " + str(opponentRating))

    # calculate rating changes for outcome
    currentWin = ratingChange(userRating, opponentRating, 1, 50)
    currentDraw = ratingChange(userRating, opponentRating, 0.5, 50)
    currentLoss = ratingChange(userRating, opponentRating, 0, 50)

    opponentWin = ratingChange(opponentRating, userRating, 1, 50)
    opponentDraw = ratingChange(opponentRating, userRating, 0.5, 50)
    opponentLoss = ratingChange(opponentRating, userRating, 0, 50)

    dashboard.pvpStage2Widget.currentUserRatingDelta.setText(f"Win {'+' if currentWin >= 0 else ''}{currentWin} / Draw {'+' if currentDraw >= 0 else ''}{currentDraw} / Loss {'+' if currentLoss >= 0 else ''}{currentLoss}")

    dashboard.pvpStage2Widget.opponentUserRatingDelta.setText(f"Win {'+' if opponentWin >= 0 else ''}{opponentWin} / Draw {'+' if opponentDraw >= 0 else ''}{opponentDraw} / Loss {'+' if opponentLoss >= 0 else ''}{opponentLoss}")

    # hold rating changes in accessible array
    dashboard.pvpStage2Widget.currentUserRatingDeltaArray = [currentWin, currentDraw, currentLoss]
    dashboard.pvpStage2Widget.opponentUserRatingDeltaArray = [opponentWin, opponentDraw, opponentLoss]

    # hides the cover screen on the chess board to allow players to make their moves
    dashboard.chessBoard.coverScreen.setHidden(True)

    # sends pvp widget to stage 2
    dashboard.pvpStackedWidget.setCurrentIndex(1)



# algebraically calculates ratings based on outcome and difference between ratings
def ratingChange(ratingA, ratingB, outcome, sensitivity):
    diff = ratingB - ratingA

    expectedScore = 1 / (1 + 10**(diff / 400))

    ratingChange = int(sensitivity*(outcome - expectedScore) + 10 * (outcome - 0.5))

    return ratingChange


# handles when a draw button is clicked
def requestDraw(dashboard):

    if dashboard.chessBoard.offerLabel.isVisible() == False:

        dashboard.chessBoard.coverScreen.setHidden(False)

        dashboard.chessBoard.offerLabel.setText("Draw offered")
        dashboard.chessBoard.offerLabel.setHidden(False)

        dashboard.chessBoard.acceptOfferButton.setText("Accept")
        dashboard.chessBoard.acceptOfferButton.setHidden(False)

        dashboard.chessBoard.rejectOfferButton.setText("Decline")
        dashboard.chessBoard.rejectOfferButton.setHidden(False)



# handles when resign button is clicked
def resign(dashboard):

    if dashboard.chessBoard.offerLabel.isVisible() == False:

        dashboard.chessBoard.coverScreen.setHidden(False)

        dashboard.chessBoard.offerLabel.setText("Are you sure?")
        dashboard.chessBoard.offerLabel.setHidden(False)

        dashboard.chessBoard.acceptOfferButton.setText("Resign")
        dashboard.chessBoard.acceptOfferButton.setHidden(False)

        dashboard.chessBoard.rejectOfferButton.setText("Cancel")
        dashboard.chessBoard.rejectOfferButton.setHidden(False)



# outcome is relative to the white player with 1 connoting a win, 0 a draw, and -1 a loss
def goToStage3(dashboard, outcome):
    # resets stage 3 ui
    dashboard.pvpStage3Widget.resetUi()

    # populate widget
    dashboard.pvpStage3Widget.currentUserLabel.setText(dashboard.pvpStage2Widget.currentUserLabel.text())
    dashboard.pvpStage3Widget.opponentLabel.setText(dashboard.pvpStage2Widget.opponentUserLabel.text())

    # if current user is the white player
    # if so the outcome is relative to the current user
    # the outcome is either 1, 0, or -1 whilst the rating change array holds win in position 0, draw in position 1, and loss in position 2
    # so therefore the outcome must be flipped by multiplying it by -1 and then shifting it by 1
    # outcome doesnt need to be flipped for rating of other player
    if dashboard.chessBoard.whitePlayer == dashboard.pvpStage2Widget.userUsername:
        dashboard.pvpStage3Widget.currentRating = dashboard.pvpStage2Widget.userRating + dashboard.pvpStage2Widget.currentUserRatingDeltaArray[(outcome * -1) + 1]
        dashboard.pvpStage3Widget.opponentRating = dashboard.pvpStage2Widget.opponentRating + dashboard.pvpStage2Widget.opponentUserRatingDeltaArray[(outcome) + 1]

    else:
        dashboard.pvpStage3Widget.currentRating = dashboard.pvpStage2Widget.userRating + dashboard.pvpStage2Widget.currentUserRatingDeltaArray[(outcome) + 1]
        dashboard.pvpStage3Widget.opponentRating = dashboard.pvpStage2Widget.opponentRating + dashboard.pvpStage2Widget.opponentUserRatingDeltaArray[(outcome * -1) + 1]

    # populate widget
    dashboard.pvpStage3Widget.currentUserRatingChange.setText(str(dashboard.pvpStage2Widget.userRating) + " -> " + str(dashboard.pvpStage3Widget.currentRating))
    dashboard.pvpStage3Widget.opponentUserRatingChange.setText(str(dashboard.pvpStage2Widget.opponentRating) + " -> " + str(dashboard.pvpStage3Widget.opponentRating))

    # get pgn from chess board
    dashboard.pvpStage3Widget.moveset.setText(dashboard.chessBoard.pgn)

    # finalise record
    finaliseMatch(dashboard, dashboard.chessBoard.currentMatchId, outcome, dashboard.chessBoard.pgn)

    dashboard.pvpStackedWidget.setCurrentIndex(2)



# handles going back to stage 1
def goToStage1(dashboard):
    dashboard.playWidget.resetUi(dashboard.pvpStage2Widget.userId)

    dashboard.chessBoard.resetUi()

    dashboard.pvpStackedWidget.setCurrentIndex(0)



# creates match record
def createMatch(whiteId, blackId):
    record = {"whitePlayer": whiteId,
              "blackPlayer": blackId,
              "winner": "",
              "pgn": "",
              "finished": False}
    
    matchId = insert("matches", record)

    return matchId



# finalises match record and alters users' ratings
def finaliseMatch(dashboard, matchId, outcome, pgn):
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

    currentUser = getData("users", id = dashboard.pvpStage2Widget.userId)
    currentUser = currentUser[0]

    currentUser["rating"] = dashboard.pvpStage3Widget.currentRating
    currentUser["match3"] = currentUser["match2"]
    currentUser["match2"] = currentUser["match1"]
    currentUser["match1"] = matchId

    update("users", currentUser, dashboard.pvpStage2Widget.userId)

    if dashboard.pvpStage2Widget.opponentId != "guest":
        opponentUser = getData("users", id = dashboard.pvpStage2Widget.opponentId)
        opponentUser = opponentUser[0]

        opponentUser["rating"] = dashboard.pvpStage3Widget.opponentRating
        opponentUser["match3"] = opponentUser["match2"]
        opponentUser["match2"] = opponentUser["match1"]
        opponentUser["match1"] = matchId

        update("users", opponentUser, dashboard.pvpStage2Widget.opponentId)



# finalises unifinished matches when program is exited
def finaliseMatchOnExit(dashboard):
    if dashboard.pvpStackedWidget.currentIndex() == 1:
        matchId = dashboard.chessBoard.currentMatchId

        query = {"id": matchId}

        match = getData("matches", **query)

        match = match[0]

        match["pgn"] = dashboard.chessBoard.pgn

        match["winner"] = "Unfinished match"

        update("matches", match, matchId)

    