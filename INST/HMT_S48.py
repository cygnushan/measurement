# -*- coding: utf-8 -*-
'''
Created on 2015-7-18

@author: Administrator
'''
import minimalmodbus
from mylog import logger
from init_op import read_config
from qmdz_const import SYS_CONF_PATH

inst_addr = 1
baud_rate = 9600
frame_delay = 28*1000/9600.0 
          
REG_CLOSE  = 0
REG_CONTROL = 1
REG_CLEN = 2
REG_STA = 3
REG_AUTOZERO = 4
REG_UNIT = 6
REG_ALRAM = 7
REG_DISPFLOW = 16
REG_SETFLOW = 17
REG_FLOW_RANGE = 48
REG_OFFSET = 49
REG_COEF = 50
REG_ADDR = 51
REG_BAUD = 53
REG_ERR = 60
REG_VER = 61
REG_SN1 = 62
REG_SN2 = 63
ENABLE_PWD = 57

REG_DICT = {
0 :REG_CLOSE,
1 :REG_CONTROL,
2 :REG_CLEN,
3 :REG_STA,
4 :REG_AUTOZERO,
5 :REG_UNIT,
6 :REG_DISPFLOW,
7 :REG_SETFLOW,
8 :REG_FLOW_RANGE,
9 :REG_OFFSET
}

BAUD = read_config(SYS_CONF_PATH, 'HMTS48', 'baud')

class C_S48():
    
    def __init__(self, port, addr):
        
        self.port = port
        self.addr = int(addr)
        minimalmodbus.BAUDRATE = BAUD
        minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True

    def comm_connect(self):
        try:
            self.S48 = minimalmodbus.Instrument(self.port,self.addr)
            return True
        except:
            logger.error("HMT_S48 com port %s addr %s has already opened!" % (self.port,self.addr))
            return False

    def read_para(self,para_reg,dp_num=0):
        result = self.comm_connect()
        if result:
            if para_reg <= 7:
                para_value = self.S48.read_bit(para_reg, 1)
            else:
                para_value = self.S48.read_register(para_reg,dp_num,signed=True)
            self.comm_close()
            return para_value
        else:
            return "NA"

    def write_para(self,para_reg,para_value,dp_num=0):#dp_num锛屽皬鏁扮偣浣嶆暟
        result = self.comm_connect()
        if result:
            if para_reg <= 7:
                if para_value:
                    para_value = 1 # 开关量，只写0/1
                self.S48.write_bit(para_reg, para_value)
            else:
                self.S48.write_register(para_reg, para_value, dp_num, 6)
            self.comm_close()

    def set_flow(self,flow_value,dp_num=0):#dp_num锛屽皬鏁扮偣浣嶆暟 0x0FFF浠ｈ〃婊″害4095
        
        self.write_para(REG_SETFLOW, flow_value, dp_num)

    def read_setflow(self,dp_num=0):
        
        flow = self.read_para(REG_SETFLOW, dp_num)
        return flow

    def read_dispflow(self,dp_num=0):
        
        flow = self.read_para(REG_DISPFLOW, dp_num)
        return flow       
    
    def read_range(self):
        addr = self.read_para(REG_FLOW_RANGE)
        return addr
        
    def set_valve_close(self):
        try:
            self.comm_connect()
            self.S48.write_bit(0, 1, 5)
            self.comm_close()
        except:
            self.comm_close()
            logger.error("set_valve_close failed!")

    def set_valve_ctrl(self):
        try:
            self.comm_connect()
            self.S48.write_bit(1, 1, 5)
            self.comm_close()
        except:
            self.comm_close()
            logger.error("set_valve_ctrl failed!")

    def set_valve_clen(self):
        try:
            self.comm_connect()
            self.S48.write_bit(2, 1, 5)
            self.comm_close()
        except:
            self.comm_close()
            logger.error("set_valve_clen failed!")

    def set_sta_analog(self):
        try:
            self.comm_connect()
            self.S48.write_bit(3, 0, 5)
            self.comm_close()
        except:
            self.comm_close()
            logger.error("set_sta_analog failed!")
        
    def set_sta_digital(self):
        try:
            self.comm_connect()
            self.S48.write_bit(3, 1, 5)
            self.comm_close()
        except:
            self.comm_close()
            logger.error("set_sta_digital failed!")
    
    def set_autozero_on(self):
        try:
            self.comm_connect()
            self.S48.write_bit(4,1,5)
            self.comm_close()
        except:
            self.comm_close()
            logger.error("set_autozero_on failed!")
    
    def set_autozero_off(self):
        try:
            self.comm_connect()
            self.S48.write_bit(4,0,5)
            self.comm_close()
        except:
            self.comm_close()
            logger.error("set_autozero_off failed!")
        
    def read_valve_close(self):
        try:
            self.comm_connect()
            state = self.S48.read_bit(0, 1)
            self.comm_close()
            return state
        except:
            logger.error("read_valve_close failed!")
            self.comm_close()
            return 0

    def read_valve_ctrl(self):
        try:
            self.comm_connect()
            state = self.S48.read_bit(1, 1)
            self.comm_close()
            return state
        except:
            logger.error("read_valve_ctrl failed!")
            self.comm_close()
            return 0

    def read_valve_clen(self):
        try:
            self.comm_connect()
            state = self.S48.read_bit(2, 1)
            self.comm_close()
            return state
        except:
            logger.error("read_valve_clen failed!")
            self.comm_close()
            return 0
    
    def read_sta(self):
        try:
            self.comm_connect()
            sta = self.S48.read_bit(3, 1)
            self.comm_close()
            return sta
        except:
            logger.error("read_sta failed!")
            self.comm_close()
            return 0

    def read_autozero(self):
        try:
            self.comm_connect()
            autozero = self.S48.read_bit(4, 1)
            self.comm_close()
            return autozero
        except:
            logger.error("read_autozero failed!")
            self.comm_close()
            return 0
    
    def read_unit(self): # 0:ml/min 1:L/min
        try:
            self.comm_connect()
            unit = self.S48.read_bit(6, 1)
            self.comm_close()
            return unit
        except:
            logger.error("read_unit failed!")
            self.comm_close()
            return 0
        
    def comm_close(self):
        try:
            self.S48.serial.close()
            # logger.info("HMT_S48 com port %s addr %s closed!" % (self.port,self.addr))
        except:
            logger.info("HMT_S48 com port %s addr %s close failed!" % (self.port,self.addr))

#llj = C_S48('COM1',3)    
    
if __name__ == "__main__":
    port = 'COM1'
    addr = 3
    llj = C_S48(port,2)
    llj.comm_connect()
    #no = llj.set_valve_close()
    # no = llj.read_range()
    #llj.set_flow(1638)
    llj.set_valve_ctrl()
    #time.sleep(2)
    #llj.set_valve_close()
    #llj.set_sta_analog()
    #llj.set_sta_digital()
    #no = llj.read_dispflow()
    no = llj.read_valve_ctrl()
    print "no=",no
    llj.comm_close()
    # llj.disp_flow()
    
