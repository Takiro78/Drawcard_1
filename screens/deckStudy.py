from PyQt5.QtWidgets import QWidget,QPushButton,QVBoxLayout,QLabel
from PyQt5.QtGui import QPixmap
from screens.pageParent import page
import json

class study(page):
    def __init__(self,stack):
        super().__init__(stack)


        self.current_card_index=0
        
        self.card_side = "front"
        self.previous_card_index = -1
        self.card_count = 1
        self.deck_title=""

        next_btn = QPushButton("Next")
        prev_btn = QPushButton("Previous")
        flip_btn = QPushButton("Flip")
        back_btn = QPushButton("Back")

        back_btn.clicked.connect(lambda: self.goToIndex(1))

        flip_btn.clicked.connect(lambda:self.flip())

        self.current_card=QLabel()


        #add buttons to layout
        self.layout.addWidget(self.current_card)
        self.layout.addWidget(next_btn)
        self.layout.addWidget(prev_btn)
        self.layout.addWidget(flip_btn)
        self.layout.addWidget(back_btn)
        

    def flip(self):
        print(self.card_side)
        if self.card_side =="front":
            self.card_side ="back"
        elif self.card_side =="back":
            self.card_side = "front"

        self.change_card(self.current_card_index)

    def change_card(self,index):
        path =f"decks/{self.deck_title}/{index}{self.card_side}.png"
        print(path)
        pixmap = QPixmap(path)
        self.current_card.setPixmap(pixmap)
        self.current_card.resize(pixmap.width(),pixmap.height())
        #self.current_card.resize(300,300)


        


    def update_deck(self,title):
        flag=False
        with open("decks/decks.json") as f:

            data=json.load(f)

        for key in data:
            if key == title:
                self.card_count=data.get(title)
                flag=True
                break;

        if flag:
            self.deck_title = title
            self.change_card(self.current_card_index)
            
        return flag




        

