# -*- coding: utf-8 -*-

"""
Module implementing UI_2400.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_VI_2400_set import Ui_Dialog

from init_op import read_config,write_config
import qmdz_const

from INST.INST2400 import Keithley2400

class UI_2400(QDialog, Ui_Dialog):
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

    @pyqtSignature("int")
    def on_meas_mode_currentIndexChanged(self, index):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        qmdz_const.MEAS_MODE = index

    @pyqtSignature("int")
    def on_output_mode_currentIndexChanged(self, index):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        qmdz_const.OUTPUT_MODE = index
    

    @pyqtSignature("int")
    def on_Vunit1_currentIndexChanged(self, index):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.Vunit2.setCurrentIndex(index)
        self.Vunit3.setCurrentIndex(index)
        
    
    @pyqtSignature("int")
    def on_Iunit1_currentIndexChanged(self, index):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.Iunit2.setCurrentIndex(index)
        self.Iunit3.setCurrentIndex(index)

    @pyqtSignature("")
    def on_res_detect_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        R_range = qmdz_const.res_range[self.res_range.currentIndex()]
        print "detect res range:", R_range
        self.voltage,self.current,self.resistance = Keithley2400.measure_ohms_auto(R_range, qmdz_const.MEAS_MODE)
        self.detectV.setText(str(self.voltage))
        self.detectI.setText(str(self.current))
        self.detectR.setText(str(self.resistance))
        qmdz_const.res_det = self.resistance
    
    @pyqtSignature("")
    def on_save_2400_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        set_value('meas_mode', self.meas_mode.currentIndex())
        set_value('out_mode', self.output_mode.currentIndex())
        if self.VI_MODE.isChecked():
            set_value('vi_mode', '1')
        else:
            set_value('vi_mode', '0')
        set_value('iv_unit', self.Vunit1.currentIndex())
        set_value('iv_sweep', self.IV_sweep.currentIndex())
        set_value('iv_start', self.Vstart.text())
        set_value('iv_stop', self.Vend.text())
        set_value('iv_step', self.Vstep.text())
        set_value('iv_loop', self.IV_loop.text())
        set_value('iv_range', self.IV_range.currentIndex())
        
        set_value('vi_sweep', self.VI_sweep.currentIndex())
        set_value('vi_start', self.Istart.text())
        set_value('vi_stop', self.Iend.text())
        set_value('vi_step', self.Istep.text())
        set_value('vi_loop', self.VI_loop.text())
        set_value('vi_unit', self.Iunit1.currentIndex())
        set_value('vi_range', self.VI_range.currentIndex())
        
        #if get_value('vi_mode')=='1':
        self.generate_ilist()
        self.generate_vlist()
    
    def get_2400_conf(self): 
        self.meas_mode.setCurrentIndex(int(get_value('meas_mode')))
        self.output_mode.setCurrentIndex(int(get_value('out_mode')))
        if qmdz_const.VI_MODE:
            self.VI_MODE.setChecked(True)
        else:
            self.IV_MODE.setChecked(True)
        self.IV_sweep.setCurrentIndex(int(get_value('iv_sweep')))
        self.Vstart.setText(get_value('iv_start'))
        self.Vend.setText(get_value('iv_stop'))
        self.Vstep.setText(get_value('iv_step'))
        self.IV_loop.setText(get_value('iv_loop'))
        self.Vunit1.setCurrentIndex(int(get_value('iv_unit')))
        self.Vunit2.setCurrentIndex(int(get_value('iv_unit')))
        self.Vunit3.setCurrentIndex(int(get_value('iv_unit')))
        self.IV_range.setCurrentIndex(int(get_value('iv_range')))
        
        self.VI_sweep.setCurrentIndex(int(get_value('vi_sweep')))
        self.Istart.setText(get_value('vi_start'))
        self.Iend.setText(get_value('vi_stop'))
        self.Istep.setText(get_value('vi_step'))
        self.VI_loop.setText(get_value('vi_loop'))
        self.Iunit1.setCurrentIndex(int(get_value('vi_unit')))
        self.Iunit2.setCurrentIndex(int(get_value('vi_unit')))
        self.Iunit3.setCurrentIndex(int(get_value('vi_unit')))
        self.VI_range.setCurrentIndex(int(get_value('vi_range')))
        
        
    def generate_vlist(self):
        
        def func_neg(x):
            return -1*x
        
        qmdz_const.IV_VLIST = []
        pos_list = []
        start = float(get_value('iv_start'))
        step = float(get_value('iv_step'))
        end = float(get_value('iv_stop'))
        pos_list.append(start)
        mid_ref = start
        while(mid_ref < end):
            mid_ref += step
            pos_list.append(mid_ref)
            
        pos_rev = pos_list[::-1]
        neg_list = map(func_neg, pos_list)
        neg_rev = neg_list[::-1]
        pos_ful = pos_list + pos_rev[1:]
        neg_ful = map(func_neg, pos_ful)

        if get_value('iv_sweep') == '0':
            iv_list = pos_ful + ['0'] +neg_ful 
            if get_value('iv_unit') == '0':
                for value in iv_list:
                    qmdz_const.IV_VLIST.append(str(value)+'e-3')
            else:
                for value in iv_list:
                    qmdz_const.IV_VLIST.append(str(value))
        else:
            iv_list = neg_rev + ['0'] + pos_ful + ['0'] + neg_list
            if get_value('iv_unit') == '0':
                for value in iv_list:
                    qmdz_const.IV_VLIST.append(str(value)+'e-3')
            else:
                for value in iv_list:
                    qmdz_const.IV_VLIST.append(str(value))

    def generate_ilist(self):
        
        def func_neg(x):
            return -1*x
        
        qmdz_const.VI_ILIST = []
        pos_list = []
        start = float(get_value('vi_start'))
        step = float(get_value('vi_step'))
        end = float(get_value('vi_stop'))
        mid_ref = start
        while(mid_ref <= end):
            pos_list.append(mid_ref)
            mid_ref += step
            
        pos_rev = pos_list[::-1]
        neg_list = map(func_neg, pos_list)
        neg_rev = neg_list[::-1]
        pos_ful = pos_list + pos_rev[1:]
        neg_ful = map(func_neg, pos_ful)

        if get_value('vi_sweep') == '0':
            vi_list = pos_ful + ['0'] + neg_ful 
            if get_value('vi_unit') == '0':
                for value in vi_list:
                    qmdz_const.VI_ILIST.append(str(value)+'e-6')
            elif get_value('vi_unit') == '1':
                for value in vi_list:
                    qmdz_const.VI_ILIST.append(str(value)+'e-3')                    
            else:
                for value in vi_list:
                    qmdz_const.VI_ILIST.append(str(value))
        else:
            vi_list = neg_rev + ['0'] + pos_ful + ['0'] + neg_list
            if get_value('vi_unit') == '0':
                for value in vi_list:
                    qmdz_const.VI_ILIST.append(str(value)+'e-6')
            elif get_value('vi_unit') == '1':
                for value in vi_list:
                    qmdz_const.VI_ILIST.append(str(value)+'e-3') 
            else:
                for value in vi_list:
                    qmdz_const.VI_ILIST.append(str(value))


def get_value(key):
    key_value = read_config(qmdz_const.VI_CONF_PATH, 'INST', key)
    return key_value
    
def set_value(key,value):
    write_config(qmdz_const.VI_CONF_PATH, 'INST', key, value)
    return value

def dispVI_2400():
    UI_APP = UI_2400()
    UI_APP.show()
    UI_APP.exec_()
    return True