import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.userWidgets.loginPage import Ui_LogInPage
from widgets.userWidgets.registerPage import Ui_RegisterPage
from widgets.userWidgets.forgotPasswordPage import Ui_ForgotPasswordPage
from widgets.dashboard import Ui_Dashboard

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

        # sets widgets to class of respective page and uses the setupUI function to populate itself
        self.logInWidget = Ui_LogInPage()
        self.registerWidget = Ui_RegisterPage()
        self.forgotPasswordWidget = Ui_ForgotPasswordPage()
        self.dashboard = Ui_Dashboard()

        # passes in the object in order to allow the widgets to cycle between widget stack
        self.registerWidget.setupUi(self)
        self.forgotPasswordWidget.setupUi(self)
        self.logInWidget.setupUi(self, self.registerWidget, self.forgotPasswordWidget)
        self.dashboard.setupUi(self)

        # adds the widgets to the stack
        self.stackedWidget.addWidget(self.logInWidget)
        self.stackedWidget.addWidget(self.registerWidget)
        self.stackedWidget.addWidget(self.forgotPasswordWidget)
        self.stackedWidget.addWidget(self.dashboard)
        
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
        