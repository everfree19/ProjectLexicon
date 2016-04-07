
from AxDynamicTemplate.lexiconDynamicTemplate import *
from Presenter.IPresenter import *


class lexiconDynamicCallback:
    def __init__(self):
        pass

    def interfaceBinding (self, window, dao ) :
        self.mainFrame = window
        self._dao = dao

    def OnReceiveTrData(self,  ScrNo, RQName, TrCode, RecordName, PrevNext, DataLength, ErrorCode, Message, SplmMsg):
        if RQName == "RequestRapidVolumnList":
            extractTrData_RapidVolumnListData (self.mainFrame, self._dao, TrCode, RQName)
        elif RQName == "ConclusionInfo":
            extractTrData_ConclusionInfo ( self.mainFrame, self._dao, TrCode, RQName)
