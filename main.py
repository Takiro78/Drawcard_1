from PyQt5.QtWidgets import QWidget,QVBoxLayout,QApplication,QStackedWidget
import sys,os
from screens.home import HomeScreen
from screens.loader import deckLoader
from screens.create import createDeck
from screens.deckStudy import study


class MainWindow(QWidget):
    def __init__(self):
        #super constructor
        super().__init__()

        #make full screen
        

        #stack containing all windows
        self.windowStack =QStackedWidget()

        #instantiate windows
        self.home = HomeScreen(self.windowStack)
        self.loadDeck = deckLoader(self.windowStack)
        self.createDeck = createDeck(self.windowStack)
        self.studyDeck = study(self.windowStack)


        #add windows to stack
        self.windowStack.addWidget(self.home)
        self.windowStack.addWidget(self.loadDeck)
        self.windowStack.addWidget(self.createDeck)
        self.windowStack.addWidget(self.studyDeck)


        #layout containter
        layout = QVBoxLayout()

        #add stack to layout container
        layout.addWidget(self.windowStack)

        #set current layout
        self.setLayout(layout)

        #set which window to display
        self.windowStack.setCurrentWidget(self.home)



def run():
    app = QApplication(sys.argv)
    window = MainWindow()

    #show window
    
    
    window.showMaximized()

    #closes app after it executes
    sys.exit(app.exec_())



#always runs - main code
if __name__ =="__main__":
    run()



