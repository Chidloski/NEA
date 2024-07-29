from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.centralWidgets.chessBoard import Ui_chessBoard
from widgets.utilityWidgets.playStage1 import Ui_PlayStage1
from widgets.utilityWidgets.pvpStage2 import Ui_PvpStage2
from widgets.utilityWidgets.pvpStage3 import Ui_PvpStage3
from widgets.utilityWidgets.functions.playFunctions import finaliseMatchOnExit
import atexit

# welcome page will house a widget stack containing:
#   - Puzzles
#   - Free Play
#   - Tournaments
# and a second widget containing buttons to scroll through these widgets

class Ui_Dashboard(QtWidgets.QWidget):
    
    def setupUi(self, baseWindow):

        self.baseWindow = baseWindow

        self.setObjectName("WelcomePage")
        self.resize(560, 560)

        # declares a widget stack which currently holds only the chess board
        # in future may hold the tournament design
        self.centralStackedWidget = QtWidgets.QStackedWidget(self)
        self.centralStackedWidget.setGeometry(QtCore.QRect(170, 20, 560, 560))
        self.centralStackedWidget.setObjectName("stackedWidget")

        # assigns chessBoard the class of chess board from the python ui file
        self.chessBoard = Ui_chessBoard()

        # populates the class
        self.chessBoard.setupUi(self)

        # sets a stylesheet in the same format as css for the board
        # previous colours (cream / green):
        # -> cream: rgb(235, 236, 211)
        # -> green: rgb(125, 148, 93)
        styleSheet = """
            lightSquare {
            background-color: rgb(184, 184, 184);
            color: rgb(133, 133, 133);
            }

            darkSquare {
            background-color: rgb(133, 133, 133);
            color: rgb(184, 184, 184);
            };"""
        
        # applies the stylesheet
        self.chessBoard.setStyleSheet(styleSheet)

        # adds the chess board to the widget stack
        self.centralStackedWidget.addWidget(self.chessBoard)


        # declares a widget stack which currently holds only the chess board
        # in future may hold the tournament design
        self.utilityStackedWidget = QtWidgets.QStackedWidget(self)
        self.utilityStackedWidget.setGeometry(QtCore.QRect(750, 20, 230, 560))
        self.utilityStackedWidget.setObjectName("stackedWidget")

        self.playWidget = Ui_PlayStage1()
        self.pvpStage2Widget = Ui_PvpStage2()
        self.pvpStage3Widget = Ui_PvpStage3()
        
        self.playWidget.setupUi(self, baseWindow)
        self.pvpStage2Widget.setupUi(self, baseWindow)
        self.pvpStage3Widget.setupUi(self, baseWindow)

        self.utilityStackedWidget.addWidget(self.playWidget)
        self.utilityStackedWidget.addWidget(self.pvpStage2Widget)
        self.utilityStackedWidget.addWidget(self.pvpStage3Widget)

        QtCore.QMetaObject.connectSlotsByName(self)

        atexit.register(self.onExit)

    def onExit(self):
        finaliseMatchOnExit(self)


