# -*- coding: utf-8 -*-

"""
Module implementing ST_GUI.
"""
import os
import sys
import time
import xlwt
import numpy as np
from math import *
from PyQt4 import QtGui
from PyQt4.QtGui import QDialog,QApplication
from PyQt4.QtCore import pyqtSignature, QTimer, SIGNAL

script_path = os.getcwd()
root_path = os.path.dirname(script_path)
sys.path.insert(0,root_path)

from Ui_SC_main import Ui_SC_APP

from SC_2400 import dispSC_2400
from SC_gas_set import dispSC_gas
from coordinate import disp_coord

from INST.AI518P import ai518p_api
from INST.HMT_S48 import C_S48
from INST.INST2400 import Keithley2400
from INST.valve_ctrl import Valve_Ctrl

import qmdz_const

from mylog import logger

from init_op import read_config

class SC_GUI(QDialog, Ui_SC_APP):
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
        self.vi_mode = 0

    
    @pyqtSignature("bool")
    def on_log_state_toggled(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        logger.info("log!")
    
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
        dispSC_2400()
        
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
    def on_GAS_SET_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        dispSC_gas()
        self.res_offset = int(read_config(qmdz_const.SC_CONF_PATH, 'GAS', 'res_offset'))
        self.res_hold = int(read_config(qmdz_const.SC_CONF_PATH, 'GAS', 'res_hold'))
        self.t_resp = int(read_config(qmdz_const.SC_CONF_PATH, 'GAS', 'response')) 
        self.t_recy = int(read_config(qmdz_const.SC_CONF_PATH, 'GAS', 'recovery')) 
        self.measure_times = int(read_config(qmdz_const.SC_CONF_PATH, 'GAS', 'repeat'))
        print self.measure_times

    
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
            self.SC_MPLS.setCurrentIndex(0)

    @pyqtSignature("bool")
    def on_SC_Curve_toggled(self, checked):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if checked:
            self.SC_MPLS.setCurrentIndex(1)
            if self.dataS == []:
                QtGui.QMessageBox.information(self,u'提示', u'请先进行R-t测试!')
            else:
                self.SC_MPL.generateData(self.dataC, self.dataS[0:9], type=1)
    

    @pyqtSignature("bool")
    def on_f1_open_toggled(self, checked):
        if checked:
            logger.info("f1 open")
        else:
            logger.info("f1 close")
            
    @pyqtSignature("bool")
    def on_f2_open_toggled(self, checked):
        if checked:
            logger.info("f2 open")
        else:
            logger.info("f2 close")
            
    @pyqtSignature("bool")
    def on_f3_open_toggled(self, checked):
        if checked:
            logger.info("f3 open")
        else:
            logger.info("f3 close")
    
    @pyqtSignature("")
    def on_SC_start_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        logger.info("test start!")
        self.xls_name = str(self.save_path.text() + '/'+ self.sample_id.text() + '-'+ time.strftime("%m%d%H%M")+ ".xls")
        self.xtime = 0
        self.meas_mode = 0
        self.test_times = 1
        self.c_index = 0
     
        self.dataC = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
        self.Sens = []
        self.dataS = []
        self.dataX = []
        self.dataY = []
        self.dataX.append([])
        self.dataY.append([])
        self.Rt_MPL.clear_curve()
        self.SC_MPL.clear_curve()
        
        self.get_inst_conf()
        
        if self.vi_mode:
            Keithley2400.measure_voltage(self.src_curr, self.vlimit, self.meas_type)
        else:
            Keithley2400.measure_current(self.src_vol, self.ilimit, self.meas_type)        
        # self.ref_time = int(time.time())
        self.timer.start(1000)
        
    
    @pyqtSignature("")
    def on_SC_stop_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        logger.info("test stop!")
        self.meas_stop()
    
    @pyqtSignature("")
    def on_SC_save_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.xls_write()
        self.xls.save(self.xls_name)
        # pic_path = self.xls_name[:-4] + ".png"
        # self.Rt_MPL.save_curve(str(pic_path))
        QtGui.QMessageBox.information(self,u'提示', (u'测试数据%s保存成功!' % self.xls_name))


    def meas_stop(self):
        self.timer.stop()
        # Keithley2400.close_inst()
        self.stop_all_flow()
        ai518p_api.set_stop()
         
        QtGui.QMessageBox.information(self,u'提示', u'本次测试完成!')  
        
          
    def measure(self):
        self.disp_flow()
        self.SC_measure()
    
    def SC_measure(self):
        self.xtime += 1
        self.run_time.setText(str(self.xtime))
        # self.dataX[self.c_index].append(self.xtime)
        self.now_time = int(time.time())
        if self.test_times <= self.measure_times:
            if qmdz_const.SC_GAS_MODE:
                self.Rt_meas_manul()
            else:
                self.Rt_meas_auto()      
        else:
            self.c_index += 1
            print "c index:",self.c_index
            if self.c_index < 10:
                self.xtime = 0
                self.test_times = 1
                self.dataX.append([])
                self.dataY.append([])
                self.dataS.append(np.mean(self.Sens))
                self.Sens = []
                # self.open_flow(qmdz_const.SC_GAS_PARA[self.c_index])
                print "dataX:",self.dataX
                print "dataY:",self.dataY
                print "dataS:",self.dataS
            else:
                self.meas_stop() 
    
    
    def Rt_meas_auto(self):
        self.dataX[self.c_index].append(self.xtime)
        if self.xtime == 1:
            self.ref_time = int(time.time())
            self.response = 1
            self.open_flow(qmdz_const.SC_GAS_PARA[self.c_index])
        if self.now_time > self.ref_time + self.res_hold and self.response == 1: # 响应阶段
            res_array = np.array(self.dataY[self.c_index][-self.res_hold:])
            print np.std(res_array)
            if np.std(res_array) <= self.res_offset:
                self.res_low = np.mean(res_array)
                print "response stable++++++++++++++++++++++",self.res_low
                gas_args = [0,0,0,0,0,0,2,0]
                self.open_flow(gas_args)
                self.response = 0
                self.ref_time = int(time.time())
                self.resp_time = self.xtime
                
        if self.response == 0:
            # 恢复时间与响应时间对称        
            if self.now_time > self.ref_time + self.resp_time:  # 恢复阶段
                self.res_high = self.dataY[self.c_index][-1]
                print "recovery stable++++++++++++++++++++++",self.res_high
                gas_args = [0,0,0,0,0,0,0,0]
                self.open_flow(gas_args)
                self.response = 1
                self.ref_time = int(time.time())
                self.test_times += 1
                self.Sens.append(self.res_high/self.res_low)
                print "Senstive:",self.Sens
                self.open_flow(qmdz_const.SC_GAS_PARA[self.c_index])
                return
            else:
                pass
                # self.dataX[self.c_index].append(self.xtime)
        
        self.get_resistance()
        
    
    def Rt_meas_manul(self):
        if self.xtime == 1:
            self.ref_time = int(time.time())
            self.response = 1
            self.open_flow(qmdz_const.SC_GAS_PARA[self.c_index])
        if self.now_time > self.ref_time + self.t_resp and self.response == 1:
            print "open pump"
            self.response = 0
            gas_args = [0,0,0,0,0,0,2,0]
            self.open_flow(gas_args)
        if self.now_time > self.ref_time + self.t_resp + self.t_recy and self.response == 0:
            self.response = 1
            gas_args = [0,0,0,0,0,0,0,0]
            self.open_flow(gas_args)
            self.test_times += 1
            self.ref_time = int(time.time())

            self.res_high = self.dataY[self.c_index][-1]
            self.res_low = self.dataY[self.c_index][self.t_resp]
            self.Sens.append(self.res_high/self.res_low)
            print "Senstive:",self.Sens
            self.open_flow(qmdz_const.SC_GAS_PARA[self.c_index])
            return
        else:
            self.dataX[self.c_index].append(self.xtime)

        self.get_resistance()
        
    def get_resistance(self):
        if self.vi_mode:
            vol,curr,res = Keithley2400.read_vdata()
        else:
            vol,curr,res = Keithley2400.read_idata()
        self.now_R.setText(str(res))
        self.dataY[self.c_index].append(res)
        if len(self.dataX[self.c_index]) == 1:
            self.Rt_MPL.generateData(self.dataX[self.c_index], self.dataY[self.c_index],
                                     style=qmdz_const.color_list[self.c_index], 
                                     label='C' + str(self.c_index+1), type=1)
        else:
            self.Rt_MPL.generateData(self.dataX[self.c_index], self.dataY[self.c_index], type=0)
            
    
    def open_flow(self, args_list):
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
        if self.meas_type:
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
        self.tab_conf.write(11,0,"总流量(mL)")
        self.tab_conf.write(12,0,"流量计1（mL/min）")
        if read_config(qmdz_const.SC_CONF_PATH, 'GAS', 'flow1')=='0':
            self.tab_conf.write(12,1,"0")
        else:
            if read_config(qmdz_const.SC_CONF_PATH, 'GAS', 'flow1_change')=='0':
                self.tab_conf.write(12, 1,
                    read_config(qmdz_const.SC_CONF_PATH, 'GAS', 'flow1_val'))
            elif read_config(qmdz_const.SC_CONF_PATH, 'GAS', 'flow1_change')=='1':
                self.tab_conf.write(12, 1,"10%-90%")
            else:
                self.tab_conf.write(12, 1,"90%-10%")
                
        self.tab_conf.write(13,0,"流量计2（mL/min）")
        if read_config(qmdz_const.SC_CONF_PATH, 'GAS', 'flow2')=='0':
            self.tab_conf.write(13,1,"0")
        else:
            if read_config(qmdz_const.SC_CONF_PATH, 'GAS', 'flow2_change')=='0':
                self.tab_conf.write(13, 1,
                    read_config(qmdz_const.SC_CONF_PATH, 'GAS', 'flow2_val'))
            elif read_config(qmdz_const.SC_CONF_PATH, 'GAS', 'flow2_change')=='1':
                self.tab_conf.write(13, 1,"10%-90%")
            else:
                self.tab_conf.write(13, 1,"90%-10%")
                
        self.tab_conf.write(14,0,"流量计3（mL/min）")
        if read_config(qmdz_const.SC_CONF_PATH, 'GAS', 'flow3')=='0':
            self.tab_conf.write(14,1,"0")
        else:
            if read_config(qmdz_const.SC_CONF_PATH, 'GAS', 'flow3_change')=='0':
                self.tab_conf.write(14, 1,
                    read_config(qmdz_const.SC_CONF_PATH, 'GAS', 'flow3_val'))
            elif read_config(qmdz_const.SC_CONF_PATH, 'GAS', 'flow3_change')=='1':
                self.tab_conf.write(14, 1,"10%-90%")
            else:
                self.tab_conf.write(14, 1,"90%-10%")
        
        self.tab_conf.write(15,0,"电阻偏差范围(Ω)")
        self.tab_conf.write(15, 1,
            read_config(qmdz_const.SC_CONF_PATH, 'GAS', 'res_offset'))
        self.tab_conf.write(16,0,"电阻温度时间(S)")
        self.tab_conf.write(16, 1,
            read_config(qmdz_const.SC_CONF_PATH, 'GAS', 'res_hold'))
        self.tab_conf.write(17,0,"响应时间(S)")
        self.tab_conf.write(17, 1,
            read_config(qmdz_const.SC_CONF_PATH, 'GAS', 'response'))
        self.tab_conf.write(18,0,"恢复时间(S)")
        self.tab_conf.write(18, 1,
            read_config(qmdz_const.SC_CONF_PATH, 'GAS', 'recovery'))
      
        self.tab_Rt = self.xls.add_sheet(u'R-t曲线',cell_overwrite_ok=True)
        self.tab_SC = self.xls.add_sheet(u'S-C曲线',cell_overwrite_ok=True)
        
        self.tab_Rt.write(0,0,u'温度(℃)')
        self.tab_Rt.write(0,1,str(self.temprature) + u'℃')
        self.tab_Rt.write(1,0,u'浓度')
        self.tab_Rt.write(2,0,u'时间(S)')
        for i in xrange(1,len(self.dataY)+1):
            self.tab_Rt.write(1,i,'C'+str(i)) 
            self.tab_Rt.write(2,i,u'电阻(Ω)')
            y_row = 2
            for data in self.dataY[i-1]:
                y_row += 1
                self.tab_Rt.write(y_row, i, str(data))
        
        x_row = 2
        for data in self.dataX[0]:
            x_row += 1
            self.tab_Rt.write(x_row, 0, data)
            
        
        self.tab_SC.write(0, 0, u'浓度')
        self.tab_SC.write(0, 1, u'灵敏度')
        if len(self.dataY)==9:
            for i in xrange(0,9):
                self.tab_SC.write(i+1, 0, self.dataC[i])
                self.tab_SC.write(i+1, 1, self.dataS[i])
        else:    
            for i in xrange(0,len(self.dataY)-1):
                self.tab_SC.write(i+1, 0, self.dataC[i])
                self.tab_SC.write(i+1, 1, self.dataS[i])

        self.style = xlwt.XFStyle
        self.font = xlwt.Font
        self.font.name = 'SimSun'
        self.style.font = self.font

 
def dispSC_Dialog():
    SC_APP = SC_GUI()
    SC_APP.show()
    SC_APP.exec_()
    return True    
    
#运行UI APP
if __name__ == "__main__":
    app = QApplication(sys.argv)
    UI_ST = SC_GUI()
    UI_ST.show()
    sys.exit(app.exec_())    
