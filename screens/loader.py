from PyQt5.QtWidgets import QWidget, QVBoxLayout,QStackedWidget, QPushButton,QLabel

from screens import pageParent
from pathlib import Path
import json

class deckLoader(pageParent.page):
    def __init__(self,stack):
        super().__init__(stack)
        self.setStyleSheet("""
    #deckWidget {
        border: 3px dashed red;
        background-color: yellow;
    }
""")

        
        
        back_btn = QPushButton("back")
        back_btn.clicked.connect(lambda: self.goToIndex(0))

        with open("Drawcard_1/decks/decks.json") as f:
            data= json.load(f)
        
        for deckName,cardCount in data.items():
            self.layout.addWidget(deck(deckName,cardCount))
        

        self.layout.addWidget(back_btn)

        

        print(self.styleSheet())
        #self.setStyleSheet("* { border: 1px solid red; }")

    def loadDeck(self,title):
        self.windowStack.widget(3).update_deck(title)
        self.goToIndex(3)

    def add_deck(self,title,count):

        widget = deck(title,count)
        widget.setNew()
        self.layout.insertWidget(0,widget)
        



        



class deck(QWidget):
    def __init__(self, title, count):
        super().__init__()

        self.setObjectName("deckWidget")  # Must match the selector

        self.layout = QVBoxLayout()

        deckTitle = QLabel(title)

        cardCount = QLabel(f"Cards: {count}")

        edit_btn = QPushButton("Edit")

        del_btn = QPushButton("Delete")

        study_btn = QPushButton("Study")
        study_btn.clicked.connect(lambda: self.parent().loadDeck(title))
        

        self.layout.addWidget(deckTitle)
        self.layout.addWidget(cardCount)
        self.layout.addWidget(edit_btn)
        self.layout.addWidget(del_btn)
        self.layout.addWidget(study_btn)

        self.setLayout(self.layout)

    def setNew(self):
        label = QLabel("NEW")
        self.layout.insertWidget(0,label)
        

    
