from PyQt5.QtWidgets import QWidget,QLabel,QVBoxLayout,QPushButton,QStackedWidget
from screens.pageParent import page

class HomeScreen(page):
    def __init__(self,stack):
        super().__init__(stack)
        
        
        label = QLabel("DrawCard",self)
        self.layout.addWidget(label)

        create_btn = QPushButton("create new deck")
        create_btn.clicked.connect(lambda: self.goToIndex(2))
        self.layout.addWidget(create_btn)

        load_btn = QPushButton("load Deck")
        load_btn.clicked.connect(lambda :self.goToIndex(1))

        self.layout.addWidget(load_btn)

    

