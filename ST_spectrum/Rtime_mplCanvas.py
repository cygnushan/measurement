# -*- coding: utf-8 -*-

from PyQt4 import  QtGui
from matplotlib.backends.backend_qt4agg import  FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from pylab import * 

mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体  
  
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题   

import qmdz_const
 
class Rt_Canvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure(figsize=(6,4), dpi=80,facecolor="white")
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.ax.set_title(u"R-t谱")
        self.ax.set_xlabel(u"时间(S)",labelpad=0)
        self.ax.set_ylabel(u"电阻(Ω)",labelpad=0)
        self.curveObj = None 
        
    def setxy(self,xmin,xmax,ymin,ymax):
        self.ax.set_xlim(xmin,xmax)
        self.ax.set_ylim(ymin,ymax)
        self.draw()
    
    def set_ylog(self, islog, ytype):
        if islog:
            self.ax.set_ylabel(u"电阻(logR)",labelpad=0)       
        self.draw()

    def plot(self, datax, datay, log, style, label, type):
        if type == 1:
            if log:
                self.curveObj,= self.ax.semilogy(datax,datay,style,label=label)
            else:
                self.curveObj,= self.ax.plot(datax,datay,style,label=label)
            self.ax.legend(loc=1,fontsize='x-small')
        else:
            self.curveObj.set_data(datax,datay)
        self.ax.relim()
        self.ax.autoscale_view(True,True,True)
        self.draw()

    def save_pic(self, path):
        self.fig.savefig(path)
        
    def clear_lines(self):
        from weakref import ref
        # wr = ref(ax.lines[0])
        # ax.lines.remove(wr())
        axline = []
        if self.ax.legend_:
            self.ax.legend_.remove()
        for i, line in enumerate(self.ax.lines):
            # print i,line
            # self.ax.lines.pop(i)
            # del line
            axline.append(ref(self.ax.lines[i]))
            
        for line in axline:
            self.ax.lines.remove(line())
        self.draw()
       
class  Rt_CanvasWidget(QtGui.QWidget):
   
    def __init__(self , parent =None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = Rt_Canvas()
        self.vbl = QtGui.QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
        self.dataX= []
        self.dataY= []
       
    def generateData(self,x,y,log, style='b', label='RT', type=0):
        try:
            self.canvas.plot(x,y,log, style,label,type) 
        except Exception,e:
            print e
            print "x:",x,len(x)
            print "y:",y,len(y)
        
    def change_xy(self, xmin, xmax, ymin, ymax):
        self.canvas.setxy(xmin, xmax, ymin, ymax) 
        
    def set_log(self, islog, ylabe):
        self.canvas.set_ylog(islog, ylabe)
        
    def save_curve(self, path):
        self.canvas.save_pic(path)
        
    def clear_curve(self):
        self.canvas.clear_lines()
        
# ax.semilogx(x,y) #x轴为对数坐标轴
# 
# ax.semilogy(x,y) #y轴为对数坐标轴
# 
# ax.loglog(x,y) #双对数坐标轴
        
        