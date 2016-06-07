# -*- coding: utf-8 -*-

"""
Module implementing gas_set.
"""
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_SC_gas_set import Ui_SC_gas

import qmdz_const
from init_op import read_config,write_config
from qmdz_const import SC_CONF_PATH, SYS_CONF_PATH

class gas_set(QDialog, Ui_SC_gas):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.get_gas_conf()
        self.const = 0
        
    @pyqtSignature("int")
    def on_work_mode_currentIndexChanged(self, index):
        if index==0:
            qmdz_const.SC_GAS_MODE = 0
            self.res_offset.setEnabled(True)
            self.res_stable.setEnabled(True)
            self.response_time.setEnabled(False)
            self.recovery_time.setEnabled(False)
        else:
            qmdz_const.SC_GAS_MODE = 1
            self.res_offset.setEnabled(False)
            self.res_stable.setEnabled(False)
            self.response_time.setEnabled(True)
            self.recovery_time.setEnabled(True)       
            
    @pyqtSignature("int")
    def on_flow1_change_currentIndexChanged(self, index):    
        if index == 0:
            self.flow1_value.setEnabled(True)
        else:
            self.flow1_value.setEnabled(False)

    @pyqtSignature("int")
    def on_flow2_change_currentIndexChanged(self, index):    
        if index == 0:
            self.flow2_value.setEnabled(True)
        else:
            self.flow2_value.setEnabled(False)
            
    @pyqtSignature("int")
    def on_flow3_change_currentIndexChanged(self, index):    
        if index == 0:
            self.flow3_value.setEnabled(True)
        else:
            self.flow3_value.setEnabled(False)


    @pyqtSignature("")
    def on_SC_gas_save_clicked(self):
        """
        Slot documentation goes here.
        """
        set_value('work_mode', self.work_mode.currentIndex())
        self.total = set_value('total', self.total_flow.text())
        self.f1 = set_value('flow1', self.flow1.checkState())
        set_value('flow1_gas', self.flow1_type.currentIndex())
        self.f1c = set_value('flow1_change', self.flow1_change.currentIndex())
        set_value('flow1_val', self.flow1_value.text())
        self.f2 = set_value('flow2', self.flow2.checkState())
        set_value('flow2_gas', self.flow2_type.currentIndex())
        self.f2c = set_value('flow2_change', self.flow2_change.currentIndex())
        set_value('flow2_val', self.flow2_value.text())
        self.f3 = set_value('flow3', self.flow3.checkState())
        set_value('flow3_gas', self.flow3_type.currentIndex())
        self.f3c = set_value('flow3_change', self.flow3_change.currentIndex())
        set_value('flow3_val', self.flow3_value.text())
        
        set_value('res_offset', self.res_offset.text())
        set_value('res_hold', self.res_stable.text())
        set_value('response', self.response_time.text())
        set_value('recovery', self.recovery_time.text())
        set_value('repeat', self.repeat.text())
        
        qmdz_const.SC_FLOW1 = []
        qmdz_const.SC_FLOW2 = []
        qmdz_const.SC_FLOW3 = []
        self.get_para_list() 

        
    def get_para_list(self):
        flow1_range = int(get_range('flow1_range'))
        flow2_range = int(get_range('flow2_range'))
        flow3_range = int(get_range('flow3_range'))
        
        if self.f1 + self.f2 + self.f3 == 6:
            if self.f1c == 0 and self.f2c!=0 and self.f3c!=0:
                f1_val = int(self.flow1_value.text())*4095/flow1_range
                f23_val = self.total - int(self.flow1_value.text())
                qmdz_const.SC_FLOW1.append(f1_val)
                if self.f2c == 1:
                    for i in range(1,10):
                        qmdz_const.SC_FLOW2.append(f23_val*10*i/100*4095/flow2_range)
                        qmdz_const.SC_FLOW3.append(f23_val*(100-10*i)/100*4095/flow3_range)
                elif self.f3c == 1:
                    for i in range(1,10):
                        qmdz_const.SC_FLOW3.append(f23_val*10*i/100*4095/flow3_range)
                        qmdz_const.SC_FLOW2.append(f23_val*(100-10*i)/100*4095/flow2_range)         
            elif self.f2c == 0 and self.f1c!=0 and self.f3c!=0:
                f2_val = int(self.flow2_value.text())*4095/flow2_range
                f13_val = self.total - int(self.flow2_value.text())
                qmdz_const.SC_FLOW2.append(f2_val)
                if self.f1c == 1:
                    for i in range(1,10):
                        qmdz_const.SC_FLOW1.append(f13_val*10*i/100*4095/flow1_range)
                        qmdz_const.SC_FLOW3.append(f13_val*(100-10*i)/100*4095/flow3_range)
                elif self.f3c == 1:
                    for i in range(1,10):
                        qmdz_const.SC_FLOW3.append(f13_val*10*i/100*4095/flow3_range)
                        qmdz_const.SC_FLOW1.append(f13_val*(100-10*i)/100*4095/flow1_range)  
            elif self.f3c == 0 and self.f1c!=0 and self.f2c!=0:
                f3_val = int(self.flow3_value.text())*4095/flow3_range
                f12_val = self.total - int(self.flow3_value.text())
                qmdz_const.SC_FLOW3.append(f3_val)
                if self.f1c == 1:
                    for i in range(1,10):
                        qmdz_const.SC_FLOW1.append(f12_val*10*i/100*4095/flow1_range)
                        qmdz_const.SC_FLOW2.append(f12_val*(100-10*i)/100*4095/flow2_range)
                elif self.f2c == 1:
                    for i in range(1,10):
                        qmdz_const.SC_FLOW2.append(f12_val*10*i/100*4095/flow2_range)
                        qmdz_const.SC_FLOW1.append(f12_val*(100-10*i)/100*4095/flow1_range)
            else:
                f1_val = int(self.flow1_value.text())*4095/flow1_range
                qmdz_const.SC_FLOW1.append(f1_val)
                f2_val = int(self.flow2_value.text())*4095/flow2_range
                qmdz_const.SC_FLOW2.append(f2_val)
                f3_val = int(self.flow3_value.text())*4095/flow3_range
                qmdz_const.SC_FLOW3.append(f3_val)
                
        elif self.f1 + self.f2 + self.f3 == 4:
            if self.f1 == 0:
                if self.f2c == 1:
                    for i in range(1,10):
                        qmdz_const.SC_FLOW2.append(self.total*10*i/100*4095/flow2_range)
                        qmdz_const.SC_FLOW3.append(self.total*(100-10*i)/100*4095/flow3_range)
                elif self.f3c == 1:
                    for i in range(1,10):
                        qmdz_const.SC_FLOW3.append(self.total*10*i/100*4095/flow3_range)
                        qmdz_const.SC_FLOW2.append(self.total*(100-10*i)/100*4095/flow2_range)
            elif self.f2 == 0:
                if self.f1c == 1:
                    for i in range(1,10):
                        qmdz_const.SC_FLOW1.append(self.total*10*i/100*4095/flow1_range)
                        qmdz_const.SC_FLOW3.append(self.total*(100-10*i)/100*4095/flow3_range)
                elif self.f3c == 1:
                    for i in range(1,10):
                        qmdz_const.SC_FLOW3.append(self.total*10*i/100*4095/flow3_range)
                        qmdz_const.SC_FLOW1.append(self.total*(100-10*i)/100*4095/flow1_range)  
            elif self.f3 == 0:
                if self.f1c == 1:
                    for i in range(1,10):
                        qmdz_const.SC_FLOW1.append(self.total*10*i/100*4095/flow1_range)
                        qmdz_const.SC_FLOW2.append(self.total*(100-10*i)/100*4095/flow2_range)
                elif self.f2c == 1:
                    for i in range(1,10):
                        qmdz_const.SC_FLOW2.append(self.total*10*i/100*4095/flow2_range)
                        qmdz_const.SC_FLOW1.append(self.total*(100-10*i)/100*4095/flow1_range) 
        
        for i in xrange(0,9):
            qmdz_const.SC_GAS_PARA.append([])
            if qmdz_const.SC_FLOW1 != []:
                if len(qmdz_const.SC_FLOW1) == 1:
                    qmdz_const.SC_GAS_PARA[i].extend([2, qmdz_const.SC_FLOW1[0]])
                else:
                    qmdz_const.SC_GAS_PARA[i].extend([2, qmdz_const.SC_FLOW1[i]])
            else:
                qmdz_const.SC_GAS_PARA[i].extend([0, 0])
                
            if qmdz_const.SC_FLOW2 != []:
                if len(qmdz_const.SC_FLOW2) == 1:
                    qmdz_const.SC_GAS_PARA[i].extend([2, qmdz_const.SC_FLOW2[0]])
                else:
                    qmdz_const.SC_GAS_PARA[i].extend([2, qmdz_const.SC_FLOW2[i]])
            else:
                qmdz_const.SC_GAS_PARA[i].extend([0, 0])
                
            if qmdz_const.SC_FLOW3 != []:
                if len(qmdz_const.SC_FLOW3) == 1:
                    qmdz_const.SC_GAS_PARA[i].extend([2, qmdz_const.SC_FLOW3[0]])
                else:
                    qmdz_const.SC_GAS_PARA[i].extend([2, qmdz_const.SC_FLOW3[i]])
            else:
                qmdz_const.SC_GAS_PARA[i].extend([0, 0])
            qmdz_const.SC_GAS_PARA[i].extend([0, 0])                
        print qmdz_const.SC_GAS_PARA

    
    def get_gas_conf(self):
        work_mode = int(get_value('work_mode'))
        if work_mode==0:
            self.response_time.setEnabled(False)
            self.recovery_time.setEnabled(False)
        else:
            self.response_time.setEnabled(True)
            self.recovery_time.setEnabled(True)   
            
        self.work_mode.setCurrentIndex(work_mode)
        
         
        self.total_flow.setText(get_value('total'))
        
        self.flow1.setCheckState(int(get_value('flow1')))
        self.flow1_type.setCurrentIndex(int(get_value('flow1_gas')))
        self.flow1_change.setCurrentIndex(int(get_value('flow1_change')))
        self.flow1_value.setText(get_value('flow1_val'))
        self.flow2.setCheckState(int(get_value('flow2')))
        self.flow2_type.setCurrentIndex(int(get_value('flow2_gas')))
        self.flow2_change.setCurrentIndex(int(get_value('flow2_change')))
        self.flow2_value.setText(get_value('flow2_val'))
        self.flow3.setCheckState(int(get_value('flow3')))
        self.flow3_type.setCurrentIndex(int(get_value('flow3_gas')))
        self.flow3_change.setCurrentIndex(int(get_value('flow3_change')))
        self.flow3_value.setText(get_value('flow3_val'))
        
        self.flow1_range.setText(get_range('flow1_range'))
        self.flow2_range.setText(get_range('flow2_range'))
        self.flow3_range.setText(get_range('flow3_range'))   
        
        self.res_offset.setText(get_value('res_offset')) 
        self.res_stable.setText(get_value('res_hold'))
        self.response_time.setText(get_value('response'))
        self.recovery_time.setText(get_value('recovery'))
        self.repeat.setText(get_value('repeat'))        
        
def get_value(key):
    key_value = read_config(SC_CONF_PATH, 'GAS', key)
    return key_value
    
def set_value(key,value):
    write_config(SC_CONF_PATH, 'GAS', key, value)
    return int(value)

def get_range(key):
    key_value = read_config(SYS_CONF_PATH, 'HMTS48', key)
    return key_value
    

def dispSC_gas():
    UI_gas = gas_set()
    UI_gas.show()
    UI_gas.exec_()
    return True

