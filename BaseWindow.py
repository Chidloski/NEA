import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from loginPage import Ui_LogInPage
from welcomePage import Ui_WelcomePage
from chessBoard import Ui_chessBoard

# base window houses two widgets
#   - login
#   - welcome page

class groupingWindow(object):
    def setupUi(self, MainWindow):
        
        # sizing of the widget
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setAutoFillBackground(False)

        # sets itself as the widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # defines the stacked widget
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.stackedWidget.setObjectName("stackedWidget")

        # sets logInWidget to class of login page and uses the setupUI function to populate itself
        logInWidget = Ui_LogInPage()
        logInWidget.setupUi(self)

        # adds the login widget to the stack
        self.stackedWidget.addWidget(logInWidget)

        # first assigns welcomewidget to the ui class for welcome page
        # then populates it using the setupUI function
        welcomeWidget = Ui_WelcomePage()
        welcomeWidget.setupUi()

        # adds the welcome page widget to the stack
        self.stackedWidget.addWidget(welcomeWidget)
        
        # sets itself as the widget
        MainWindow.setCentralWidget(self.centralwidget)
        
        # creates the top menu bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 24))
        self.menubar.setObjectName("menubar")

        self.menuChess = QtWidgets.QMenu(self.menubar)
        self.menuChess.setObjectName("menuChess")

        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuChess.menuAction())

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        