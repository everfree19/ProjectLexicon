# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kiwoom.ui'
#
# Created: Tue Oct 27 22:49:48 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QAxContainer import *
from PyQt4.QtCore import QVariant
import re

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

#class Ui_Form(object):
class Ui_Form(QAxWidget):
    def __init__(self):
        super().__init__()
        self.setControl('KHOPENAPI.KHOpenAPICtrl.1')
        self.connect(self, SIGNAL("OnEventConnect(int)"), self.OnEventConnect)
        self.connect(self, SIGNAL("OnReceiveMsg(QString, QString, QString, QString)"), self.OnReceiveMsg)
        self.connect(self, SIGNAL("OnReceiveTrData(QString, QString, QString, QString, QString, int, QString, QString, QString)"), self.OnReceiveTrData)
        self.connect(self, SIGNAL("OnReceiveChejanData(QString, int, QString)"),self.OnReceiveChejanData)


    def btn_login(self):
        ret = self.dynamicCall("CommConnect()")

    def btn_Quit(self):
        self.dynamicCall("CommTerminate()")
        sys.exit()

    def OnEventConnect(self, nErrCode):
        if nErrCode == 0:
            self.textEdit.append("서버에 연결 되었습니다...")
            print("서버에 연결 되었습니다...")
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(False)
            self.pushButton_3.setEnabled(True)
            self.SendOrder.setEnabled(True)
            self.textEdit.setEnabled(True)
            self.comboBox.setEnabled(True)
            self.comboBox_2.setEnabled(True)
            self.lineEdit.setEnabled(True)
            self.lineEdit_2.setEnabled(False)
            self.lineEdit_5.setEnabled(True)
            self.lineEdit_6.setEnabled(True)
            self.lineEdit_4.setEnabled(True)

        else:
            self.textEdit.append("서버 연결에 실패 했습니다...")
            print("서버 연결에 실패 했습니다...")

    def OnReceiveMsg(self, sScrNo, sRQName, sTrCode, sMsg):
        if sScrNo == "0003":
            print(sMsg)
            self.textEdit.append(sMsg)

        else:
            print(sMsg)
            self.textEdit.append(sMsg)

    def OnReceiveChejanData(self, sGubun, nItemCnt, sFidList):
        self.lineEdit_6.setText(self.GetChjanData(9203))
        self.textEdit.append("주문번호: "+self.GetChjanData(9203))
        self.textEdit.append("종 목 명: "+self.GetChjanData(302))
        self.textEdit.append("주문수량: "+self.GetChjanData(900))
        self.textEdit.append("주문가격: "+self.GetChjanData(901))

    def OnReceiveTrData(self, sScrNo, sRQName, sTrCode, sRecordName, sPreNext, nDataLength, sErrorCode, sMessage, sSPlmMsg):
        if sRQName == "주식기본정보":
            cnt = self.dynamicCall('GetRepeatCnt(QString, QString)', sTrCode, sRQName)
            종목명 = self.dynamicCall('CommGetData(QString, QString, QString, int, QString)', sTrCode, "", sRQName, 0, "종목명")
            현재가 = self.dynamicCall('CommGetData(QString, QString, QString, int, QString)', sTrCode, "", sRQName, 0, "현재가")
            self.textEdit.append("창번호: "+sScrNo)
            self.textEdit.append("종목명: "+종목명.strip())
            self.textEdit.append("현재가: "+현재가.strip())

    def btn_clicked3(self):
        Code = self.lineEdit.text().strip()
        ret = self.dynamicCall('SetInputValue(QString, QString)', "종목코드", Code)
        ret = self.dynamicCall('CommRqData(QString, QString, int, QString)', "주식기본정보", "OPT10001", 0, "0101")


    def btn_info(self):
        ACCOUNT_CNT = self.dynamicCall('GetLoginInfo("ACCOUNT_CNT")')
        ACC_NO = self.dynamicCall('GetLoginInfo("ACCNO")')
        ACCNO = re.sub(';','', ACC_NO)
        self.textEdit.append("보유 계좌수: "+ACCOUNT_CNT + " " + "계좌번호: "+ACCNO)
        self.lineEdit_2.setText(ACCNO)


    def GetChjanData(self, nFid):
        chjang = self.dynamicCall('GetChejanData(QString)', nFid)
        return chjang


    def btn_SendOrder(self):
        HogaGb = self.comboBox.currentText()[0:2].strip()
        Type = int(self.comboBox_2.currentText()[0:1].strip())
        Code = self.lineEdit.text().strip()
        Qty = int(self.lineEdit_4.text().strip())
        Price = int(self.lineEdit_5.text().strip())
        OrgNo = self.lineEdit_6.text().strip()
        ACCNO = self.lineEdit_2.text().strip()
        Order = self.dynamicCall('SendOrder(QString, QString, QString, int, QString, int, int, QString, QString)', ["주식주문", "0107", ACCNO, Type, Code, Qty, Price, HogaGb, OrgNo])

        
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(570, 289)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 211, 221))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayoutWidget = QtGui.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 20, 191, 161))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_4 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_5 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_6 = QtGui.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_6 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEdit_6)
        self.comboBox = QtGui.QComboBox(self.formLayoutWidget)
        self.comboBox.setEnabled(False)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboBox)
        
        self.comboBox_2 = QtGui.QComboBox(self.formLayoutWidget)
        self.comboBox_2.setEnabled(False)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.comboBox_2)
        
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(120, 190, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.connect(self.pushButton, SIGNAL("clicked()"), self.btn_clicked3)
        
        self.SendOrder = QtGui.QPushButton(self.groupBox)
        self.SendOrder.setEnabled(False)
        self.SendOrder.setGeometry(QtCore.QRect(10, 190, 75, 23))
        self.SendOrder.setObjectName(_fromUtf8("SendOrder"))
        self.connect(self.SendOrder, SIGNAL("clicked()"), self.btn_SendOrder)
        
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(230, 20, 331, 211))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 250, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.connect(self.pushButton_2, SIGNAL("clicked()"), self.btn_login)
        
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(480, 250, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.connect(self.pushButton_4, SIGNAL("clicked()"), self.btn_Quit)
        
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 250, 61, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.connect(self.pushButton_3, SIGNAL("clicked()"), self.btn_info)
        
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 250, 141, 20))
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(350, 270, 211, 20))
        self.label_7.setStyleSheet(_fromUtf8("color: rgb(85, 170, 255);"))
        self.label_7.setIndent(-1)
        self.label_7.setOpenExternalLinks(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "키움 API", None))
        self.groupBox.setTitle(_translate("Form", "주문입력", None))
        self.label.setText(_translate("Form", "종목코드", None))
        self.label_2.setText(_translate("Form", "거래구분", None))
        self.label_3.setText(_translate("Form", "매매구분", None))
        self.label_4.setText(_translate("Form", "주문수량", None))
        self.label_5.setText(_translate("Form", "주문가격", None))
        self.label_6.setText(_translate("Form", "원주문번호", None))
        self.comboBox.setItemText(0, _translate("Form", "00: 지정가", None))
        self.comboBox.setItemText(1, _translate("Form", "03: 시장가", None))
        self.comboBox.setItemText(2, _translate("Form", "61: 시간외 단일가", None))
        self.comboBox_2.setItemText(0, _translate("Form", "1:   매   수", None))
        self.comboBox_2.setItemText(1, _translate("Form", "2:   매   도", None))
        self.comboBox_2.setItemText(2, _translate("Form", "3:   매수취소", None))
        self.comboBox_2.setItemText(3, _translate("Form", "4:   매도취소", None))
        self.pushButton.setText(_translate("Form", "GetInfo", None))
        self.SendOrder.setText(_translate("Form", "주 문", None))
        self.pushButton_2.setText(_translate("Form", "로그인", None))
        self.pushButton_4.setText(_translate("Form", "종 료", None))
        self.pushButton_3.setText(_translate("Form", "계좌조회", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

