# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\WorkDir\gas-sensing_resistors\VI_spectrum\VI_2400_set.ui'
#
# Created: Tue Apr 12 21:45:55 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 480)
        Dialog.setMinimumSize(QtCore.QSize(640, 480))
        Dialog.setMaximumSize(QtCore.QSize(640, 480))
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/icons/yb.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_8 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setMargin(10)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setSpacing(20)
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_3.addWidget(self.label_12)
        self.res_range = QtGui.QComboBox(Dialog)
        self.res_range.setMaximumSize(QtCore.QSize(16777215, 22))
        self.res_range.setObjectName(_fromUtf8("res_range"))
        self.res_range.addItem(_fromUtf8(""))
        self.res_range.addItem(_fromUtf8(""))
        self.res_range.addItem(_fromUtf8(""))
        self.res_range.addItem(_fromUtf8(""))
        self.res_range.addItem(_fromUtf8(""))
        self.res_range.addItem(_fromUtf8(""))
        self.res_range.addItem(_fromUtf8(""))
        self.res_range.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.res_range)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        self.horizontalLayout_23.addLayout(self.horizontalLayout_3)
        self.res_detect = QtGui.QPushButton(Dialog)
        self.res_detect.setMaximumSize(QtCore.QSize(16777215, 22))
        self.res_detect.setObjectName(_fromUtf8("res_detect"))
        self.horizontalLayout_23.addWidget(self.res_detect)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem)
        self.verticalLayout_7.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setSpacing(20)
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setSpacing(2)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_15.addWidget(self.label_2)
        self.detectV = QtGui.QLineEdit(Dialog)
        self.detectV.setEnabled(True)
        self.detectV.setMaximumSize(QtCore.QSize(16777215, 22))
        self.detectV.setReadOnly(True)
        self.detectV.setObjectName(_fromUtf8("detectV"))
        self.horizontalLayout_15.addWidget(self.detectV)
        self.label_18 = QtGui.QLabel(Dialog)
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_15.addWidget(self.label_18)
        self.horizontalLayout_21.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setSpacing(2)
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.label_19 = QtGui.QLabel(Dialog)
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_19.addWidget(self.label_19)
        self.detectI = QtGui.QLineEdit(Dialog)
        self.detectI.setMaximumSize(QtCore.QSize(16777215, 22))
        self.detectI.setReadOnly(True)
        self.detectI.setObjectName(_fromUtf8("detectI"))
        self.horizontalLayout_19.addWidget(self.detectI)
        self.label_20 = QtGui.QLabel(Dialog)
        self.label_20.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_19.addWidget(self.label_20)
        self.horizontalLayout_21.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setSpacing(2)
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.label_21 = QtGui.QLabel(Dialog)
        self.label_21.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.horizontalLayout_20.addWidget(self.label_21)
        self.detectR = QtGui.QLineEdit(Dialog)
        self.detectR.setMaximumSize(QtCore.QSize(16777215, 22))
        self.detectR.setReadOnly(True)
        self.detectR.setObjectName(_fromUtf8("detectR"))
        self.horizontalLayout_20.addWidget(self.detectR)
        self.label_22 = QtGui.QLabel(Dialog)
        self.label_22.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_20.addWidget(self.label_22)
        self.horizontalLayout_21.addLayout(self.horizontalLayout_20)
        self.verticalLayout_7.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setSpacing(30)
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout.addWidget(self.label_8)
        self.meas_mode = QtGui.QComboBox(Dialog)
        self.meas_mode.setMaximumSize(QtCore.QSize(16777215, 22))
        self.meas_mode.setObjectName(_fromUtf8("meas_mode"))
        self.meas_mode.addItem(_fromUtf8(""))
        self.meas_mode.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.meas_mode)
        self.horizontalLayout_22.addLayout(self.horizontalLayout)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(2)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_8.addWidget(self.label)
        self.output_mode = QtGui.QComboBox(Dialog)
        self.output_mode.setMaximumSize(QtCore.QSize(16777215, 22))
        self.output_mode.setObjectName(_fromUtf8("output_mode"))
        self.output_mode.addItem(_fromUtf8(""))
        self.output_mode.addItem(_fromUtf8(""))
        self.horizontalLayout_8.addWidget(self.output_mode)
        self.horizontalLayout_22.addLayout(self.horizontalLayout_8)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.IV_MODE = QtGui.QRadioButton(Dialog)
        self.IV_MODE.setChecked(True)
        self.IV_MODE.setObjectName(_fromUtf8("IV_MODE"))
        self.verticalLayout_5.addWidget(self.IV_MODE)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.VI_sweep = QtGui.QComboBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VI_sweep.sizePolicy().hasHeightForWidth())
        self.VI_sweep.setSizePolicy(sizePolicy)
        self.VI_sweep.setObjectName(_fromUtf8("VI_sweep"))
        self.VI_sweep.addItem(_fromUtf8(""))
        self.VI_sweep.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.VI_sweep)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(64, 19))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_9.addWidget(self.label_4)
        self.Vstart = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Vstart.sizePolicy().hasHeightForWidth())
        self.Vstart.setSizePolicy(sizePolicy)
        self.Vstart.setMinimumSize(QtCore.QSize(118, 22))
        self.Vstart.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Vstart.setObjectName(_fromUtf8("Vstart"))
        self.horizontalLayout_9.addWidget(self.Vstart)
        self.Vunit1 = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Vunit1.sizePolicy().hasHeightForWidth())
        self.Vunit1.setSizePolicy(sizePolicy)
        self.Vunit1.setMinimumSize(QtCore.QSize(39, 22))
        self.Vunit1.setObjectName(_fromUtf8("Vunit1"))
        self.Vunit1.addItem(_fromUtf8(""))
        self.Vunit1.addItem(_fromUtf8(""))
        self.horizontalLayout_9.addWidget(self.Vunit1)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(64, 19))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_10.addWidget(self.label_5)
        self.Vend = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Vend.sizePolicy().hasHeightForWidth())
        self.Vend.setSizePolicy(sizePolicy)
        self.Vend.setMinimumSize(QtCore.QSize(112, 22))
        self.Vend.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Vend.setObjectName(_fromUtf8("Vend"))
        self.horizontalLayout_10.addWidget(self.Vend)
        self.Vunit2 = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Vunit2.sizePolicy().hasHeightForWidth())
        self.Vunit2.setSizePolicy(sizePolicy)
        self.Vunit2.setMinimumSize(QtCore.QSize(39, 22))
        self.Vunit2.setObjectName(_fromUtf8("Vunit2"))
        self.Vunit2.addItem(_fromUtf8(""))
        self.Vunit2.addItem(_fromUtf8(""))
        self.horizontalLayout_10.addWidget(self.Vunit2)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(64, 19))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_11.addWidget(self.label_6)
        self.Vstep = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Vstep.sizePolicy().hasHeightForWidth())
        self.Vstep.setSizePolicy(sizePolicy)
        self.Vstep.setMinimumSize(QtCore.QSize(112, 22))
        self.Vstep.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Vstep.setObjectName(_fromUtf8("Vstep"))
        self.horizontalLayout_11.addWidget(self.Vstep)
        self.Vunit3 = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Vunit3.sizePolicy().hasHeightForWidth())
        self.Vunit3.setSizePolicy(sizePolicy)
        self.Vunit3.setMinimumSize(QtCore.QSize(39, 22))
        self.Vunit3.setObjectName(_fromUtf8("Vunit3"))
        self.Vunit3.addItem(_fromUtf8(""))
        self.Vunit3.addItem(_fromUtf8(""))
        self.horizontalLayout_11.addWidget(self.Vunit3)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(64, 19))
        self.label_10.setMaximumSize(QtCore.QSize(64, 19))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_17.addWidget(self.label_10)
        self.IV_range = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IV_range.sizePolicy().hasHeightForWidth())
        self.IV_range.setSizePolicy(sizePolicy)
        self.IV_range.setMaximumSize(QtCore.QSize(16777215, 22))
        self.IV_range.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.IV_range.setObjectName(_fromUtf8("IV_range"))
        self.IV_range.addItem(_fromUtf8(""))
        self.IV_range.addItem(_fromUtf8(""))
        self.IV_range.addItem(_fromUtf8(""))
        self.IV_range.addItem(_fromUtf8(""))
        self.IV_range.addItem(_fromUtf8(""))
        self.IV_range.addItem(_fromUtf8(""))
        self.IV_range.addItem(_fromUtf8(""))
        self.IV_range.addItem(_fromUtf8(""))
        self.IV_range.addItem(_fromUtf8(""))
        self.horizontalLayout_17.addWidget(self.IV_range)
        self.verticalLayout.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(64, 19))
        self.label_9.setMaximumSize(QtCore.QSize(64, 19))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_5.addWidget(self.label_9)
        self.IV_loop = QtGui.QLineEdit(self.groupBox_2)
        self.IV_loop.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IV_loop.setObjectName(_fromUtf8("IV_loop"))
        self.horizontalLayout_5.addWidget(self.IV_loop)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.VI_MODE = QtGui.QRadioButton(Dialog)
        self.VI_MODE.setObjectName(_fromUtf8("VI_MODE"))
        self.verticalLayout_6.addWidget(self.VI_MODE)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(2)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_13 = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_12.addWidget(self.label_13)
        self.IV_sweep = QtGui.QComboBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IV_sweep.sizePolicy().hasHeightForWidth())
        self.IV_sweep.setSizePolicy(sizePolicy)
        self.IV_sweep.setObjectName(_fromUtf8("IV_sweep"))
        self.IV_sweep.addItem(_fromUtf8(""))
        self.IV_sweep.addItem(_fromUtf8(""))
        self.horizontalLayout_12.addWidget(self.IV_sweep)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_14 = QtGui.QLabel(self.groupBox_4)
        self.label_14.setMinimumSize(QtCore.QSize(64, 19))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_13.addWidget(self.label_14)
        self.Istart = QtGui.QLineEdit(self.groupBox_4)
        self.Istart.setMinimumSize(QtCore.QSize(112, 22))
        self.Istart.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Istart.setObjectName(_fromUtf8("Istart"))
        self.horizontalLayout_13.addWidget(self.Istart)
        self.Iunit1 = QtGui.QComboBox(self.groupBox_4)
        self.Iunit1.setMinimumSize(QtCore.QSize(39, 22))
        self.Iunit1.setObjectName(_fromUtf8("Iunit1"))
        self.Iunit1.addItem(_fromUtf8(""))
        self.Iunit1.addItem(_fromUtf8(""))
        self.Iunit1.addItem(_fromUtf8(""))
        self.horizontalLayout_13.addWidget(self.Iunit1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_15 = QtGui.QLabel(self.groupBox_4)
        self.label_15.setMinimumSize(QtCore.QSize(64, 19))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_14.addWidget(self.label_15)
        self.Iend = QtGui.QLineEdit(self.groupBox_4)
        self.Iend.setMinimumSize(QtCore.QSize(112, 22))
        self.Iend.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Iend.setObjectName(_fromUtf8("Iend"))
        self.horizontalLayout_14.addWidget(self.Iend)
        self.Iunit2 = QtGui.QComboBox(self.groupBox_4)
        self.Iunit2.setMinimumSize(QtCore.QSize(39, 22))
        self.Iunit2.setObjectName(_fromUtf8("Iunit2"))
        self.Iunit2.addItem(_fromUtf8(""))
        self.Iunit2.addItem(_fromUtf8(""))
        self.Iunit2.addItem(_fromUtf8(""))
        self.horizontalLayout_14.addWidget(self.Iunit2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_16 = QtGui.QLabel(self.groupBox_4)
        self.label_16.setMinimumSize(QtCore.QSize(64, 19))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_16.addWidget(self.label_16)
        self.Istep = QtGui.QLineEdit(self.groupBox_4)
        self.Istep.setMinimumSize(QtCore.QSize(112, 22))
        self.Istep.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Istep.setObjectName(_fromUtf8("Istep"))
        self.horizontalLayout_16.addWidget(self.Istep)
        self.Iunit3 = QtGui.QComboBox(self.groupBox_4)
        self.Iunit3.setMinimumSize(QtCore.QSize(39, 22))
        self.Iunit3.setObjectName(_fromUtf8("Iunit3"))
        self.Iunit3.addItem(_fromUtf8(""))
        self.Iunit3.addItem(_fromUtf8(""))
        self.Iunit3.addItem(_fromUtf8(""))
        self.horizontalLayout_16.addWidget(self.Iunit3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.label_11 = QtGui.QLabel(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(64, 19))
        self.label_11.setMaximumSize(QtCore.QSize(64, 19))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_18.addWidget(self.label_11)
        self.VI_range = QtGui.QComboBox(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VI_range.sizePolicy().hasHeightForWidth())
        self.VI_range.setSizePolicy(sizePolicy)
        self.VI_range.setMaximumSize(QtCore.QSize(16777215, 22))
        self.VI_range.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.VI_range.setObjectName(_fromUtf8("VI_range"))
        self.VI_range.addItem(_fromUtf8(""))
        self.VI_range.addItem(_fromUtf8(""))
        self.VI_range.addItem(_fromUtf8(""))
        self.VI_range.addItem(_fromUtf8(""))
        self.VI_range.addItem(_fromUtf8(""))
        self.VI_range.addItem(_fromUtf8(""))
        self.VI_range.addItem(_fromUtf8(""))
        self.VI_range.addItem(_fromUtf8(""))
        self.VI_range.addItem(_fromUtf8(""))
        self.VI_range.addItem(_fromUtf8(""))
        self.horizontalLayout_18.addWidget(self.VI_range)
        self.verticalLayout_4.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_17 = QtGui.QLabel(self.groupBox_4)
        self.label_17.setMinimumSize(QtCore.QSize(64, 19))
        self.label_17.setMaximumSize(QtCore.QSize(64, 19))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_6.addWidget(self.label_17)
        self.VI_loop = QtGui.QLineEdit(self.groupBox_4)
        self.VI_loop.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.VI_loop.setObjectName(_fromUtf8("VI_loop"))
        self.horizontalLayout_6.addWidget(self.VI_loop)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addWidget(self.groupBox_4)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.save_2400 = QtGui.QPushButton(Dialog)
        self.save_2400.setObjectName(_fromUtf8("save_2400"))
        self.horizontalLayout_7.addWidget(self.save_2400)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.cancel_2400 = QtGui.QPushButton(Dialog)
        self.cancel_2400.setObjectName(_fromUtf8("cancel_2400"))
        self.horizontalLayout_7.addWidget(self.cancel_2400)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.cancel_2400, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QObject.connect(self.save_2400, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "IV谱仪器设置", None))
        self.label_12.setText(_translate("Dialog", "电阻范围", None))
        self.res_range.setItemText(0, _translate("Dialog", "100", None))
        self.res_range.setItemText(1, _translate("Dialog", "1K", None))
        self.res_range.setItemText(2, _translate("Dialog", "10K", None))
        self.res_range.setItemText(3, _translate("Dialog", "100K", None))
        self.res_range.setItemText(4, _translate("Dialog", "1M", None))
        self.res_range.setItemText(5, _translate("Dialog", "10M", None))
        self.res_range.setItemText(6, _translate("Dialog", "100M", None))
        self.res_range.setItemText(7, _translate("Dialog", "200M", None))
        self.label_7.setText(_translate("Dialog", "Ω", None))
        self.res_detect.setText(_translate("Dialog", "电阻探测", None))
        self.label_2.setText(_translate("Dialog", "电压", None))
        self.label_18.setText(_translate("Dialog", "V", None))
        self.label_19.setText(_translate("Dialog", "电流", None))
        self.label_20.setText(_translate("Dialog", "A", None))
        self.label_21.setText(_translate("Dialog", "电阻", None))
        self.label_22.setText(_translate("Dialog", "Ω", None))
        self.label_8.setText(_translate("Dialog", "测量模式", None))
        self.meas_mode.setItemText(0, _translate("Dialog", "两线制", None))
        self.meas_mode.setItemText(1, _translate("Dialog", "四线制", None))
        self.label.setText(_translate("Dialog", "输出模式", None))
        self.output_mode.setItemText(0, _translate("Dialog", "连续输出", None))
        self.output_mode.setItemText(1, _translate("Dialog", "脉冲输出", None))
        self.IV_MODE.setText(_translate("Dialog", "通电压，测电流(I-V)", None))
        self.label_3.setText(_translate("Dialog", "扫描模式", None))
        self.VI_sweep.setItemText(0, _translate("Dialog", "0 -> +V -> 0 -> -V -> 0", None))
        self.VI_sweep.setItemText(1, _translate("Dialog", "-V -> +V -> -V", None))
        self.groupBox_2.setTitle(_translate("Dialog", "I-V模式设置", None))
        self.label_4.setText(_translate("Dialog", "起始电压", None))
        self.Vunit1.setItemText(0, _translate("Dialog", "mV", None))
        self.Vunit1.setItemText(1, _translate("Dialog", "V", None))
        self.label_5.setText(_translate("Dialog", "终止电压", None))
        self.Vunit2.setItemText(0, _translate("Dialog", "mV", None))
        self.Vunit2.setItemText(1, _translate("Dialog", "V", None))
        self.label_6.setText(_translate("Dialog", "步进电压", None))
        self.Vunit3.setItemText(0, _translate("Dialog", "mV", None))
        self.Vunit3.setItemText(1, _translate("Dialog", "V", None))
        self.label_10.setText(_translate("Dialog", "电流范围", None))
        self.IV_range.setItemText(0, _translate("Dialog", "10pA", None))
        self.IV_range.setItemText(1, _translate("Dialog", "100pA", None))
        self.IV_range.setItemText(2, _translate("Dialog", "1uA", None))
        self.IV_range.setItemText(3, _translate("Dialog", "10uA", None))
        self.IV_range.setItemText(4, _translate("Dialog", "100uA", None))
        self.IV_range.setItemText(5, _translate("Dialog", "1mA", None))
        self.IV_range.setItemText(6, _translate("Dialog", "10mA", None))
        self.IV_range.setItemText(7, _translate("Dialog", "100mA", None))
        self.IV_range.setItemText(8, _translate("Dialog", "1A", None))
        self.label_9.setText(_translate("Dialog", "循环次数", None))
        self.VI_MODE.setText(_translate("Dialog", "通电流，测电压(V-I)", None))
        self.label_13.setText(_translate("Dialog", "扫描模式", None))
        self.IV_sweep.setItemText(0, _translate("Dialog", "0 -> +I -> 0 -> -I -> 0", None))
        self.IV_sweep.setItemText(1, _translate("Dialog", "-I -> +I -> -I", None))
        self.groupBox_4.setTitle(_translate("Dialog", "V-I模式设置", None))
        self.label_14.setText(_translate("Dialog", "起始电流", None))
        self.Iunit1.setItemText(0, _translate("Dialog", "uA", None))
        self.Iunit1.setItemText(1, _translate("Dialog", "mA", None))
        self.Iunit1.setItemText(2, _translate("Dialog", "A", None))
        self.label_15.setText(_translate("Dialog", "终止电流", None))
        self.Iunit2.setItemText(0, _translate("Dialog", "uA", None))
        self.Iunit2.setItemText(1, _translate("Dialog", "mA", None))
        self.Iunit2.setItemText(2, _translate("Dialog", "A", None))
        self.label_16.setText(_translate("Dialog", "步进电流", None))
        self.Iunit3.setItemText(0, _translate("Dialog", "uA", None))
        self.Iunit3.setItemText(1, _translate("Dialog", "mA", None))
        self.Iunit3.setItemText(2, _translate("Dialog", "A", None))
        self.label_11.setText(_translate("Dialog", "电压范围", None))
        self.VI_range.setItemText(0, _translate("Dialog", "1uV", None))
        self.VI_range.setItemText(1, _translate("Dialog", "10uV", None))
        self.VI_range.setItemText(2, _translate("Dialog", "100uV", None))
        self.VI_range.setItemText(3, _translate("Dialog", "1mV", None))
        self.VI_range.setItemText(4, _translate("Dialog", "10mV", None))
        self.VI_range.setItemText(5, _translate("Dialog", "100mV", None))
        self.VI_range.setItemText(6, _translate("Dialog", "1V", None))
        self.VI_range.setItemText(7, _translate("Dialog", "10V", None))
        self.VI_range.setItemText(8, _translate("Dialog", "100V", None))
        self.VI_range.setItemText(9, _translate("Dialog", "210V", None))
        self.label_17.setText(_translate("Dialog", "循环次数", None))
        self.save_2400.setText(_translate("Dialog", "保存", None))
        self.cancel_2400.setText(_translate("Dialog", "取消", None))

import mypic_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

