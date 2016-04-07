
from Model.Account import *
from Model.StockInformDao import *
from AxDynamicTemplate.lexiconDynamicCallback import *

class lexiconPresenter:
    def __init__(self):
        self.Account = Account()
        self.StockInformDao = StockInformDao()
        self.axDynamicCallback = lexiconDynamicCallback()
