# -*- coding: utf-8 -*-
'''
Created on 2015

@author: Administrator
'''

import serial,time
import qmdz_const
from mylog import logger
from init_op import read_config

PORT = read_config(qmdz_const.SYS_CONF_PATH, 'PCB', 'port')
BAUD = read_config(qmdz_const.SYS_CONF_PATH, 'PCB', 'baud')

class C_Valve():
    
    def __init__(self, port, baud):
        
        self.baud = baud
        try:
            self.pcb = serial.Serial(port, baud, timeout=1)
        except:
            print "open pcb comm port %s failed!" % port
            
    def connect(self, port):
        try:
            self.pcb = serial.Serial(port, self.baud, timeout=1)
        except:
            print "open pcb comm port %s failed!" % port  
    
    def close(self):
        self.pcb.close()      
    
    def flowmeter1_open(self):
        
        if (qmdz_const.flowmeter1_state == 0):
            qmdz_const.flowmeter1_state = 1
            print "open flowmeter1"
            self.pcb.write("CTRL:A_VALVE:ON\n")
            res = self.pcb.readline()
            time.sleep(0.1)
            return res
        
    def flowmeter1_close(self):
        if (qmdz_const.flowmeter1_state == 1):
            qmdz_const.flowmeter1_state = 0
            print "close flowmeter1"
            self.pcb.write("CTRL:A_VALVE:OFF\n")
            res = self.pcb.readline()
            time.sleep(0.1)
            return res

    def flowmeter2_open(self):
        if (qmdz_const.flowmeter2_state == 0):
            qmdz_const.flowmeter2_state = 1
            print "open flowmeter2"
            self.pcb.write("CTRL:B_VALVE:ON\n")
            res = self.pcb.readline()
            time.sleep(0.1)
            return res
            
        
    def flowmeter2_close(self):
        if (qmdz_const.flowmeter2_state == 1):
            qmdz_const.flowmeter2_state = 0
            print "close flowmeter2"
            self.pcb.write("CTRL:B_VALVE:OFF\n")
            res = self.pcb.readline()
            time.sleep(0.1)
            return res
        
    def flowmeter3_open(self):
        if (qmdz_const.flowmeter3_state == 0):
            qmdz_const.flowmeter3_state = 1
            print "open flowmeter3"
            self.pcb.write("CTRL:V_VALVE:ON\n")
            res = self.pcb.readline()
            time.sleep(0.1)
            return res

    def flowmeter3_close(self):
        if (qmdz_const.flowmeter3_state == 1):
            qmdz_const.flowmeter3_state = 0
            print "close flowmeter3"
            self.pcb.write("CTRL:V_VALVE:OFF\n")
            res = self.pcb.readline()  
            time.sleep(0.1)
            return res
    
    def airpump_open(self):
        if (qmdz_const.airpump_state== 0):
            print "open pump"
            qmdz_const.airpump_state = 1
            self.pcb.write("CTRL:V_PUMP:ON\n")
            res = self.pcb.readline()
            time.sleep(0.1)
            return res

    def airpump_close(self):
        if (qmdz_const.airpump_state== 1):
            print "close pump"
            qmdz_const.airpump_state = 0
            self.pcb.write("CTRL:V_PUMP:OFF\n")
            res = self.pcb.readline()
            time.sleep(0.1)
            return res
        
    
    def get_pcb_state(self):
        self.pcb.write("MEAS:*IDN\n")
        try:
            res = self.pcb.readline()
            if res == "partulab\n":
                return True
            else:
                logger.error("Read return message from PCB timeout!")
                return False
        except Exception,e:
            logger.error("Read from PCB port %s error:%s" % (PORT,e))
            return False
        
Valve_Ctrl = C_Valve(PORT, BAUD)

if __name__ == "__main__":
    
    #Valve_Ctrl.flowmeter1_open()
    #Valve_Ctrl.flowmeter2_open()
    Valve_Ctrl.flowmeter1_close()
    Valve_Ctrl.flowmeter2_close()
#     time.sleep(2)
    # Valve_Ctrl.airpump_open()
#     time.sleep(5)
    Valve_Ctrl.airpump_close()    

           
        