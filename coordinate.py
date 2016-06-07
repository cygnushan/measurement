# -*- coding: utf-8 -*-

"""
Module implementing SetCoordinate.
"""
import sys
from PyQt4 import QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_coordinate import Ui_UI_Coordinate

import qmdz_const
from init_op import read_config,write_config

class SetCoordinate(QDialog, Ui_UI_Coordinate):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        self.auto_range = 0
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.get_coord_conf()
    
    @pyqtSignature("bool")
    def on_auto_fit_toggled(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if checked:
            self.auto_range = 1
            self.x_min.setEnabled(False)
            self.x_max.setEnabled(False)
            self.y_min.setEnabled(False)
            self.y_max.setEnabled(False)
        else:
            self.auto_range = 0
            self.x_min.setEnabled(True)
            self.x_max.setEnabled(True)
            self.y_min.setEnabled(True)
            self.y_max.setEnabled(True)           
    
    @pyqtSignature("")
    def on_xyset_ok_clicked(self):
        """
        Slot documentation goes here.
        """
        set_value('auto_range',self.auto_range)
        set_value('x_min',self.x_min.text())
        set_value('x_max',self.x_max.text())
        set_value('y_min',self.y_min.text())
        set_value('y_max',self.y_max.text())
        qmdz_const.Auto_Range = self.auto_range
        
    def get_coord_conf(self):
        if get_value('auto_range') == '1':
            self.auto_fit.setChecked(1)
        else:
            self.auto_fit.setChecked(0)
        self.x_min.setText(str(get_value('x_min')))
        self.x_max.setText(str(get_value('x_max')))
        self.y_min.setText(str(get_value('y_min')))
        self.y_max.setText(str(get_value('y_max')))

def get_value(key):
    key_value = read_config(qmdz_const.SYS_CONF_PATH, 'COORD', key)
    return key_value
    
def set_value(key,value):
    write_config(qmdz_const.SYS_CONF_PATH, 'COORD', key, value)
    return value    

def disp_coord():
    UI_xy = SetCoordinate()
    UI_xy.show()
    UI_xy.exec_()
    return True

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    SET_CORD = SetCoordinate()
    SET_CORD.show()
    sys.exit(app.exec_())