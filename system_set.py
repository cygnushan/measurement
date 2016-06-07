# -*- coding: utf-8 -*-

"""
Module implementing sys_set_ui.
"""
import sys
import time
import PyQt4
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature, QTimer, SIGNAL

from Ui_system_set import Ui_sys_set_ui

from init_op import read_config,write_config

from qmdz_const import SYS_CONF_PATH,PARA_NAME,PARA_DEFAULT

from INST.AI518P import ai518p_api
from INST.HMT_S48 import C_S48,REG_DICT
from INST.INST2400 import Keithley2400
from INST.valve_ctrl import Valve_Ctrl

flow_index = {'50':0,'500':1,'2000':2}

class sys_set_ui(QDialog, Ui_sys_set_ui):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.read_conf()
        self.xtime = 0
        self.timer = QTimer(self)
        self.connect(self.timer,SIGNAL("timeout()"),self.measure)

    
    @pyqtSignature("QString")
    def on_com_518p_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        write_config(SYS_CONF_PATH, 'AI518P', 'port', str(p0))
            
    
    @pyqtSignature("QString")
    def on_baud_518p_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        write_config(SYS_CONF_PATH, 'AI518P', 'baud', str(p0))
    
    @pyqtSignature("QString")
    def on_com_flowmeter_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.s48_port = str(p0)
        write_config(SYS_CONF_PATH, 'HMTS48', 'port', str(p0))
    
    @pyqtSignature("QString")
    def on_baud_flowmeter_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        write_config(SYS_CONF_PATH, 'HMTS48', 'baud', str(p0))
    
    
    @pyqtSignature("QString")
    def on_range1_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        write_config(SYS_CONF_PATH, 'HMTS48', 'flow1_range', str(p0))

    @pyqtSignature("QString")
    def on_range2_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        write_config(SYS_CONF_PATH, 'HMTS48', 'flow2_range', str(p0))

    @pyqtSignature("QString")
    def on_range3_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        write_config(SYS_CONF_PATH, 'HMTS48', 'flow3_range', str(p0))
    
    @pyqtSignature("QString")
    def on_com_pcb_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        write_config(SYS_CONF_PATH, 'PCB', 'port', str(p0))
        Valve_Ctrl.close()
        Valve_Ctrl.connect(str(p0))
    
    @pyqtSignature("QString")
    def on_baud_pcb_currentIndexChanged(self, p0):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        write_config(SYS_CONF_PATH, 'PCB', 'baud', str(p0))
    
    @pyqtSignature("int")
    def on_pcb_ctrl_obj_currentIndexChanged(self, index):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        res = ""
        if   index == 0:
            res = Valve_Ctrl.flowmeter1_open()
        elif index == 1:
            res = Valve_Ctrl.flowmeter1_close()
        elif index == 2:
            res = Valve_Ctrl.flowmeter2_open()
        elif index == 3:
            res = Valve_Ctrl.flowmeter2_close()
        elif index == 4:
            res = Valve_Ctrl.flowmeter3_open()
        elif index == 5:
            res = Valve_Ctrl.flowmeter3_close()
        elif index == 6:
            res = Valve_Ctrl.airpump_open()
        elif index == 7:
            res = Valve_Ctrl.airpump_close()
        else:
            pass
        self.pcb_ctrl_return.setText(str(res))
        
    
    @pyqtSignature("int")
    def on_flowmeter_addr_currentIndexChanged(self, index):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.flowapi.comm_close()
        self.flowapi = C_S48(self.s48_port, index+1)
        print index+1
    
    
    @pyqtSignature("")
    def on_flowmeter_read_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        para_index = self.flowmeter_para.currentIndex()
        try:
            para_value = self.flowapi.read_para(REG_DICT[para_index])
            self.flowmeter_readpara.setText(str(para_value))
        except Exception,e:
            print e
            self.flowmeter_readpara.setText('NA')
    
    @pyqtSignature("")
    def on_flowmeter_write_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        value_str = self.flowmeter_writepara.text()
        if value_str:
            para_value = int(value_str)
            para_index = self.flowmeter_para.currentIndex()
            para_reg = REG_DICT[para_index]
            self.flowapi.write_para(para_reg, para_value)
    
    @pyqtSignature("int")
    def on_ai518p_addr_currentIndexChanged(self, index):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        pass
    
    @pyqtSignature("int")
    def on_ai518p_para_currentIndexChanged(self, index):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        pass
    
    @pyqtSignature("")
    def on_ai518p_read_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        para_no = self.ai518p_para.currentIndex()
        try:
            para_dict = ai518p_api.read_para(PARA_NAME[para_no])
            self.ai518p_read_para.setText(str(para_dict['PARA']))
        except Exception,e:
            print e
            self.ai518p_read_para.setText('NA')
        
    
    @pyqtSignature("")
    def on_ai518p_write_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        para_no = self.ai518p_para.currentIndex()
        para_val = int(self.ai518p_write_para.text())
        ai518p_api.write_para(PARA_NAME[para_no],para_val)
        
    @pyqtSignature("")
    def on_restore_518p_clicked(self):
        
        for no in xrange(0,26):
            try:
                print PARA_NAME[no],PARA_DEFAULT[no]
                ai518p_api.write_para(PARA_NAME[no],PARA_DEFAULT[no])
            except:
                print "PARA %s restore failed" % PARA_NAME[no]
            time.sleep(1)
            
        PyQt4.QtGui.QMessageBox.information(self,u'提示', u'AI-518P恢复出厂成功!')
        
    @pyqtSignature("")
    def on_start_AT_clicked(self):
        print "start"
        self.xtime = 0
        self.xdata = []
        self.data_pv = []
        self.data_sv = []
        # self.AT_MPL.clear_curve()
        
        target_temp = int(self.PID_temp.text())
        ai518p_api.write_para('CtrL', 2)
        ai518p_api.write_para('c01', target_temp*10)
        ai518p_api.write_para('t01', 50)
        ai518p_api.write_para('c02', target_temp*10)
        ai518p_api.write_para('t01', -1)
        ai518p_api.write_para('RUNSTA', 0)
        
        self.AT_MPL.change_y(1, target_temp*1.5)
        self.timer.start(1000)
        
    def measure(self):
        self.xtime +=1
        self.xdata.append(self.xtime)
        pv,sv = ai518p_api.get_psv()
        self.data_pv.append(float(pv))
        self.data_sv.append(float(sv))
        self.now_PV.setText(str(pv))
        self.now_SV.setText(str(sv))
        self.now_temp.setText(str(pv))
        # print "SV:",self.data_sv
        # print "PV:",self.data_pv
        if self.xtime == 1:
            self.AT_MPL.generateData(self.xdata, self.data_pv, 'g', 'PV', 1)
            self.AT_MPL.generateData(self.xdata, self.data_sv, 'r', 'SV', 1)
        else:
            self.AT_MPL.generateData(self.xdata, self.data_pv, 'g', 'PV', 0)
            self.AT_MPL.generateData(self.xdata, self.data_sv, 'r', 'SV', 0)
        
        self.is_at_finish()
        
        
    def is_at_finish(self):
        ctrl = ai518p_api.read_para('CtrL')['PARA']
        if ctrl == 3:
            self.timer.stop()
            PyQt4.QtGui.QMessageBox.information(self,u'提示', u'恭喜！自整定完成!')
            M5_hold = ai518p_api.read_para('M5')['PARA']
            self.para_M5.setText(str(M5_hold))
            P_rate = ai518p_api.read_para('P')['PARA']
            self.para_P.setText(str(P_rate))
            t_delay = ai518p_api.read_para('t')['PARA']
            self.para_t.setText(str(t_delay))
        
        
    @pyqtSignature("")
    def on_stop_AT_clicked(self):
        print "stop"
        ai518p_api.set_stop()
        self.timer.stop()
        self.AT_MPL.clear_curve()
        
    def read_conf(self):
        ai518p_port = read_config(SYS_CONF_PATH, 'AI518P', 'port')
        self.com_518p.setCurrentIndex(int(ai518p_port[-1])-1)
        self.s48_port = read_config(SYS_CONF_PATH, 'HMTS48', 'port')
        self.com_flowmeter.setCurrentIndex(int(self.s48_port[-1])-1)
        pcb_port = read_config(SYS_CONF_PATH, 'PCB', 'port')
        self.com_pcb.setCurrentIndex(int(pcb_port[-1])-1)
        inst2400_port = Keithley2400.get_gpibport()
        if inst2400_port:
            self.com_2400.setItemText(0,inst2400_port)
        else:
            self.com_2400.setItemText(0,'NA')
        
        ai518p_baud = read_config(SYS_CONF_PATH, 'AI518P', 'baud')
        self.baud_518p.setCurrentIndex(int(ai518p_baud)/9600/2)
        s48_baud = read_config(SYS_CONF_PATH, 'HMTS48', 'baud')
        self.baud_flowmeter.setCurrentIndex(int(s48_baud)/9600/2)
        pcb_baud = read_config(SYS_CONF_PATH, 'PCB', 'baud')
        self.baud_pcb.setCurrentIndex(int(pcb_baud)/9600/2)
        
        self.addr_518p = self.ai518p_addr.currentIndex()+1
        self.addr_flowmeter = self.flowmeter_addr.currentIndex()+1
        
        flow1 = read_config(SYS_CONF_PATH, 'HMTS48', 'flow1_range')
        self.range1.setCurrentIndex(flow_index[flow1])
        flow2 = read_config(SYS_CONF_PATH, 'HMTS48', 'flow2_range')
        self.range2.setCurrentIndex(flow_index[flow2])
        flow3 = read_config(SYS_CONF_PATH, 'HMTS48', 'flow3_range')
        self.range3.setCurrentIndex(flow_index[flow3])
        
        flow_addr = self.flowmeter_addr.currentIndex() + 1
        self.flowapi = C_S48(self.s48_port, flow_addr)
        
#         M5_hold = ai518p_api.read_para('M5')['PARA']
#         self.para_M5.setText(str(M5_hold))
#         P_rate = ai518p_api.read_para('P')['PARA']
#         self.para_P.setText(str(P_rate))
#         t_delay = ai518p_api.read_para('t')['PARA']
#         self.para_t.setText(str(t_delay))
        
    @pyqtSignature("int")    
    def on_tabWidget_currentChanged(self,index):
        # pass
        if index==2:
            try:
                M5_hold = ai518p_api.read_para('M5')['PARA']
                self.para_M5.setText(str(M5_hold))
                P_rate = ai518p_api.read_para('P')['PARA']
                self.para_P.setText(str(P_rate))
                t_delay = ai518p_api.read_para('t')['PARA']
                self.para_t.setText(str(t_delay))
            except:
                self.para_M5.setText("NA")
                self.para_P.setText("NA")
                self.para_t.setText("NA")
                
        
    def closeEvent(self, event):
        pass

def disp_sys_set():
    UI_SET = sys_set_ui()
    UI_SET.show()
    UI_SET.exec_()
    return True
    
#运行UI APP
if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)
    UI_SYS_SET = sys_set_ui()
    UI_SYS_SET.show()
    sys.exit(app.exec_())
    '''
          自整定具体操作步骤：
    1、长按半圆带箭头的键，将里面CTRL改为2。
    2、Co1设定为400；
    3、按半圆带箭头的键，出现to1，设定为50  
    4、co2设定为400  
    5、to2，设定为-1  
    6、按运行键启动，此时OP1指示灯会亮红色，SV界面中会显示AT字样
    6、自整定刚结束后CTRL将变为3
    '''
