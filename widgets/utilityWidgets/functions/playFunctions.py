from PyQt5 import QtCore, QtGui, QtWidgets
from playerDB.passwordFunctions import passwordHashing, verifyPassword
from playerDB.jsonFunctions import *
import random

def secondaryLogIn(widget, username, password, state, baseWindow):
    print(widget.opponentUser)

    if state is False:
        if len(username) == 0 or len(password) == 0:
            widget.errorLabel.setText("Ensure both fields are filled")
            widget.errorLabel.setHidden(False)

        else:
            data = getData("users", username = username)
            
            if len(data) == 0:
                widget.errorLabel.setText("Incorrect username or password")
                widget.errorLabel.setHidden(False)

            elif data[0]["id"] == baseWindow.userId:
                widget.errorLabel.setText("User cannot play themselves")
                widget.errorLabel.setHidden(False)

            else:
                id = data[0]["id"]

                query = {"id": id}

                passwordData = getData("passwords", **query)
                hashedPassword = passwordData[0]["hash"]

                if not verifyPassword(hashedPassword, password):
                    widget.errorLabel.setText("Incorrect username or password")
                    widget.errorLabel.setHidden(False)

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
        widget.errorLabel.setHidden(True)
        widget.secondaryUserLabel.setHidden(True)
        widget.secondaryUserLabel.setHidden(True)

        widget.secondaryUsernameInput.setHidden(False)
        widget.secondaryPasswordInput.setHidden(False)

        widget.loginButton.setText("Log In")

        widget.opponentUser = False



def Play(baseWindow, dashboard, widget, radioButtonStatus, opponentUser):
    if radioButtonStatus == None:
        widget.errorLabel.setText("Pick opponent option")
        widget.errorLabel.setHidden(False)

    elif radioButtonStatus.text() == "Secondary User" and opponentUser is False:
        widget.errorLabel.setText("Log in other user")
        widget.errorLabel.setHidden(False)

    elif radioButtonStatus.text() == "Secondary User":
        # transition to pvp stage 2
        # pass the id of secondary user
        print("passing opponent id")
        goToStage2(dashboard, baseWindow.userId, opponentUser)

    else:
        # transition to pvp stage 2
        # pass the id of guest
        print("passing guest")
        goToStage2(dashboard, baseWindow.userId, "guest")



def goToStage2(dashboard, userId, opponentId):
    dashboard.chessBoard.resetUi()

    userQuery = {"id": userId}
    userData = getData("users", **userQuery)
    userUsername = userData[0]["username"]
    userRating = userData[0]["rating"]

    if opponentId == "guest":
        opponentUsername = "guest"
        opponentRating = 800
    
    else:
        opponentQuery = {"id": opponentId}
        opponentData = getData("users", **opponentQuery)

        opponentUsername = opponentData[0]["username"]
        opponentRating = opponentData[0]["rating"]

    dashboard.pvpStage2Widget.userId = userId
    dashboard.pvpStage2Widget.opponentId = opponentId

    dashboard.pvpStage2Widget.userRating = userRating
    dashboard.pvpStage2Widget.opponentRating = opponentRating

    dashboard.pvpStage2Widget.userUsername = userUsername
    dashboard.pvpStage2Widget.opponentUsername = opponentUsername

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

    dashboard.chessBoard.currentMatchId = createMatch(dashboard.chessBoard.whitePlayerId, dashboard.chessBoard.blackPlayerId)

    dashboard.pvpStage2Widget.currentUserRatingLabel.setText("Rating: " + str(userRating))

    dashboard.pvpStage2Widget.opponentUserRatingLabel.setText("Rating: " + str(opponentRating))

    currentWin = ratingChange(userRating, opponentRating, 1)
    currentDraw = ratingChange(userRating, opponentRating, 0.5)
    currentLoss = ratingChange(userRating, opponentRating, 0)

    opponentWin = ratingChange(opponentRating, userRating, 1)
    opponentDraw = ratingChange(opponentRating, userRating, 0.5)
    opponentLoss = ratingChange(opponentRating, userRating, 0)

    dashboard.pvpStage2Widget.currentUserRatingDelta.setText(f"Win {'+' if currentWin >= 0 else ''}{currentWin} / Draw {'+' if currentDraw >= 0 else ''}{currentDraw} / Loss {'+' if currentLoss >= 0 else ''}{currentLoss}")

    dashboard.pvpStage2Widget.opponentUserRatingDelta.setText(f"Win {'+' if opponentWin >= 0 else ''}{opponentWin} / Draw {'+' if opponentDraw >= 0 else ''}{opponentDraw} / Loss {'+' if opponentLoss >= 0 else ''}{opponentLoss}")

    dashboard.pvpStage2Widget.currentUserRatingDeltaArray = [currentWin, currentDraw, currentLoss]
    dashboard.pvpStage2Widget.opponentUserRatingDeltaArray = [opponentWin, opponentDraw, opponentLoss]

    dashboard.chessBoard.coverScreen.setHidden(True)

    dashboard.utilityStackedWidget.setCurrentIndex(1)



def ratingChange(ratingA, ratingB, outcome):
    diff = ratingB - ratingA

    expectedScore = 1 / (1 + 10**(diff / 400))

    ratingChange = int(50*(outcome - expectedScore) + 10 * (outcome - 0.5))

    return ratingChange


def requestDraw(dashboard):

    if dashboard.chessBoard.offerLabel.isVisible() == False:

        dashboard.chessBoard.coverScreen.setHidden(False)

        dashboard.chessBoard.offerLabel.setText("Draw offered")
        dashboard.chessBoard.offerLabel.setHidden(False)

        dashboard.chessBoard.acceptOfferButton.setText("Accept")
        dashboard.chessBoard.acceptOfferButton.setHidden(False)

        dashboard.chessBoard.rejectOfferButton.setText("Decline")
        dashboard.chessBoard.rejectOfferButton.setHidden(False)



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
    dashboard.pvpStage3Widget.currentUserLabel.setText(dashboard.pvpStage2Widget.currentUserLabel.text())
    dashboard.pvpStage3Widget.opponentLabel.setText(dashboard.pvpStage2Widget.opponentUserLabel.text())

    if dashboard.chessBoard.whitePlayer == dashboard.pvpStage2Widget.userUsername:
        dashboard.pvpStage3Widget.currentRating = dashboard.pvpStage2Widget.userRating + dashboard.pvpStage2Widget.currentUserRatingDeltaArray[(outcome * -1) + 1]
        dashboard.pvpStage3Widget.opponentRating = dashboard.pvpStage2Widget.opponentRating + dashboard.pvpStage2Widget.opponentUserRatingDeltaArray[(outcome) + 1]

    else:
        dashboard.pvpStage3Widget.currentRating = dashboard.pvpStage2Widget.userRating + dashboard.pvpStage2Widget.currentUserRatingDeltaArray[(outcome) + 1]
        dashboard.pvpStage3Widget.opponentRating = dashboard.pvpStage2Widget.opponentRating + dashboard.pvpStage2Widget.opponentUserRatingDeltaArray[(outcome * -1) + 1]

    dashboard.pvpStage3Widget.currentUserRatingChange.setText(str(dashboard.pvpStage2Widget.userRating) + " -> " + str(dashboard.pvpStage3Widget.currentRating))
    dashboard.pvpStage3Widget.opponentUserRatingChange.setText(str(dashboard.pvpStage2Widget.opponentRating) + " -> " + str(dashboard.pvpStage3Widget.opponentRating))

    dashboard.pvpStage3Widget.moveset.setText(dashboard.chessBoard.pgn)

    finaliseMatch(dashboard, dashboard.chessBoard.currentMatchId, outcome, dashboard.chessBoard.pgn)

    dashboard.utilityStackedWidget.setCurrentIndex(2)



def goToStage1(dashboard):
    dashboard.playWidget.populate(dashboard.pvpStage2Widget.userId)

    dashboard.chessBoard.resetUi()

    dashboard.playWidget.refreshRadioButtons()

    dashboard.utilityStackedWidget.setCurrentIndex(0)



def createMatch(whiteId, blackId):
    record = {"whitePlayer": whiteId,
              "blackPlayer": blackId,
              "winner": "",
              "pgn": "",
              "finished": False}
    
    matchId = insert("matches", record)

    return matchId



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





def finaliseMatchOnExit(dashboard):
    if dashboard.utilityStackedWidget.currentIndex() == 1:
        matchId = dashboard.chessBoard.currentMatchId

        query = {"id": matchId}

        match = getData("matches", **query)

        match = match[0]

        match["pgn"] = dashboard.chessBoard.pgn

        match["winner"] = "Unfinished match"

        update("matches", match, matchId)

    