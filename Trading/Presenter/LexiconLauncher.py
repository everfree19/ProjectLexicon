import sys
from View.LexiconMainFrame import *
from Presenter.IPresenter import *
# run mainFrame
if __name__ == "__main__":

    app = QApplication(sys.argv)
    lexiconMainpresenter = LexiconPresenter.lexiconPresenter()
    lexiconMainView = LexiconMainFrame()
    lexiconMainView.show()
    app.exec_()


