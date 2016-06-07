# -*- coding: utf-8 -*-

"""
Module implementing UI_SC2400.
"""
# import sys,os
# from PyQt4 import QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_SC_2400 import Ui_UI_sens2400
from init_op import read_config,write_config
import qmdz_const

from INST.INST2400 import Keithley2400

class UI_SC2400(QDialog, Ui_UI_sens2400):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.get_2400_conf()
     
    @pyqtSignature("")    
    def on_res_detect_clicked(self):
        R_range = qmdz_const.res_range[self.res_range.currentIndex()]
        print "detect res range:", R_range
        self.voltage,self.current,self.resistance = Keithley2400.measure_ohms_auto(R_range,qmdz_const.MEAS_MODE)
        self.detV.setText(str(self.voltage))
        self.detI.setText(str(self.current))
        self.detR.setText(str(self.resistance))


    @pyqtSignature("bool")
    def on_VI_mode_toggled(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if checked:
            set_value('vi_mode','1')
        else:
            set_value('vi_mode','0')
            
    @pyqtSignature("")
    def on_SC2400_save_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        set_value('meas_mode', self.mode2or4.currentIndex())
        set_value('out_mode', self.output_mode.currentIndex())
        set_value('iv_voltage', self.VI_voltage.text())
        set_value('iv_unit', self.voltage_unit.currentIndex())
        set_value('iv_range', self.VI_current_range.currentIndex())
        set_value('vi_current', self.IV_current.text())
        set_value('vi_unit', self.current_unit.currentIndex())
        set_value('vi_range', self.IV_voltage_range.currentIndex())
    
    def get_2400_conf(self): 
        self.mode2or4.setCurrentIndex(int(get_value('meas_mode')))
        self.output_mode.setCurrentIndex(int(get_value('out_mode')))
        if get_value('vi_mode')=='1':
            self.VI_mode.setChecked(True)
        else:
            self.IV_mode.setChecked(True)
        self.VI_voltage.setText(get_value('iv_voltage'))
        self.IV_current.setText(get_value('vi_current'))
        self.voltage_unit.setCurrentIndex(int(get_value('iv_unit')))
        self.current_unit.setCurrentIndex(int(get_value('vi_unit')))
        self.VI_current_range.setCurrentIndex(int(get_value('iv_range')))
        self.IV_voltage_range.setCurrentIndex(int(get_value('vi_range')))
    
def get_value(key):
    key_value = read_config(qmdz_const.SC_CONF_PATH, 'INST', key)
    return key_value
    
def set_value(key,value):
    write_config(qmdz_const.SC_CONF_PATH, 'INST', key, value)
    return value


def dispSC_2400():
    UI_2400 = UI_SC2400()
    UI_2400.show()
    UI_2400.exec_()
    return True

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     UI_ST2400 = UI_ST2400()
#     UI_ST2400.show()
#     sys.exit(app.exec_())   