def goToAccount(dashboard):
    dashboard.centralStackedWidget.setCurrentIndex(4)
    dashboard.utilityStackedWidget.setCurrentIndex(3)
    dashboard.accountUtilityWidget.resetUi()
    dashboard.accountUtilityWidget.populate(dashboard.baseWindow.userId)

def goToPuzzles(dashboard):
    dashboard.centralStackedWidget.setCurrentIndex(1)
    dashboard.utilityStackedWidget.setCurrentIndex(1)

def goToPlay(dashboard):
    dashboard.centralStackedWidget.setCurrentIndex(0)
    dashboard.utilityStackedWidget.setCurrentIndex(0)

def goToPros(dashboard):
    dashboard.centralStackedWidget.setCurrentIndex(2)
    dashboard.utilityStackedWidget.setCurrentIndex(2)