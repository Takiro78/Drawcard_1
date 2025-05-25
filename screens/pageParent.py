from PyQt5.QtWidgets import QWidget, QVBoxLayout,QStackedWidget

class page(QWidget):
    def __init__(self,stack):
        super().__init__()

        self.windowStack=stack

        self.layout=QVBoxLayout()
        self.setLayout(self.layout)
    
    def goToIndex(self,index):
        self.windowStack.setCurrentIndex(index)
        
