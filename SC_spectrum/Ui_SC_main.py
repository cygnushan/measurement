# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\WorkDir\gas-sensing_resistors\SC_spectrum\SC_main.ui'
#
# Created: Wed Jan 20 20:49:15 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from Rt_mplCanvas import Rt_CanvasWidget
from SC_mplCanvas import SC_CanvasWidget

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SC_APP(object):
    def setupUi(self, SC_APP):
        SC_APP.setObjectName(_fromUtf8("SC_APP"))
        SC_APP.resize(800, 600)
        SC_APP.setMinimumSize(QtCore.QSize(800, 600))
        SC_APP.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(12)
        SC_APP.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/icons/lmd.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SC_APP.setWindowIcon(icon)
        self.verticalLayout_13 = QtGui.QVBoxLayout(SC_APP)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.SC_MPLS = QtGui.QStackedWidget(SC_APP)
        self.SC_MPLS.setMinimumSize(QtCore.QSize(480, 320))
        self.SC_MPLS.setMaximumSize(QtCore.QSize(480, 320))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SC_MPLS.setFont(font)
        self.SC_MPLS.setObjectName(_fromUtf8("SC_MPLS"))
        self.Rt_MPL = Rt_CanvasWidget()
        self.Rt_MPL.setObjectName(_fromUtf8("Rt_MPL"))
        self.SC_MPLS.addWidget(self.Rt_MPL)
        self.SC_MPL = SC_CanvasWidget()
        self.SC_MPL.setObjectName(_fromUtf8("SC_MPL"))
        self.SC_MPLS.addWidget(self.SC_MPL)
        self.verticalLayout_10.addWidget(self.SC_MPLS)
        self.log_state = QtGui.QCheckBox(SC_APP)
        self.log_state.setObjectName(_fromUtf8("log_state"))
        self.verticalLayout_10.addWidget(self.log_state)
        self.groupBox_5 = QtGui.QGroupBox(SC_APP)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_18 = QtGui.QLabel(self.groupBox_5)
        self.label_18.setMinimumSize(QtCore.QSize(64, 32))
        self.label_18.setMaximumSize(QtCore.QSize(64, 32))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_12.addWidget(self.label_18)
        self.run_time = QtGui.QLineEdit(self.groupBox_5)
        self.run_time.setMinimumSize(QtCore.QSize(113, 22))
        self.run_time.setMaximumSize(QtCore.QSize(113, 22))
        self.run_time.setReadOnly(True)
        self.run_time.setObjectName(_fromUtf8("run_time"))
        self.horizontalLayout_12.addWidget(self.run_time)
        self.label_5 = QtGui.QLabel(self.groupBox_5)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_12.addWidget(self.label_5)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.label_19 = QtGui.QLabel(self.groupBox_5)
        self.label_19.setMinimumSize(QtCore.QSize(56, 32))
        self.label_19.setMaximumSize(QtCore.QSize(56, 32))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_18.addWidget(self.label_19)
        self.flow1 = QtGui.QLineEdit(self.groupBox_5)
        self.flow1.setMinimumSize(QtCore.QSize(113, 22))
        self.flow1.setMaximumSize(QtCore.QSize(113, 22))
        # self.flow1.setReadOnly(True)
        self.flow1.setObjectName(_fromUtf8("flow1"))
        self.horizontalLayout_18.addWidget(self.flow1)
        self.label_7 = QtGui.QLabel(self.groupBox_5)
        self.label_7.setMinimumSize(QtCore.QSize(48, 32))
        self.label_7.setMaximumSize(QtCore.QSize(48, 32))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_18.addWidget(self.label_7)
        self.f1_open = QtGui.QCheckBox(self.groupBox_5)
        self.f1_open.setText(_fromUtf8(""))
        self.f1_open.setObjectName(_fromUtf8("f1_open"))
        self.horizontalLayout_18.addWidget(self.f1_open)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_18)
        self.verticalLayout_7.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_20 = QtGui.QLabel(self.groupBox_5)
        self.label_20.setMinimumSize(QtCore.QSize(64, 32))
        self.label_20.setMaximumSize(QtCore.QSize(64, 32))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_13.addWidget(self.label_20)
        self.now_R = QtGui.QLineEdit(self.groupBox_5)
        self.now_R.setMinimumSize(QtCore.QSize(113, 22))
        self.now_R.setMaximumSize(QtCore.QSize(113, 22))
        self.now_R.setReadOnly(True)
        self.now_R.setObjectName(_fromUtf8("now_R"))
        self.horizontalLayout_13.addWidget(self.now_R)
        self.label_6 = QtGui.QLabel(self.groupBox_5)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_13.addWidget(self.label_6)
        self.horizontalLayout_20.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.label_26 = QtGui.QLabel(self.groupBox_5)
        self.label_26.setMinimumSize(QtCore.QSize(56, 32))
        self.label_26.setMaximumSize(QtCore.QSize(56, 32))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.horizontalLayout_17.addWidget(self.label_26)
        self.flow2 = QtGui.QLineEdit(self.groupBox_5)
        self.flow2.setMinimumSize(QtCore.QSize(113, 22))
        self.flow2.setMaximumSize(QtCore.QSize(113, 22))
        # self.flow2.setReadOnly(True)
        self.flow2.setObjectName(_fromUtf8("flow2"))
        self.horizontalLayout_17.addWidget(self.flow2)
        self.label_8 = QtGui.QLabel(self.groupBox_5)
        self.label_8.setMinimumSize(QtCore.QSize(48, 32))
        self.label_8.setMaximumSize(QtCore.QSize(48, 32))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_17.addWidget(self.label_8)
        self.f2_open = QtGui.QCheckBox(self.groupBox_5)
        self.f2_open.setText(_fromUtf8(""))
        self.f2_open.setObjectName(_fromUtf8("f2_open"))
        self.horizontalLayout_17.addWidget(self.f2_open)
        self.horizontalLayout_20.addLayout(self.horizontalLayout_17)
        self.verticalLayout_7.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_27 = QtGui.QLabel(self.groupBox_5)
        self.label_27.setMinimumSize(QtCore.QSize(64, 32))
        self.label_27.setMaximumSize(QtCore.QSize(64, 32))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.horizontalLayout_14.addWidget(self.label_27)
        self.now_T = QtGui.QLineEdit(self.groupBox_5)
        self.now_T.setMinimumSize(QtCore.QSize(113, 22))
        self.now_T.setMaximumSize(QtCore.QSize(113, 22))
        self.now_T.setReadOnly(True)
        self.now_T.setObjectName(_fromUtf8("now_T"))
        self.horizontalLayout_14.addWidget(self.now_T)
        self.label_4 = QtGui.QLabel(self.groupBox_5)
        self.label_4.setMinimumSize(QtCore.QSize(0, 16))
        self.label_4.setMaximumSize(QtCore.QSize(32, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_14.addWidget(self.label_4)
        self.horizontalLayout_21.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_28 = QtGui.QLabel(self.groupBox_5)
        self.label_28.setMinimumSize(QtCore.QSize(56, 32))
        self.label_28.setMaximumSize(QtCore.QSize(56, 32))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.horizontalLayout_16.addWidget(self.label_28)
        self.flow3 = QtGui.QLineEdit(self.groupBox_5)
        self.flow3.setMinimumSize(QtCore.QSize(113, 22))
        self.flow3.setMaximumSize(QtCore.QSize(113, 22))
        # self.flow3.setReadOnly(True)
        self.flow3.setObjectName(_fromUtf8("flow3"))
        self.horizontalLayout_16.addWidget(self.flow3)
        self.label_9 = QtGui.QLabel(self.groupBox_5)
        self.label_9.setMinimumSize(QtCore.QSize(48, 32))
        self.label_9.setMaximumSize(QtCore.QSize(48, 32))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_16.addWidget(self.label_9)
        self.f3_open = QtGui.QCheckBox(self.groupBox_5)
        self.f3_open.setText(_fromUtf8(""))
        self.f3_open.setObjectName(_fromUtf8("f3_open"))
        self.horizontalLayout_16.addWidget(self.f3_open)
        self.horizontalLayout_21.addLayout(self.horizontalLayout_16)
        self.verticalLayout_7.addLayout(self.horizontalLayout_21)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout_10.addWidget(self.groupBox_5)
        self.horizontalLayout_15.addLayout(self.verticalLayout_10)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupBox_15 = QtGui.QGroupBox(SC_APP)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_15.sizePolicy().hasHeightForWidth())
        self.groupBox_15.setSizePolicy(sizePolicy)
        self.groupBox_15.setMinimumSize(QtCore.QSize(281, 120))
        self.groupBox_15.setMaximumSize(QtCore.QSize(281, 120))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_15.setFont(font)
        self.groupBox_15.setObjectName(_fromUtf8("groupBox_15"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.groupBox_15)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_32 = QtGui.QHBoxLayout()
        self.horizontalLayout_32.setObjectName(_fromUtf8("horizontalLayout_32"))
        self.label_16 = QtGui.QLabel(self.groupBox_15)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_32.addWidget(self.label_16)
        self.sample_id = QtGui.QLineEdit(self.groupBox_15)
        self.sample_id.setObjectName(_fromUtf8("sample_id"))
        self.horizontalLayout_32.addWidget(self.sample_id)
        self.verticalLayout_4.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_33 = QtGui.QHBoxLayout()
        self.horizontalLayout_33.setObjectName(_fromUtf8("horizontalLayout_33"))
        self.label_21 = QtGui.QLabel(self.groupBox_15)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_33.addWidget(self.label_21)
        self.save_path = QtGui.QLineEdit(self.groupBox_15)
        self.save_path.setObjectName(_fromUtf8("save_path"))
        self.horizontalLayout_33.addWidget(self.save_path)
        self.btn_savepath = QtGui.QPushButton(self.groupBox_15)
        self.btn_savepath.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/icons/folder.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_savepath.setIcon(icon1)
        self.btn_savepath.setIconSize(QtCore.QSize(16, 16))
        self.btn_savepath.setObjectName(_fromUtf8("btn_savepath"))
        self.horizontalLayout_33.addWidget(self.btn_savepath)
        self.verticalLayout_4.addLayout(self.horizontalLayout_33)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.horizontalLayout_35 = QtGui.QHBoxLayout()
        self.horizontalLayout_35.setObjectName(_fromUtf8("horizontalLayout_35"))
        self.label_24 = QtGui.QLabel(self.groupBox_15)
        self.label_24.setMinimumSize(QtCore.QSize(36, 24))
        self.label_24.setMaximumSize(QtCore.QSize(36, 24))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.horizontalLayout_35.addWidget(self.label_24)
        self.sample_area = QtGui.QLineEdit(self.groupBox_15)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sample_area.sizePolicy().hasHeightForWidth())
        self.sample_area.setSizePolicy(sizePolicy)
        self.sample_area.setMinimumSize(QtCore.QSize(40, 22))
        self.sample_area.setMaximumSize(QtCore.QSize(40, 22))
        self.sample_area.setText(_fromUtf8(""))
        self.sample_area.setObjectName(_fromUtf8("sample_area"))
        self.horizontalLayout_35.addWidget(self.sample_area)
        self.label_25 = QtGui.QLabel(self.groupBox_15)
        self.label_25.setMinimumSize(QtCore.QSize(32, 29))
        self.label_25.setMaximumSize(QtCore.QSize(32, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.horizontalLayout_35.addWidget(self.label_25)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_35)
        self.horizontalLayout_34 = QtGui.QHBoxLayout()
        self.horizontalLayout_34.setObjectName(_fromUtf8("horizontalLayout_34"))
        self.label_22 = QtGui.QLabel(self.groupBox_15)
        self.label_22.setMinimumSize(QtCore.QSize(36, 29))
        self.label_22.setMaximumSize(QtCore.QSize(36, 29))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_34.addWidget(self.label_22)
        self.sample_height = QtGui.QLineEdit(self.groupBox_15)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sample_height.sizePolicy().hasHeightForWidth())
        self.sample_height.setSizePolicy(sizePolicy)
        self.sample_height.setMinimumSize(QtCore.QSize(40, 22))
        self.sample_height.setMaximumSize(QtCore.QSize(40, 22))
        self.sample_height.setText(_fromUtf8(""))
        self.sample_height.setObjectName(_fromUtf8("sample_height"))
        self.horizontalLayout_34.addWidget(self.sample_height)
        self.label_23 = QtGui.QLabel(self.groupBox_15)
        self.label_23.setMinimumSize(QtCore.QSize(23, 29))
        self.label_23.setMaximumSize(QtCore.QSize(23, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_23.setFont(font)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout_34.addWidget(self.label_23)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_34)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.verticalLayout_9.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addWidget(self.groupBox_15)
        self.groupBox_2 = QtGui.QGroupBox(SC_APP)
        self.groupBox_2.setMinimumSize(QtCore.QSize(281, 131))
        self.groupBox_2.setMaximumSize(QtCore.QSize(281, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setMargin(10)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.INST_SET = QtGui.QPushButton(self.groupBox_2)
        self.INST_SET.setObjectName(_fromUtf8("INST_SET"))
        self.horizontalLayout.addWidget(self.INST_SET)
        self.AI518P_SET = QtGui.QPushButton(self.groupBox_2)
        self.AI518P_SET.setObjectName(_fromUtf8("AI518P_SET"))
        self.horizontalLayout.addWidget(self.AI518P_SET)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.GAS_SET = QtGui.QPushButton(self.groupBox_2)
        self.GAS_SET.setObjectName(_fromUtf8("GAS_SET"))
        self.horizontalLayout_9.addWidget(self.GAS_SET)
        self.COORD_SET = QtGui.QPushButton(self.groupBox_2)
        self.COORD_SET.setObjectName(_fromUtf8("COORD_SET"))
        self.horizontalLayout_9.addWidget(self.COORD_SET)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.verticalLayout_11.addLayout(self.verticalLayout)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.groupBox_4 = QtGui.QGroupBox(SC_APP)
        self.groupBox_4.setMinimumSize(QtCore.QSize(281, 111))
        self.groupBox_4.setMaximumSize(QtCore.QSize(281, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setMargin(10)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.Rt_Curve = QtGui.QRadioButton(self.groupBox_4)
        self.Rt_Curve.setChecked(True)
        self.Rt_Curve.setObjectName(_fromUtf8("Rt_Curve"))
        self.verticalLayout_3.addWidget(self.Rt_Curve)
        self.SC_Curve = QtGui.QRadioButton(self.groupBox_4)
        self.SC_Curve.setObjectName(_fromUtf8("SC_Curve"))
        self.verticalLayout_3.addWidget(self.SC_Curve)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.SC_start = QtGui.QPushButton(SC_APP)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SC_start.setFont(font)
        self.SC_start.setObjectName(_fromUtf8("SC_start"))
        self.horizontalLayout_2.addWidget(self.SC_start)
        self.SC_stop = QtGui.QPushButton(SC_APP)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SC_stop.setFont(font)
        self.SC_stop.setObjectName(_fromUtf8("SC_stop"))
        self.horizontalLayout_2.addWidget(self.SC_stop)
        self.SC_save = QtGui.QPushButton(SC_APP)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SC_save.setFont(font)
        self.SC_save.setObjectName(_fromUtf8("SC_save"))
        self.horizontalLayout_2.addWidget(self.SC_save)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_15.addLayout(self.verticalLayout_5)
        self.verticalLayout_12.addLayout(self.horizontalLayout_15)
        self.groupBox_3 = QtGui.QGroupBox(SC_APP)
        self.groupBox_3.setMinimumSize(QtCore.QSize(780, 61))
        self.groupBox_3.setMaximumSize(QtCore.QSize(780, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.inst_sta = QtGui.QLabel(self.groupBox_3)
        self.inst_sta.setText(_fromUtf8(""))
        self.inst_sta.setPixmap(QtGui.QPixmap(_fromUtf8(":/icon/icons/noyb.png")))
        self.inst_sta.setObjectName(_fromUtf8("inst_sta"))
        self.horizontalLayout_4.addWidget(self.inst_sta)
        self.pcb_sta = QtGui.QLabel(self.groupBox_3)
        self.pcb_sta.setText(_fromUtf8(""))
        self.pcb_sta.setPixmap(QtGui.QPixmap(_fromUtf8(":/icon/icons/nodlb.png")))
        self.pcb_sta.setObjectName(_fromUtf8("pcb_sta"))
        self.horizontalLayout_4.addWidget(self.pcb_sta)
        self.ai518_sta = QtGui.QLabel(self.groupBox_3)
        self.ai518_sta.setText(_fromUtf8(""))
        self.ai518_sta.setPixmap(QtGui.QPixmap(_fromUtf8(":/icon/icons/nowky.png")))
        self.ai518_sta.setObjectName(_fromUtf8("ai518_sta"))
        self.horizontalLayout_4.addWidget(self.ai518_sta)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_4)
        self.sys_state = QtGui.QLineEdit(self.groupBox_3)
        self.sys_state.setEnabled(False)
        self.sys_state.setObjectName(_fromUtf8("sys_state"))
        self.horizontalLayout_11.addWidget(self.sys_state)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_14 = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_5.addWidget(self.label_14)
        self.valve1_sta = QtGui.QLabel(self.groupBox_3)
        self.valve1_sta.setText(_fromUtf8(""))
        self.valve1_sta.setPixmap(QtGui.QPixmap(_fromUtf8(":/icon/icons/guan.png")))
        self.valve1_sta.setObjectName(_fromUtf8("valve1_sta"))
        self.horizontalLayout_5.addWidget(self.valve1_sta)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_13 = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_3.addWidget(self.label_13)
        self.valve2_sta = QtGui.QLabel(self.groupBox_3)
        self.valve2_sta.setText(_fromUtf8(""))
        self.valve2_sta.setPixmap(QtGui.QPixmap(_fromUtf8(":/icon/icons/guan.png")))
        self.valve2_sta.setObjectName(_fromUtf8("valve2_sta"))
        self.horizontalLayout_3.addWidget(self.valve2_sta)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_15 = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_6.addWidget(self.label_15)
        self.valve3_sta = QtGui.QLabel(self.groupBox_3)
        self.valve3_sta.setText(_fromUtf8(""))
        self.valve3_sta.setPixmap(QtGui.QPixmap(_fromUtf8(":/icon/icons/guan.png")))
        self.valve3_sta.setObjectName(_fromUtf8("valve3_sta"))
        self.horizontalLayout_6.addWidget(self.valve3_sta)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_17 = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_7.addWidget(self.label_17)
        self.clean_sta = QtGui.QLabel(self.groupBox_3)
        self.clean_sta.setText(_fromUtf8(""))
        self.clean_sta.setPixmap(QtGui.QPixmap(_fromUtf8(":/icon/icons/guan.png")))
        self.clean_sta.setObjectName(_fromUtf8("clean_sta"))
        self.horizontalLayout_7.addWidget(self.clean_sta)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/icon/icons/partulab.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_11.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.verticalLayout_12.addWidget(self.groupBox_3)
        self.verticalLayout_13.addLayout(self.verticalLayout_12)
        
        self.AI518P_SET.setEnabled(False)

        self.retranslateUi(SC_APP)
        self.SC_MPLS.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SC_APP)

    def retranslateUi(self, SC_APP):
        SC_APP.setWindowTitle(_translate("SC_APP", "灵敏度-浓度谱", None))
        self.log_state.setText(_translate("SC_APP", "log", None))
        self.groupBox_5.setTitle(_translate("SC_APP", "测量参数", None))
        self.label_18.setText(_translate("SC_APP", "测量时间", None))
        self.label_5.setText(_translate("SC_APP", "S", None))
        self.label_19.setText(_translate("SC_APP", "流量计1", None))
        self.label_7.setText(_translate("SC_APP", "mL/min", None))
        self.label_20.setText(_translate("SC_APP", "当前阻值", None))
        self.label_6.setText(_translate("SC_APP", "Ω", None))
        self.label_26.setText(_translate("SC_APP", "流量计2", None))
        self.label_8.setText(_translate("SC_APP", "mL/min", None))
        self.label_27.setText(_translate("SC_APP", "当前温度", None))
        self.label_4.setText(_translate("SC_APP", "℃", None))
        self.label_28.setText(_translate("SC_APP", "流量计3", None))
        self.label_9.setText(_translate("SC_APP", "mL/min", None))
        self.groupBox_15.setTitle(_translate("SC_APP", "样品信息", None))
        self.label_16.setText(_translate("SC_APP", "样品标识", None))
        self.sample_id.setText(_translate("SC_APP", "SC_test", None))
        self.label_21.setText(_translate("SC_APP", "保存路径", None))
        self.save_path.setText(_translate("SC_APP", "D:/", None))
        self.label_24.setText(_translate("SC_APP", "面积", None))
        self.label_25.setText(_translate("SC_APP", "mm^2", None))
        self.label_22.setText(_translate("SC_APP", "厚度", None))
        self.label_23.setText(_translate("SC_APP", "mm", None))
        self.groupBox_2.setTitle(_translate("SC_APP", "参数设置", None))
        self.INST_SET.setText(_translate("SC_APP", "仪器设置", None))
        self.AI518P_SET.setText(_translate("SC_APP", "温度设置", None))
        self.GAS_SET.setText(_translate("SC_APP", "气压控制", None))
        self.COORD_SET.setText(_translate("SC_APP", "XY坐标设置", None))
        self.groupBox_4.setTitle(_translate("SC_APP", "曲线选择", None))
        self.Rt_Curve.setText(_translate("SC_APP", "R-t曲线", None))
        self.SC_Curve.setText(_translate("SC_APP", "S-C曲线", None))
        self.SC_start.setText(_translate("SC_APP", "开始测量", None))
        self.SC_stop.setText(_translate("SC_APP", "停止测量", None))
        self.SC_save.setText(_translate("SC_APP", "保存数据", None))
        self.groupBox_3.setTitle(_translate("SC_APP", "当前状态", None))
        self.label_14.setText(_translate("SC_APP", "阀门1", None))
        self.label_13.setText(_translate("SC_APP", "阀门2", None))
        self.label_15.setText(_translate("SC_APP", "阀门3", None))
        self.label_17.setText(_translate("SC_APP", "清洗阀", None))

import mypic_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SC_APP = QtGui.QDialog()
    ui = Ui_SC_APP()
    ui.setupUi(SC_APP)
    SC_APP.show()
    sys.exit(app.exec_())
