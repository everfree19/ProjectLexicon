
from Model.Account import *
from Model.StockInformDao import *
from AxDynamicTemplate.lexiconDynamicCallback import *

class lexiconPresenter:
    def __init__(self):
        self.Account = Account()
        self.StockInformDao = StockInformDao()
        self.axDynamicCallback = lexiconDynamicCallback()
        self.isActivate = False
    def setActivate (self, activate) :
        self.isActivate = activate

    def isSessionActivate(self):
        return self.isActivate