# -*- coding: utf-8 -*-
'''
Created on 2015-6-1

@author: Administrator
'''
import serial 
import struct
from mylog import logger
from init_op import read_config
from qmdz_const import SYS_CONF_PATH

ADDR = read_config(SYS_CONF_PATH, 'AI518P', 'addr')
PORT = read_config(SYS_CONF_PATH, 'AI518P', 'port')
BAUD = read_config(SYS_CONF_PATH, 'AI518P', 'baud')

para_dict = {'SteP'  : 0x00,
             'HIAL': 0x01,
             'LoAL': 0x02,
             'HdAL': 0x03,
             'LdAL': 0x04,
             'AHYS': 0x05,
             'CtrL': 0x06,
             'M5': 0x07,
             'P': 0x08,
             't': 0x09,
             'CtI': 0x0A,
             'InP': 0x0B,
             'dPt': 0x0C,
             'SCL': 0x0D,
             'SCH': 0x0E,
             'AOP': 0x0F,
             'Scb': 0x10,
             'OPt': 0x11,
             'OPL': 0x12,
             'OPH': 0x13,
             'AF': 0x14,
             'RUNSTA': 0x15,
             'Addr': 0x16,
             'FILt': 0x17,
             'AmAn' : 0x18,
             'Loc'  : 0x19,
             'c01' : 0x1A,
             't01' : 0x1B,             
             'c02' : 0x1C,
             't02' : 0x1D, 
             'c03' : 0x1E,
             't03' : 0x1F
              }


class C_AI518P():
    def __init__(self, addr, com_port, baud):
        self.addr = int(addr)
        self.com_port = com_port
        self.baud = int(baud)
        
    def comm_connect(self):
        try:
            self.ser = serial.Serial(self.com_port, self.baud, timeout=1)
        except:
            logger.error("can not find port:%s" % self.com_port)
            self.ser = None
        return self.ser
    
    def get_read_crc(self,para_code):
        crc_value = (para_code*256 + 82 + self.addr)%65535
        return crc_value
        
    def get_write_crc(self,para_code,para_value):
        crc_total = para_code*256 + 67 + para_value + self.addr
        if crc_total < 0:
            crc_total = crc_total + 65536
        crc_value = crc_total%65535       
        return crc_value
    
    def read_para(self,para_name):
        self.ser = self.comm_connect()
        if self.ser:
            addr_code = self.addr + 0x80
            para_code = para_dict[para_name]
            crc_value = self.get_read_crc(para_code)
            crc_low = crc_value%256
            crc_high = crc_value/256
            cmdstr = struct.pack("BBBBBBBB",addr_code,addr_code,82,para_code,0,0,crc_low,crc_high)
            # print "cmdstr:",repr(cmdstr)
            self.ser.write(cmdstr)
            try:
                para_str = self.ser.read(10)
            except:
                self.comm_close()
                return None
            if para_str == "":
                self.comm_close()
                return ""
            PV,SV,MV,STA,PARA_VAL,CRC = struct.unpack("hhbbhH",para_str)
            bSTA = bin(STA)
            rPV = self.para_convert(PV)
            rSV = self.para_convert(SV)
            # print rPV,rSV,MV,bSTA,PARA_VAL,CRC
            data_dict = {'PV':rPV,'SV':rSV,'MV':MV,'STA':bSTA,'PARA':PARA_VAL}
            self.comm_close()
            return data_dict

    def write_para(self,para_name,para_value):
        self.comm_connect()
        addr_code = self.addr + 0x80
        para_code = para_dict[para_name]
        crc_value = self.get_write_crc(para_code,para_value)
        # print "crc:",crc_value
        crc_low = crc_value%256
        crc_high = crc_value/256
        if (para_value<0):
            para_value = 65536 + para_value
        value_low = para_value%256
        vlaue_high = para_value/256
        cmdstr = struct.pack("BBBBBBBB",addr_code,addr_code,67,para_code,value_low,vlaue_high,crc_low,crc_high)
        self.ser.write(cmdstr)
        para_str = self.ser.read(10)
        PV,SV,MV,STA,PARA_VAL,CRC = struct.unpack("hhbbhH",para_str)
        bSTA = bin(STA)
        EXP_CRC = (PV + SV + (STA*256 + MV) + PARA_VAL + self.addr)%65535
        # print PV,SV,MV,bSTA,PARA_VAL,CRC
        self.comm_close()
    
    def get_point(self):
        addr_code = self.addr + 0x80
        para_code = para_dict['dPt']
        crc_value = self.get_read_crc(para_code)
        crc_low = crc_value%256
        crc_high = crc_value/256
        cmdstr = struct.pack("BBBBBBBB",addr_code,addr_code,82,para_code,0,0,crc_low,crc_high)
        self.ser.write(cmdstr)
        para_str = self.ser.read(10)
        PV,SV,MV,STA,PARA_VAL,CRC = struct.unpack("hhbbhH",para_str)
        point_num = PARA_VAL
        return point_num
    
    def para_convert(self,para_value):
        
        point_num = self.get_point()
        if point_num >= 128:
            para_value = para_value/10
            point_num = point_num - 128
        
        if point_num == 0:
            real_para = para_value
        elif point_num == 1:
            real_para = para_value / 10.0
        elif point_num == 2:
            real_para = para_value / 100.0
        elif point_num == 3:
            real_para = para_value / 1000.0
        else:
            logger.error("point_num error!")
            
        return  real_para
    
    def get_now_temp(self):
        
        para_dict = self.read_para('SteP')
        if para_dict != "":
            temp = para_dict['PV']
        else:
            temp = ""
        return temp
    
    def get_sv(self):
        
        sv_value = self.read_para('SteP')['SV']
        return sv_value
    
    def get_psv(self):
        para_dict = self.read_para('SteP')
        pv = para_dict['PV']
        sv = para_dict['SV']
        return pv,sv
    
    def set_hold(self):
        self.write_para('RUNSTA',4)  #HOLD仪表暂停运行
        
    def set_stop(self):
        try:
            self.write_para('RUNSTA',12)  #HOLD仪表暂停运行 
        except:
            logger.error("stop ai518p failed!")       
        
    def comm_close(self):
        self.ser.close()
        
    def set_518p_constmode(self,now_temp,target_temp,up_slop,down_slop):
        
        self.write_para('c01',now_temp*10)#设置c01为当前温度
        self.write_para('RUNSTA',4)  #HOLD仪表暂停运行
        self.write_para('SteP',1)  #设置程序段为1
        if target_temp > now_temp:
            rasie_time = (target_temp-now_temp)/up_slop 
        else:
            rasie_time = (now_temp-target_temp)/down_slop 
        self.write_para('t01',rasie_time) #设置t01为升温时间
        self.write_para('c02',target_temp*10)#设置c02为目标温度  
        self.write_para('t02',1)  #设置t02为保温时间 分钟
        self.write_para('c03',target_temp*10)#设置c03为目标温度  
        self.write_para('t03',-2)  #设置t03为-2，表示运行后执行第1条曲线（2-4）FFFE
        self.write_para('RUNSTA',0)  #仪表开始运行
        
ai518p_api = C_AI518P(ADDR, PORT, BAUD)
        
if __name__ == "__main__":
    
    #ai518.comm_connect()
#     print "write"
    # ai518.set_518p_constmode(15, 20)
    res = ai518p_api.write_para('RUNSTA', 12)
    #res = ai518.read_para('RUNSTA')
    print res
    temp = ai518p_api.get_now_temp()
    print temp
    #ai518.para_convert(0) 
# PAF=A×1+B×2 +C×4 +D×8+E×16+F×32    
# 鍝堝搱鍝堬紝鍙堝弬鑰冪綉涓婄殑鎸囧鐞㈢（浜嗕竴浼氬紕鍑烘潵浜嗭紝鍒嗕韩缁欏ぇ瀹躲��
# 杩欓噷鎴戜滑瀵煎叆binascii妯″潡锛岃繘琛岃繘鍒惰浆鎹紝鍦ㄥ彂閫佹暟鎹墠鍏堟妸鍗佽繘鍒舵暟鎹浆鎹负鍗佸叚杩涘埗鍗冲彲鍙戦��
# 鍓嶉潰鐨勪覆鍙ｆ搷浣滅渷鐣�
# >>> import binascii
# >>> a="FF 55 AA 66 88"
# >>> a=a.split()
# >>> for i in range(len(a)):
#               a=binascii.a2b_hex(a)        
# >>> a                       #杩欐椂a鐨勫唴瀹瑰凡缁忚浆涓哄崄鍏繘鍒讹紝鎴戜滑鍙戦�佸嵆鍙�
# ['\xff', 'U', '\xaa', 'f', '\x88']
# >>> comm.write(a)
# COM1,Wirte(8): 81 81 52 01 00 00 53 01  | 浜朢\#1\#0\#0S\#1 璇籋1AL 
# COM1, Read(1): 3B  | ;
# COM1, Read(9): 33 E8 03 00 51 E8 03 0C 8C  | 3閼�#3\#0Q閼�#3\#12
# COM1,Wirte(8): 81 81 43 01 E8 03 2C 05  | 浜朇\#1閼�#3,\#5    璁剧疆H1AL 1000
# COM1, Read(1): 3B  | ;
# COM1, Read(9): 33 E8 03 00 51 E8 03 0C 8C  | 3閼�#3\#0Q閼�#3\#12

# C01 t01 ~ C30 t30  1AH - 55H
# 当前程序段运行时间                      56H