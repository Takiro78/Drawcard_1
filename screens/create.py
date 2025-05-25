from PyQt5.QtWidgets import QWidget, QVBoxLayout,QStackedWidget, QPushButton, QLabel,QLineEdit,QFileDialog
from screens import pageParent
from cards.card import cardEditor
from pathlib import Path
import json

class createDeck(pageParent.page):
    def __init__(self,stack):
        super().__init__(stack)

        #-------------enter name ---------#
        self.name_label = QLabel("Enter set name")
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Type here...")



        
        #back button
        self.back_btn = QPushButton("back")
        self.back_btn.clicked.connect(lambda: self.backIndex(0))

        #add cards button
        self.add_btn = QPushButton("add card")
        self.add_btn.clicked.connect(self.addCard)

        #save deck button
        self.save_btn = QPushButton("save deck")
        self.save_btn.clicked.connect(self.saveDeck)

        #add widgets to layout
        self.layout.addWidget(self.name_label)#0
        self.layout.addWidget(self.name_input)#1

        self.layout.addWidget(cardEditor())#2

        self.layout.addWidget(self.add_btn)#3
        self.layout.addWidget(self.save_btn)#4
        self.layout.addWidget(self.back_btn)#5



        

    def backIndex(self, index):
        self.resetPage()
        self.windowStack.setCurrentIndex(index)

    def resetPage(self):
        self.name_input.clear()

        self.addCard()

        while self.layout.count()>6:
            item = self.layout.itemAt(2).widget()
            if item:
                item.setParent(None)

        
        

    def addCard(self):
        card = cardEditor()
        self.layout.insertWidget(self.layout.count()-3,card)
        print(card.parentWidget())

    def saveDeck(self):
        deckName = self.name_input.text()
        if deckName.strip()  != "":
            folder_name = Path(deckName)
    

            base_path = Path("Drawcard_1/decks")
            full_path = base_path / folder_name
            if not full_path.exists():


                full_path.mkdir()

                count=self.layout.count()-5
                print(count)

                for i in range(2,count+2):
                    current_Widget = self.layout.itemAt(i).widget()
                    current_Widget.saveSelf(full_path,i-2)

                metaFile="Drawcard_1/decks/decks.json"

                with open(metaFile) as f:
                    data = json.load(f)

                load = self.windowStack.widget(1)
                load.add_deck(deckName,count)

                data[deckName] = count

                with open(metaFile,"w") as f:
                    json.dump(data, f, indent=4)



                self.backIndex(0)

            else:
                print("name already exits")
        else:
            print("deck must have a name")

