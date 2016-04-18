# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:36:37 2015

"""
import sys
import pymysql
import re
import PyQt4
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic
from PyQt4.QAxContainer import *
import re
import logging
import logging.handlers
import time
import datetime


#1.로그 인스턴스를 만든다.
logger = logging.getLogger('mylogger')
#2.formatter를 만든다.
formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s]%(asctime)s>%(message)s')

loggerLevel = logging.DEBUG
filename = "./mylog.log"

#스트림과 파일로 로그를 출력하는 핸들러를 각각 만든다.
fileHandler = logging.FileHandler(filename)
streamHandler = logging.StreamHandler()

#각 핸들러에 formatter를 지정한다.
fileHandler.setFormatter(formatter)
streamHandler.setFormatter(formatter)

#로그 인스턴스에 스트림 핸들러와 파일 핸들러를 붙인다.
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)
logger.setLevel(loggerLevel)
logger.debug("=============================================================================")
logger.info("LOG START")
    
form_class = uic.loadUiType("Invest.ui")[0]

class SimpleWindow(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("종목별투자자기관별차트요청")
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.connect(self.kiwoom, SIGNAL("OnEventConnect(int)"), self.OnEventConnect)
        self.kiwoom.connect(self.kiwoom, SIGNAL("OnReceiveTrData(QString, QString, QString, QString, QString, int, QString, QString, QString)"), self.OnReceiveTrData)
        self.comboBox_4.activated['QString'].connect(self.handleActivated)
        data = datetime.datetime.now()
        today = data.strftime('%Y%m%d')
        self.today = today
        self.lineEdit.setText(today)
        self.allcode = self.comboBox_4.currentText().strip()
        
        #로그인 버튼
        self.connect(self.btn_login, SIGNAL("clicked()"), self.btn_clicked)
        
        #투자자별 매매 버튼
        self.connect(self.btn_invest, SIGNAL("clicked()"), self.btn_clicked2)

    def OnEventConnect(self, nErrCode):
        if nErrCode == 0:
            self.textEdit.append("서버에 연결 되었습니다...")
            print("서버에 연결 되었습니다...")
            self.btn_login.setText("접속중")
            self.btn_login.setStyleSheet("color: red")
            self.btn_invest.setEnabled(True)
            self.groupBox.setEnabled(True)
            self.comboBox.setEnabled(True)
            self.comboBox_2.setEnabled(True)
            self.comboBox_3.setEnabled(True)
            if self.allcode == "전 종 목":
                self.lineEdit2.setEnabled(False)

        else:
            self.textEdit.append("서버 연결에 실패 했습니다...")
            print("서버 연결에 실패 했습니다...")
    
    def OnReceiveTrData(self, sScrNo, sRQName, sTRCode, sRecordName, sPreNext, nDataLength, sErrorCode, sMessage, sSPlmMsg):
        cnt = self.kiwoom.dynamicCall('GetRepeatCnt(QString, QString)', sTRCode, sRQName)
        self.cur = self.conn.cursor()

        if sRQName == "종목별투자자기관별차트요청":
            logger.debug("OnReceiveTrData code:%s cnt:%s", self.code, cnt)
            logger.debug("code:%s sRecordName:%s Length:%d Err_code:%s Err_Msg:%s", self.code, sRecordName, int(nDataLength), sErrorCode, sMessage)
            #if cnt > 0:
            for i in range(cnt) :
                date = self.kiwoom.dynamicCall('CommGetData(QString, QString, QString, int, QString)', sTRCode, "", sRQName, i, "일자")
                #종목코드
                code = self.code.strip()
                price = self.kiwoom.dynamicCall('CommGetData(QString, QString, QString, int, QString)', sTRCode, "", sRQName, i, "현재가")
                #price = int(re.sub(r"\,|\+|\-","",price))
                vud = self.kiwoom.dynamicCall('CommGetData(QString, QString, QString, int, QString)', sTRCode, "", sRQName, i, "전일대비")
                #vud = int(re.sub(r"\,|\+","",vud))
                ac_amt = self.kiwoom.dynamicCall('CommGetData(QString, QString, QString, int, QString)', sTRCode, "", sRQName, i, "누적거래대금")
                #ac_amt = int(re.sub(r"\,|\+","",ac_amt))
                ant = self.kiwoom.dynamicCall('CommGetData(QString, QString, QString, int, QString)', sTRCode, "", sRQName, i, "개인투자자")
                #ant = int(re.sub(r"\,|\+","",ant))
                foreigner = self.kiwoom.dynamicCall('CommGetData(QString, QString, QString, int, QString)', sTRCode, "", sRQName, i, "외국인투자자")
                #foreigner = int(re.sub(r"\,|\+","",foreigner))
                cop = self.kiwoom.dynamicCall('CommGetData(QString, QString, QString, int, QString)', sTRCode, "", sRQName, i, "기관계")
                #cop = int(re.sub(r"\,|\+","",cop))
                kofia = self.kiwoom.dynamicCall('CommGetData(QString, QString, QString, int, QString)', sTRCode, "", sRQName, i, "금융투자")
                #kofia = int(re.sub(r"\,|\+","",kofia))
                insu = self.kiwoom.dynamicCall('CommGetData(QString, QString, QString, int, QString)', sTRCode, "", sRQName, i, "보험")
                #insu = int(re.sub(r"\,|\+","",insu))
                am = self.kiwoom.dynamicCall('CommGetData(QString, QString, QString, int, QString)', sTRCode, "", sRQName, i, "투신")
                #am = int(re.sub(r"\,|\+","",am))
                etc = self.kiwoom.dynamicCall('CommGetData(QString, QString, QString, int, QString)', sTRCode, "", sRQName, i, "기타금융")
                #etc = int(re.sub(r"\,|\+","",etc))
                bnk = self.kiwoom.dynamicCall('CommGetData(QString, QString, QString, int, QString)', sTRCode, "", sRQName, i, "은행")
                #bnk = int(re.sub(r"\,|\+","",bnk))
                pens = self.kiwoom.dynamicCall('CommGetData(QString, QString, QString, int, QString)', sTRCode, "", sRQName, i, "연기금등")
                #pens = int(re.sub(r"\,|\+","",pens))
                nat = self.kiwoom.dynamicCall('CommGetData(QString, QString, QString, int, QString)', sTRCode, "", sRQName, i, "국가")
                #nat = int(re.sub(r"\,|\+","",nat))
                pers = self.kiwoom.dynamicCall('CommGetData(QString, QString, QString, int, QString)', sTRCode, "", sRQName, i, "내외국인")
                #pers = int(re.sub(r"\,|\+","",pers))
                priv = self.kiwoom.dynamicCall('CommGetData(QString, QString, QString, int, QString)', sTRCode, "", sRQName, i, "사모펀드")
                #priv = int(re.sub(r"\,|\+","",priv))
                etc_co = self.kiwoom.dynamicCall('CommGetData(QString, QString, QString, int, QString)', sTRCode, "", sRQName, i, "기타법인")
                #etc_co = int(re.sub(r"\,|\+","",etc_co))
                time.sleep(0.001)
                try:
                    self.cur.execute("""insert into invest_anal(tr_dt, code, close, vs_bf, ac_vol, \
                                     ant, fore, t_cop, kofia, insur, am, etc, \
                                     bnk,pens, nat, pers, prf, etc_cop) \
                                     values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",\
                                    (date.strip(), code.strip(),price,vud,ac_amt, ant,foreigner,cop,kofia,insu,am,etc,bnk,pens,nat,pers,priv,etc_co))
                    logger.debug("일자 [%s] insert", date.strip())
              
                except pymysql.err:
                    print("insert error: {}".format(err))

            if sPreNext == "2":
                self.conn.commit()
                self.textEdit.append(code + " 를 DB에 기록 중입니다.....")
                self.jongmok(code, 2)

            else:
                if self.allcode == "전 종 목":
                    row = self.cur1.fetchone()
                    if row != None:
                        self.jongmok(row[0].strip(), 0)

                    else:
                        self.cur.close()
                        self.conn.commit()
                        self.conn.close()
                        self.textEdit.append("DB 작업이 완료 되었습니다.....")

                            

                else: 
                    self.cur.close()
                    self.conn.commit()
                    self.conn.close()
                    self.textEdit.append(self.code + " 의 DB 작업이 완료 되었습니다.....")

         
    def btn_clicked(self):
        if self.btn_login.text().strip() == "Login":
            self.kiwoom.dynamicCall("CommConnect()")

        else:
            self.kiwoom.dynamicCall("CommTerminate()")
            while True:
                if self.kiwoom.dynamicCall('GetConnectState()') == 0:
                    self.btn_login.setStyleSheet("color: black)")
                    self.btn_login.setText("Login")
                    self.textEdit.append("서버 연결을 종료했습니다...")
                    break

    def jongmok(self,code,_next):
        금액수량 = int(self.comboBox.currentText()[0:1].strip())
        매매 = int(self.comboBox_3.currentText()[0:1].strip())
        단위 = int(self.comboBox_2.currentText()[0:4].strip())
        tr_date = self.lineEdit.text()
        self.code = code
        ret = self.kiwoom.dynamicCall('SetInputValue(Qstring, Qstring)', "일자", tr_date.strip())
        ret = self.kiwoom.dynamicCall('SetInputValue(Qstring, Qstring)', "종목코드", self.code)
        logger.debug("파람[%s] 코드[%s] 코드명[%s] call", self.code, self.code, ret)
        ret = self.kiwoom.dynamicCall('SetInputValue(Qstring, int)', "금액수량구분", 금액수량) #1:금액, 2:수량
        ret = self.kiwoom.dynamicCall('SetInputValue(Qstring, int)', "매매구분", 매매) #0:순매수, 1:매수, 2:매도
        ret = self.kiwoom.dynamicCall('SetInputValue(Qstring, int)', "단위구분", 단위) #1000:천주, 1:단주
        ret = self.kiwoom.dynamicCall('CommRqData(QString, QString, int, QString)', "종목별투자자기관별차트요청", "OPT10060", _next, "0716")
    
    #종목별 투자자별 매매현황 구현
    def btn_clicked2(self):
        #MariaDB 구축
        self.conn = pymysql.connect(host = 'localhost', port=3306, user='root', passwd='1234', db='stockdb', charset='utf8')
        self.cur1 = self.conn.cursor()
        self.cur1.execute("select code from sec_master order by code")
        row = self.cur1.fetchone()
        if self.allcode == "전 종 목":
            self.textEdit.append("전종목 를 DB에 기록 합니다.....")
            if row != None:
                self.jongmok(row[0].strip(),"0")

        else:
            jcode = self.lineEdit2.text().strip()
            if jcode != None:
                self.textEdit.append(jcode + " 를 DB에 기록 중입니다.....")
                self.jongmok(jcode,"0")

    def handleActivated(self, text):
        self.allcode = text
        if self.allcode == "전 종 목":
            self.lineEdit2.setEnabled(False)

        else:
            self.lineEdit2.setEnabled(True)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = SimpleWindow()
    myWindow.show()
    app.exec_()
    
