from PyQt5 import QtCore, QtGui, QtWidgets
from dashboardWidgets.chessBoard import Ui_chessBoard

# welcome page will house a widget stack containing:
#   - Puzzles
#   - Free Play
#   - Tournaments
# and a second widget containing buttons to scroll through these widgets

class Ui_Dashboard(QtWidgets.QWidget):
    
    def setupUi(self):

        self.setObjectName("WelcomePage")
        self.resize(1000, 600)

        # declares a widget stack which currently holds only the chess board
        # in future may hold the tournament design
        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.stackedWidget.setGeometry(QtCore.QRect(170, 20, 560, 560))
        self.stackedWidget.setObjectName("stackedWidget")

        # assigns chessBoard the class of chess board from the python ui file
        chessBoard = Ui_chessBoard()

        # populates the class
        chessBoard.setupUi()

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
        chessBoard.setStyleSheet(styleSheet)

        # adds the chess board to the widget stack
        self.stackedWidget.addWidget(chessBoard)

        QtCore.QMetaObject.connectSlotsByName(self)


