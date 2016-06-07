# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\WorkDir\gas-sensing_resistors\main.ui'
#
# Created: Mon Feb 01 22:52:45 2016
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/icons/lmd.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 800, 150))
        self.label_2.setMinimumSize(QtCore.QSize(800, 150))
        self.label_2.setMaximumSize(QtCore.QSize(800, 150))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/icon/icons/title.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.listWidget = QtGui.QListWidget(self.centralWidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 150, 800, 420))
        self.listWidget.setMinimumSize(QtCore.QSize(800, 420))
        self.listWidget.setMaximumSize(QtCore.QSize(800, 420))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listWidget.setAutoFillBackground(True)
        self.listWidget.setAutoScroll(False)
        self.listWidget.setAutoScrollMargin(16)
        self.listWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.listWidget.setIconSize(QtCore.QSize(128, 128))
        self.listWidget.setGridSize(QtCore.QSize(194, 200))
        self.listWidget.setViewMode(QtGui.QListView.IconMode)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/icons/27.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/icons/22.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/icons/13.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/icons/25.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/icons/14.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon5)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.listWidget.addItem(item)
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(0, 570, 800, 30))
        self.label.setMinimumSize(QtCore.QSize(800, 30))
        self.label.setMaximumSize(QtCore.QSize(800, 30))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/icon/icons/copyright.png")))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "气敏电阻测量系统", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "I-V谱", None))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "S-T谱", None))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "S-C谱", None))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "系统设置", None))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "系统帮助", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)

import mypic_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

