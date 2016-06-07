# -*- coding: utf-8 -*-
import sys
import os

from init_op import read_config
# ROOT_PATH = os.path.split(os.path.realpath(__file__))[0]

if getattr(sys, 'frozen', None):
    ROOT_DIR = os.path.dirname(sys.executable)
else:
    ROOT_DIR = os.path.dirname(__file__)


VI_CONF_PATH = ROOT_DIR + "\conf\VI_CONF.ini"

ST_CONF_PATH = ROOT_DIR + "\conf\ST_CONF.ini"

SC_CONF_PATH = ROOT_DIR + "\conf\SC_CONF.ini"

SYS_CONF_PATH = ROOT_DIR + "\conf\SYS_CONF.ini"


vrange_dict = {0:"AUTO", 1:"1e-6", 2:"10e-6", 3:"100e-6",4:"1e-3", 5:"10e-3", 
               6:"100e-3", 7:"1", 8:"10", 9:"210"}

irange_dict= {0:"AUTO", 1:"10e-9", 2:"100e-9", 3:"1e-6", 4:"10e-6", 5:"100e-6", 
              6:"1e-3", 7:"10e-3", 8:"100e-3", 9:"1"}

gas_coef = {0:1.000, 1:1.400, 2:0.446, 3:0.785, 4:0.515, 5:0.610, 6:0.500,
            7:0.250, 8:0.410, 9:0.350, 10:0.300, 11:0.250, 12:0.260, 13:1.000,
            14:0.740, 15:0.790, 16:1.010, 17:1.000, 18:1.400, 19:1.400, 20:1.000,
            21:0.510, 22:0.990, 23:0.710, 24:1.400, 25:0.985, 26:0.630, 27:0.280,
            28:0.620, 29:1.360}

res_range = {0:"100", 1:"1e3", 2:"10e3", 3:"100e3", 4:"1e6", 5:"10e6", 6:"100e6", 7:"200e6"}

res_det = 0

VI_ILIST = []
IV_VLIST = []
VI_GAS = []

ST_GAS_AUTO = [0,0,0,0,0,0,0,0]
ST_GAS_MODE = 0 # 0:自动控制   1：手动

SC_GAS_MODE = 0 # 0:自动控制   1：手动
SC_FLOW1 = []
SC_FLOW2 = []
SC_FLOW3 = []
SC_GAS_PARA = []

hold_time = 60
low_offset = 0.2
high_offset = 1
up_slot = 1
down_slot = 1
critical_temp = 500
measure_times = 1
temp_list = []

Auto_Range = 1

# 2400设置全局变量
MEAS_MODE = 0 #0：2线制，1：4线制
OUTPUT_MODE = 0 # 0：脉冲输出，1：连续输出
VI_MODE = 1


# 测试时间段
TIME_t1 = 0
TIME_t2 = 0
TIME_t3 = 0
TIME_t4 = 0
TIME_SUM = 0

#[流量计1状态，流量值1,流量计2状态，流量值2,流量计3状态，流量值3,空气状态，空气流量值,]
t1_gas = []
t2_gas = []
t3_gas = []
t4_gas = []


flowmeter1_state = 0
flowmeter2_state = 0
flowmeter3_state = 0
airpump_state = 0

color_list = ["Aqua","Black","Fuchsia","Gray","Green","Lime","Maroon","Navy",
              "Red","Silver","Teal","Yellow","Blue","Olive","Purple","White"]

PARA_NAME = ['SteP','HIAL','LoAL','HdAL','LdAL','AHYS','CtrL','M5',
            'P','t','CtI','InP','dPt','SCL','SCH','AOP',
            'Scb','OPt','OPL','OPH','AF','RUNSTA','Addr','FILt',
            'AmAn','Loc','c01','t01','c02','t02', 'c03','t03']

PARA_DEFAULT = [1,8000,-1960,9999,9999,2,3,50,65,20,2,0,1,0,
                5000,5543,0,0,0,100,6,12,1,10,27,808]


def get_range(key):
    key_value = read_config(SYS_CONF_PATH, 'HMTS48', key)
    return key_value

flow1_range = int(get_range('flow1_range'))
flow2_range = int(get_range('flow2_range'))
flow3_range = int(get_range('flow3_range'))
