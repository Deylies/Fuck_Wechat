# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\regits.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_regist(object):
    def setupUi(self, regist):
        regist.setObjectName("regist")
        regist.resize(298, 300)
        regist.setStyleSheet("")
        self.widget = QtWidgets.QWidget(regist)
        self.widget.setGeometry(QtCore.QRect(0, 0, 300, 40))
        self.widget.setObjectName("widget")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(50, 10, 211, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.widget_2 = QtWidgets.QWidget(regist)
        self.widget_2.setGeometry(QtCore.QRect(0, 40, 100, 220))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 71, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.widget_3 = QtWidgets.QWidget(regist)
        self.widget_3.setGeometry(QtCore.QRect(100, 40, 200, 220))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.widget_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 0, 141, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.username = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.username.setObjectName("username")
        self.verticalLayout_2.addWidget(self.username)
        self.passwd = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd.setObjectName("passwd")
        self.verticalLayout_2.addWidget(self.passwd)
        self.passwd2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.passwd2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwd2.setObjectName("passwd2")
        self.verticalLayout_2.addWidget(self.passwd2)
        self.phone_num = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.phone_num.setObjectName("phone_num")
        self.verticalLayout_2.addWidget(self.phone_num)
        self.keys = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.keys.setObjectName("keys")
        self.verticalLayout_2.addWidget(self.keys)
        self.widget_4 = QtWidgets.QWidget(regist)
        self.widget_4.setGeometry(QtCore.QRect(0, 260, 300, 40))
        self.widget_4.setObjectName("widget_4")
        self.back_label = QtWidgets.QLabel(self.widget_4)
        self.back_label.setGeometry(QtCore.QRect(0, 0, 120, 30))
        self.back_label.setStyleSheet("image:url(:/image/left.jpg)")
        self.back_label.setText("")
        self.back_label.setObjectName("back_label")
        self.confirm = QtWidgets.QPushButton(self.widget_4)
        self.confirm.setGeometry(QtCore.QRect(210, 0, 75, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.confirm.setFont(font)
        self.confirm.setObjectName("confirm")

        self.retranslateUi(regist)
        QtCore.QMetaObject.connectSlotsByName(regist)

    def retranslateUi(self, regist):
        _translate = QtCore.QCoreApplication.translate
        regist.setWindowTitle(_translate("regist", "Form"))
        self.label_5.setText(_translate("regist", "欢迎！注册DeyLies微信助手"))
        self.label_2.setText(_translate("regist", "用户名"))
        self.label.setText(_translate("regist", "密码"))
        self.label_3.setText(_translate("regist", "确认密码"))
        self.label_4.setText(_translate("regist", "手机号"))
        self.label_6.setText(_translate("regist", "密钥"))
        self.confirm.setText(_translate("regist", "提交"))

import resource.regist
