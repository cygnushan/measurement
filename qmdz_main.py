# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys,os
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature

from Ui_main import Ui_MainWindow
from VI_spectrum.VI_main import dispVI_Dialog
from ST_spectrum.ST_main import dispST_Dialog
from SC_spectrum.SC_main import dispSC_Dialog
from system_set import disp_sys_set

script_path = os.getcwd()
root_path = os.path.dirname(script_path)
sys.path.insert(0,root_path)

defaultEncoding = 'utf-8'
if sys.getdefaultencoding() != defaultEncoding:
    reload(sys)
    sys.setdefaultencoding(defaultEncoding)

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
    
#     @pyqtSignature("int")
#     def on_listWidget_currentRowChanged(self, currentRow):
#         """
#         Slot documentation goes here.
#         """
#         # TODO: not implemented yet
#         if (currentRow==3):
#             dispST_Dialog()
            
    @pyqtSignature("QModelIndex")
    def on_listWidget_clicked(self, index):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if (index.row()==0):
            dispVI_Dialog()
        elif (index.row()==1):            
            dispST_Dialog()
        elif (index.row()==2):
            dispSC_Dialog()
        elif (index.row()==3):
            disp_sys_set()
        
            

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    UIMain = MainWindow()
    UIMain.show()
    sys.exit(app.exec_())
