from PyQt4.QtCore import *
from Presenter.IPresenter import *

class authenticateWidget:
    def __init__(self, loginCtrl ):
        self.loginInfoCtrl = loginCtrl
        self.loginInfoCtrl.setGeometry(10, 10, 150, 50)
        self.loginInfoCtrl.setEnabled(False)

    def authenticate( self, lexiconCtrl ):
        self.lexiconCtrl = lexiconCtrl
        self.lexiconCtrl .dynamicCall("CommConnect()")
        self.lexiconCtrl .connect(self.lexiconCtrl , SIGNAL("OnEventConnect(int)"), self.OnEventConnect)

    def requestLoginInfo(self):
        global lexiconMainpresenter

        account_num = self.lexiconCtrl.dynamicCall("GetLoginInfo(QString)", ["ACCNO"])
        AccountStr = account_num.rstrip(';')
        lexiconMainpresenter.Account.setAccount(AccountStr)
        self.loginInfoCtrl.append("계좌번호: " + AccountStr)

    # callback from stock server
    def OnEventConnect( self, nErrCode ):
        if nErrCode == 0:
            self.loginInfoCtrl.append("로그인 성공")
            self.requestLoginInfo()
        else :
            self.loginInfoCtrl.append("로그인 실패")