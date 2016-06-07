# -*- coding: utf-8 -*-

from PyQt4 import  QtGui
from matplotlib.backends.backend_qt4agg import  FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from pylab import * 

mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体  
  
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题   

import qmdz_const
 
class AT_Canvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure(figsize=(9,5), dpi=80,facecolor="white")
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.ax.set_title(u"温度-时间曲线")
        self.ax.set_xlabel(u"时间(S)",labelpad=0)
        self.ax.set_ylabel(u"温度(℃)",labelpad=0)
        self.curveObj = {} 
        
    def sety(self,ymin,ymax):
        # self.ax.set_xlim(xmin,xmax)
        self.ax.set_ylim(ymin,ymax)
        self.draw()

    def plot(self, datax, datay, style, label, type):
        if type == 1:
            self.curveObj[label],= self.ax.plot(datax,datay,style,label=label)
            self.ax.legend(loc=1,fontsize='large')
        else:
            self.curveObj[label].set_data(datax,datay)
        self.ax.autoscale_view(True,True,False)
        self.ax.relim()
        self.draw()

    def save_pic(self, path):
        self.fig.savefig(path)
        
    def clear_lines(self):
        for i, line in enumerate(self.ax.lines):
            print i,line
            self.ax.legend_.remove()
            self.ax.lines.pop(i)
            #line.remove()
        self.draw()
       
class  AT_CanvasWidget(QtGui.QWidget):
   
    def __init__(self , parent =None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = AT_Canvas()
        self.vbl = QtGui.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
        self.dataX= []
        self.dataY= []
       
    def generateData(self, x, y, label, style='b', type=0):
        self.canvas.plot(x,y,label,style,type)   
        
    def change_y(self, ymin, ymax):
        self.canvas.sety(ymin, ymax) 
        
    def set_log(self, islog, ylabe):
        self.canvas.set_ylog(islog, ylabe)
        
    def save_curve(self, path):
        self.canvas.save_pic(path)
        
    def clear_curve(self):
        self.canvas.clear_lines()
        
        