from playerDB.jsonFunctions import *
from PyQt5.QtGui import QPixmap

def populateForPlayer(dashboard, name):
    if not hasattr(dashboard.proWidget, "pro") or dashboard.proWidget.pro["id"] != name:

        goToInfo(dashboard)

        dashboard.proWidget.pro = getData("professionals", id = name)

        dashboard.proWidget.pro = dashboard.proWidget.pro[0]

        dashboard.infoBoard.proNameLabel.setText(name)

        dashboard.infoBoard.photos = [f"{dashboard.proWidget.pro['photoRoute']}1.png", f"{dashboard.proWidget.pro['photoRoute']}2.png", f"{dashboard.proWidget.pro['photoRoute']}3.png"]
        dashboard.infoBoard.photoIndex = 0
        dashboard.infoBoard.imageLabel.setPixmap(QPixmap(dashboard.infoBoard.photos[dashboard.infoBoard.photoIndex]))

        dashboard.infoBoard.peakRatingLabel.setText(f"• Peak Rating: {dashboard.proWidget.pro['peakRating']}")
        dashboard.infoBoard.titleLabel.setText(f"• Title: {dashboard.proWidget.pro['title']}")
        dashboard.infoBoard.birthLabel.setText(f"• Born: {dashboard.proWidget.pro['birth']}")
        dashboard.infoBoard.genderLabel.setText(f"• Gender: {dashboard.proWidget.pro['gender']}")
        dashboard.infoBoard.nationalityLabel.setText(f"• Nationality: {dashboard.proWidget.pro['nationality']}")

        dashboard.infoBoard.major1Label.setText(f"• {dashboard.proWidget.pro['major1']}")
        dashboard.infoBoard.major2Label.setText(f"• {dashboard.proWidget.pro['major2']}")
        dashboard.infoBoard.major3Label.setText(f"• {dashboard.proWidget.pro['major3']}")

        dashboard.infoBoard.descriptionLabel.setText(dashboard.proWidget.pro["description"])

def switchPhoto(widget, direction):
    widget.photoIndex = (widget.photoIndex + direction) % 3

    widget.imageLabel.setPixmap(QPixmap(widget.photos[widget.photoIndex]))

def populateForMatch(dashboard, matchId):
    dashboard.proChessBoard.resetUi()
    dashboard.proChessBoard.coverScreen.setHidden(False)
    dashboard.proCentralStackedWidget.setCurrentIndex(1)

    match = getData("proMatches", id = dashboard.proWidget.pro[f"match{str(matchId)}"])
    match = match[0]

    dashboard.proWidget.currentMatch = match

    dashboard.proWidget.matchLabel.setText(f"Match {str(matchId)}")
    dashboard.proWidget.yearLabel.setText(match["year_location"])
    dashboard.proWidget.tournamentLabel.setText(match["tournament"])
    dashboard.proWidget.matchupLabel.setText(match["versus"])
    dashboard.proWidget.outcomeLabel.setText(match["outcome"])
    dashboard.proWidget.matchDescriptionLabel.setText(match["description"])

    dashboard.proWidget.pgn = match["pgn"]

    dashboard.proWidget.matchLabel.setHidden(False)
    dashboard.proWidget.yearLabel.setHidden(False)
    dashboard.proWidget.tournamentLabel.setHidden(False)
    dashboard.proWidget.matchupLabel.setHidden(False)
    dashboard.proWidget.outcomeLabel.setHidden(False)
    dashboard.proWidget.matchDescriptionLabel.setHidden(False)
    dashboard.proWidget.fullBackButton.setHidden(False)
    dashboard.proWidget.backButton.setHidden(False)
    dashboard.proWidget.fullForwardButton.setHidden(False)
    dashboard.proWidget.forwardButton.setHidden(False)

    dashboard.proWidget.moveIndex = 0

def forwardMove(dashboard):
    dashboard.proChessBoard.runPgnTurn(dashboard.proChessBoard.moveNumber, dashboard.proWidget.pgn, dashboard.proWidget.moveIndex)

    dashboard.proWidget.moveIndex += 1

def backwardMove(dashboard):
    if dashboard.proWidget.moveIndex > 0:

        dashboard.proChessBoard.resetUi()

        pgn = dashboard.proWidget.pgn[:dashboard.proWidget.moveIndex]

        dashboard.proWidget.moveIndex -= 1

        dashboard.proChessBoard.runPgn(pgn)

def fullBackMove(dashboard):
    dashboard.proChessBoard.resetUi()
    dashboard.proWidget.moveIndex = 0

def fullForwardMove(dashboard):
    dashboard.proChessBoard.resetUi()

    dashboard.proChessBoard.runPgn(dashboard.proWidget.pgn)

    dashboard.proWidget.moveIndex = dashboard.proChessBoard.moveNumber

def goToInfo(dashboard):
    dashboard.proCentralStackedWidget.setCurrentIndex(0)

    dashboard.proWidget.matchLabel.setHidden(True)
    dashboard.proWidget.yearLabel.setHidden(True)
    dashboard.proWidget.tournamentLabel.setHidden(True)
    dashboard.proWidget.matchupLabel.setHidden(True)
    dashboard.proWidget.outcomeLabel.setHidden(True)
    dashboard.proWidget.matchDescriptionLabel.setHidden(True)
    dashboard.proWidget.fullBackButton.setHidden(True)
    dashboard.proWidget.backButton.setHidden(True)
    dashboard.proWidget.fullForwardButton.setHidden(True)
    dashboard.proWidget.forwardButton.setHidden(True)





