import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from widgets.loginPage import Ui_LogInPage
from widgets.registerPage import Ui_RegisterPage
from widgets.forgotPasswordPage import Ui_ForgotPasswordPage
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
        logInWidget = Ui_LogInPage()
        registerWidget = Ui_RegisterPage()
        forgotPasswordWidget = Ui_ForgotPasswordPage()
        dashboardWidget = Ui_Dashboard()

        # passes in the object in order to allow the widgets to cycle between widget stack
        registerWidget.setupUi(self)
        forgotPasswordWidget.setupUi(self)
        logInWidget.setupUi(self, registerWidget, forgotPasswordWidget)
        dashboardWidget.setupUi(self)

        # adds the widgets to the stack
        self.stackedWidget.addWidget(logInWidget)
        self.stackedWidget.addWidget(registerWidget)
        self.stackedWidget.addWidget(forgotPasswordWidget)
        self.stackedWidget.addWidget(dashboardWidget)
        
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
        