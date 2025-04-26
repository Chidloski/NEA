from widgets.utilityWidgets.functions.playFunctions import finaliseMatchOnExit
from widgets.utilityWidgets.functions.tournamentFunctions import finaliseMatchAndTournamentOnExit
from widgets.utilityWidgets.functions.proFunctions import populateForPlayer

# go to account widgets
def goToAccount(dashboard):
    dashboard.centralStackedWidget.setCurrentIndex(4)
    dashboard.utilityStackedWidget.setCurrentIndex(3)
    dashboard.accountUtilityWidget.resetUi()
    dashboard.accountUtilityWidget.populate(dashboard.baseWindow.userId)

# go to puzzle widgets
def goToPuzzles(dashboard):
    dashboard.centralStackedWidget.setCurrentIndex(1)
    dashboard.utilityStackedWidget.setCurrentIndex(1)

# go to play widgets
def goToPlay(dashboard):
    dashboard.centralStackedWidget.setCurrentIndex(0)
    dashboard.utilityStackedWidget.setCurrentIndex(0)

# go to pros widget
def goToPros(dashboard):
    dashboard.centralStackedWidget.setCurrentIndex(2)
    dashboard.utilityStackedWidget.setCurrentIndex(2)

# reset all necessary widgets so when a user logs back in there is no activity
def logOut(dashboard):
    dashboard.baseWindow.userId = -1

    finaliseMatchAndTournamentOnExit(dashboard)
    finaliseMatchOnExit(dashboard)

    dashboard.menu.logOut.setStyleSheet("color: rgb(255, 255, 255)")
    dashboard.menu.logOut.isClicked = False

    dashboard.menu.playSection.setStyleSheet("color: rgb(237, 119, 47)")
    dashboard.menu.playSection.isClicked = True

    dashboard.baseWindow.logInWidget.resetUi()
    dashboard.baseWindow.forgotPasswordWidget.resetUi()
    dashboard.baseWindow.registerWidget.resetUi()

    dashboard.baseWindow.stackedWidget.setCurrentIndex(0)

    dashboard.utilityStackedWidget.setCurrentIndex(0)
    dashboard.proStackedWidget.setCurrentIndex(0)
    dashboard.puzzleStackedWidget.setCurrentIndex(0)
    dashboard.pvpStackedWidget.setCurrentIndex(0)

    dashboard.chessBoard.resetUi()
    dashboard.proChessBoard.resetUi()
    dashboard.puzzleChessBoard.resetUi()
    dashboard.tournamentChessBoard.resetUi()

    dashboard.proWidget.pro1Label.simulateClick()
    dashboard.proWidget.infoLabel.simulateClick()

    dashboard.centralStackedWidget.setCurrentIndex(0)
    dashboard.proCentralStackedWidget.setCurrentIndex(0)