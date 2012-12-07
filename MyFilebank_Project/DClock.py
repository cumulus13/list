import sys, os, errno
from PyQt4 import QtGui, QtCore

class DigitalClock(QtGui.QLCDNumber):
    def __init__(self, parent=None):
        super(DigitalClock, self).__init__(parent)

        self.setSegmentStyle(QtGui.QLCDNumber.Filled)

        timer = QtCore.QTimer(self)
        #timer.timeout.connect(self.showTime)
        self.connect(timer, QtCore.SIGNAL("timeout()"), self.showTime)
        timer.start(1000)

        self.showTime()

        self.setWindowTitle(self.tr("Digital Clock"))
        self.resize(100, 60)

    def showTime(self):
        time = QtCore.QTime.currentTime()
        text = time.toString("hh:mm")
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]

        self.display(text)