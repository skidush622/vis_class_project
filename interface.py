import sys
from graphlet import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from utilities import draw_layout
from layout import draw
import sip

test_matrix = []

class App(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'Final Project'
        self.width = 1140
        self.height = 500
        self.initUI()
    
    def initUI(self):
        global test_matrix
        test_matrix = create_matrix(100, 100)
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.m1 = PlotCanvas(self, width=5, height=5, id=1)
        self.m1.move(0,0)
        
        button = QPushButton('Rerun', self)
        button.move(500,0)
        button.resize(140,100)
        button.clicked.connect(self.click_on)
        
        self.m2 = PlotCanvas(self, width=5, height=5, id=2)
        self.m2.move(640,0)
        
        self.show()

    def click_on(self):
        self.m1.hide()
        self.m2.hide()
        global test_matrix
        test_matrix = create_matrix(100, 100)
        m3 = PlotCanvas(self, width=5, height=5, id=1)
        m3.move(0,0)
        m4 = PlotCanvas(self, width=5, height=5, id=2)
        m4.move(640,0)
        self.m1 = m3
        self.m2 = m4
        self.m1.show()
        self.m2.show()

class PlotCanvas(FigureCanvas):
    
    def __init__(self, parent=None, width=5, height=5, dpi=100, id=1):
        self.id = id
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.update_figure()
    
    def update_figure(self):
        if(self.id==1):
           self.axes.set_title('estimated_layout')
           draw_layout(self.axes, test_matrix)
        else:
           self.axes.set_title('real_layout')
           draw(test_matrix, 'real_layout', self.axes)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
