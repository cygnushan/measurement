# -*- coding: utf-8 -*-
'''
Created on 2015-7-4

@author: Administrator
'''

import visa,time,math
from mylog import logger
import qmdz_const

class C2400():
    
    def __init__(self):
        
        self.rm = visa.ResourceManager()
    
    def get_gpibport(self):
        GPIB_port = ""
        rm_list = self.rm.list_resources()
        print rm_list
        for io in rm_list:
            if io.find('GPIB') != -1:
                GPIB_port = io
        if GPIB_port != "":
            logger.info("Find GPIB port:%s" % GPIB_port)
        else:
            logger.warning("CAN NOT FOUND GPIB PORT!")
        return GPIB_port
    
    def conncet_inst(self):
        GPIB_port = self.get_gpibport()
        if GPIB_port != "":
            self.inst = self.rm.open_resource(GPIB_port)
            return True
        else:
            logger.warning("Keithley2400 is not connected!")
            return False
        
    def close_inst(self):
        try:
            self.inst.close()
        except Exception,e:
            logger.error(str(e))
        
    def get_inst_info(self):
        self.devinfo = self.inst.query("*IDN?")
        logger.info(self.devinfo)
        return self.devinfo
    
    def measure_current(self, v_out, i_limit=0, mode=0):
        
        self.inst.write("*RST")
        self.inst.write(":SOUR:FUNC VOLT")
        self.inst.write(":SOUR:VOLT:MODE FIX")
        # self.inst.write(":SOUR:VOLT:RANGE " + v_out)
        self.inst.write(":SOUR:VOLT:LEV " + v_out)
        self.inst.write(":SENS:FUNC \"CURR\"")
        if i_limit:
            self.inst.write(":SENS:CURR:PROT " + i_limit) #i_limit 10e-3 
            self.inst.write(":SENS:CURR:RANG " + i_limit) 
        else:
            self.inst.write(":SENS:CURR:RANG:AUTO ON")
        if mode:
            self.inst.write(":SYST:RSEN ON")
        else:
            self.inst.write(":SYST:RSEN OFF")
        self.inst.write(":OUTP ON")  
        
    def measure_voltage(self, i_out, v_limit=0, mode=0):

        self.inst.write("*RST")
        self.inst.write(":SOUR:FUNC CURR")
        self.inst.write(":SOUR:CURR:MODE FIX")
        # self.inst.write(":SOUR:CURR:RANGE " + i_out)
        self.inst.write(":SOUR:CURR:LEV " + i_out)
        self.inst.write(":SENS:FUNC \"VOLT\"")
        # self.inst.write(":SENS:VOLT:PROT " + v_limit) #i_limit 10e-3   
        if v_limit:
            self.inst.write(":SENS:VOLT:RANG " + v_limit) 
        else:
            self.inst.write(":SENS:VOLT:RANG:AUTO ON") 
        if mode:
            self.inst.write(":SYST:RSEN ON")
        else:
            self.inst.write(":SYST:RSEN OFF")
        self.inst.write(":OUTP ON")
        
    def measure_ohms_auto(self, res_range, mode=0):
        
        self.inst.write("*RST")
        self.inst.write(":SENS:FUNC \"RES\"")
        self.inst.write(":SENS:RES:RANGE " + res_range)
        self.inst.write(":SENS:RES:MODE AUTO")
        if mode:
            self.inst.write(":SYST:RSEN ON")
        else:
            self.inst.write(":SYST:RSEN OFF")
        self.inst.write(":OUTP ON")
        self.inst.write(":READ?")
        
        data = str(self.inst.read())
        data_list = data.split(',')
        voltage = "%3.1E" % float(data_list[0])
        current = "%3.1E" % float(data_list[1])
        resistance = "%3.1E" % float(data_list[2])
        print "resistance = %s" % resistance
        self.output_off()
        return voltage, current, resistance
    
    def measure_ohms_manual(self, volt_level, i_limit, mode=0):
        
        print "measure_ohms_manual:",volt_level,i_limit
        self.inst.write("*RST")
        self.inst.write(":SENS:FUNC \"RES\"")
        self.inst.write(":SENS:RES:MODE MAN")
        
        self.inst.write(":SOUR:FUNC VOLT")
        self.inst.write(":SOUR:VOLT:MODE FIX")
        self.inst.write(":SOUR:VOLT:RANGE " + str(volt_level))
        self.inst.write(":SOUR:VOLT:LEV " + str(volt_level))
        
        self.inst.write(":SENS:CURR:PROT "+ i_limit)#閽充綅鐢垫祦
        self.inst.write(":SENS:CURR:RANGE:AUTO ON")
        if mode:
            self.inst.write(":SYST:RSEN ON")
        else:
            self.inst.write(":SYST:RSEN OFF")
        self.inst.write(":OUTP ON")
        self.inst.write(":READ?")        

        data = str(self.inst.read())
        #print "data:",data
        data_list = data.split(',')
        resistance = float(data_list[2])
        print "resistance = %s" % resistance,type(resistance)
        #self.inst.close()
        return resistance
    
    def vol_linear_sweep(self, start, stop, step, delay, mode=0, base='0'):
        points = (int(stop)-int(start))/int(step) + 1
        self.inst.write("*RST")
        self.inst.write(":SOUR:VOLT " + base) #set bias level to 0V
        self.inst.write(":SOUR:DEL " + delay) #set delay to delay seconds(0.1=100ms)
        self.inst.write(":SOUR:SWE:RANGE BEST")
        self.inst.write(":SOUR:VOLT:MODE SWE")
        self.inst.write(":SOUR:SWE:SPAC LIN")
        self.inst.write(":SOUR:VOLT:START " + start)
        self.inst.write(":SOUR:VOLT:STOP " + stop)
        self.inst.write(":SOUR:VOLT:STEP " + step)
        self.inst.write(":TRIG:COUN " + str(points))
        if mode:
            self.inst.write(":SYST:RSEN ON")
        else:
            self.inst.write(":SYST:RSEN OFF")
        self.inst.write(":OUTP ON")
        self.inst.write(":READ?") 
        while True:
            try:
                print "read"
                data = str(self.inst.read())
                print data
            except Exception,e:
                print e 

    def curr_linear_sweep(self, start, stop, step, delay, mode=0, base='0'):
        points = (float(stop)-float(start))/float(step) + 1
        self.inst.write("*RST")
        #self.inst.write(":SOUR:CURR " + base) #set bias level to 0V
        self.inst.write(":SOUR:FUNC CURR")
        self.inst.write(":SENS:FUNC 'VOLT:DC'")

        self.inst.write(":SOUR:CURR:START " + start)
        self.inst.write(":SOUR:CURR:STOP " + stop)
        self.inst.write(":SOUR:CURR:STEP " + step)
        self.inst.write(":SOUR:CURR:MODE SWE")
        self.inst.write(":SOUR:SWE:RANGE BEST")
        self.inst.write(":SOUR:SWE:SPAC LIN")
        self.inst.write(":TRIG:COUN " + str(int(points)))
        self.inst.write(":SOUR:DEL " + delay) #set delay to delay seconds(0.1=100ms)
        if mode:
            self.inst.write(":SYST:RSEN ON")
        else:
            self.inst.write(":SYST:RSEN OFF")
        self.inst.write(":OUTP ON")
        self.inst.write(":READ?")  
        while True:
            try:
                print "read"
                data = str(self.inst.read())
                print data
            except Exception,e:
                print e
        
    def vol_list_sweep(self, value_list, delay, mode=0, base=0):
        
        self.inst.write("*RST")
        self.inst.write(":SOUR:VOLT " + str(base)) #set bias level to 0V
        self.inst.write(":SOUR:DEL " + delay) #set delay to delay seconds(0.1=100ms)
        self.inst.write(":SOUR:SWE:RANGE BEST")
        self.inst.write(":SOUR:VOLT:MODE LIST")
        self.inst.write(":SOUR:SWE:SPAC LIN")
        self.inst.write(":SOUR:LIST:VOLT " + value_list) #sourece list(1,0,1,0,1,0)
        self.inst.write(":TRIG:COUN " + len(value_list.split(',')))
        if mode:
            self.inst.write(":SYST:RSEN ON")
        else:
            self.inst.write(":SYST:RSEN OFF")
        self.inst.write(":OUTP ON")
        self.inst.write(":READ?")
        
    def curr_list_sweep(self, value_list, delay, mode=0, base=0):
        
        self.inst.write("*RST")
        self.inst.write(":SOUR:CURR " + str(base)) #set bias level to 0V
        self.inst.write(":SOUR:DEL " + delay) #set delay to delay seconds(0.1=100ms)
        self.inst.write(":SOUR:SWE:RANGE BEST")
        self.inst.write(":SOUR:CURR:MODE LIST")
        self.inst.write(":SOUR:SWE:SPAC LIN")
        self.inst.write(":SOUR:LIST:CURR " + value_list) #sourece list(1,0,1,0,1,0)
        self.inst.write(":TRIG:COUN " + len(value_list.split(','))) # length of value_list
        if mode:
            self.inst.write(":SYST:RSEN ON")
        else:
            self.inst.write(":SYST:RSEN OFF")
        self.inst.write(":OUTP ON")
        self.inst.write(":READ?")

    def output_on(self):
        self.inst.write(":OUTP ON") 
        # logger.info("OUTPUT ON!")        
        
    def output_off(self):
        self.inst.write(":OUTP OFF") 
        # logger.info("OUTPUT OFF!")
        
    def inst_init(self):
        self.inst.write("*RST")
    
    def read_idata(self):
        if qmdz_const.OUTPUT_MODE == 0:
            self.output_on()
        self.inst.write(":READ?")
        time.sleep(0.1)
        data = str(self.inst.read())
        data_list = data.split(',')
        voltage = data_list[0]
        current = data_list[1]
        resistance = float(voltage)/float(current)
        # print voltage, current, resistance
            # self.inst.write(":OUTP OFF")
        if qmdz_const.OUTPUT_MODE == 0:
            self.output_off()
        print resistance
        return voltage, current, resistance
    
    def read_vdata(self):
        if qmdz_const.OUTPUT_MODE == 0:
            self.output_on()

        self.inst.write(":READ?")
        data = str(self.inst.read())
        data_list = data.split(',')
        voltage = data_list[0]
        current = data_list[1]
        resistance = float(voltage)/float(current)

        if qmdz_const.OUTPUT_MODE == 0:
            self.output_off()
            # self.inst.write(":OUTP OFF")
        print resistance
        return voltage, current, resistance 

    def set_immediate_trigger(self):
        """ Sets up the measurement to be taken with the internal
        trigger at the maximum sampling rate
        """
        self.inst.write(":ARM:SOUR IMM;:TRIG:SOUR IMM;")

    def config_current_source(self, source_current=0.00e-3,
                              complicance_voltage=0.1, current_range=1.0e-3,
                              auto_range=True):
        """ Set up to source current
        """
        self.source_mode = "Current"
        if auto_range:
            self.inst.write(":sour:func curr;"
                       ":sour:curr:rang:auto 1;"
                       ":sour:curr:lev %g;" % source_current)
        else:
            self.inst.write(":sour:func curr;"
                       ":sour:curr:rang:auto 0;"
                       ":sour:curr:rang %g;:sour:curr:lev %g;" % (
                            current_range, source_current))
        self.inst.write(":sens:volt:prot %g;" % complicance_voltage)
        # self.check_errors()

    def config_voltage_source(self, source_voltage=0.00e-3,
                              compliance_current=0.1, current_range=2.0,
                              voltage_range=2.0, auto_range=True):
        """ Set up to source voltage
        """
        self.source_mode = "Voltage"
        if auto_range:
            self.inst.write("sour:func volt;"
                       ":sour:volt:rang:auto 1;"
                       ":sour:volt:lev %g;" % source_voltage)
        else:
            self.inst.write("sour:func volt;"
                       ":sour:volt:rang:auto 0;"
                       ":sour:volt:rang %g;:sour:volt:lev %g;" % (
                            voltage_range, source_voltage))
        self.inst.write(":sens:curr:prot %g;" % compliance_current)
        # self.check_errors()                

Keithley2400 = C2400()


if __name__ == "__main__":
    
    # Keithley2400.get_gpibport()

    Keithley2400.conncet_inst()
    # Keithley2400.get_inst_info()
    # Keithley2400.output_off()
#     while True:
#         Keithley2400.measure_ohms_manual('5','100e-3')
#         time.sleep(1)
        # Keithley2400.measure_ohms_auto('10e+6')
    # Keithley2400.curr_linear_sweep('1e-7', '1e-6', '1e-7', '0.2')
    # Keithley2400.vol_linear_sweep('1',' 10',' 1', '0.5')
    # Keithley2400.measure_voltage('1e-6','1')
    Keithley2400.measure_current('30')

    for i in range(10):
        time.sleep(1)
        # Keithley2400.config_voltage_source(10.0)
        Keithley2400.read_idata()
    Keithley2400.output_off()
        

        
        
        