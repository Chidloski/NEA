from PyQt5.QtGui import QPixmap
from widgets.utilityWidgets.functions.playFunctions import goToStage3
from widgets.utilityWidgets.functions.tournamentFunctions import goBackToTournamentStage3

def onClickAcceptOffer(dashboard, domain):
    domain.offerLabel.setHidden(True)
    domain.acceptOfferButton.setHidden(True)
    domain.rejectOfferButton.setHidden(True)

    # handles when offer is checking whether player wants to resign
    if domain.offerLabel.text() == "Are you sure?":
        # finalises pgn with resign terminology
        if domain.moveNumber / 2 == int(domain.moveNumber / 2):
            domain.pgn = domain.pgn + " 0-1"

            domain.gameOverLabel.setText(domain.blackPlayer + " wins!")

            if domain.objectName() == "chessBoard":
                goToStage3(dashboard, -1)

            else:
                goBackToTournamentStage3(dashboard, -1)

        else:
            domain.pgn = domain.pgn + " 1-0"

            domain.gameOverLabel.setText(domain.whitePlayer + " wins!")

            if domain.objectName() == "chessBoard":
                goToStage3(dashboard, 1)

            else:
                goBackToTournamentStage3(dashboard, 1)

    else:
        if domain.objectName() == "chessBoard":
            domain.gameOverLabel.setText("It's a draw!")

            goToStage3(dashboard, 0)

        else:
            if dashboard.tournamentStage3Widget.tournamentType == "Knockout":
                domain.drawMessage.setHidden(False)

            domain.gameOverLabel.setText("It's a draw!")

            goBackToTournamentStage3(dashboard, 0)

    domain.gameOverLabel.setHidden(False)
    domain.playAgainButton.setHidden(False)



def onClickRejectOffer(domain):
    domain.offerLabel.setHidden(True)
    domain.acceptOfferButton.setHidden(True)
    domain.rejectOfferButton.setHidden(True)
    domain.coverScreen.setHidden(True)

        


