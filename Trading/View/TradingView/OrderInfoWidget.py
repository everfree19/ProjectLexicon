from PyQt4.QtCore import *
from PyQt4.QtGui import *

from AxDynamicTemplate.lexiconDynamicTemplate import *
from Presenter.IPresenter import *
from TradingUtil import RealDataRequestTimer
#base X : 450
#base Y : 8


class orderInfoWidget:
    def __init__(self, lexiconWindow ):
        #주문 정보 위젯
        label = QLabel('주문 정보', lexiconWindow)
        label.move(450, 420)

        self.lexiconAxCtrl = lexiconWindow.lexiconAxCtrl
        self.orderInfoView = QTextEdit(lexiconWindow)
        self.orderInfoView.setGeometry(450, 450, 380, 300)

        btn_Order = QPushButton("Test Order", lexiconWindow)
        btn_Order.move(520, 420)
        btn_Order.clicked.connect(self.btn_clicked_Order )

        label = QLabel('체결 정보', lexiconWindow)
        label.move(850, 420)
        self.contractInfoView = QTextEdit(lexiconWindow)
        self.contractInfoView.setGeometry(850, 450, 380, 300)

    def btn_clicked_Order(self):
        #imple send order
        #HogaGb = self.comboBox.currentText()[0:2].strip()
        #Type = int(self.comboBox_2.currentText()[0:1].strip())
        #Code = self.lineEdit.text().strip()
        #Qty = int(self.lineEdit_4.text().strip())
        #Price = int(self.lineEdit_5.text().strip())
        #OrgNo = self.lineEdit_6.text().strip()
        #ACCNO = self.lineEdit_2.text().strip()
        if lexiconMainpresenter.isSessionActivate() :
            ACCNO = lexiconMainpresenter.Account.getAccount()
            Type = 1  # 1 : 신규 매수 , 2: 신규 매도 3: 매수 취소 4: 매도 취소 5: 매수 정정 6: 매도 정정
            Code = "041020"  # 주식 종목 코드.  ex) 인프라웨어
            Qty = 100       # 수량
            Price = 4000    #가격
            HogaGb = "00" # 00 : 지정가, 03 :시장가
            OrgNo ="" #원주문번호

            OrderResult = self.lexiconAxCtrl.dynamicCall('SendOrder(QString, QString, QString, int, QString, int, int, QString, QString)', ["Order", "0107", ACCNO, Type, Code, Qty, Price, HogaGb, OrgNo])
            if ( OrderResult == 0 ):
                 self.orderInfoView.append("========================\n" )
                 self.orderInfoView.append("매수 주문 전송 완료 \n" )
                 self.orderInfoView.append("계좌번호  :" + ACCNO + "\n" )
                 self.orderInfoView.append("매수 구분 : 신규 매수 \n" )
                 self.orderInfoView.append("종목 코드 : " + Code + "\n" )
                 self.orderInfoView.append("수량 : " + str(Qty) + "\n")
                 self.orderInfoView.append("가격 : " + str(Price) + "\n")
                 self.orderInfoView.append("주문유형 : 지정가 \n" )
                 self.orderInfoView.append("========================\n" )
            else:
                 self.orderInfoView.append("========================\n" )
                 self.orderInfoView.append("주문 실패\n" )
                 self.orderInfoView.append("========================\n" )


