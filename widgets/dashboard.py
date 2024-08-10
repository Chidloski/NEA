from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.centralWidgets.chessBoard import Ui_chessBoard
from widgets.centralWidgets.puzzleChessBoard import Ui_puzzleChessBoard
from widgets.centralWidgets.proChessBoard import Ui_proChessBoard
from widgets.centralWidgets.infoBoard import Ui_infoBoard
from widgets.utilityWidgets.pvpWidgets.playStage1 import Ui_PlayStage1
from widgets.utilityWidgets.pvpWidgets.pvpStage2 import Ui_PvpStage2
from widgets.utilityWidgets.pvpWidgets.pvpStage3 import Ui_PvpStage3
from widgets.menuWidgets.menu import Ui_Menu
from widgets.utilityWidgets.puzzleWidgets.puzzleWidget import Ui_PuzzleWidget
from widgets.utilityWidgets.puzzleWidgets.dailyStage2 import Ui_dailyStage2
from widgets.utilityWidgets.puzzleWidgets.dailyStage3 import Ui_dailyStage3
from widgets.utilityWidgets.proWidgets.proWidget import Ui_proWidget
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

        self.menuStackedWidget = QtWidgets.QStackedWidget(self)
        self.menuStackedWidget.setGeometry(QtCore.QRect(20, 20, 130, 560))
        self.menuStackedWidget.setObjectName("menuStackedWidget")

        self.menu = Ui_Menu()
        self.menu.setupUi(self)

        self.menuStackedWidget.addWidget(self.menu)

        # declares a widget stack which currently holds only the chess board
        # in future may hold the tournament design
        self.centralStackedWidget = QtWidgets.QStackedWidget(self)
        self.centralStackedWidget.setGeometry(QtCore.QRect(170, 20, 560, 560))
        self.centralStackedWidget.setObjectName("stackedWidget")

        # assigns chessBoard the class of chess board from the python ui file
        self.chessBoard = Ui_chessBoard()
        self.puzzleChessBoard = Ui_puzzleChessBoard()
        
        self.proCentralStackedWidget = QtWidgets.QStackedWidget(self)
        self.proCentralStackedWidget.setGeometry(QtCore.QRect(170, 20, 560, 560))
        self.proCentralStackedWidget.setObjectName("proCentralStackedWidget")

        self.proWidget = Ui_proWidget()
        self.proWidget.setupUi(self)

        self.infoBoard = Ui_infoBoard()
        self.proChessBoard = Ui_proChessBoard()

        self.infoBoard.setupUi(self)
        self.proChessBoard.setupUi(self)

        self.proCentralStackedWidget.addWidget(self.infoBoard)
        self.proCentralStackedWidget.addWidget(self.proChessBoard)

        # populates the class
        self.chessBoard.setupUi(self)
        self.puzzleChessBoard.setupUi(self)

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
        self.puzzleChessBoard.setStyleSheet(styleSheet)
        self.proChessBoard.setStyleSheet(styleSheet)

        # adds the chess board to the widget stack
        self.centralStackedWidget.addWidget(self.chessBoard)
        self.centralStackedWidget.addWidget(self.puzzleChessBoard)
        self.centralStackedWidget.addWidget(self.proCentralStackedWidget)


        # declares a widget stack which currently holds only the chess board
        # in future may hold the tournament design
        self.utilityStackedWidget = QtWidgets.QStackedWidget(self)
        self.utilityStackedWidget.setGeometry(QtCore.QRect(750, 20, 230, 560))
        self.utilityStackedWidget.setObjectName("utilityStackedWidget")


        self.pvpStackedWidget = QtWidgets.QStackedWidget(self)
        self.pvpStackedWidget.setGeometry(QtCore.QRect(750, 20, 230, 560))
        self.pvpStackedWidget.setObjectName("pvpStackedWidget")

        self.playWidget = Ui_PlayStage1()
        self.pvpStage2Widget = Ui_PvpStage2()
        self.pvpStage3Widget = Ui_PvpStage3()
        
        self.playWidget.setupUi(self, baseWindow)
        self.pvpStage2Widget.setupUi(self, baseWindow)
        self.pvpStage3Widget.setupUi(self, baseWindow)

        self.pvpStackedWidget.addWidget(self.playWidget)
        self.pvpStackedWidget.addWidget(self.pvpStage2Widget)
        self.pvpStackedWidget.addWidget(self.pvpStage3Widget)


        self.puzzleStackedWidget = QtWidgets.QStackedWidget(self)
        self.puzzleStackedWidget.setGeometry(QtCore.QRect(750, 20, 230, 560))
        self.puzzleStackedWidget.setObjectName("puzzleStackedWidget")

        self.puzzleWidget = Ui_PuzzleWidget()
        self.dailyStage2Widget = Ui_dailyStage2()
        self.dailyStage3Widget = Ui_dailyStage3()

        self.puzzleWidget.setupUi(self)
        self.dailyStage2Widget.setupUi(self)
        self.dailyStage3Widget.setupUi(self)


        self.proStackedWidget = QtWidgets.QStackedWidget(self)
        self.proStackedWidget.setGeometry(QtCore.QRect(750, 20, 230, 560))
        self.proStackedWidget.setObjectName("proStackedWidget")

        self.proStackedWidget.addWidget(self.proWidget)

        self.puzzleStackedWidget.addWidget(self.puzzleWidget)
        self.puzzleStackedWidget.addWidget(self.dailyStage2Widget)
        self.puzzleStackedWidget.addWidget(self.dailyStage3Widget)
        
        self.utilityStackedWidget.addWidget(self.pvpStackedWidget)
        self.utilityStackedWidget.addWidget(self.puzzleStackedWidget)
        self.utilityStackedWidget.addWidget(self.proStackedWidget)

        QtCore.QMetaObject.connectSlotsByName(self)

        atexit.register(self.onExit)

    def onExit(self):
        finaliseMatchOnExit(self)


