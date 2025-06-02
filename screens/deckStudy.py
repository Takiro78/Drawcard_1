from PyQt5.QtWidgets import QWidget,QPushButton,QVBoxLayout,QLabel
from PyQt5.QtGui import QPixmap
from screens.pageParent import page
import random
import json

class study(page):
    def __init__(self,stack):
        super().__init__(stack)


        self.current_card_index=0
        
        self.card_side = "front"
        self.previous_card_stack = []
        self.card_count = 1
        self.deck_title=""

        next_btn = QPushButton("Next")
        prev_btn = QPushButton("Previous")
        flip_btn = QPushButton("Flip")
        back_btn = QPushButton("Back")

        back_btn.clicked.connect(lambda: self.goToIndex(1))

        flip_btn.clicked.connect(lambda:self.flip())

        next_btn.clicked.connect(lambda: self.next_card())

        prev_btn.clicked.connect(lambda:self.prev_card())

        self.current_card=QLabel()


        #add buttons to layout
        self.layout.addWidget(self.current_card)
        self.layout.addWidget(next_btn)
        self.layout.addWidget(prev_btn)
        self.layout.addWidget(flip_btn)
        self.layout.addWidget(back_btn)
        

    def next_card(self):
        print("a")
        self.previous_card_stack.append(self.current_card_index)
        print("b")

        self.current_card_index = random.randrange(0,self.card_count)

        while self.previous_card_stack[-1] == self.current_card_index:

            print("c")
            self.current_card_index = random.randrange(0,self.card_count)
            print(self.current_card_index)

        self.card_side="front"
        self. change_card()  

    def prev_card(self):
        if len(self.previous_card_stack)!=0:
            self.current_card_index=self.previous_card_stack.pop()
            
            self.card_side="front"

            self.change_card()
         

    def flip(self):
        print(self.card_side)
        if self.card_side =="front":
            self.card_side ="back"
        elif self.card_side =="back":
            self.card_side = "front"

        self.change_card(self.current_card_index)

    def change_card(self,index=None,side= None):
        if index == None:
            index = self.current_card_index
        if side is None:
            side = self.card_side
        path =f"decks/{self.deck_title}/{index}{side}.png"
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
            self.change_card()
            
        return flag




        

