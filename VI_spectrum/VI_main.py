# -*- coding: utf-8 -*-

"""
Module implementing VI_TEST.
"""
import os
import sys
import time
import xlwt
from math import *

script_path = os.getcwd()
root_path = os.path.dirname(script_path)
sys.path.insert(0,root_path)

from PyQt4 import QtGui
from PyQt4.QtGui import QDialog,QApplication
from PyQt4.QtCore import pyqtSignature, QTimer, SIGNAL

from Ui_VI_main import Ui_Dialog

from VI_2400_set import dispVI_2400
from VI_gas_set import dispVI_gas
from set518p import disp_518P
from coordinate import disp_coord

from INST.AI518P import ai518p_api
from INST.HMT_S48 import C_S48
from INST.INST2400 import Keithley2400
from INST.valve_ctrl import Valve_Ctrl

from mylog import logger
import qmdz_const


from init_op import read_config


class VI_TEST(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        self.vimode = 1
        self.gas_set = 0
        self.runtime = 0
        self.dataX = []
        self.dataY = []
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.get_sys_state()
        self.timer = QTimer(self)
        self.connect(self.timer,SIGNAL("timeout()"),self.measure)
        
    def xls_init(self):
        self.xls = xlwt.Workbook(encoding='utf-8')
        self.table = self.xls.add_sheet(u'试验数据',cell_overwrite_ok=True)
        if len(qmdz_const.temp_list) > 0:
            self.table.write(0,0,u'温度(℃)')
            for i in range(0, len(qmdz_const.temp_list)):
                self.table.write(0,i+1,str(qmdz_const.temp_list[i])+'℃')
                if self.vimode:
                    self.table.write(1,0,'电流(I)')
                    self.table.write(1,i+1,'电压(V)')
                else:
                    self.table.write(1,0,'电压(V)')
                    self.table.write(1,i+1,'电流(I)')
        else:
            self.table.write(0,0,u'温度(℃)')
            if self.vimode:
                self.table.write(1,0,u'电流(I)')
                self.table.write(1,1,u'电压(V)')
            else:
                self.table.write(1,0,u'电压(V)')
                self.table.write(1,1,u'电流(I)')
            self.table.write(0,1,str(self.temprature) + u'℃')
        self.style = xlwt.XFStyle
        self.font = xlwt.Font
        self.font.name = 'SimSun'
        self.style.font = self.font
                 
    
    @pyqtSignature("")
    def on_btn_savepath_clicked(self):
        """
        Slot documentation goes here.
        """
        self.getPath = QtGui.QFileDialog.getExistingDirectory(self, u"请选择保存目录", "D:/")
        if self.getPath:
            self.save_path.setText(self.getPath)
    
    @pyqtSignature("bool")
    def on_gas_filled_toggled(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if checked:
            self.gas_set = 1
            self.VI_gas_set.setEnabled(True)
        else:
            self.gas_set = 0
            self.VI_gas_set.setEnabled(False)
    
    @pyqtSignature("")
    def on_VI_2400_set_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        dispVI_2400()
        print "VI:",qmdz_const.VI_ILIST
        print "IV:",qmdz_const.IV_VLIST
        # 通电压测电流   IV 
        self.vrange = read_config(qmdz_const.VI_CONF_PATH, 'INST', 'iv_stop')
        vi_range_index = int(read_config(qmdz_const.VI_CONF_PATH, 'INST', 'iv_range'))
        self.ilimit = qmdz_const.irange_dict[vi_range_index]
        iv_unit = read_config(qmdz_const.VI_CONF_PATH, 'INST', 'iv_unit')
        if iv_unit == '0':
            self.vrange = self.vrange + "e-3"
        # 通电流测电压 VI
        self.irange = read_config(qmdz_const.VI_CONF_PATH, 'INST', 'vi_stop')
        iv_range_index = int(read_config(qmdz_const.VI_CONF_PATH, 'INST', 'vi_range'))
        self.vlimit = qmdz_const.vrange_dict[iv_range_index]
        vi_unit = read_config(qmdz_const.VI_CONF_PATH, 'INST', 'vi_unit')
        if vi_unit == '0':
            self.irange = self.irange + "e-6"
        if vi_unit == '1':
            self.irange = self.irange + "e-3"
            
        if self.vimode:    
            self.loops = int(read_config(qmdz_const.VI_CONF_PATH, 'INST', 'vi_loop'))
        else:
            self.loops = int(read_config(qmdz_const.VI_CONF_PATH, 'INST', 'iv_loop'))
    
    @pyqtSignature("")
    def on_VI_518p_set_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        disp_518P()
        self.up_slot = qmdz_const.up_slot
        self.down_slot = qmdz_const.down_slot
    
    @pyqtSignature("")
    def on_VI_gas_set_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        dispVI_gas()
        print "GAS PARA:", qmdz_const.VI_GAS
    
    @pyqtSignature("")
    def on_VI_XY_set_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        disp_coord()
        if qmdz_const.Auto_Range == 0:
            xmin = int(read_config(qmdz_const.SYS_CONF_PATH, 'COORD', 'x_min'))
            xmax = int(read_config(qmdz_const.SYS_CONF_PATH, 'COORD', 'x_max'))
            ymin = int(read_config(qmdz_const.SYS_CONF_PATH, 'COORD', 'y_min'))
            ymax = int(read_config(qmdz_const.SYS_CONF_PATH, 'COORD', 'y_max'))
            self.VI_MPL.change_xy(xmin, xmax, ymin, ymax)
    
    @pyqtSignature("bool")
    def on_VI_mode_toggled(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if checked:
            self.vimode = 1
            qmdz_const.VI_MODE = 1
            self.sample_id.setText("VI_test")
            self.VI_MPL.clear_curve()
            self.VI_MPL.set_vi_mode()
            
    @pyqtSignature("bool")
    def on_IV_mode_toggled(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if checked:
            self.vimode = 0
            qmdz_const.VI_MODE = 0
            self.sample_id.setText("IV_test")
            self.VI_MPL.clear_curve()
            self.VI_MPL.set_iv_mode()
            
    @pyqtSignature("")
    def on_VI_start_clicked(self):
        print "start"
        self.index = 0
        self.temp_index = 0
        self.meas_mode = 0
        self.runtime = 0
        self.measure_times = 1
        self.temp_flag = 0
        self.stable_time = 0
        self.dataX = []
        self.dataY = []
        self.dataX.append([])
        self.dataY.append([])
        
        self.xls_name = str(self.save_path.text() + '/'+ self.sample_id.text() + '-'+ time.strftime("%m%d%H%M")+ ".xls")
        self.xls_init()
        
        # self.coord_init()
        self.VI_MPL.clear_curve()
        
        Keithley2400.conncet_inst()
        if self.gas_set:
            self.open_flow()
        
        if len(qmdz_const.temp_list) > 0:
            temp_now = ai518p_api.get_now_temp() + 0.5
            self.exp_temp = qmdz_const.temp_list[0]
            ai518p_api.set_518p_constmode(temp_now,self.exp_temp,self.up_slot,self.down_slot)
            
        self.timer.start(1000)

    @pyqtSignature("")
    def on_VI_stop_clicked(self):
        print "stop"   
        self.meas_stop()
        
    @pyqtSignature("")
    def on_VI_save_clicked(self):
        self.write_xls()
        self.xls.save(self.xls_name)

        pic_path = self.xls_name[:-4] + ".png"
        self.VI_MPL.save_curve(str(pic_path))
        
        QtGui.QMessageBox.information(self,u'提示', (u'测试数据%s保存成功!' % self.xls_name))  
        
    def coord_init(self):
        if qmdz_const.Auto_Range:
            if self.vimode:
                xmin = min(map(float, qmdz_const.VI_ILIST))*2
                xmax = max(map(float, qmdz_const.VI_ILIST))*2
                ymin = xmin*float(self.resistance)
                ymax = xmax*float(self.resistance)
                print xmin,xmax,ymin,ymax
                self.VI_MPL.change_xy(xmin, xmax, ymin, ymax)
                self.loops = int(read_config(qmdz_const.VI_CONF_PATH, 'INST', 'vi_loop'))
            else:
                xmin = min(map(float, qmdz_const.IV_VLIST))*2
                xmax = max(map(float, qmdz_const.IV_VLIST))*2
                ymin = xmin/float(self.resistance)
                ymax = xmax/float(self.resistance)
                self.VI_MPL.change_xy(xmin, xmax, ymin, ymax)
                self.loops = int(read_config(qmdz_const.VI_CONF_PATH, 'INST', 'iv_loop'))

    def wait_temp(self,temp):
        now_temp = ai518p_api.get_now_temp()
        now_sv = ai518p_api.get_sv()
        self.now_T.setText(str(now_temp))
        if (now_sv == temp):
            if (fabs(now_temp-now_sv)<=qmdz_const.low_offset):
                self.stable_time = self.stable_time + 1
            else:
                self.stable_time = 0
            if self.stable_time >= qmdz_const.hold_time:
                self.temp_flag = 1
                print "temp stable,begin measure"
            
    def measure(self):
        self.runtime += 1
        self.meas_time.setText(str(self.runtime))
        if self.gas_set:
            self.disp_flow()
        # 等待温度达到测量点
        if (self.meas_mode == 0 and len(qmdz_const.temp_list) > 0):
            self.wait_temp(self.exp_temp)
            if (self.temp_flag == 0):
                return
            else:
                self.temp_flag = 0
                self.meas_mode = 1
        else:# 温度稳定，开始测量
            print "times:", self.measure_times , self.loops
            if self.measure_times <= self.loops:
                if self.vimode == 0:
                    self.iv_meas()
                else:
                    self.vi_meas()
                
                self.index += 1
            else:
                if len(qmdz_const.temp_list) > 0:
                    self.temp_index = self.temp_index + 1
                if self.temp_index < len(qmdz_const.temp_list):
                    self.st_temp = self.exp_temp
                    self.exp_temp = qmdz_const.temp_list[self.temp_index]
                    self.meas_mode = 0
                    self.measure_times = 1
                    self.dataX.append([])
                    self.dataY.append([])
                    ai518p_api.set_518p_constmode(self.st_temp,self.exp_temp,self.up_slot,self.down_slot)
                else:
                    self.meas_stop() 
        
    def iv_meas(self):
        if self.index < len(qmdz_const.IV_VLIST):
            v_out = qmdz_const.IV_VLIST[self.index]
            if float(v_out) == 0:
                meas_V = meas_I = meas_R = 0
            else:
                meas_V,meas_I,meas_R = Keithley2400.measure_current(v_out, self.ilimit, qmdz_const.MEAS_MODE)
            self.now_v.setText(str(meas_V))
            self.now_I.setText(str(meas_I))
            self.now_R.setText(str(meas_R))
            self.dataX[self.temp_index].append(float(v_out))
            self.dataY[self.temp_index].append(float(meas_I))
            print "dataX:",self.dataX
            print "dataY:",self.dataY
            if len(self.dataX[self.temp_index]) == 1:
                if len(qmdz_const.temp_list) > 0:
                    self.VI_MPL.generateData(self.dataX[self.temp_index], self.dataY[self.temp_index],
                                             style=qmdz_const.color_list[self.temp_index], 
                                             label=str(qmdz_const.temp_list[self.temp_index])+u'\u2103', type=1)
                else:
                    self.VI_MPL.generateData(self.dataX[self.temp_index], self.dataY[self.temp_index],
                                             style=qmdz_const.color_list[self.temp_index], 
                                             label=str(self.temprature)+u'\u2103', type=1)
            else:
                self.VI_MPL.generateData(self.dataX[self.temp_index], self.dataY[self.temp_index], type=0)
        else:
            self.measure_times += 1
            self.index = -1


    def vi_meas(self):
        print self.irange, self.vlimit
        if self.index < len(qmdz_const.VI_ILIST):
            i_out = qmdz_const.VI_ILIST[self.index]
            if float(i_out) == 0:
                meas_V = meas_I = meas_R = 0
            else:
                meas_V,meas_I,meas_R = Keithley2400.measure_voltage(i_out, self.vlimit, qmdz_const.MEAS_MODE)
            self.now_v.setText(str(meas_V))
            self.now_I.setText(str(meas_I))
            self.now_R.setText(str(meas_R))
            
            self.dataX[self.temp_index].append(float(i_out))
            self.dataY[self.temp_index].append(float(meas_V))
            print "dataX:",self.dataX
            print "dataY:",self.dataY
            if len(self.dataX[self.temp_index]) == 1:
                if len(qmdz_const.temp_list) > 0:
                    self.VI_MPL.generateData(self.dataX[self.temp_index], self.dataY[self.temp_index],
                                             style=qmdz_const.color_list[self.temp_index], 
                                             label=str(qmdz_const.temp_list[self.temp_index])+u'\u2103', type=1)
                else:
                    self.VI_MPL.generateData(self.dataX[self.temp_index], self.dataY[self.temp_index],
                                             style=qmdz_const.color_list[self.temp_index], 
                                             label=str(self.temprature)+u'\u2103', type=1)
            else:
                self.VI_MPL.generateData(self.dataX[self.temp_index], self.dataY[self.temp_index], type=0)
        else:
            self.measure_times += 1
            self.index = -1
    
    def meas_stop(self):
        self.timer.stop()
        self.stop_all_flow()
        
        Keithley2400.close_inst()
        ai518p_api.set_stop()
         
        QtGui.QMessageBox.information(self,u'提示', u'本次测试完成!')   

    def write_xls(self):
        x_row = 1
        for data in self.dataX[0]:
            x_row += 1
            # data = "%E" % data
            self.table.write(x_row, 0, data)
            
        y_row = 1
        y_colum = 1
        for data_list in self.dataY:
            for data in data_list:
                y_row += 1
                # data = "%E" % data
                self.table.write(y_row, y_colum, data)
            y_row = 1
            y_colum += 1
        
    
    def stop_all_flow(self):
        llj = C_S48(self.flow_port, self.flow1_addr)
        llj.set_valve_close()
        Valve_Ctrl.flowmeter1_close()
        self.valve1_sta.setPixmap(QtGui.QPixmap(":/icon/icons/guan.png"))
        
        llj = C_S48(self.flow_port, self.flow2_addr)
        llj.set_valve_close()
        Valve_Ctrl.flowmeter2_close()
        self.valve2_sta.setPixmap(QtGui.QPixmap(":/icon/icons/guan.png"))

        llj = C_S48(self.flow_port, self.flow3_addr)
        llj.set_valve_close()
        Valve_Ctrl.flowmeter3_close() 
        self.valve3_sta.setPixmap(QtGui.QPixmap(":/icon/icons/guan.png"))

        Valve_Ctrl.airpump_close() 
        self.valve_clean_sta.setPixmap(QtGui.QPixmap(":/icon/icons/guan.png"))
    
    def open_flow(self):
        
        for i in range(0,3):
            if (qmdz_const.VI_GAS[2*i]==2): # 流量计勾选
                flow_value=qmdz_const.VI_GAS[2*i+1]
                if (i==0):
                    llj = C_S48(self.flow_port, self.flow1_addr)
                    llj.set_flow(flow_value)
                    llj.set_valve_ctrl()
                    # llj.comm_close()
                    Valve_Ctrl.flowmeter1_open()
                    self.valve1_sta.setPixmap(QtGui.QPixmap(":/icon/icons/kai.png"))
                    
                elif (i==1):
                    llj = C_S48(self.flow_port, self.flow2_addr)
                    llj.set_flow(flow_value)
                    llj.set_valve_ctrl()
                    # llj.comm_close()
                    Valve_Ctrl.flowmeter2_open()
                    self.valve2_sta.setPixmap(QtGui.QPixmap(":/icon/icons/kai.png"))
                    
                else:
                    llj = C_S48(self.flow_port, self.flow3_addr)
                    llj.set_flow(flow_value)
                    llj.set_valve_ctrl()
                    # llj.comm_close()   
                    Valve_Ctrl.flowmeter3_open() 
                    self.valve3_sta.setPixmap(QtGui.QPixmap(":/icon/icons/kai.png"))
                    
    def disp_flow(self):
        try:
            llj = C_S48(self.flow_port, self.flow1_addr)
            vflow1 = llj.read_dispflow()*self.flow1_range/4095
            self.flow1.setText(str(vflow1))
        except:
            llj.comm_close()
            self.flow1.setText("NA")
        try:
            llj = C_S48(self.flow_port, self.flow2_addr)
            vflow1 = llj.read_dispflow()*self.flow1_range/4095
            self.flow2.setText(str(vflow1))
        except:
            llj.comm_close()
            self.flow2.setText("NA")
        try:
            llj = C_S48(self.flow_port, self.flow3_addr)
            vflow1 = llj.read_dispflow()*self.flow1_range/4095
            self.flow3.setText(str(vflow1))
        except:
            llj.comm_close()
            self.flow3.setText("NA")
            
           
    def get_sys_state(self):
        
        if Valve_Ctrl.get_pcb_state():
            self.pcb_sta.setPixmap(QtGui.QPixmap(":/icon/icons/dlb.png"))
        else:
            QtGui.QMessageBox.warning(self, u'警告', u"电路板未连接!")
            logger.warning("PCB isn't connected!")
            self.pcb_sta.setPixmap(QtGui.QPixmap(":/icon/icons/nodlb.png"))
        
        self.temprature = ai518p_api.get_now_temp()
        if self.temprature != "":
            self.now_T.setText(str(self.temprature))
            self.ai518_sta.setPixmap(QtGui.QPixmap(":/icon/icons/wky.png"))
        else:
            QtGui.QMessageBox.warning(self, u'警告', u"温控仪未连接!")
            logger.warning("AI518P isn't connected!")
            self.ai518_sta.setPixmap(QtGui.QPixmap(":/icon/icons/nowky.png"))
            
        GPIB_PORT = Keithley2400.get_gpibport()
        if GPIB_PORT !="":
            Keithley2400.conncet_inst()
            self.inst_sta.setPixmap(QtGui.QPixmap(":/icon/icons/yb.png"))
            # self.voltage,self.current,self.resistance = Keithley2400.measure_ohms_auto('200e6',qmdz_const.MEAS_MODE)
            self.voltage,self.current,self.resistance = Keithley2400.measure_voltage('1e-6', '100', qmdz_const.MEAS_MODE)
            self.now_v.setText(str(self.voltage))
            self.now_I.setText(str(self.current)) 
            self.now_R.setText(str(self.resistance))
            Keithley2400.close_inst()         
        else:
            QtGui.QMessageBox.warning(self, u'警告', u"仪表2400未连接!")
            logger.warning("2400 isn't connected!")
            self.inst_sta.setPixmap(QtGui.QPixmap(":/icon/icons/noyb.png"))  
            
        self.flow_port = read_config(qmdz_const.SYS_CONF_PATH, 'HMTS48', 'port') 
        self.flow1_addr =  read_config(qmdz_const.SYS_CONF_PATH, 'HMTS48', 'flow1_addr')
        self.flow1_range =  int(read_config(qmdz_const.SYS_CONF_PATH, 'HMTS48', 'flow1_range'))
        self.flow2_addr =  read_config(qmdz_const.SYS_CONF_PATH, 'HMTS48', 'flow2_addr')
        self.flow2_range = int(read_config(qmdz_const.SYS_CONF_PATH, 'HMTS48', 'flow2_range'))
        self.flow3_addr =  read_config(qmdz_const.SYS_CONF_PATH, 'HMTS48', 'flow3_addr') 
        self.flow3_range =  int(read_config(qmdz_const.SYS_CONF_PATH, 'HMTS48', 'flow3_range'))    
             
def dispVI_Dialog():
    VI_APP = VI_TEST()
    VI_APP.show()
    VI_APP.exec_()
    return True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    UI_VI = VI_TEST()
    UI_VI.show()
    sys.exit(app.exec_())