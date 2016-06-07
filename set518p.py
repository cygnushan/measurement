# -*- coding: utf-8 -*-

"""
Module implementing UI518P.
"""
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_set518p import Ui_Dialog

from init_op import read_config,write_config
import qmdz_const

from INST.AI518P import ai518p_api

class UI518P(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        self.up_mode = 0
        self.down_mode = 0
        self.seg_mode = 1
        self.temp_list = []
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.get_518p_conf()
    
    @pyqtSignature("")
    def on_temp_confirm_clicked(self):
        """
        Slot documentation goes here.
        """
        set_value('up_meas',self.up_mode)
        set_value('down_meas',self.down_mode)
        set_value('seg_raise',self.seg_mode)
        
        qmdz_const.critical_temp = float(set_value('critical', self.critical_temp.text()))
        qmdz_const.low_offset = float(set_value('low_offset', self.low_offset.text()))
        qmdz_const.high_offset = float(set_value('high_offset', self.high_offset.text()))
        qmdz_const.measure_times = int(set_value('meas_times', self.meas_times.text()))
        
        self.temp_start = float(set_value('start', self.start_temp.text()))
        self.temp_end = float(set_value('end', self.end_temp.text()))
        self.temp_step = float(set_value('interval', self.interval.text()))
        
        qmdz_const.up_slot = float(set_value('up_slot', self.up_slope.text()))
        qmdz_const.down_slot = float(set_value('down_slot', self.down_slope.text()))
        qmdz_const.hold_time = float(set_value('hold_time', self.constant_time.text()))
        
#         if int(get_value('up_slot')) > 10 or int(get_value('down_slot')) > 10:
#             QtGui.QMessageBox.warning(self, u"警告",u"升温斜率最大为10℃/min，请重新设置！")
#             return 
        
        self.get_meas_point()
        qmdz_const.temp_list = self.temp_list
        
    @pyqtSignature("bool")
    def on_up_meas_toggled(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        if checked:
            self.up_mode = 1
        else:
            self.up_mode = 0
       
    
    @pyqtSignature("bool")
    def on_down_meas_toggled(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if checked:
            self.down_mode = 1
        else:
            self.down_mode = 0
    
    @pyqtSignature("bool")
    def on_continuous_toggled(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if checked:
            self.seg_mode = 0
            self.segment.setCheckState(0)
            # self.interval.setEnabled(False)
            # self.critical_temp.setEnabled(False)
            # self.low_offset.setEnabled(False)
            # self.high_offset.setEnabled(False)
            self.constant_time.setEnabled(False)
            self.meas_times.setEnabled(False)
        else:
            self.segment.setCheckState(2)
            
    
    @pyqtSignature("bool")
    def on_segment_toggled(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if checked:
            self.seg_mode = 1
            self.continuous.setCheckState(0)
            # self.interval.setEnabled(True)
            # self.critical_temp.setEnabled(True)
            # self.low_offset.setEnabled(True)
            # self.high_offset.setEnabled(True)
            self.constant_time.setEnabled(True)
            self.meas_times.setEnabled(True)
        else:
            self.continuous.setCheckState(2)
            
    def get_meas_point(self):
        
        self.temp_list[:] = []
        self.table_temp.clearContents()
        #升温模式
        if(self.up_mode == 1 and self.down_mode == 0):
            temp_point = self.temp_start
            while temp_point < self.temp_end:
                self.temp_list.append(temp_point)
                temp_point = temp_point + self.temp_step
            self.temp_list.append(self.temp_end)
            temp_count = len(self.temp_list)
            self.table_temp.setRowCount(temp_count)
            row = 0
            for temp in self.temp_list:
                value = QtGui.QTableWidgetItem(str(temp))
                value.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.table_temp.setItem(row,0,value)
                row = row + 1 
        #降温模式        
        elif(self.up_mode == 0 and self.down_mode == 1):
            temp_point = self.temp_end
            while temp_point > self.temp_start:
                self.temp_list.append(temp_point)
                temp_point = temp_point - self.temp_step
            self.temp_list.append(self.temp_start)
            temp_count = len(self.temp_list)
            self.table_temp.setRowCount(temp_count)
            row = 0
            for temp in self.temp_list:
                value = QtGui.QTableWidgetItem(str(temp))
                value.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.table_temp.setItem(row,0,value)
                row = row + 1 

        elif(self.up_mode == 1 and self.down_mode == 1):
            temp_point = self.temp_start
            while temp_point < self.temp_end:
                self.temp_list.append(temp_point)
                temp_point = temp_point + self.temp_step
            temp_point = self.temp_end
            while temp_point > self.temp_start:
                self.temp_list.append(temp_point)
                temp_point = temp_point - self.temp_step
            self.temp_list.append(self.temp_start)
            temp_count = len(self.temp_list)
            self.table_temp.setRowCount(temp_count)
            row = 0
            for temp in self.temp_list:
                value = QtGui.QTableWidgetItem(str(temp))
                value.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.table_temp.setItem(row,0,value)
                row = row + 1  
        
        else:
            #QtGui.QMessageBox.warning(self, u"警告",u"请选择测试序列!")  
            pass
   
        
    def get_518p_conf(self):
        self.up_meas.setChecked(int(get_value('up_meas')))
        self.down_meas.setChecked(int(get_value('down_meas')))
        if get_value('seg_raise') == '1':
            self.continuous.setChecked(0)
            self.segment.setChecked(2)
        else:
            self.continuous.setChecked(2)
            self.segment.setChecked(0)
        self.start_temp.setText(str(get_value('start')))
        self.end_temp.setText(str(get_value('end')))
        self.up_slope.setText(str(get_value('up_slot')))
        self.down_slope.setText(str(get_value('down_slot')))
        self.interval.setText(str(get_value('interval')))
        self.critical_temp.setText(str(get_value('critical')))
        self.low_offset.setText(str(get_value('low_offset')))
        self.high_offset.setText(str(get_value('high_offset')))
        self.constant_time.setText(str(get_value('hold_time')))
        self.meas_times.setText(str(get_value('meas_times')))
        
        temp_count = len(qmdz_const.temp_list)
        self.table_temp.setRowCount(temp_count)
        for i in range(0,temp_count):
            newItem = QtGui.QTableWidgetItem(str(qmdz_const.temp_list[i]))
            self.table_temp.setItem(i,0,newItem)
            
        temp = ai518p_api.get_now_temp()
        if temp != "":
            self.now_temp.setText(str(temp))
        
def get_value(key):
    key_value = read_config(qmdz_const.SYS_CONF_PATH, 'AI518P', key)
    return key_value
    
def set_value(key,value):
    write_config(qmdz_const.SYS_CONF_PATH, 'AI518P', key, value)
    return value

def disp_518P():
    SET518P = UI518P()
    SET518P.show()
    SET518P.exec_()
    return True

#运行UI APP
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    SET518P = UI518P()
    SET518P.show()
    sys.exit(app.exec_())
