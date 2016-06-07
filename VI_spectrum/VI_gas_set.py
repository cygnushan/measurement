# -*- coding: utf-8 -*-

"""
Module implementing UI_gas.
"""
from PyQt4 import QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_VI_gas_set import Ui_Dialog

import qmdz_const
from init_op import read_config,write_config
from qmdz_const import VI_CONF_PATH, SYS_CONF_PATH

class UI_gas(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        self.const = 0
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.get_gas_conf()

    @pyqtSignature("QString")
    def on_flow1_ratio_textEdited(self, text):
        flow_value = int(self.total_flow.text())*int(text)/100
        self.flow1_rate.setText(str(flow_value))

    @pyqtSignature("QString")
    def on_flow2_ratio_textEdited(self, text):
        flow_value = int(self.total_flow.text())*int(text)/100
        self.flow2_rate.setText(str(flow_value))

    @pyqtSignature("QString")
    def on_flow3_ratio_textEdited(self, text):
        flow_value = int(self.total_flow.text())*int(text)/100
        self.flow3_rate.setText(str(flow_value))
        
    @pyqtSignature("bool")
    def on_const_flow_toggled(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if checked:
            self.const = 1
            self.total_flow.setEnabled(True)
            self.flow1_ratio.setEnabled(True)
            self.flow2_ratio.setEnabled(True)
            self.flow3_ratio.setEnabled(True)
            self.flow1_rate.setEnabled(False)
            self.flow2_rate.setEnabled(False)
            self.flow3_rate.setEnabled(False)
#             flow_value1 = int(self.total_flow.text())*int(self.flow1_ratio.text())/100
#             self.flow1_rate.setText(str(flow_value1))
#             flow_value2 = int(self.total_flow.text())*int(self.flow2_ratio.text())/100
#             self.flow2_rate.setText(str(flow_value2))
#             flow_value3 = int(self.total_flow.text())*int(self.flow3_ratio.text())/100
#             self.flow3_rate.setText(str(flow_value3))
        else:
            self.const = 0
            self.total_flow.setEnabled(False)
            self.flow1_ratio.setEnabled(False)
            self.flow2_ratio.setEnabled(False)
            self.flow3_ratio.setEnabled(False)
            self.flow1_ratio.clear()
            self.flow2_ratio.clear()
            self.flow3_ratio.clear()
            self.flow1_rate.setEnabled(True)
            self.flow2_rate.setEnabled(True)
            self.flow3_rate.setEnabled(True)
    
    @pyqtSignature("")
    def on_gas_save_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        set_value('const_gas', self.const_flow.checkState())
        set_value('total', self.total_flow.text())
        set_value('flow1', self.flow1.checkState())
        set_value('flow1_gas', self.gas_type1.currentIndex())
        set_value('flow1_ratio', self.flow1_ratio.text())
        set_value('flow1_val', self.flow1_rate.text())
        set_value('flow2', self.flow2.checkState())
        set_value('flow2_gas', self.gas_type2.currentIndex())
        set_value('flow2_ratio', self.flow2_ratio.text())
        set_value('flow2_val', self.flow2_rate.text())
        set_value('flow3', self.flow3.checkState())
        set_value('flow3_gas', self.gas_type3.currentIndex())
        set_value('flow3_ratio', self.flow3_ratio.text())
        set_value('flow3_val', self.flow3_rate.text())
        if self.const:
            percent = 0
            if self.flow1.checkState()==2:
                percent += int(self.flow1_ratio.text()) 
            if self.flow2.checkState()==2:
                percent += int(self.flow2_ratio.text()) 
            if self.flow3.checkState()==2:
                percent += int(self.flow3_ratio.text())
            if percent != 100:
                QtGui.QMessageBox.warning(self, u'警告', u"流量百分比之和不为100%，请重新设置!")
                return

        self.get_para_list() 
        

    
    def get_gas_conf(self): 
        self.const_flow.setCheckState(int(get_value('const_gas')))
        self.total_flow.setText(get_value('total'))
        if int(get_value('const_gas')):
            self.total_flow.setEnabled(True)
            self.flow1_ratio.setEnabled(True)
            self.flow2_ratio.setEnabled(True)
            self.flow3_ratio.setEnabled(True)
        else:
            self.total_flow.setEnabled(False)
            self.flow1_ratio.setEnabled(False)
            self.flow2_ratio.setEnabled(False)
            self.flow3_ratio.setEnabled(False)
        self.flow1.setCheckState(int(get_value('flow1')))
        self.gas_type1.setCurrentIndex(int(get_value('flow1_gas')))
        self.flow1_ratio.setText(get_value('flow1_ratio'))
        self.flow1_rate.setText(get_value('flow1_val'))
        self.flow2.setCheckState(int(get_value('flow2')))
        self.gas_type2.setCurrentIndex(int(get_value('flow2_gas')))
        self.flow2_ratio.setText(get_value('flow2_ratio'))
        self.flow2_rate.setText(get_value('flow2_val'))
        self.flow3.setCheckState(int(get_value('flow3')))
        self.gas_type3.setCurrentIndex(int(get_value('flow3_gas')))
        self.flow3_ratio.setText(get_value('flow3_ratio'))
        self.flow3_rate.setText(get_value('flow3_val'))
        
        self.flow1_range.setText(get_range('flow1_range'))
        self.flow2_range.setText(get_range('flow2_range'))
        self.flow3_range.setText(get_range('flow3_range'))
        
        
    def get_para_list(self):
        qmdz_const.VI_GAS = []
        flow1_range = int(get_range('flow1_range'))
        flow2_range = int(get_range('flow2_range'))
        flow3_range = int(get_range('flow3_range'))
        qmdz_const.VI_GAS.append(int(self.flow1.checkState()))
        qmdz_const.VI_GAS.append(int(self.flow1_rate.text())*4095/flow1_range)
        qmdz_const.VI_GAS.append(int(self.flow2.checkState()))
        qmdz_const.VI_GAS.append(int(self.flow2_rate.text())*4095/flow2_range)
        qmdz_const.VI_GAS.append(int(self.flow3.checkState()))
        qmdz_const.VI_GAS.append(int(self.flow3_rate.text())*4095/flow3_range)
        

def get_value(key):
    key_value = read_config(VI_CONF_PATH, 'GAS', key)
    return key_value
    
def set_value(key,value):
    write_config(VI_CONF_PATH , 'GAS', key, value)
    return value

def get_range(key):
    key_value = read_config(SYS_CONF_PATH, 'HMTS48', key)
    return key_value

def dispVI_gas():
    UI_APP = UI_gas()
    UI_APP.show()
    UI_APP.exec_()
    return True