# -*- coding: utf-8 -*-

"""
Module implementing ST_GUI.
"""
import os
import sys
import time
import numpy as np
import xlwt
from math import *
from PyQt4 import QtGui
from PyQt4.QtGui import QDialog,QApplication
from PyQt4.QtCore import pyqtSignature, QTimer, SIGNAL

script_path = os.getcwd()
root_path = os.path.dirname(script_path)
sys.path.insert(0,root_path)

from Ui_ST_main import Ui_ST_APP

from ST_2400 import dispST_2400
from ST_gas_set import dispST_gas
from set518p import disp_518P
from coordinate import disp_coord

from INST.AI518P import ai518p_api
from INST.HMT_S48 import C_S48
from INST.INST2400 import Keithley2400
from INST.valve_ctrl import Valve_Ctrl

import qmdz_const

from mylog import logger

from init_op import read_config

class ST_GUI(QDialog, Ui_ST_APP):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.timer = QTimer(self)
        self.connect(self.timer,SIGNAL("timeout()"),self.measure)
        self.get_sys_state()
        # self.get_sys_conf()
        self.RT_test = 0
        self.vi_mode = 0
        self.dataS = []
        self.resp_time = 0 
        self.log_flag = 0

    
    @pyqtSignature("bool")
    def on_log_state_toggled(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if checked:
            self.log_flag = 1
        else:
            self.log_flag = 0
        logger.info(self.log_flag)
    
    @pyqtSignature("")
    def on_btn_savepath_clicked(self):
        """
        Slot documentation goes here.
        """
        self.getPath = QtGui.QFileDialog.getExistingDirectory(self, u"请选择保存目录", "D:/")
        if self.getPath:
            self.save_path.setText(self.getPath)
    
    @pyqtSignature("")
    def on_INST_SET_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        dispST_2400()
    
    def get_inst_conf(self):
        self.meas_type = int(read_config(qmdz_const.ST_CONF_PATH, 'INST', 'meas_mode'))
        self.vi_mode = int(read_config(qmdz_const.ST_CONF_PATH, 'INST', 'vi_mode'))
        self.src_vol = read_config(qmdz_const.ST_CONF_PATH, 'INST', 'iv_voltage')
        self.iv_unit = read_config(qmdz_const.ST_CONF_PATH, 'INST', 'iv_unit')
        self.ilimit = qmdz_const.irange_dict[int(read_config(qmdz_const.ST_CONF_PATH, 'INST', 'iv_range'))]
        
        self.src_curr = read_config(qmdz_const.ST_CONF_PATH, 'INST', 'vi_current') 
        self.vi_unit = read_config(qmdz_const.ST_CONF_PATH, 'INST', 'vi_unit')
        self.vlimit = qmdz_const.vrange_dict[int(read_config(qmdz_const.ST_CONF_PATH, 'INST', 'vi_range'))]
        
        if self.iv_unit == '0':
            self.src_vol = self.src_vol + 'e-3'
        if self.vi_unit == '0':
            self.src_curr = self.src_curr + 'e-6'
        elif self.vi_unit == '1':
            self.src_curr = self.src_curr + 'e-3'
        print self.vi_mode,self.src_vol,self.ilimit
        print "vi:",self.src_curr,self.vlimit

    
    @pyqtSignature("")
    def on_AI518P_SET_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        disp_518P()
        self.up_slot = qmdz_const.up_slot
        self.down_slot = qmdz_const.down_slot
#         print qmdz_const.hold_time
#         print qmdz_const.low_offset 
#         print qmdz_const.high_offset 
#         print qmdz_const.up_slot 
#         print qmdz_const.down_slot 
#         print qmdz_const.critical_temp 
#         print qmdz_const.measure_times
    
    @pyqtSignature("")
    def on_GAS_SET_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        dispST_gas()
  
    def get_gas_conf(self):
        self.res_offset = int(read_config(qmdz_const.ST_CONF_PATH, 'GAS', 'res_offset'))
        self.res_hold = int(read_config(qmdz_const.ST_CONF_PATH, 'GAS', 'res_hold'))
        
        self.t1 = int(read_config(qmdz_const.ST_CONF_PATH, 'GAS', 't1')) 
        self.t2 = int(read_config(qmdz_const.ST_CONF_PATH, 'GAS', 't2')) 
        self.t3 = int(read_config(qmdz_const.ST_CONF_PATH, 'GAS', 't3')) 
        self.t4 = int(read_config(qmdz_const.ST_CONF_PATH, 'GAS', 't4')) 
        logger.info("GAS SET PARA:%d %d %d %d %d" % (qmdz_const.ST_GAS_MODE,self.t1,self.t2,self.t3,self.t4))
      
        if self.RT_test==0 and qmdz_const.t1_gas == []:
            QtGui.QMessageBox.warning(self,u'警告', u'请先设置气体参数!')
            return False
        
        return True
    
    @pyqtSignature("")
    def on_COORD_SET_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        disp_coord()
    
    @pyqtSignature("bool")
    def on_Rt_Curve_toggled(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if checked:
            self.GAS_SET.setEnabled(True)
            self.f1_open.setEnabled(False)
            self.f2_open.setEnabled(False)
            self.f3_open.setEnabled(False)
            self.flow1.setReadOnly(True)
            self.flow2.setReadOnly(True)
            self.flow3.setReadOnly(True)
            self.ST_MPLS.setCurrentIndex(0)

    @pyqtSignature("bool")
    def on_RT_Curve_toggled(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if checked:
            self.GAS_SET.setEnabled(False)
            self.f1_open.setEnabled(True)
            self.f2_open.setEnabled(True)
            self.f3_open.setEnabled(True)
            self.flow1.setReadOnly(False)
            self.flow2.setReadOnly(False)
            self.flow3.setReadOnly(False)
            self.RT_test = 1
            self.RT_dataX = []
            self.RT_dataY = []
            self.ST_MPLS.setCurrentIndex(1)
    
    @pyqtSignature("bool")
    def on_ST_Curve_toggled(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if checked:
            self.GAS_SET.setEnabled(True)
            self.f1_open.setEnabled(False)
            self.f2_open.setEnabled(False)
            self.f3_open.setEnabled(False)
            self.flow1.setReadOnly(True)
            self.flow2.setReadOnly(True)
            self.flow3.setReadOnly(True)
            self.ST_MPLS.setCurrentIndex(2)
            if self.dataS == []:
                QtGui.QMessageBox.information(self,u'提示', u'请先进行R-t测试!')
            else:
                self.ST_MPL.generateData(qmdz_const.temp_list, self.dataS, type=0)

    @pyqtSignature("bool")
    def on_f1_open_toggled(self, checked):
        if checked:
            if self.flow1.text():
                flow_value = int(self.flow1.text())*4095/qmdz_const.flow1_range
                llj = C_S48(self.flow_port, self.flow1_addr)
                llj.set_flow(flow_value)
                llj.set_valve_ctrl()
                Valve_Ctrl.flowmeter1_open()
                self.valve1_sta.setPixmap(QtGui.QPixmap(":/icon/icons/kai.png"))
            else:
                QtGui.QMessageBox.information(self,u'提示', u'请输入流量值！')
                self.f1_open.setChecked(False)
        else:
            llj = C_S48(self.flow_port, self.flow1_addr)
            llj.set_valve_close()
            Valve_Ctrl.flowmeter1_close()
            self.valve1_sta.setPixmap(QtGui.QPixmap(":/icon/icons/guan.png"))  

    @pyqtSignature("bool")
    def on_f2_open_toggled(self, checked):
        if checked:
            if self.flow2.text():
                flow_value = int(self.flow2.text())*4095/qmdz_const.flow2_range
                llj = C_S48(self.flow_port, self.flow2_addr)
                llj.set_flow(flow_value)
                llj.set_valve_ctrl()
                Valve_Ctrl.flowmeter2_open()
                self.valve2_sta.setPixmap(QtGui.QPixmap(":/icon/icons/kai.png"))
            else:
                QtGui.QMessageBox.information(self,u'提示', u'请输入流量值！')
        else:
            llj = C_S48(self.flow_port, self.flow2_addr)
            llj.set_valve_close()
            Valve_Ctrl.flowmeter2_close()
            self.valve2_sta.setPixmap(QtGui.QPixmap(":/icon/icons/guan.png"))
            
    @pyqtSignature("bool")
    def on_f3_open_toggled(self, checked):
        if checked:
            if self.flow3.text():
                flow_value = int(self.flow3.text())*4095/qmdz_const.flow3_range
                llj = C_S48(self.flow_port, self.flow3_addr)
                llj.set_flow(flow_value)
                llj.set_valve_ctrl()
                Valve_Ctrl.flowmeter3_open()
                self.valve3_sta.setPixmap(QtGui.QPixmap(":/icon/icons/kai.png"))
            else:
                QtGui.QMessageBox.information(self,u'提示', u'请输入流量值！')
        else:
            llj = C_S48(self.flow_port, self.flow1_addr)
            llj.set_valve_close()
            Valve_Ctrl.flowmeter3_close()
            self.valve3_sta.setPixmap(QtGui.QPixmap(":/icon/icons/guan.png"))          
            
    
    @pyqtSignature("")
    def on_ST_start_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        logger.info("test start!")
        self.xls_name = str(self.save_path.text() + '/'+ self.sample_id.text() + '-'+ time.strftime("%m%d%H%M")+ ".xls")
        self.xtime = 0
        self.meas_mode = 0
        self.temp_index = 0
        self.test_times = 1
        self.temp_flag = 0
        self.stable_time = 0

        self.t1_set_flag = 0
        self.t2_set_flag = 0
        self.t3_set_flag = 0
        self.t4_set_flag = 0        
        
        self.Sens = []
        self.dataS = []
        self.dataX = []
        self.dataY = []
        self.dataX.append([])
        self.dataY.append([])
        
        self.Rt_MPL.clear_curve()
        self.RT_MPL.clear_curve()
        self.ST_MPL.clear_curve()
        
        self.get_inst_conf()
        if self.get_gas_conf() == False:
            return
        
        if self.RT_test:
            if len(qmdz_const.temp_list) > 0:
                temp_start = ai518p_api.get_now_temp() + 0.5
                temp_end = qmdz_const.temp_list[-1]
                ai518p_api.set_518p_constmode(temp_start,temp_end,self.up_slot,self.down_slot)
        else:
            if len(qmdz_const.temp_list) > 0:
                temp_now = ai518p_api.get_now_temp() + 0.5
                self.exp_temp = qmdz_const.temp_list[0]
                ai518p_api.set_518p_constmode(temp_now,self.exp_temp,self.up_slot,self.down_slot)

        if self.vi_mode:
            Keithley2400.measure_voltage(self.src_curr, self.vlimit, self.meas_type)
        else:
            Keithley2400.measure_current(self.src_vol, self.ilimit, self.meas_type)
        
        self.ref_time = int(time.time())
        self.timer.start(1000)
        
    
    @pyqtSignature("")
    def on_ST_stop_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        logger.info("test stop!")
        self.meas_stop()
    
    @pyqtSignature("")
    def on_ST_save_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        logger.info("test save!")
        self.xls_write()
        self.xls.save(self.xls_name)
        # pic_path = self.xls_name[:-4] + ".png"
        # self.Rt_MPL.save_curve(str(pic_path))
        QtGui.QMessageBox.information(self,u'提示', (u'测试数据%s保存成功!' % self.xls_name))

    def meas_stop(self):
        self.timer.stop()
        # self.stop_all_flow()
        # Keithley2400.close_inst()
        self.stop_all_flow()
        ai518p_api.set_stop()
         
        QtGui.QMessageBox.information(self,u'提示', u'本次测试完成!')  
        
    def wait_temp(self,temp):
        now_temp = ai518p_api.get_now_temp()
        now_sv = ai518p_api.get_sv() 
        self.now_T.setText(str(now_temp))
        print "wait temp:",self.exp_temp
        if (now_sv == temp):
            if (fabs(now_temp-now_sv)<=qmdz_const.low_offset):
                self.stable_time = self.stable_time + 1
            else:
                self.stable_time = 0
            if self.stable_time >= qmdz_const.hold_time:
                self.temp_flag = 1
                self.sys_state.setText("Temp %s stable, begin measure!" % temp)
            
    def measure(self):
        
        # self.meas_time.setText(str(self.runtime))
        # if self.gas_set:
        self.disp_flow()
        if self.RT_test:
            self.RT_measure()
        else:
            self.Rt_measure()
            
 
    def RT_measure(self):
        
        now_temp = float(ai518p_api.get_now_temp())
        self.now_T.setText(str(now_temp))
        
        if self.temp_index < len(qmdz_const.temp_list):
            exp_temp = float(qmdz_const.temp_list[self.temp_index])
            if now_temp < qmdz_const.critical_temp:
                if fabs(exp_temp-now_temp) < qmdz_const.low_offset:
                    self.RT_dataX.append(exp_temp)
                    self.temp_index += 1
                    self.RT_plot()
            else:
                if fabs(exp_temp-now_temp) > qmdz_const.high_offset:
                    self.RT_dataX.append(exp_temp)
                    self.temp_index += 1
                    self.RT_plot()
        else:
            self.meas_stop()
    
    def RT_plot(self):
        if self.vi_mode:
            vol,curr,res = Keithley2400.read_vdata()
        else:
            vol,curr,res = Keithley2400.read_idata()
        self.now_R.setText(str(res))
        self.RT_dataY.append(res)
        if len(self.RT_dataY) == 1:
            self.RT_MPL.generateData(self.RT_dataX, self.RT_dataY, self.log_flag, type=1)
        else:
            self.RT_MPL.generateData(self.RT_dataX, self.RT_dataY, self.log_flag, type=0)
    
    def Rt_measure(self):
        # 等待温度达到测量点
        if (self.meas_mode == 0 and len(qmdz_const.temp_list) > 0):
            self.wait_temp(self.exp_temp)
            if (self.temp_flag == 0):
                return
            else:
                self.temp_flag = 0
                self.meas_mode = 1
                self.ref_time = int(time.time())
        else:# 温度稳定，开始测量
            self.xtime += 1
            self.run_time.setText(str(self.xtime))
            # self.dataX[self.temp_index].append(self.xtime)
            self.now_time = int(time.time())
            if self.test_times <= qmdz_const.measure_times:
                if qmdz_const.ST_GAS_MODE:
                    self.Rt_meas_manul()
                else:
                    self.Rt_meas_auto()      
            else:
                if len(qmdz_const.temp_list) > 0:
                    self.temp_index = self.temp_index + 1
                if self.temp_index < len(qmdz_const.temp_list):
                    self.st_temp = self.exp_temp
                    self.exp_temp = qmdz_const.temp_list[self.temp_index]
                    self.meas_mode = 0
                    self.xtime = 0
                    self.test_times = 1
                    self.dataX.append([])
                    self.dataY.append([])
                    self.dataS.append(np.mean(self.Sens))
                    self.Sens = []
                    ai518p_api.set_518p_constmode(self.st_temp,self.exp_temp,self.up_slot,self.down_slot)
                else:
                    self.meas_stop() 
    
    
    def Rt_meas_auto(self):
        if self.xtime == 1:
            self.response = 1
            self.open_flow(qmdz_const.ST_GAS_AUTO)
        if self.now_time > self.ref_time + self.res_hold and self.response == 1: # 响应阶段
            res_array = np.array(self.dataY[self.temp_index][-self.res_hold:])
            print np.std(res_array)
            if np.std(res_array) <= self.res_offset:
                self.res_low = np.mean(res_array)
                print "response stable++++++++++++++++++++++",self.res_low
                gas_args = [0,0,0,0,0,0,2,0]
                self.open_flow(gas_args)
                self.response = 0
                self.ref_time = int(time.time())
                self.resp_time = self.xtime
                print "response time:",self.resp_time
        # 恢复时间与响应时间对称        
        if self.now_time >= self.ref_time + self.resp_time and self.response == 0: # 恢复阶段
            self.res_high = self.dataY[self.temp_index][-1]
            print "recovery stable++++++++++++++++++++++",self.res_high
            gas_args = [0,0,0,0,0,0,0,0]
            self.open_flow(gas_args)
            self.response = 1
            self.ref_time = int(time.time())
            self.test_times += 1
            self.Sens.append(self.res_high/self.res_low)
            print "Senstive:",self.Sens
                
        self.get_resistance()
        

    def Rt_meas_manul(self):
        if(self.now_time <= self.ref_time + self.t1 and self.t1_set_flag==0):
            logger.info("******t1******") 
            self.sys_state.setText(u"响应前期试验中。。。")
            self.open_flow(qmdz_const.t1_gas)
            self.t1_set_flag = 1
        elif(self.now_time > self.ref_time + self.t1 and
            self.now_time <= self.ref_time + self.t1 + self.t2 and
            self.t2_set_flag==0):
            logger.info("******t2******") 
            self.sys_state.setText(u"响应后期试验中。。。")
            self.open_flow(qmdz_const.t2_gas)
            self.t2_set_flag = 1
        elif(self.now_time > self.ref_time + self.t1 + self.t2 and
            self.now_time <= self.ref_time + self.t1 + self.t2 + self.t3 and
            self.t3_set_flag == 0):
            logger.info("******t3******") 
            self.sys_state.setText(u"恢复前期试验中。。。")
            self.open_flow(qmdz_const.t3_gas)
            self.t3_set_flag = 1
        elif(self.now_time > self.ref_time + self.t1 + self.t2 + self.t3 and
            self.now_time <= self.ref_time + self.t1 + self.t2 + self.t3 + self.t4 and
            self.t4_set_flag == 0):
            logger.info("******t4******") 
            self.sys_state.setText(u"恢复后期试验中。。。")
            self.open_flow(qmdz_const.t4_gas)
            self.t4_set_flag = 1
        elif(self.now_time > self.ref_time + self.t1 + self.t2 + self.t3 + self.t4):
            self.stop_all_flow()
            self.ref_time = int(time.time())
            self.t1_set_flag = 0
            self.t2_set_flag = 0
            self.t3_set_flag = 0
            self.t4_set_flag = 0
            self.test_times += 1
            
            self.res_high = self.dataY[self.temp_index][-1]
            self.res_low = self.dataY[self.temp_index][self.t1 + self.t2]
            self.Sens.append(self.res_high/self.res_low)
            print "Senstive:",self.Sens   
        self.get_resistance()
        
    def get_resistance(self):
        
        if self.vi_mode:
            vol,curr,res = Keithley2400.read_vdata()
        else:
            vol,curr,res = Keithley2400.read_idata()
        self.now_R.setText(str(res))
        self.dataX[self.temp_index].append(self.xtime)
        self.dataY[self.temp_index].append(res)
        if len(self.dataX[self.temp_index]) == 1:
            if len(qmdz_const.temp_list) > 0:
                self.Rt_MPL.generateData(self.dataX[self.temp_index], self.dataY[self.temp_index],self.log_flag,
                                         style=qmdz_const.color_list[self.temp_index], 
                                         label=str(qmdz_const.temp_list[self.temp_index])+u'\u2103', type=1)
            else:
                self.Rt_MPL.generateData(self.dataX[self.temp_index], self.dataY[self.temp_index],self.log_flag,
                                         style=qmdz_const.color_list[self.temp_index], 
                                         label=str(self.temprature)+u'\u2103', type=1)
        else:
            self.Rt_MPL.generateData(self.dataX[self.temp_index], self.dataY[self.temp_index], self.log_flag, type=0)
            
    
    def open_flow(self, args_list):
        print args_list
        for i in range(0,4):
            if (args_list[2*i]==2): # 流量计勾选
                flow_value = args_list[2*i+1]
                if (i==0):
                    llj = C_S48(self.flow_port, self.flow1_addr)
                    llj.set_flow(flow_value)
                    llj.set_valve_ctrl()
                    Valve_Ctrl.flowmeter1_open()
                    self.valve1_sta.setPixmap(QtGui.QPixmap(":/icon/icons/kai.png"))
                elif (i==1):
                    llj = C_S48(self.flow_port, self.flow2_addr)
                    llj.set_flow(flow_value)
                    llj.set_valve_ctrl()
                    Valve_Ctrl.flowmeter2_open()
                    self.valve2_sta.setPixmap(QtGui.QPixmap(":/icon/icons/kai.png")) 
                elif (i==2):
                    llj = C_S48(self.flow_port, self.flow3_addr)
                    llj.set_flow(flow_value)
                    llj.set_valve_ctrl()
                    Valve_Ctrl.flowmeter3_open() 
                    self.valve3_sta.setPixmap(QtGui.QPixmap(":/icon/icons/kai.png"))
                else:
                    Valve_Ctrl.airpump_open()
                    self.clean_sta.setPixmap(QtGui.QPixmap(":/icon/icons/kai.png"))
            else:
                if (i==0):
                    llj = C_S48(self.flow_port, self.flow1_addr)
                    llj.set_valve_close()
                    Valve_Ctrl.flowmeter1_close()
                    self.valve1_sta.setPixmap(QtGui.QPixmap(":/icon/icons/guan.png"))
                elif (i==1):
                    llj = C_S48(self.flow_port, self.flow2_addr)
                    llj.set_valve_close()
                    Valve_Ctrl.flowmeter2_close()
                    self.valve2_sta.setPixmap(QtGui.QPixmap(":/icon/icons/guan.png")) 
                elif (i==2):
                    llj = C_S48(self.flow_port, self.flow3_addr)
                    llj.set_valve_close()
                    Valve_Ctrl.flowmeter3_close() 
                    self.valve3_sta.setPixmap(QtGui.QPixmap(":/icon/icons/guan.png"))
                else:
                    Valve_Ctrl.airpump_close()
                    self.clean_sta.setPixmap(QtGui.QPixmap(":/icon/icons/guan.png"))

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
            vflow1 = llj.read_dispflow()*self.flow2_range/4095
            self.flow2.setText(str(vflow1))
        except:
            llj.comm_close()
            self.flow2.setText("NA")
        try:
            llj = C_S48(self.flow_port, self.flow3_addr)
            vflow1 = llj.read_dispflow()*self.flow3_range/4095
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
            
        instState = Keithley2400.conncet_inst()
        if instState:
            self.inst_sta.setPixmap(QtGui.QPixmap(":/icon/icons/yb.png"))     
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
 
        qmdz_const.measure_times = int(read_config(qmdz_const.SYS_CONF_PATH, 'AI518P', 'meas_times'))

        
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
        self.clean_sta.setPixmap(QtGui.QPixmap(":/icon/icons/guan.png"))
        

    def xls_write(self):
        self.xls = xlwt.Workbook(encoding='utf-8')
        self.tab_conf = self.xls.add_sheet(u'配置信息',cell_overwrite_ok=True)
        self.tab_conf.write(0,0,"[试验信息]")
        self.tab_conf.write(1,0,"试验时间：")
        self.tab_conf.write(1,1,time.ctime())
        self.tab_conf.write(2,0,"样品名称：")
        self.tab_conf.write(2,1,str(self.sample_id.text()))
        self.tab_conf.write(3,0,"样品面积：")
        self.tab_conf.write(3,1,str(self.sample_area.text()))
        self.tab_conf.write(4,0,"样品厚度：")
        self.tab_conf.write(4,1,str(self.sample_height.text()))
        self.tab_conf.write(5,0,"温度测量点：")
        self.tab_conf.write(5,1,str(qmdz_const.temp_list))
        self.tab_conf.write(6,0,"[2400配置]")
        self.tab_conf.write(7,0,"测量模式：")
        if self.meas_type == 0:
            self.tab_conf.write(7,1,"二线制")
        else:
            self.tab_conf.write(7,1,"四线制")
        self.tab_conf.write(8,0,"激励电流(A)")
        if self.vi_mode==1:
            self.tab_conf.write(8,1,self.src_curr)
        self.tab_conf.write(9,0,"激励电压(V)")
        if self.vi_mode==0:
            self.tab_conf.write(9,1,self.src_vol)
        self.tab_conf.write(10,0,"[气压配置]")
        self.tab_conf.write(11,0,"工作模式：")
        if qmdz_const.ST_GAS_MODE:
            self.tab_conf.write(11,1,"手动")
        else:
            self.tab_conf.write(11,1,"自动")

        self.tab_conf.write(13,0,"时间（S）")
        self.tab_conf.write(14,0,"流量计1（mL/min）")
        self.tab_conf.write(15,0,"流量计2（mL/min）")
        self.tab_conf.write(16,0,"流量计3（mL/min）")
        self.tab_conf.write(17,0,"空气泵（L/min）")
        if qmdz_const.ST_GAS_MODE:
            self.tab_conf.write(12,1,"响应前期")
            self.tab_conf.write(12,2,"响应后期")
            self.tab_conf.write(12,3,"恢复前期")
            self.tab_conf.write(12,4,"恢复后期")
            self.tab_conf.write(13,1,str(self.t1))
            self.tab_conf.write(14, 1,
                    read_config(qmdz_const.ST_CONF_PATH, 'GAS', 't1_flow1_val'))
            self.tab_conf.write(15, 1,
                    read_config(qmdz_const.ST_CONF_PATH, 'GAS', 't1_flow2_val'))
            self.tab_conf.write(16, 1,
                    read_config(qmdz_const.ST_CONF_PATH, 'GAS', 't1_flow3_val'))
            if read_config(qmdz_const.ST_CONF_PATH, 'GAS', 't1_air')=='1':
                self.tab_conf.write(17,1,"10")
            else:
                self.tab_conf.write(17,1,"0")
            
            self.tab_conf.write(13,2,str(self.t2))
            self.tab_conf.write(14, 2,
                    read_config(qmdz_const.ST_CONF_PATH, 'GAS', 't2_flow1_val'))
            self.tab_conf.write(15, 2,
                    read_config(qmdz_const.ST_CONF_PATH, 'GAS', 't2_flow2_val'))
            self.tab_conf.write(16, 2,
                    read_config(qmdz_const.ST_CONF_PATH, 'GAS', 't2_flow3_val'))
            if read_config(qmdz_const.ST_CONF_PATH, 'GAS', 't2_air')=='1':
                self.tab_conf.write(17,2,"10")
            else:
                self.tab_conf.write(17,2,"0")  
                      
            self.tab_conf.write(13,3,str(self.t3))
            self.tab_conf.write(14, 3,
                    read_config(qmdz_const.ST_CONF_PATH, 'GAS', 't3_flow1_val'))
            self.tab_conf.write(15, 3,
                    read_config(qmdz_const.ST_CONF_PATH, 'GAS', 't3_flow2_val'))
            self.tab_conf.write(16, 3,
                    read_config(qmdz_const.ST_CONF_PATH, 'GAS', 't3_flow3_val'))
            if read_config(qmdz_const.ST_CONF_PATH, 'GAS', 't3_air')=='1':
                self.tab_conf.write(17,3,"10")
            else:
                self.tab_conf.write(17,3,"0")
                
            self.tab_conf.write(13,4,str(self.t4))
            self.tab_conf.write(14, 4,
                    read_config(qmdz_const.ST_CONF_PATH, 'GAS', 't4_flow1_val'))
            self.tab_conf.write(15, 4,
                    read_config(qmdz_const.ST_CONF_PATH, 'GAS', 't4_flow2_val'))
            self.tab_conf.write(16, 4,
                    read_config(qmdz_const.ST_CONF_PATH, 'GAS', 't4_flow3_val'))
            if read_config(qmdz_const.ST_CONF_PATH, 'GAS', 't4_air')=='1':
                self.tab_conf.write(17,4,"10")
            else:
                self.tab_conf.write(17,4,"0")
        else:
            self.tab_conf.write(12, 1, "响应时期")
            self.tab_conf.write(17, 1, '0') 
            if read_config(qmdz_const.ST_CONF_PATH, 'GAS', 'flow1')=='2':
                self.tab_conf.write(14, 1,
                    read_config(qmdz_const.ST_CONF_PATH, 'GAS', 'flow1_val'))
            else:
                self.tab_conf.write(14, 1, '0')
            if read_config(qmdz_const.ST_CONF_PATH, 'GAS', 'flow2')=='2':
                self.tab_conf.write(15, 1,
                    read_config(qmdz_const.ST_CONF_PATH, 'GAS', 'flow2_val'))
            else:
                self.tab_conf.write(15, 1, '0')
            if read_config(qmdz_const.ST_CONF_PATH, 'GAS', 'flow3')=='2':
                self.tab_conf.write(16, 1,
                    read_config(qmdz_const.ST_CONF_PATH, 'GAS', 'flow3_val'))
            else:
                self.tab_conf.write(16, 1, '0')                
                
            self.tab_conf.write(12,2,"恢复时期")
            self.tab_conf.write(14, 2, '0')
            self.tab_conf.write(15, 2, '0')
            self.tab_conf.write(16, 2, '0')
            self.tab_conf.write(17, 2, '10')
            self.tab_conf.write(13, 1, str(self.resp_time))
            self.tab_conf.write(13, 2, str(self.resp_time))
      
        self.tab_Rt = self.xls.add_sheet(u'R-time曲线',cell_overwrite_ok=True)
        self.tab_RT = self.xls.add_sheet(u'R-Temp曲线',cell_overwrite_ok=True)
        self.tab_ST = self.xls.add_sheet(u'S-Temp曲线',cell_overwrite_ok=True)
        

        if len(qmdz_const.temp_list) > 0:
            self.tab_RT.write(0,0,u'温度(℃)')
            self.tab_ST.write(0,0,u'温度(℃)')
            self.tab_ST.write(0,1,u'灵敏度')
            # 未测完保存有问题
            for i in range(0, len(qmdz_const.temp_list)):
                self.tab_RT.write(0,i+1,str(qmdz_const.temp_list[i])+'℃')
                self.tab_RT.write(1,i+1,u'电阻(Ω)')
                self.tab_ST.write(i+1,0,str(qmdz_const.temp_list[i])+'℃')
                self.tab_ST.write(i+1,1,self.dataS[i])
            x_row = 1
            for data in self.dataX[0]:
                x_row += 1
                self.tab_RT.write(x_row, 0, data)

            y_row = 1
            y_colum = 1
            for data_list in self.dataY:
                for data in data_list:
                    y_row += 1
                    self.tab_RT.write(y_row, y_colum, data)
                y_row = 1
                y_colum += 1

        else:
            self.tab_Rt.write(0,0,u'温度(℃)')
            self.tab_Rt.write(1,0,u'时间(S)')
            self.tab_Rt.write(1,1,u'电阻(Ω)')
            self.tab_Rt.write(0,1,str(self.temprature) + u'℃')
            
            x_row = 1
            for data in self.dataX[0]:
                x_row += 1
                self.tab_Rt.write(x_row, 0, data)

            y_row = 1
            for data in self.dataY[0]:
                y_row += 1
                self.tab_Rt.write(y_row, 1, data)
                

        self.style = xlwt.XFStyle
        self.font = xlwt.Font
        self.font.name = 'SimSun'
        self.style.font = self.font
        
    def closeEvent(self, event):
        Keithley2400.close_inst()
        
def dispST_Dialog():
    ST_APP = ST_GUI()
    ST_APP.show()
    ST_APP.exec_()
    return True
    
#运行UI APP
if __name__ == "__main__":
    app = QApplication(sys.argv)
    UI_ST = ST_GUI()
    UI_ST.show()
    sys.exit(app.exec_())    
