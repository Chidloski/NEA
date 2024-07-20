from PyQt5 import QtCore, QtGui, QtWidgets
from BaseWindow import groupingWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    # ui is the variable with class UI_MainWindow and thus when editing attributes ui must be called
    ui = groupingWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    sys.exit(app.exec_())