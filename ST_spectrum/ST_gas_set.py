# -*- coding: utf-8 -*-

"""
Module implementing gas_set.
"""
from PyQt4 import QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_ST_gas_set import Ui_ST_gas

import qmdz_const
from init_op import read_config,write_config
from qmdz_const import ST_CONF_PATH, SYS_CONF_PATH

class gas_set(QDialog, Ui_ST_gas):
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
        self.toolBox.setCurrentIndex(index)
        if index == 0:
            qmdz_const.ST_GAS_MODE = 0
        else:
            qmdz_const.ST_GAS_MODE = 1

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
    def on_ST_gas_save_clicked(self):
        """
        Slot documentation goes here.
        """
        index = self.work_mode.currentIndex()
        set_value('work_mode', index)
        if index == 0:
            qmdz_const.ST_GAS_MODE = 0
        else:
            qmdz_const.ST_GAS_MODE = 1
        # AUTO CONF
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
        
        set_value('res_offset', self.res_offset.text())
        set_value('res_hold', self.res_hold_time.text())
        
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

        self.get_auto_list() 
                
        # ******************t1 conf***********************
        set_value('t1',self.resp_t1.text())
        set_value('t1_flow1',self.flow1_t1.checkState())
        set_value('t1_flow1_gas',self.flow1_t1_type.currentIndex())
        if self.flow1value_t1.text()=="":
            self.flow1value_t1.setText('0')
        set_value('t1_flow1_val',self.flow1value_t1.text())
        
        set_value('t1_flow2',self.flow2_t1.checkState())
        set_value('t1_flow2_gas',self.flow2_t1_type.currentIndex())
        if self.flow2value_t1.text()=="":
            self.flow2value_t1.setText('0')
        set_value('t1_flow2_val',self.flow2value_t1.text())
        
        set_value('t1_flow3',self.flow3_t1.checkState())
        set_value('t1_flow3_gas',self.flow3_t1_type.currentIndex())
        if self.flow3value_t1.text()=="":
            self.flow3value_t1.setText('0')
        set_value('t1_flow3_val',self.flow3value_t1.text())
        set_value('t1_air',self.air_t1.checkState())
        
        # ******************t2 conf******************
        set_value('t2',self.resp_t2.text())
        set_value('t2_flow1',self.flow1_t2.checkState())
        set_value('t2_flow1_gas',self.flow1_t2_type.currentIndex())
        if self.flow1value_t2.text()=="":
            self.flow1value_t2.setText('0')
        set_value('t2_flow1_val',self.flow1value_t2.text())
        set_value('t2_flow2',self.flow2_t2.checkState())
        set_value('t2_flow2_gas',self.flow2_t2_type.currentIndex())
        if self.flow2value_t2.text()=="":
            self.flow2value_t2.setText('0')
        set_value('t2_flow2_val',self.flow2value_t2.text())
        set_value('t2_flow3',self.flow3_t2.checkState())
        set_value('t2_flow3_gas',self.flow3_t2_type.currentIndex())
        if self.flow3value_t2.text()=="":
            self.flow3value_t2.setText('0')
        set_value('t2_flow3_val',self.flow3value_t2.text())
        set_value('t2_air',self.air_t2.checkState())
        # ***********************t3 conf**********************
        set_value('t3',self.restore_t3.text())
        set_value('t3_flow1',self.flow1_t3.checkState())
        set_value('t3_flow1_gas',self.flow1_t3_type.currentIndex())
        if self.flow1value_t3.text()=="":
            self.flow1value_t3.setText('0')
        set_value('t3_flow1_val',self.flow1value_t3.text())
        set_value('t3_flow2',self.flow2_t3.checkState())
        set_value('t3_flow2_gas',self.flow2_t3_type.currentIndex())
        if self.flow2value_t3.text()=="":
            self.flow2value_t3.setText('0')
        set_value('t3_flow2_val',self.flow2value_t3.text())
        set_value('t3_flow3',self.flow3_t3.checkState())
        set_value('t3_flow3_gas',self.flow3_t3_type.currentIndex())
        if self.flow3value_t3.text()=="":
            self.flow3value_t3.setText('0')
        set_value('t3_flow3_val',self.flow3value_t3.text())
        set_value('t3_air',self.air_t3.checkState())
        # ***********************t4 conf****************************
        set_value('t4',self.restore_t4.text())
        set_value('t4_flow1',self.flow1_t4.checkState())
        set_value('t4_flow1_gas',self.flow1_t4_type.currentIndex())
        if self.flow1value_t4.text()=="":
            self.flow1value_t4.setText('0')
        set_value('t4_flow1_val',self.flow1value_t4.text())
        set_value('t4_flow2',self.flow2_t4.checkState())
        set_value('t4_flow2_gas',self.flow2_t4_type.currentIndex())
        if self.flow2value_t4.text()=="":
            self.flow2value_t4.setText('0')
        set_value('t4_flow2_val',self.flow2value_t4.text())
        set_value('t4_flow3',self.flow3_t4.checkState())
        set_value('t4_flow3_gas',self.flow3_t4_type.currentIndex())
        if self.flow3value_t4.text()=="":
            self.flow3value_t4.setText('0')
        set_value('t4_flow3_val',self.flow3value_t4.text())
        set_value('t4_air',self.air_t4.checkState())
        
        self.get_para_list()
        
    def get_para_list(self):
        
        flow1_range = int(get_range('flow1_range'))
        flow2_range = int(get_range('flow2_range'))
        flow3_range = int(get_range('flow3_range'))
        qmdz_const.TIME_t1 = int(self.resp_t1.text())
        qmdz_const.TIME_t2 = int(self.resp_t2.text())
        qmdz_const.TIME_t3 = int(self.restore_t3.text())
        qmdz_const.TIME_t4 = int(self.restore_t4.text())
        qmdz_const.TIME_SUM = qmdz_const.TIME_t1 + qmdz_const.TIME_t2 + qmdz_const.TIME_t3 + qmdz_const.TIME_t4
        
        qmdz_const.t1_gas.append(int(self.flow1_t1.checkState()))
        qmdz_const.t1_gas.append(int(self.flow1value_t1.text())*4095/flow1_range)
        qmdz_const.t1_gas.append(int(self.flow2_t1.checkState()))
        qmdz_const.t1_gas.append(int(self.flow2value_t1.text())*4095/flow2_range)
        qmdz_const.t1_gas.append(int(self.flow3_t1.checkState()))
        qmdz_const.t1_gas.append(int(self.flow3value_t1.text())*4095/flow3_range)
        qmdz_const.t1_gas.append(int(self.air_t1.checkState()))
        qmdz_const.t1_gas.append(int(self.airvalue_t1.text()))
        
        qmdz_const.t2_gas.append(int(self.flow1_t2.checkState()))
        qmdz_const.t2_gas.append(int(self.flow1value_t2.text())*4095/flow1_range)
        qmdz_const.t2_gas.append(int(self.flow2_t2.checkState()))
        qmdz_const.t2_gas.append(int(self.flow2value_t2.text())*4095/flow2_range)
        qmdz_const.t2_gas.append(int(self.flow3_t2.checkState()))
        qmdz_const.t2_gas.append(int(self.flow3value_t2.text())*4095/flow3_range)
        qmdz_const.t2_gas.append(int(self.air_t2.checkState()))
        qmdz_const.t2_gas.append(int(self.airvalue_t2.text()))
        
        qmdz_const.t3_gas.append(int(self.flow1_t3.checkState()))
        qmdz_const.t3_gas.append(int(self.flow1value_t3.text())*4095/flow1_range)
        qmdz_const.t3_gas.append(int(self.flow2_t3.checkState()))
        qmdz_const.t3_gas.append(int(self.flow2value_t3.text())*4095/flow2_range)
        qmdz_const.t3_gas.append(int(self.flow3_t3.checkState()))
        qmdz_const.t3_gas.append(int(self.flow3value_t3.text())*4095/flow3_range)
        qmdz_const.t3_gas.append(int(self.air_t3.checkState()))
        qmdz_const.t3_gas.append(int(self.airvalue_t3.text()))
        
        qmdz_const.t4_gas.append(int(self.flow1_t4.checkState()))
        qmdz_const.t4_gas.append(int(self.flow1value_t4.text())*4095/flow1_range)
        qmdz_const.t4_gas.append(int(self.flow2_t4.checkState()))
        qmdz_const.t4_gas.append(int(self.flow2value_t4.text())*4095/flow2_range)
        qmdz_const.t4_gas.append(int(self.flow3_t4.checkState()))
        qmdz_const.t4_gas.append(int(self.flow3value_t4.text())*4095/flow3_range)
        qmdz_const.t4_gas.append(int(self.air_t4.checkState()))
        qmdz_const.t4_gas.append(int(self.airvalue_t4.text())) 
        
        print qmdz_const.t1_gas,qmdz_const.t2_gas,qmdz_const.t3_gas,qmdz_const.t4_gas       
    
    def get_auto_list(self):
        qmdz_const.ST_GAS_AUTO = []
        flow1_range = int(get_range('flow1_range'))
        flow2_range = int(get_range('flow2_range'))
        flow3_range = int(get_range('flow3_range'))
        qmdz_const.ST_GAS_AUTO.append(int(self.flow1.checkState()))
        qmdz_const.ST_GAS_AUTO.append(int(self.flow1_rate.text())*4095/flow1_range)
        qmdz_const.ST_GAS_AUTO.append(int(self.flow2.checkState()))
        qmdz_const.ST_GAS_AUTO.append(int(self.flow2_rate.text())*4095/flow2_range)
        qmdz_const.ST_GAS_AUTO.append(int(self.flow3.checkState()))
        qmdz_const.ST_GAS_AUTO.append(int(self.flow3_rate.text())*4095/flow3_range)
        qmdz_const.ST_GAS_AUTO.extend([0,0])    
        print qmdz_const.ST_GAS_AUTO
    
    def get_gas_conf(self):
        self.work_mode.setCurrentIndex(int(get_value('work_mode'))) 
        ###################### AUTO ##################################
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
        
        self.res_offset.setText(get_value('res_offset')) 
        self.res_hold_time.setText(get_value('res_hold'))
        
        ###################### MANUAL ##################################
        self.resp_t1.setText(get_value('t1'))
        self.flow1_t1.setChecked(int(get_value('t1_flow1')))    
        self.flow1_t1_type.setCurrentIndex(int(get_value('t1_flow1_gas')))
        self.flow1value_t1.setText(get_value('t1_flow1_val'))
        self.flow2_t1.setChecked(int(get_value('t1_flow2')))
        self.flow2_t1_type.setCurrentIndex(int(get_value('t1_flow2_gas')))
        self.flow2value_t1.setText(get_value('t1_flow2_val'))
        self.flow3_t1.setChecked(int(get_value('t1_flow3')))
        self.flow3_t1_type.setCurrentIndex(int(get_value('t1_flow3_gas')))
        self.flow3value_t1.setText(get_value('t1_flow3_val'))
        self.air_t1.setChecked(int(get_value('t1_air')))
        self.flow1_range_t1.setText(get_range('flow1_range'))
        self.flow2_range_t1.setText(get_range('flow2_range'))
        self.flow3_range_t1.setText(get_range('flow3_range'))
        
        self.resp_t2.setText(get_value('t2'))
        self.flow1_t2.setChecked(int(get_value('t2_flow1')))    
        self.flow1_t2_type.setCurrentIndex(int(get_value('t2_flow1_gas')))
        self.flow1value_t2.setText(get_value('t2_flow1_val'))
        self.flow2_t2.setChecked(int(get_value('t2_flow2')))
        self.flow2_t2_type.setCurrentIndex(int(get_value('t2_flow2_gas')))
        self.flow2value_t2.setText(get_value('t2_flow2_val'))
        self.flow3_t2.setChecked(int(get_value('t2_flow3')))
        self.flow3_t2_type.setCurrentIndex(int(get_value('t2_flow3_gas')))
        self.flow3value_t2.setText(get_value('t2_flow3_val'))
        self.air_t2.setChecked(int(get_value('t2_air')))
        self.flow1_range_t2.setText(get_range('flow1_range'))
        self.flow2_range_t2.setText(get_range('flow2_range'))
        self.flow3_range_t2.setText(get_range('flow3_range'))

        self.restore_t3.setText(get_value('t3'))
        self.flow1_t3.setChecked(int(get_value('t3_flow1')))    
        self.flow1_t3_type.setCurrentIndex(int(get_value('t3_flow1_gas')))
        self.flow1value_t3.setText(get_value('t3_flow1_val'))
        self.flow2_t3.setChecked(int(get_value('t3_flow2')))
        self.flow2_t3_type.setCurrentIndex(int(get_value('t3_flow2_gas')))
        self.flow2value_t3.setText(get_value('t3_flow2_val'))
        self.flow3_t3.setChecked(int(get_value('t3_flow3')))
        self.flow3_t3_type.setCurrentIndex(int(get_value('t3_flow3_gas')))
        self.flow3value_t3.setText(get_value('t3_flow3_val'))
        self.air_t3.setChecked(int(get_value('t3_air')))
        self.flow1_range_t3.setText(get_range('flow1_range'))
        self.flow2_range_t3.setText(get_range('flow2_range'))
        self.flow3_range_t3.setText(get_range('flow3_range'))

        self.restore_t4.setText(get_value('t4'))
        self.flow1_t4.setChecked(int(get_value('t4_flow1')))    
        self.flow1_t4_type.setCurrentIndex(int(get_value('t4_flow1_gas')))
        self.flow1value_t4.setText(get_value('t4_flow1_val'))
        self.flow2_t4.setChecked(int(get_value('t4_flow2')))
        self.flow2_t4_type.setCurrentIndex(int(get_value('t4_flow2_gas')))
        self.flow2value_t4.setText(get_value('t4_flow2_val'))
        self.flow3_t4.setChecked(int(get_value('t4_flow3')))
        self.flow3_t4_type.setCurrentIndex(int(get_value('t4_flow3_gas')))
        self.flow3value_t4.setText(get_value('t4_flow3_val'))
        self.air_t4.setChecked(int(get_value('t4_air')))
        self.flow1_range_t4.setText(get_range('flow1_range'))
        self.flow2_range_t4.setText(get_range('flow2_range'))
        self.flow3_range_t4.setText(get_range('flow3_range'))
        
def get_value(key):
    key_value = read_config(ST_CONF_PATH, 'GAS', key)
    return key_value
    
def set_value(key,value):
    write_config(ST_CONF_PATH, 'GAS', key, value)
    return value

def get_range(key):
    key_value = read_config(SYS_CONF_PATH, 'HMTS48', key)
    return key_value
    

def dispST_gas():
    UI_gas = gas_set()
    UI_gas.show()
    UI_gas.exec_()
    return True

