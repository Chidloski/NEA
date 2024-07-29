from PyQt5.QtGui import QPixmap
from widgets.utilityWidgets.functions.playFunctions import goToStage3

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

            goToStage3(dashboard, -1)

        else:
            domain.pgn = domain.pgn + " 1-0"

            domain.gameOverLabel.setText(domain.whitePlayer + " wins!")

            goToStage3(dashboard, 1)

    else:
        domain.gameOverLabel.setText("It's a draw!")

        goToStage3(dashboard, 0)

    domain.gameOverLabel.setHidden(False)
    domain.playAgainButton.setHidden(False)



def onClickRejectOffer(domain):
    domain.offerLabel.setHidden(True)
    domain.acceptOfferButton.setHidden(True)
    domain.rejectOfferButton.setHidden(True)
    domain.coverScreen.setHidden(True)

        


