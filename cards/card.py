from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton,QFileDialog
from PyQt5.QtGui import QPen,QPixmap,QPainter
from PyQt5.QtCore import QSize,Qt,QPoint
import os 

class cardEditor(QWidget):
    def __init__(self):
        super().__init__()

        #self.a=QLabel("hello")
        #self.b = QLabel("world")

        self.front_canvas=canvasWidget()
        self.back_canvas = canvasWidget()

        self.delete_btn = QPushButton("X")
        self.delete_btn.clicked.connect(self.deleteSelf)

        

        layout=QVBoxLayout()
        #layout.addWidget(self.a)
        #layout.addWidget(self.b)

        layout.addWidget(self.delete_btn)
        layout.addWidget(self.front_canvas)
        layout.addWidget(self.back_canvas)

       
        self.setLayout(layout)

    def deleteSelf(self):
        parent = self.parentWidget()
        #print(parent)
        layout =parent.layout
        #print(layout)
        if layout.count() >6:
            layout.removeWidget(self)
            self.setParent(None)
            self.deleteLater()

    def saveSelf(self,folder,index):
    
        self.front_canvas.canvas.save(str(folder)+"/"+str(index)+"front"+".png","PNG")
        self.back_canvas.canvas.save(str(folder)+"/"+str(index)+"back"+".png","PNG")

        

    

class canvasWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.canvas = QPixmap(QSize(200,200))
        self.canvas.fill(Qt.white)

        self.last_point = QPoint()
        self.drawing = False

    def paintEvent(self, a0):
        painter = QPainter(self)
        painter.drawPixmap(0,0,self.canvas)

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.drawing = True
            self.last_point = event.pos()

    def mouseMoveEvent(self,event):
        if self.drawing:
            current_point = event.pos()
            painter = QPainter(self.canvas)
            pen = QPen(Qt.black,2,Qt.SolidLine)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setPen(pen)
            painter.drawLine(self.last_point,current_point)
            self.last_point = current_point
            self.update()


    def mouseReleaseEvent(self,event):
        self.drawing = False


