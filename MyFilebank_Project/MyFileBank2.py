import sys, os, errno
from PyQt4 import QtGui, QtCore

os.system('cls')
print "\n\n\n"

	    
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

class MainApp(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        
        self.setWindowTitle('MyFile - Bank')
        self.resize(700, 500)
        self.setWindowIcon(QtGui.QIcon('Bug.png'))
        
        #tootip
        self.setToolTip('Searching MyFile Data Bank On MyFile')
        QtGui.QToolTip.setFont(QtGui.QFont('Arial', 10))
        self.statusBar().showMessage('Main Application')
        
        #make screen On center Windows
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 3, (screen.height() - size.height()) / 3)
        self.setFixedSize(700, 500)
	
        #Group For Category Of File
        self.Gbox1 = QtGui.QGroupBox(self)
        self.Gbox1.setTitle('Category')
        self.Gbox1.setGeometry(20, 20, 320, 200)
        self.Gbox1.setToolTip('Category Of Data File')
        self.Gbox1.setStatusTip('Category Of Data File')
        
        #Group For File Kind Of Data File
        self.Gbox2 = QtGui.QGroupBox(self)
        self.Gbox2.setTitle('File')
        self.Gbox2.setGeometry(350, 20, 300, 100)
        self.Gbox2.setToolTip('File Choice')
        self.Gbox2.setStatusTip('File Choice')
        
        #Group For Search File 
        self.Gbox3 = QtGui.QGroupBox(self)
        self.Gbox3.setTitle('Search ')
        self.Gbox3.setGeometry(350, 120, 300, 100)
        self.Gbox3.setToolTip('Search File')
        self.Gbox3.setStatusTip('Search File')
        
	#Group Digital Clock 
        #self.Gbox4 = QtGui.QGroupBox(self)
        #self.Gbox4.setTitle('')
        #self.Gbox4.setGeometry(590, 2, 66, 20)
        #self.Gbox4.setToolTip('Digital Clock')
        #self.Gbox4.setStatusTip('Digital Clock')
	
	self.pagesWidget = QtGui.QStackedWidget(self)
	self.pagesWidget.setGeometry(618, 1, 80, 24)
        self.pagesWidget.addWidget(DigitalClock())
	self.pagesWidget.setToolTip('DigitalClock')
	self.pagesWidget.setStatusTip('DigitalClock')
	
        #Radio Button For GBox1
        self.RB_winfile = QtGui.QRadioButton(self.Gbox1)
        self.RB_winfile.setText('Programming Soft')
        self.RB_winfile.setGeometry(10, 20, 120, 20)
        self.RB_winfile.setToolTip('Programming Soft')
        self.RB_winfile.setStatusTip('Programming Soft')
	self.connect(self.RB_winfile, QtCore.SIGNAL("clicked()"), self.windowfile)
	
	#if self.RB_winfile.isActiveWindow():
	#    sys.exit()
	#    self.readerr
	#    self.windowfile()
	#self.windowfile()
        
        self.RB_linfile = QtGui.QRadioButton(self.Gbox1)
        self.RB_linfile.setText('Linux Programs')
        self.RB_linfile.setGeometry(10, 40, 120, 20)
        self.RB_linfile.setToolTip('Linux Programs')
        self.RB_linfile.setStatusTip('Linux Programs')
	self.connect(self.RB_linfile, QtCore.SIGNAL("clicked()"), self.linuxfile)
        
        self.RB_winmaster = QtGui.QRadioButton(self.Gbox1)
        self.RB_winmaster.setText('Windows Master')
        self.RB_winmaster.setGeometry(10, 60, 120, 20)
        self.RB_winmaster.setToolTip('Windows Master')
        self.RB_winmaster.setStatusTip('Windows Master')
	self.connect(self.RB_winmaster, QtCore.SIGNAL("clicked()"), self.windowmasterfile)
        
        self.RB_linmaster = QtGui.QRadioButton(self.Gbox1)
        self.RB_linmaster.setText('Linux Master')
        self.RB_linmaster.setGeometry(10, 80, 120, 20)
        self.RB_linmaster.setToolTip('Linux Master')
        self.RB_linmaster.setStatusTip('Linux Master')
	self.connect(self.RB_linmaster, QtCore.SIGNAL("clicked()"), self.linuxmaster)
        
        self.RB_music = QtGui.QRadioButton(self.Gbox1)
        self.RB_music.setText('Music Master')
        self.RB_music.setGeometry(10, 100, 130, 20)
        self.RB_music.setToolTip('Music Master')
        self.RB_music.setStatusTip('Music Master')
	self.connect(self.RB_music, QtCore.SIGNAL("clicked()"), self.musicmaster)
        
        self.RB_driverstudio = QtGui.QRadioButton(self.Gbox1)
        self.RB_driverstudio.setText('Driver Studio')
        self.RB_driverstudio.setGeometry(10, 120, 120, 20)
        self.RB_driverstudio.setToolTip('Driver Studio')
        self.RB_driverstudio.setStatusTip('Driver Studio')
	self.connect(self.RB_driverstudio, QtCore.SIGNAL("clicked()"), self.driverstudiomaster)
        
        self.RB_ebookfile = QtGui.QRadioButton(self.Gbox1)
        self.RB_ebookfile.setText('Ebooks')
        self.RB_ebookfile.setGeometry(10, 140, 120, 20)
        self.RB_ebookfile.setToolTip('Ebooks')
        self.RB_ebookfile.setStatusTip('Ebooks')
	self.connect(self.RB_ebookfile, QtCore.SIGNAL("clicked()"), self.ebookmaster)
        
        self.RB_netsoft = QtGui.QRadioButton(self.Gbox1)
        self.RB_netsoft.setText('Networking Soft')
        self.RB_netsoft.setGeometry(10, 160, 120, 20)
        self.RB_netsoft.setToolTip('Networking Soft')
        self.RB_netsoft.setStatusTip('Networking Soft')
	self.connect(self.RB_netsoft, QtCore.SIGNAL("clicked()"), self.netsoftmaster)
        
        self.RB_hddbck = QtGui.QRadioButton(self.Gbox1)
        self.RB_hddbck.setText('Harddisk Backup')
        self.RB_hddbck.setGeometry(140, 20, 120, 20)
        self.RB_hddbck.setToolTip('Harddisk Backup')
        self.RB_hddbck.setStatusTip('Harddisk Backup')
	self.connect(self.RB_hddbck, QtCore.SIGNAL("clicked()"), self.hddbckmaster)
        
        #self.RB_programmingsoft = QtGui.QRadioButton(self.Gbox1)
        #self.RB_programmingsoft.setText('Programming Soft')
        #self.RB_programmingsoft.setGeometry(140, 20, 120, 20)
        #self.RB_programmingsoft.setToolTip('Programming Soft')
        #self.RB_programmingsoft.setStatusTip('Programming Soft')
        
        self.RB_hackersoft = QtGui.QRadioButton(self.Gbox1)
        self.RB_hackersoft.setText('Hacker Soft')
        self.RB_hackersoft.setGeometry(140, 40, 120, 20)
        self.RB_hackersoft.setToolTip('Hacker Soft')
        self.RB_hackersoft.setStatusTip('Hacker Soft')
	self.connect(self.RB_hackersoft, QtCore.SIGNAL("clicked()"), self.hackersoftmaster)
        
        self.RB_gamesoft = QtGui.QRadioButton(self.Gbox1)
        self.RB_gamesoft.setText('Gamers')
        self.RB_gamesoft.setGeometry(140, 60, 120, 20)
        self.RB_gamesoft.setToolTip('Gamers')
        self.RB_gamesoft.setStatusTip('Gamers')
	self.connect(self.RB_gamesoft, QtCore.SIGNAL("clicked()"), self.gamesoftmaster)
        
        self.RB_bootsoft = QtGui.QRadioButton(self.Gbox1)
        self.RB_bootsoft.setText('Booting Soft')
        self.RB_bootsoft.setGeometry(140, 80, 120, 20)
        self.RB_bootsoft.setToolTip('Booting Soft')
        self.RB_bootsoft.setStatusTip('Booting Soft')
	self.connect(self.RB_bootsoft, QtCore.SIGNAL("clicked()"), self.bootsoftmaster)
        
        self.RB_databck = QtGui.QRadioButton(self.Gbox1)
        self.RB_databck.setText('Data Backup')
        self.RB_databck.setGeometry(140, 100, 120, 20)
        self.RB_databck.setToolTip('Data Backup')
        self.RB_databck.setStatusTip('Data Backup')
	self.connect(self.RB_databck, QtCore.SIGNAL("clicked()"), self.databckmaster)
	
	self.RB_datadrive = QtGui.QRadioButton(self.Gbox1)
        self.RB_datadrive.setText('Data Drive')
        self.RB_datadrive.setGeometry(140, 120, 120, 20)
        self.RB_datadrive.setToolTip('Data Drive')
        self.RB_datadrive.setStatusTip('Data Drive')
	self.connect(self.RB_datadrive, QtCore.SIGNAL("clicked()"), self.showdrive)
	
	self.Gbox4 = QtGui.QGroupBox(self.Gbox1)
	self.Gbox4.setTitle("Drive : ")
	self.Gbox4.setGeometry(113, 140, 204, 55)
	self.Gbox4.setFont(QtGui.QFont('Arial', 8))
	
	self.RB_C = QtGui.QRadioButton(self.Gbox4)
	self.RB_C.setGeometry(5, 15, 28, 13)
	self.RB_C.setText("C")
	self.RB_C.setToolTip("Drive C")
	self.RB_C.setStatusTip("Drive C")
	textme = self.RB_C.text()
	self.connect(self.RB_C, QtCore.SIGNAL("clicked()"), self.fileOpen2)
	
	self.RB_D = QtGui.QRadioButton(self.Gbox4)
	self.RB_D.setGeometry(5, 35, 28, 13)
	self.RB_D.setText("D")
	self.RB_D.setToolTip("Drive D")
	self.RB_D.setStatusTip("Drive D")
	self.connect(self.RB_D, QtCore.SIGNAL("clicked()"), self.fileOpen2)
	
	self.RB_E = QtGui.QRadioButton(self.Gbox4)
	self.RB_E.setGeometry(34, 15, 28, 13)
	self.RB_E.setText("E")
	self.RB_E.setToolTip("Drive E")
	self.RB_E.setStatusTip("Drive E")
	self.connect(self.RB_E, QtCore.SIGNAL("clicked()"), self.fileOpen2)
	
	self.RB_I = QtGui.QRadioButton(self.Gbox4)
	self.RB_I.setGeometry(34, 35, 28, 13)
	self.RB_I.setText("I")
	self.RB_I.setToolTip("Drive I")
	self.RB_I.setStatusTip("Drive I")
	self.connect(self.RB_I, QtCore.SIGNAL("clicked()"), self.fileOpen2)
	
	self.RB_J = QtGui.QRadioButton(self.Gbox4)
	self.RB_J.setGeometry(63, 15, 28, 13)
	self.RB_J.setText("J")
	self.RB_J.setToolTip("Drive J")
	self.RB_J.setStatusTip("Drive J")
	self.connect(self.RB_J, QtCore.SIGNAL("clicked()"), self.fileOpen2)
	
	self.RB_K = QtGui.QRadioButton(self.Gbox4)
	self.RB_K.setGeometry(63, 35, 28, 13)
	self.RB_K.setText("K")
	self.RB_K.setToolTip("Drive K")
	self.RB_K.setStatusTip("Drive K")
	self.connect(self.RB_K, QtCore.SIGNAL("clicked()"), self.fileOpen2)
	
	self.RB_L = QtGui.QRadioButton(self.Gbox4)
	self.RB_L.setGeometry(92, 15, 28, 13)
	self.RB_L.setText("L")
	self.RB_L.setToolTip("Drive L")
	self.RB_L.setStatusTip("Drive L")
	self.connect(self.RB_L, QtCore.SIGNAL("clicked()"), self.fileOpen2)
	
	self.RB_O = QtGui.QRadioButton(self.Gbox4)
	self.RB_O.setGeometry(92, 35, 28, 13)
	self.RB_O.setText("O")
	self.RB_O.setToolTip("Drive O")
	self.RB_O.setStatusTip("Drive O")
	self.connect(self.RB_O, QtCore.SIGNAL("clicked()"), self.fileOpen2)
	
	self.RB_P = QtGui.QRadioButton(self.Gbox4)
	self.RB_P.setGeometry(121, 15, 28, 13)
	self.RB_P.setText("P")
	self.RB_P.setToolTip("Drive P")
	self.RB_P.setStatusTip("Drive P")
	self.connect(self.RB_P, QtCore.SIGNAL("clicked()"), self.fileOpen2)
	
	self.RB_Q = QtGui.QRadioButton(self.Gbox4)
	self.RB_Q.setGeometry(121, 35, 28, 13)
	self.RB_Q.setText("Q")
	self.RB_Q.setToolTip("Drive Q")
	self.RB_Q.setStatusTip("Drive Q")
	self.connect(self.RB_Q, QtCore.SIGNAL("clicked()"), self.fileOpen2)
	
	self.Gbox5 = QtGui.QGroupBox(self.Gbox4)
	self.Gbox5.setTitle("Type : ")
	self.Gbox5.setFont(QtGui.QFont('Arial', 7))
	self.Gbox5.setGeometry(152, 7, 49, 45)
	
	self.RB_drivelist = QtGui.QRadioButton(self.Gbox5)
	self.RB_drivelist.setGeometry(3, 12, 40, 13)
	self.RB_drivelist.setText("List")
	self.RB_drivelist.setToolTip("List Type Drive")
	self.RB_drivelist.setStatusTip("List Type Drive")
	self.connect(self.RB_drivelist, QtCore.SIGNAL("clicked()"), self.showdrivebox4)
	self.connect(self.RB_drivelist, QtCore.SIGNAL("clicked()"), self.fileOpen2)
	
	self.RB_drivetree = QtGui.QRadioButton(self.Gbox5)
	self.RB_drivetree.setGeometry(3, 27, 40, 13)
	self.RB_drivetree.setText("Tree")
	self.RB_drivetree.setToolTip("Tree Type Drive")
	self.RB_drivetree.setStatusTip("Tree Type Drive")
	self.connect(self.RB_drivetree, QtCore.SIGNAL("clicked()"), self.showdrivebox4)
	self.connect(self.RB_drivetree, QtCore.SIGNAL("clicked()"), self.fileOpen2)
	
	#Hide GBox4
	self.Gbox4.hide()
	
#******************************************************************************************************************	
        
        #Combobox For File Chooce
        self.combolabel = QtGui.QLabel(self.Gbox2)
        self.combolabel.setGeometry(10, 10, 100, 30)
        self.combolabel.setText('File Choose    : ')
        
        self.combofile = QtGui.QComboBox(self.Gbox2)
        self.combofile.setGeometry(100, 15, 190, 20)
        self.combofile.setToolTip('Choose A File')
        self.combofile.setStatusTip('Choose A File')
        self.combofile.addItem("")
	self.connect(self.combofile, QtCore.SIGNAL("clicked()"), self.addinfo2)
	
	self.combofilelist = QtGui.QRadioButton(self.Gbox2)
        self.combofilelist.setText('List')
        self.combofilelist.setGeometry(100, 70, 100, 20)
        self.combofilelist.setToolTip('Format List')
        self.combofilelist.setStatusTip('Format List')
	self.connect(self.combofilelist, QtCore.SIGNAL("clicked()"), self.addinfo2)
	
	self.combofiletree = QtGui.QRadioButton(self.Gbox2)
        self.combofiletree.setText('Tree')
        self.combofiletree.setGeometry(160, 70, 100, 20)
        self.combofiletree.setToolTip('Format Tree')
        self.combofiletree.setStatusTip('Format Tree')
	self.connect(self.combofiletree, QtCore.SIGNAL("clicked()"), self.addinfo2)
	
	self.combolabeladdinfo1 = QtGui.QLabel(self.Gbox2)
        self.combolabeladdinfo1.setGeometry(10, 40, 100, 30)
        self.combolabeladdinfo1.setText('Info Add        : ')
	
	#Format Type Group Label
	self.formatLabel = QtGui.QLabel(self.Gbox2)
	self.formatLabel.setText("Format Type  : ")
	self.formatLabel.setGeometry(10, 65, 100, 30)
	
	self.combolabeladdinfo2 = QtGui.QLabel(self.Gbox2)
        self.combolabeladdinfo2.setGeometry(100, 40, 200, 30)
        #self.combolabeladdinfo2.setText('Hallo ')
	#datar =  self.combofile.currentText()
	#print datar
	
        
        self.combofilebt = QtGui.QPushButton(self.Gbox2)
	#self.combofilebt.setGeometry(20, 80, 70, 30)
        self.combofilebt.setGeometry(220, 65, 70, 30)
        self.combofilebt.setToolTip('See This File')
        self.combofilebt.setStatusTip('See This File')
        self.combofilebt.setText('See')
	self.connect(self.combofilebt, QtCore.SIGNAL('clicked()'), self.fileOpen)
	self.connect(self.combofilebt, QtCore.SIGNAL('clicked()'), self.addinfo2)

        
        #TextEdit For Searching File
	text=""
        self.search = QtGui.QComboBox(self.Gbox3)
        self.search.setGeometry(10, 20, 280, 20)
	self.search.setEditable(True)
        self.search.addItem(text)
        self.search.setSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
        self.search.setToolTip('Type A Text')
        self.search.setStatusTip('Type A Text')
	
	self.searchtext = QtGui.QComboBox(self.Gbox3)
        self.searchtext.setGeometry(95, 48, 120, 20)
	self.searchtext.setEditable(True)
        self.searchtext.addItem(text)
        self.searchtext.setSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Preferred)
	self.searchtext.setToolTip('Contained Text') 
        self.searchtext.setStatusTip('Contained Text')
	
	self.searchtextlabel = QtGui.QLabel(self.Gbox3)
        self.searchtextlabel.setGeometry(10, 43, 100, 30)
        self.searchtextlabel.setText('Contained Text : ')
        
        self.searchbt = QtGui.QPushButton(self.Gbox3)
        self.searchbt.setGeometry(220, 45, 70, 30)
        self.searchbt.setText('Search')
        self.searchbt.setToolTip('Search')
        self.searchbt.setStatusTip('Search')
	self.connect(self.searchbt, QtCore.SIGNAL("clicked()"), self.find)
	
	#self.filesFoundLabel = QtGui.QLabel(self)
	#self.filesFoundLabel.setGeometry(300, 470, 300, 30)
	#self.filesFoundLabel.setText("BLACKIDBLACKID - LIC")
        
        #Workscpace For Result
        self.wrk = QtGui.QWorkspace(self)
        self.wrk.setMinimumSize(500, 200)
        self.wrk.setGeometry(20, 245, 660, 230)
        self.wrk.setScrollBarsEnabled(True)
	
	self.createFilesTable()
        
        #Result Search
        self.result = QtGui.QTextEdit(self.wrk)
        self.result.setGeometry(0, 0, 660, 230)
        self.result.setToolTip('Result From Searching')
        self.result.setStatusTip('Result From Searching')
        
        self.resultlabel = QtGui.QLabel(self)
        self.resultlabel.setGeometry(20, 218, 100, 30)
        self.resultlabel.setText('Result        : ')
	
	self.resultlabelout = QtGui.QLabel(self)
	self.resultlabelout.setGeometry(100, 218, 400, 30)
	
	#In Current File Or In All File
	self.RB_currentFile = QtGui.QRadioButton(self.Gbox3)
	self.RB_currentFile.setText("Current File")
	self.RB_currentFile.setToolTip("Current File")
	self.RB_currentFile.setStatusTip("Current File")
	self.RB_currentFile.setGeometry(40, 75, 120, 20)
	
	self.RB_allFile = QtGui.QRadioButton(self.Gbox3)
	self.RB_allFile.setText("All File in Same Of Kinds")
	self.RB_allFile.setToolTip("All File in Same Of Kinds")
	self.RB_allFile.setStatusTip("All File in Same Of Kinds")
	self.RB_allFile.setGeometry(140, 75, 150, 20)
	
	self.combofilelist.hide()
	self.combofiletree.hide()
	
	#Create Table File Widget 
	#self.filesTable = QtGui.QTableWidget(self.wrk)
        #self.filesTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        #labels = QtCore.QStringList()
        #labels << self.tr("File Name") << self.tr("Size")
        #elf.filesTable.setHorizontalHeaderLabels(labels)
        #self.filesTable.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Stretch)
        #self.filesTable.verticalHeader().hide()
        #self.filesTable.setShowGrid(False)
	#self.filesTable.cellActivated.connect(self.openFileOfItem)
	#self.filesTable.setGeometry(0, 0, 660, 230)

#******************************************************************************************************************
	
    def windowfile(self):
	    self.combofilelist.show()
	    self.combofiletree.show()
	    self.combofile.clear()
	    self.combofilelist.clearFocus()
	    self.combofiletree.clearFocus()
	    self.result.clear()
	    self.resultlabelout.clear()
	    self.combofile.addItem("Choose A Format Type Of File")
	    self.resultlabelout.setText("Choose A Format Type Of File")
	    self.filesTable.hide()
	    self.result.show()
	    self.Gbox4.hide()
	    self.addinfo2
	    

	    if self.combofilelist.isChecked() + self.RB_winfile.isChecked():
		self.addinfo2
		self.connect(self.combofilelist, QtCore.SIGNAL("clicked()"), self.windowfilelist)
	    if self.combofiletree.isChecked() + self.RB_winfile.isChecked():
		self.addinfo2
		self.connect(self.combofiletree, QtCore.SIGNAL("clicked()"), self.windowfiletree)
    
    def linuxfile(self):
	    self.combofilelist.show()
	    self.combofiletree.show()
	    self.combofile.clear()
	    self.combofilelist.clearFocus()
	    self.combofiletree.clearFocus()
	    self.result.clear()
	    self.resultlabelout.clear()
	    self.combofile.addItem("Choose A Format Type Of File")
	    self.resultlabelout.setText("Choose A Format Type Of File")
	    self.filesTable.hide()
	    self.result.show()
	    self.Gbox4.hide()
	    self.addinfo2

	    if self.combofilelist.isChecked() + self.RB_linfile.isChecked():
		self.connect(self.combofilelist, QtCore.SIGNAL("clicked()"), self.linuxfilelist)
	    if self.combofiletree.isChecked() + self.RB_linfile.isChecked():
		self.connect(self.combofiletree, QtCore.SIGNAL("clicked()"), self.linuxfiletree)
    
    def linuxmaster(self):
	    self.combofilelist.show()
	    self.combofiletree.show()
	    self.combofile.clear()
	    self.combofilelist.clearFocus()
	    self.combofiletree.clearFocus()
	    self.result.clear()
	    self.resultlabelout.clear()
	    self.combofile.addItem("Choose A Format Type Of File")
	    self.resultlabelout.setText("Choose A Format Type Of File")
	    self.filesTable.hide()
	    self.result.show()
	    self.Gbox4.hide()
	    self.addinfo2

	    if self.combofilelist.isChecked() + self.RB_linmaster.isChecked():
		self.connect(self.combofilelist, QtCore.SIGNAL("clicked()"), self.linuxmfilelist)
	    if self.combofiletree.isChecked() + self.RB_linmaster.isChecked():
		self.connect(self.combofiletree, QtCore.SIGNAL("clicked()"), self.linuxmfiletree)
		
    def windowmasterfile(self):
	    self.combofilelist.show()
	    self.combofiletree.show()
	    self.combofile.clear()
	    self.combofilelist.clearFocus()
	    self.combofiletree.clearFocus()
	    self.result.clear()
	    self.resultlabelout.clear()
	    self.combofile.addItem("Choose A Format Type Of File")
	    self.resultlabelout.setText("Choose A Format Type Of File")
	    self.filesTable.hide()
	    self.result.show()
	    self.Gbox4.hide()
	    self.addinfo2

	    if self.combofilelist.isChecked() + self.RB_winmaster.isChecked():
		self.connect(self.combofilelist, QtCore.SIGNAL("clicked()"), self.windowMfilelist)
	    if self.combofiletree.isChecked() + self.RB_winmaster.isChecked():
		self.connect(self.combofiletree, QtCore.SIGNAL("clicked()"), self.windowMfiletree)
		
		
    def musicmaster(self):
	    self.combofilelist.show()
	    self.combofiletree.show()
	    self.combofile.clear()
	    self.combofilelist.clearFocus()
	    self.combofiletree.clearFocus()
	    self.result.clear()
	    self.resultlabelout.clear()
	    self.combofile.addItem("Choose A Format Type Of File")
	    self.resultlabelout.setText("Choose A Format Type Of File")
	    self.filesTable.hide()
	    self.result.show()
	    self.Gbox4.hide()
	    self.addinfo2

	    if self.combofilelist.isChecked() + self.RB_music.isChecked():
		self.connect(self.combofilelist, QtCore.SIGNAL("clicked()"), self.musicfilelist)
	    if self.combofiletree.isChecked() + self.RB_music.isChecked():
		self.connect(self.combofiletree, QtCore.SIGNAL("clicked()"), self.musicfiletree)
		
    def driverstudiomaster(self):
	    self.combofilelist.show()
	    self.combofiletree.show()
	    self.combofile.clear()
	    self.combofilelist.clearFocus()
	    self.combofiletree.clearFocus()
	    self.result.clear()
	    self.resultlabelout.clear()
	    self.combofile.addItem("Choose A Format Type Of File")
	    self.resultlabelout.setText("Choose A Format Type Of File")
	    self.filesTable.hide()
	    self.result.show()
	    self.Gbox4.hide()
	    self.addinfo2

	    if self.combofilelist.isChecked() + self.RB_driverstudio.isChecked():
		self.connect(self.combofilelist, QtCore.SIGNAL("clicked()"), self.driverstudiofilelist)
	    if self.combofiletree.isChecked() + self.RB_driverstudio.isChecked():
		self.connect(self.combofiletree, QtCore.SIGNAL("clicked()"), self.driverstudiofiletree)
		
    def ebookmaster(self):
	    self.combofilelist.show()
	    self.combofiletree.show()
	    self.combofile.clear()
	    self.combofilelist.clearFocus()
	    self.combofiletree.clearFocus()
	    self.result.clear()
	    self.resultlabelout.clear()
	    self.combofile.addItem("Choose A Format Type Of File")
	    self.resultlabelout.setText("Choose A Format Type Of File")
	    self.filesTable.hide()
	    self.result.show()
	    self.Gbox4.hide()
	    self.addinfo2

	    if self.combofilelist.isChecked() + self.RB_ebookfile.isChecked():
		self.connect(self.combofilelist, QtCore.SIGNAL("clicked()"), self.ebookfilelist)
	    if self.combofiletree.isChecked() + self.RB_ebookfile.isChecked():
		self.connect(self.combofiletree, QtCore.SIGNAL("clicked()"), self.ebookfiletree)
    
    def netsoftmaster(self):
	    self.combofilelist.show()
	    self.combofiletree.show()
	    self.combofile.clear()
	    self.combofilelist.clearFocus()
	    self.combofiletree.clearFocus()
	    self.result.clear()
	    self.resultlabelout.clear()
	    self.combofile.addItem("Choose A Format Type Of File")
	    self.resultlabelout.setText("Choose A Format Type Of File")
	    self.filesTable.hide()
	    self.result.show()
	    self.Gbox4.hide()
	    self.addinfo2

	    if self.combofilelist.isChecked() + self.RB_netsoft.isChecked():
		self.connect(self.combofilelist, QtCore.SIGNAL("clicked()"), self.netsoftlist)
	    if self.combofiletree.isChecked() + self.RB_netsoft.isChecked():
		self.connect(self.combofiletree, QtCore.SIGNAL("clicked()"), self.netsofttree)
        
    def hddbckmaster(self):
	    self.combofilelist.show()
	    self.combofiletree.show()
	    self.combofile.clear()
	    self.combofilelist.clearFocus()
	    self.combofiletree.clearFocus()
	    self.result.clear()
	    self.resultlabelout.clear()
	    self.combofile.addItem("Choose A Format Type Of File")
	    self.resultlabelout.setText("Choose A Format Type Of File")
	    self.filesTable.hide()
	    self.result.show()
	    self.Gbox4.hide()
	    self.addinfo2

	    if self.combofilelist.isChecked() + self.RB_hddbck.isChecked():
		self.connect(self.combofilelist, QtCore.SIGNAL("clicked()"), self.hddbcklist)
	    if self.combofiletree.isChecked() + self.RB_hddbck.isChecked():
		self.connect(self.combofiletree, QtCore.SIGNAL("clicked()"), self.hddbcktree)
    
    def hackersoftmaster(self):
	    self.combofilelist.show()
	    self.combofiletree.show()
	    self.combofile.clear()
	    self.combofilelist.clearFocus()
	    self.combofiletree.clearFocus()
	    self.result.clear()
	    self.resultlabelout.clear()
	    self.combofile.addItem("Choose A Format Type Of File")
	    self.resultlabelout.setText("Choose A Format Type Of File")
	    self.filesTable.hide()
	    self.result.show()
	    self.Gbox4.hide()
	    self.addinfo2

	    if self.combofilelist.isChecked() + self.RB_hackersoft.isChecked():
		self.connect(self.combofilelist, QtCore.SIGNAL("clicked()"), self.hackersoftlist)
	    if self.combofiletree.isChecked() + self.RB_hackersoft.isChecked():
		self.connect(self.combofiletree, QtCore.SIGNAL("clicked()"), self.hackersofttree)
        
    def gamesoftmaster(self):
	    self.combofilelist.show()
	    self.combofiletree.show()
	    self.combofile.clear()
	    self.combofilelist.clearFocus()
	    self.combofiletree.clearFocus()
	    self.result.clear()
	    self.resultlabelout.clear()
	    self.combofile.addItem("Choose A Format Type Of File")
	    self.resultlabelout.setText("Choose A Format Type Of File")
	    self.filesTable.hide()
	    self.result.show()
	    self.Gbox4.hide()
	    self.addinfo2

	    if self.combofilelist.isChecked() + self.RB_gamesoft.isChecked():
		self.connect(self.combofilelist, QtCore.SIGNAL("clicked()"), self.gamesoftlist)
	    if self.combofiletree.isChecked() + self.RB_gamesoft.isChecked():
		self.connect(self.combofiletree, QtCore.SIGNAL("clicked()"), self.gamesofttree)
    
    def bootsoftmaster(self):
	    self.combofilelist.show()
	    self.combofiletree.show()
	    self.combofile.clear()
	    self.combofilelist.clearFocus()
	    self.combofiletree.clearFocus()
	    self.result.clear()
	    self.resultlabelout.clear()
	    self.combofile.addItem("Choose A Format Type Of File")
	    self.resultlabelout.setText("Choose A Format Type Of File")
	    self.filesTable.hide()
	    self.result.show()
	    self.Gbox4.hide()
	    self.addinfo2

	    if self.combofilelist.isChecked() + self.RB_bootsoft.isChecked():
		self.connect(self.combofilelist, QtCore.SIGNAL("clicked()"), self.bootsoftlist)
	    if self.combofiletree.isChecked() + self.RB_bootsoft.isChecked():
		self.connect(self.combofiletree, QtCore.SIGNAL("clicked()"), self.bootsofttree)
        
    def databckmaster(self):
	    self.combofilelist.show()
	    self.combofiletree.show()
	    self.combofile.clear()
	    self.combofilelist.clearFocus()
	    self.combofiletree.clearFocus()
	    self.result.clear()
	    self.resultlabelout.clear()
	    self.combofile.addItem("Choose A Format Type Of File")
	    self.resultlabelout.setText("Choose A Format Type Of File")
	    self.filesTable.hide()
	    self.result.show()
	    self.Gbox4.hide()
	    self.addinfo2

	    if self.combofilelist.isChecked() + self.RB_databck.isChecked():
		self.connect(self.combofilelist, QtCore.SIGNAL("clicked()"), self.databcklist)
	    if self.combofiletree.isChecked() + self.RB_databck.isChecked():
		self.connect(self.combofiletree, QtCore.SIGNAL("clicked()"), self.databcktree)
        		
#------------------------------------------------------------------------------------------------------------------------

    def windowfilelist(self):
	    self.combofile.clear()
	    self.resultlabelout.setText("")
	    self.addinfo2
	    if self.RB_winfile.isChecked() and self.combofilelist.isChecked():
		self.addinfo2
                datanumlist =  os.popen('dir /d e:\CD_DVD_LIST\P*list*').readlines( )
                dataxnumlist =  datanumlist[-2].split(" File(s)")
                dataznumlist =  dataxnumlist[0].split(" ")
                x = int(dataznumlist[-1])
                print x
                #print dataz[-1]
                datalist = os.popen('dir /b e:\CD_DVD_LIST\P*list*').readlines( )
                
                for i in range(0,x):
		    datazlist =  datalist[i].split("\n")
		    #datay = dataz[0].split("_list")
		    #datax = datay[0].split("_")
		    #datax2 = datay[1].split(".txt")
		    #datax3 = datax2[0].split(")")
		    #datax4 = datax3[0].split("(")
		    self.combofile.addItem(datazlist[0])
		    #print datax3
                if self.combofile.itemText:
		    print self.combofile.currentIndex()
	    else:
		self.checkerr
		self.combofile.addItem("Choose A Format Type Of File")
		
		    
    def windowfiletree(self):
	self.combofile.clear()
	self.resultlabelout.setText("")
	self.addinfo2
        if self.RB_winfile.isChecked() and self.combofiletree.isChecked():
	    self.addinfo2
            datanumtree =  os.popen('dir /d e:\CD_DVD_LIST\P*tree*').readlines( )
            dataxnumtree =  datanumtree[-2].split(" File(s)")
            dataznumtree =  dataxnumtree[0].split(" ")
            x = int(dataznumtree[-1])
            print x
            #print dataz[-1]
            datatree = os.popen('dir /b e:\CD_DVD_LIST\P*tree*').readlines( )
            
            for i in range(0,x):
		dataztree =  datatree[i].split("\n")
		#datay = dataz[0].split("_list")
		#datax = datay[0].split("_")
		#datax2 = datay[1].split(".txt")
		#datax3 = datax2[0].split(")")
		#datax4 = datax3[0].split("(")
		self.combofile.addItem(dataztree[0])
		#print datax3
            if self.combofile.itemText:
		print self.combofile.currentIndex()
	else:
	    self.checkerr

    def linuxfilelist(self):
	    self.combofile.clear()
	    self.resultlabelout.setText("")
	    if self.RB_linfile.isChecked() and self.combofilelist.isChecked():
                datanumlist =  os.popen('dir /d e:\CD_DVD_LIST\L0*list*').readlines( )
                dataxnumlist =  datanumlist[-2].split(" File(s)")
                dataznumlist =  dataxnumlist[0].split(" ")
                x = int(dataznumlist[-1])
                print x
                #print dataz[-1]
                datalist = os.popen('dir /b e:\CD_DVD_LIST\L0*list*').readlines( )
                
                for i in range(0,x):
		    datazlist =  datalist[i].split("\n")
		    #datay = dataz[0].split("_list")
		    #datax = datay[0].split("_")
		    #datax2 = datay[1].split(".txt")
		    #datax3 = datax2[0].split(")")
		    #datax4 = datax3[0].split("(")
		    self.combofile.addItem(datazlist[0])
		    #print datax3
                if self.combofile.itemText:
		    print self.combofile.currentIndex()
	    else:
		self.checkerr
		
		    
    def linuxfiletree(self):
	self.combofile.clear()
	self.resultlabelout.setText("")
        if self.RB_linfile.isChecked() and self.combofiletree.isChecked():
            datanumtree =  os.popen('dir /d e:\CD_DVD_LIST\L0*tree*').readlines( )
            dataxnumtree =  datanumtree[-2].split(" File(s)")
            dataznumtree =  dataxnumtree[0].split(" ")
            x = int(dataznumtree[-1])
            print x
            #print dataz[-1]
            datatree = os.popen('dir /b e:\CD_DVD_LIST\L0*tree*').readlines( )
            
            for i in range(0,x):
		dataztree =  datatree[i].split("\n")
		#datay = dataz[0].split("_list")
		#datax = datay[0].split("_")
		#datax2 = datay[1].split(".txt")
		#datax3 = datax2[0].split(")")
		#datax4 = datax3[0].split("(")
		self.combofile.addItem(dataztree[0])
		#print datax3
            if self.combofile.itemText:
		print self.combofile.currentIndex()
	else:
	    self.checkerr
	    
    def windowMfilelist(self):
	    self.combofile.clear()
	    self.resultlabelout.setText("")
	    if self.RB_winmaster.isChecked() and self.combofilelist.isChecked():
                datanumlist =  os.popen('dir /d e:\CD_DVD_LIST\W*list*').readlines( )
                dataxnumlist =  datanumlist[-2].split(" File(s)")
                dataznumlist =  dataxnumlist[0].split(" ")
                x = int(dataznumlist[-1])
                print x
                #print dataz[-1]
                datalist = os.popen('dir /b e:\CD_DVD_LIST\W*list*').readlines( )
                
                for i in range(0,x):
		    datazlist =  datalist[i].split("\n")
		    #datay = dataz[0].split("_list")
		    #datax = datay[0].split("_")
		    #datax2 = datay[1].split(".txt")
		    #datax3 = datax2[0].split(")")
		    #datax4 = datax3[0].split("(")
		    self.combofile.addItem(datazlist[0])
		    #print datax3
                if self.combofile.itemText:
		    print self.combofile.currentIndex()
	    else:
		self.checkerr
		
		    
    def windowMfiletree(self):
	self.combofile.clear()
	self.resultlabelout.setText("")
        if self.RB_winmaster.isChecked() and self.combofiletree.isChecked():
            datanumtree =  os.popen('dir /d e:\CD_DVD_LIST\W*tree*').readlines( )
            dataxnumtree =  datanumtree[-2].split(" File(s)")
            dataznumtree =  dataxnumtree[0].split(" ")
            x = int(dataznumtree[-1])
            print x
            #print dataz[-1]
            datatree = os.popen('dir /b e:\CD_DVD_LIST\W*tree*').readlines( )
            
            for i in range(0,x):
		dataztree =  datatree[i].split("\n")
		#datay = dataz[0].split("_list")
		#datax = datay[0].split("_")
		#datax2 = datay[1].split(".txt")
		#datax3 = datax2[0].split(")")
		#datax4 = datax3[0].split("(")
		self.combofile.addItem(dataztree[0])
		#print datax3
            if self.combofile.itemText:
		print self.combofile.currentIndex()
	else:
	    self.checkerr
    
    
    def linuxmfilelist(self):
	    self.combofile.clear()
	    self.resultlabelout.setText("")
	    if self.RB_linmaster.isChecked() and self.combofilelist.isChecked():
                datanumlist =  os.popen('dir /d e:\CD_DVD_LIST\LM*list*').readlines( )
                dataxnumlist =  datanumlist[-2].split(" File(s)")
                dataznumlist =  dataxnumlist[0].split(" ")
                x = int(dataznumlist[-1])
                print x
                #print dataz[-1]
                datalist = os.popen('dir /b e:\CD_DVD_LIST\LM*list*').readlines( )
                
                for i in range(0,x):
		    datazlist =  datalist[i].split("\n")
		    #datay = dataz[0].split("_list")
		    #datax = datay[0].split("_")
		    #datax2 = datay[1].split(".txt")
		    #datax3 = datax2[0].split(")")
		    #datax4 = datax3[0].split("(")
		    self.combofile.addItem(datazlist[0])
		    #print datax3
                if self.combofile.itemText:
		    print self.combofile.currentIndex()
	    else:
		self.checkerr
		
		    
    def linuxmfiletree(self):
	self.combofile.clear()
	self.resultlabelout.setText("")
        if self.RB_linmaster.isChecked() and self.combofiletree.isChecked():
            datanumtree =  os.popen('dir /d e:\CD_DVD_LIST\LM*tree*').readlines( )
            dataxnumtree =  datanumtree[-2].split(" File(s)")
            dataznumtree =  dataxnumtree[0].split(" ")
            x = int(dataznumtree[-1])
            print x
            #print dataz[-1]
            datatree = os.popen('dir /b e:\CD_DVD_LIST\LM*tree*').readlines( )
            
            for i in range(0,x):
		dataztree =  datatree[i].split("\n")
		#datay = dataz[0].split("_list")
		#datax = datay[0].split("_")
		#datax2 = datay[1].split(".txt")
		#datax3 = datax2[0].split(")")
		#datax4 = datax3[0].split("(")
		self.combofile.addItem(dataztree[0])
		#print datax3
            if self.combofile.itemText:
		print self.combofile.currentIndex()
	else:
	    self.checkerr    
	    
    def musicfilelist(self):
	    self.combofile.clear()
	    self.resultlabelout.setText("")
	    if self.RB_music.isChecked() and self.combofilelist.isChecked():
                datanumlist =  os.popen('dir /d e:\CD_DVD_LIST\M*list*').readlines( )
                dataxnumlist =  datanumlist[-2].split(" File(s)")
                dataznumlist =  dataxnumlist[0].split(" ")
                x = int(dataznumlist[-1])
                print x
                #print dataz[-1]
                datalist = os.popen('dir /b e:\CD_DVD_LIST\M*list*').readlines( )
                
                for i in range(0,x):
		    datazlist =  datalist[i].split("\n")
		    #datay = dataz[0].split("_list")
		    #datax = datay[0].split("_")
		    #datax2 = datay[1].split(".txt")
		    #datax3 = datax2[0].split(")")
		    #datax4 = datax3[0].split("(")
		    self.combofile.addItem(datazlist[0])
		    #print datax3
                if self.combofile.itemText:
		    print self.combofile.currentIndex()
	    else:
		self.checkerr
		
		    
    def musicfiletree(self):
	self.combofile.clear()
	self.resultlabelout.setText("")
        if self.RB_music.isChecked() and self.combofiletree.isChecked():
            datanumtree =  os.popen('dir /d e:\CD_DVD_LIST\M*tree*').readlines( )
            dataxnumtree =  datanumtree[-2].split(" File(s)")
            dataznumtree =  dataxnumtree[0].split(" ")
            x = int(dataznumtree[-1])
            print x
            #print dataz[-1]
            datatree = os.popen('dir /b e:\CD_DVD_LIST\M*tree*').readlines( )
            
            for i in range(0,x):
		dataztree =  datatree[i].split("\n")
		#datay = dataz[0].split("_list")
		#datax = datay[0].split("_")
		#datax2 = datay[1].split(".txt")
		#datax3 = datax2[0].split(")")
		#datax4 = datax3[0].split("(")
		self.combofile.addItem(dataztree[0])
		#print datax3
            if self.combofile.itemText:
		print self.combofile.currentIndex()
	else:
	    self.checkerr
    
    def driverstudiofilelist(self):
	    self.combofile.clear()
	    self.resultlabelout.setText("")
	    if self.RB_driverstudio.isChecked() and self.combofilelist.isChecked():
                datanumlist =  os.popen('dir /d e:\CD_DVD_LIST\D*list*').readlines( )
                dataxnumlist =  datanumlist[-2].split(" File(s)")
                dataznumlist =  dataxnumlist[0].split(" ")
                x = int(dataznumlist[-1])
                print x
                #print dataz[-1]
                datalist = os.popen('dir /b e:\CD_DVD_LIST\D*list*').readlines( )
                
                for i in range(0,x):
		    datazlist =  datalist[i].split("\n")
		    #datay = dataz[0].split("_list")
		    #datax = datay[0].split("_")
		    #datax2 = datay[1].split(".txt")
		    #datax3 = datax2[0].split(")")
		    #datax4 = datax3[0].split("(")
		    self.combofile.addItem(datazlist[0])
		    #print datax3
                if self.combofile.itemText:
		    print self.combofile.currentIndex()
	    else:
		self.checkerr
		
		    
    def driverstudiofiletree(self):
	self.combofile.clear()
	self.resultlabelout.setText("")
        if self.RB_driverstudio.isChecked() and self.combofiletree.isChecked():
            datanumtree =  os.popen('dir /d e:\CD_DVD_LIST\D*tree*').readlines( )
            dataxnumtree =  datanumtree[-2].split(" File(s)")
            dataznumtree =  dataxnumtree[0].split(" ")
            x = int(dataznumtree[-1])
            print x
            #print dataz[-1]
            datatree = os.popen('dir /b e:\CD_DVD_LIST\D*tree*').readlines( )
            
            for i in range(0,x):
		dataztree =  datatree[i].split("\n")
		#datay = dataz[0].split("_list")
		#datax = datay[0].split("_")
		#datax2 = datay[1].split(".txt")
		#datax3 = datax2[0].split(")")
		#datax4 = datax3[0].split("(")
		self.combofile.addItem(dataztree[0])
		#print datax3
            if self.combofile.itemText:
		print self.combofile.currentIndex()
	else:
	    self.checkerr
	    
    def ebookfilelist(self):
	    self.combofile.clear()
	    self.resultlabelout.setText("")
	    if self.RB_ebookfile.isChecked() and self.combofilelist.isChecked():
                datanumlist =  os.popen('dir /d e:\CD_DVD_LIST\E*list*').readlines( )
                dataxnumlist =  datanumlist[-2].split(" File(s)")
                dataznumlist =  dataxnumlist[0].split(" ")
                x = int(dataznumlist[-1])
                print x
                #print dataz[-1]
                datalist = os.popen('dir /b e:\CD_DVD_LIST\E*list*').readlines( )
                
                for i in range(0,x):
		    datazlist =  datalist[i].split("\n")
		    #datay = dataz[0].split("_list")
		    #datax = datay[0].split("_")
		    #datax2 = datay[1].split(".txt")
		    #datax3 = datax2[0].split(")")
		    #datax4 = datax3[0].split("(")
		    self.combofile.addItem(datazlist[0])
		    #print datax3
                if self.combofile.itemText:
		    print self.combofile.currentIndex()
	    else:
		self.checkerr
		
		    
    def ebookfiletree(self):
	self.combofile.clear()
	self.resultlabelout.setText("")
        if self.RB_ebookfile.isChecked() and self.combofiletree.isChecked():
            datanumtree =  os.popen('dir /d e:\CD_DVD_LIST\E*tree*').readlines( )
            dataxnumtree =  datanumtree[-2].split(" File(s)")
            dataznumtree =  dataxnumtree[0].split(" ")
            x = int(dataznumtree[-1])
            print x
            #print dataz[-1]
            datatree = os.popen('dir /b e:\CD_DVD_LIST\E*tree*').readlines( )
            
            for i in range(0,x):
		dataztree =  datatree[i].split("\n")
		#datay = dataz[0].split("_list")
		#datax = datay[0].split("_")
		#datax2 = datay[1].split(".txt")
		#datax3 = datax2[0].split(")")
		#datax4 = datax3[0].split("(")
		self.combofile.addItem(dataztree[0])
		#print datax3
            if self.combofile.itemText:
		print self.combofile.currentIndex()
	else:
	    self.checkerr
	    
    def netsoftlist(self):
	    self.combofile.clear()
	    self.resultlabelout.setText("")
	    if self.RB_netsoft.isChecked() and self.combofilelist.isChecked():
                datanumlist =  os.popen('dir /d e:\CD_DVD_LIST\N*list*').readlines( )
                dataxnumlist =  datanumlist[-2].split(" File(s)")
                dataznumlist =  dataxnumlist[0].split(" ")
                x = int(dataznumlist[-1])
                print x
                #print dataz[-1]
                datalist = os.popen('dir /b e:\CD_DVD_LIST\N*list*').readlines( )
                
                for i in range(0,x):
		    datazlist =  datalist[i].split("\n")
		    #datay = dataz[0].split("_list")
		    #datax = datay[0].split("_")
		    #datax2 = datay[1].split(".txt")
		    #datax3 = datax2[0].split(")")
		    #datax4 = datax3[0].split("(")
		    self.combofile.addItem(datazlist[0])
		    #print datax3
                if self.combofile.itemText:
		    print self.combofile.currentIndex()
	    else:
		self.checkerr
		
		    
    def netsofttree(self):
	self.combofile.clear()
	self.resultlabelout.setText("")
        if self.RB_netsoft.isChecked() and self.combofiletree.isChecked():
            datanumtree =  os.popen('dir /d e:\CD_DVD_LIST\N*tree*').readlines( )
            dataxnumtree =  datanumtree[-2].split(" File(s)")
            dataznumtree =  dataxnumtree[0].split(" ")
            x = int(dataznumtree[-1])
            print x
            #print dataz[-1]
            datatree = os.popen('dir /b e:\CD_DVD_LIST\N*tree*').readlines( )
            
            for i in range(0,x):
		dataztree =  datatree[i].split("\n")
		#datay = dataz[0].split("_list")
		#datax = datay[0].split("_")
		#datax2 = datay[1].split(".txt")
		#datax3 = datax2[0].split(")")
		#datax4 = datax3[0].split("(")
		self.combofile.addItem(dataztree[0])
		#print datax3
            if self.combofile.itemText:
		print self.combofile.currentIndex()
	else:
	    self.checkerr
	    
    def hddbcklist(self):
	    self.combofile.clear()
	    self.resultlabelout.setText("")
	    if self.RB_hddbck.isChecked() and self.combofilelist.isChecked():
                datanumlist =  os.popen('dir /d e:\CD_DVD_LIST\HD*list*').readlines( )
                dataxnumlist =  datanumlist[-2].split(" File(s)")
                dataznumlist =  dataxnumlist[0].split(" ")
                x = int(dataznumlist[-1])
                print x
                #print dataz[-1]
                datalist = os.popen('dir /b e:\CD_DVD_LIST\HD*list*').readlines( )
                
                for i in range(0,x):
		    datazlist =  datalist[i].split("\n")
		    #datay = dataz[0].split("_list")
		    #datax = datay[0].split("_")
		    #datax2 = datay[1].split(".txt")
		    #datax3 = datax2[0].split(")")
		    #datax4 = datax3[0].split("(")
		    self.combofile.addItem(datazlist[0])
		    #print datax3
                if self.combofile.itemText:
		    print self.combofile.currentIndex()
	    else:
		self.checkerr
		
		    
    def hddbcktree(self):
	self.combofile.clear()
	self.resultlabelout.setText("")
        if self.RB_hddbck.isChecked() and self.combofiletree.isChecked():
            datanumtree =  os.popen('dir /d e:\CD_DVD_LIST\HD*tree*').readlines( )
            dataxnumtree =  datanumtree[-2].split(" File(s)")
            dataznumtree =  dataxnumtree[0].split(" ")
            x = int(dataznumtree[-1])
            print x
            #print dataz[-1]
            datatree = os.popen('dir /b e:\CD_DVD_LIST\HD*tree*').readlines( )
            
            for i in range(0,x):
		dataztree =  datatree[i].split("\n")
		#datay = dataz[0].split("_list")
		#datax = datay[0].split("_")
		#datax2 = datay[1].split(".txt")
		#datax3 = datax2[0].split(")")
		#datax4 = datax3[0].split("(")
		self.combofile.addItem(dataztree[0])
		#print datax3
            if self.combofile.itemText:
		print self.combofile.currentIndex()
	else:
	    self.checkerr
	    
    def hackersoftlist(self):
	    self.combofile.clear()
	    self.resultlabelout.setText("")
	    if self.RB_hackersoft.isChecked() and self.combofilelist.isChecked():
                datanumlist =  os.popen('dir /d e:\CD_DVD_LIST\HCK*list*').readlines( )
                dataxnumlist =  datanumlist[-2].split(" File(s)")
                dataznumlist =  dataxnumlist[0].split(" ")
                x = int(dataznumlist[-1])
                print x
                #print dataz[-1]
                datalist = os.popen('dir /b e:\CD_DVD_LIST\HCK*list*').readlines( )
                
                for i in range(0,x):
		    datazlist =  datalist[i].split("\n")
		    #datay = dataz[0].split("_list")
		    #datax = datay[0].split("_")
		    #datax2 = datay[1].split(".txt")
		    #datax3 = datax2[0].split(")")
		    #datax4 = datax3[0].split("(")
		    self.combofile.addItem(datazlist[0])
		    #print datax3
                if self.combofile.itemText:
		    print self.combofile.currentIndex()
	    else:
		self.checkerr
		
		    
    def hackersofttree(self):
	self.combofile.clear()
	self.resultlabelout.setText("")
        if self.RB_hackersoft.isChecked() and self.combofiletree.isChecked():
            datanumtree =  os.popen('dir /d e:\CD_DVD_LIST\HCK*tree*').readlines( )
            dataxnumtree =  datanumtree[-2].split(" File(s)")
            dataznumtree =  dataxnumtree[0].split(" ")
            x = int(dataznumtree[-1])
            print x
            #print dataz[-1]
            datatree = os.popen('dir /b e:\CD_DVD_LIST\HCK*tree*').readlines( )
            
            for i in range(0,x):
		dataztree =  datatree[i].split("\n")
		#datay = dataz[0].split("_list")
		#datax = datay[0].split("_")
		#datax2 = datay[1].split(".txt")
		#datax3 = datax2[0].split(")")
		#datax4 = datax3[0].split("(")
		self.combofile.addItem(dataztree[0])
		#print datax3
            if self.combofile.itemText:
		print self.combofile.currentIndex()
	else:
	    self.checkerr
	    
    def gamesoftlist(self):
	    self.combofile.clear()
	    self.resultlabelout.setText("")
	    if self.RB_gamesoft.isChecked() and self.combofilelist.isChecked():
                datanumlist =  os.popen('dir /d e:\CD_DVD_LIST\G*list*').readlines( )
                dataxnumlist =  datanumlist[-2].split(" File(s)")
                dataznumlist =  dataxnumlist[0].split(" ")
                x = int(dataznumlist[-1])
                print x
                #print dataz[-1]
                datalist = os.popen('dir /b e:\CD_DVD_LIST\G*list*').readlines( )
                
                for i in range(0,x):
		    datazlist =  datalist[i].split("\n")
		    #datay = dataz[0].split("_list")
		    #datax = datay[0].split("_")
		    #datax2 = datay[1].split(".txt")
		    #datax3 = datax2[0].split(")")
		    #datax4 = datax3[0].split("(")
		    self.combofile.addItem(datazlist[0])
		    #print datax3
                if self.combofile.itemText:
		    print self.combofile.currentIndex()
	    else:
		self.checkerr
		
		    
    def gamesofttree(self):
	self.combofile.clear()
	self.resultlabelout.setText("")
        if self.RB_gamesoft.isChecked() and self.combofiletree.isChecked():
            datanumtree =  os.popen('dir /d e:\CD_DVD_LIST\G*tree*').readlines( )
            dataxnumtree =  datanumtree[-2].split(" File(s)")
            dataznumtree =  dataxnumtree[0].split(" ")
            x = int(dataznumtree[-1])
            print x
            #print dataz[-1]
            datatree = os.popen('dir /b e:\CD_DVD_LIST\G*tree*').readlines( )
            
            for i in range(0,x):
		dataztree =  datatree[i].split("\n")
		#datay = dataz[0].split("_list")
		#datax = datay[0].split("_")
		#datax2 = datay[1].split(".txt")
		#datax3 = datax2[0].split(")")
		#datax4 = datax3[0].split("(")
		self.combofile.addItem(dataztree[0])
		#print datax3
            if self.combofile.itemText:
		print self.combofile.currentIndex()
	else:
	    self.checkerr
	    
    def bootsoftlist(self):
	    self.combofile.clear()
	    self.resultlabelout.setText("")
	    if self.RB_bootsoft.isChecked() and self.combofilelist.isChecked():
                datanumlist =  os.popen('dir /d e:\CD_DVD_LIST\B0*list*').readlines( )
                dataxnumlist =  datanumlist[-2].split(" File(s)")
                dataznumlist =  dataxnumlist[0].split(" ")
                x = int(dataznumlist[-1])
                print x
                #print dataz[-1]
                datalist = os.popen('dir /b e:\CD_DVD_LIST\B0*list*').readlines( )
                
                for i in range(0,x):
		    datazlist =  datalist[i].split("\n")
		    #datay = dataz[0].split("_list")
		    #datax = datay[0].split("_")
		    #datax2 = datay[1].split(".txt")
		    #datax3 = datax2[0].split(")")
		    #datax4 = datax3[0].split("(")
		    self.combofile.addItem(datazlist[0])
		    #print datax3
                if self.combofile.itemText:
		    print self.combofile.currentIndex()
	    else:
		self.checkerr
		
		    
    def bootsofttree(self):
	self.combofile.clear()
	self.resultlabelout.setText("")
        if self.RB_bootsoft.isChecked() and self.combofiletree.isChecked():
            datanumtree =  os.popen('dir /d e:\CD_DVD_LIST\B0*tree*').readlines( )
            dataxnumtree =  datanumtree[-2].split(" File(s)")
            dataznumtree =  dataxnumtree[0].split(" ")
            x = int(dataznumtree[-1])
            print x
            #print dataz[-1]
            datatree = os.popen('dir /b e:\CD_DVD_LIST\B0*tree*').readlines( )
            
            for i in range(0,x):
		dataztree =  datatree[i].split("\n")
		#datay = dataz[0].split("_list")
		#datax = datay[0].split("_")
		#datax2 = datay[1].split(".txt")
		#datax3 = datax2[0].split(")")
		#datax4 = datax3[0].split("(")
		self.combofile.addItem(dataztree[0])
		#print datax3
            if self.combofile.itemText:
		print self.combofile.currentIndex()
	else:
	    self.checkerr
	    
    def databcklist(self):
	    self.combofile.clear()
	    self.resultlabelout.setText("")
	    if self.RB_databck.isChecked() and self.combofilelist.isChecked():
                datanumlist =  os.popen('dir /d e:\CD_DVD_LIST\BCK*list*').readlines( )
                dataxnumlist =  datanumlist[-2].split(" File(s)")
                dataznumlist =  dataxnumlist[0].split(" ")
                x = int(dataznumlist[-1])
                print x
                #print dataz[-1]
                datalist = os.popen('dir /b e:\CD_DVD_LIST\BCK*list*').readlines( )
                
                for i in range(0,x):
		    datazlist =  datalist[i].split("\n")
		    #datay = dataz[0].split("_list")
		    #datax = datay[0].split("_")
		    #datax2 = datay[1].split(".txt")
		    #datax3 = datax2[0].split(")")
		    #datax4 = datax3[0].split("(")
		    self.combofile.addItem(datazlist[0])
		    #print datax3
                if self.combofile.itemText:
		    print self.combofile.currentIndex()
	    else:
		self.checkerr
		
		    
    def databcktree(self):
	self.combofile.clear()
	self.resultlabelout.setText("")
        if self.RB_databck.isChecked() and self.combofiletree.isChecked():
            datanumtree =  os.popen('dir /d e:\CD_DVD_LIST\BCK*tree*').readlines( )
            dataxnumtree =  datanumtree[-2].split(" File(s)")
            dataznumtree =  dataxnumtree[0].split(" ")
            x = int(dataznumtree[-1])
            print x
            #print dataz[-1]
            datatree = os.popen('dir /b e:\CD_DVD_LIST\BCK*tree*').readlines( )
            
            for i in range(0,x):
		dataztree =  datatree[i].split("\n")
		#datay = dataz[0].split("_list")
		#datax = datay[0].split("_")
		#datax2 = datay[1].split(".txt")
		#datax3 = datax2[0].split(")")
		#datax4 = datax3[0].split("(")
		self.combofile.addItem(dataztree[0])
		#print datax3
            if self.combofile.itemText:
		print self.combofile.currentIndex()
	else:
	    self.checkerr
	    
#-----------------------------------------------------------------------------------------------------------------------
	    
    def fileOpen(self):
	self.result.show()
        try:
	    self.resultlabelout.setText(self.combofile.currentText())
            #self.namefile = QtGui.QFileDialog.getOpenFileName(self, "OpenFile")
            #self.namefile = self.combofile.itemData(self.combofile.currentIndex()).toString()
            datar =  self.combofile.currentText()
	    datahasil = (r"E:\CD_DVD_LIST" + "\\" + datar)
            print datar
            #self.namefile = self.combofile.currentText()
            self.namefile = str(datahasil)
            #self.namefile = 'E:\CD_DVD_LIST\\' + datar
            #dataku = self.namefile = str(datar)
            #print dataku.split("\\n")
            
            infile = open(self.namefile, "r")
            if infile:
		string = infile.read()
		infile.close()
		#self.textEdit.setText(filename)
		#self.loadFile(filename)
	    self.result.setText(string)

        except IOError, e:
            #self.readerr()
            print e
    
    def fileOpen2(self):
	self.result.clear()
	self.result.show()
        try:  
	    if self.RB_C.isChecked() and self.RB_drivelist.isChecked():
		datar =  self.RB_C.text()
		#self.resultlabelout.setText(datar)
		self.resultlabelout.setText(datar + ":\\")
		print datar
		datatextlist = (r"D:\LIST_DIRECTORY\LIST" + "\\" + datar + "_list.txt")
		print datatextlist
		self.namefile = str(datatextlist)
		
		infile = open(self.namefile, "r")
		if infile:
		    string = infile.read()
		    infile.close()
		self.result.setText(string)
		
	    elif self.RB_C.isChecked() and self.RB_drivetree.isChecked():
		    datar =  self.RB_C.text()
		    #self.resultlabelout.setText(datar)
		    self.resultlabelout.setText(datar + ":\\")
		    print datar
		    datatexttree = (r"D:\LIST_DIRECTORY\TREE" + "\\" + datar + "_tree.txt")
		    print datatexttree
		    self.namefile = str(datatexttree)
		    
		    infile = open(self.namefile, "r")
		    if infile:
			string = infile.read()
			infile.close()
		    self.result.setText(string)
		    
	    elif self.RB_D.isChecked() and self.RB_drivelist.isChecked():
		datar =  self.RB_D.text()
		#self.resultlabelout.setText(datar)
		self.resultlabelout.setText(datar + ":\\")
		print datar
		datatextlist = (r"D:\LIST_DIRECTORY\LIST" + "\\" + datar + "_list.txt")
		print datatextlist
		self.namefile = str(datatextlist)
		
		infile = open(self.namefile, "r")
		if infile:
		    string = infile.read()
		    infile.close()
		self.result.setText(string)
		    
	    elif self.RB_D.isChecked() and self.RB_drivetree.isChecked():
		    datar =  self.RB_D.text()
		    #self.resultlabelout.setText(datar)
		    self.resultlabelout.setText(datar + ":\\")
		    print datar
		    datatexttree = (r"D:\LIST_DIRECTORY\TREE" + "\\" + datar + "_tree.txt")
		    print datatexttree
		    self.namefile = str(datatexttree)
		    
		    infile = open(self.namefile, "r")
		    if infile:
			string = infile.read()
			infile.close()
		    self.result.setText(string)
		
	    elif self.RB_E.isChecked() and self.RB_drivelist.isChecked():
		datar =  self.RB_E.text()
		#self.resultlabelout.setText(datar)
		self.resultlabelout.setText(datar + ":\\")
		print datar
		datatextlist = (r"D:\LIST_DIRECTORY\LIST" + "\\" + datar + "_list.txt")
		print datatextlist
		self.namefile = str(datatextlist)
		
		infile = open(self.namefile, "r")
		if infile:
		    string = infile.read()
		    infile.close()
		self.result.setText(string)
		    
	    elif self.RB_E.isChecked() and self.RB_drivetree.isChecked():
		    datar =  self.RB_E.text()
		    #self.resultlabelout.setText(datar)
		    self.resultlabelout.setText(datar + ":\\")
		    print datar
		    datatexttree = (r"D:\LIST_DIRECTORY\TREE" + "\\" + datar + "_tree.txt")
		    print datatexttree
		    self.namefile = str(datatexttree)
		    
		    infile = open(self.namefile, "r")
		    if infile:
			string = infile.read()
			infile.close()
		    self.result.setText(string)
		    
	    elif self.RB_I.isChecked() and self.RB_drivelist.isChecked():
		datar =  self.RB_I.text()
		#self.resultlabelout.setText(datar)
		self.resultlabelout.setText(datar + ":\\")
		print datar
		datatextlist = (r"D:\LIST_DIRECTORY\LIST" + "\\" + datar + "_list.txt")
		print datatextlist
		self.namefile = str(datatextlist)
		
		infile = open(self.namefile, "r")
		if infile:
		    string = infile.read()
		    infile.close()
		self.result.setText(string)
		    
	    elif self.RB_I.isChecked() and self.RB_drivetree.isChecked():
		    datar =  self.RB_I.text()
		    #self.resultlabelout.setText(datar)
		    self.resultlabelout.setText(datar + ":\\")
		    print datar
		    datatexttree = (r"D:\LIST_DIRECTORY\TREE" + "\\" + datar + "_tree.txt")
		    print datatexttree
		    self.namefile = str(datatexttree)
		    
		    infile = open(self.namefile, "r")
		    if infile:
			string = infile.read()
			infile.close()
		    self.result.setText(string)
		    
	    elif self.RB_J.isChecked() and self.RB_drivelist.isChecked():
		datar =  self.RB_J.text()
		#self.resultlabelout.setText(datar)
		self.resultlabelout.setText(datar + ":\\")
		print datar
		datatextlist = (r"D:\LIST_DIRECTORY\LIST" + "\\" + datar + "_list.txt")
		print datatextlist
		self.namefile = str(datatextlist)
		
		infile = open(self.namefile, "r")
		if infile:
		    string = infile.read()
		    infile.close()
		self.result.setText(string)
		    
	    elif self.RB_J.isChecked() and self.RB_drivetree.isChecked():
		    datar =  self.RB_J.text()
		    #self.resultlabelout.setText(datar)
		    self.resultlabelout.setText(datar + ":\\")
		    print datar
		    datatexttree = (r"D:\LIST_DIRECTORY\TREE" + "\\" + datar + "_tree.txt")
		    print datatexttree
		    self.namefile = str(datatexttree)
		    
		    infile = open(self.namefile, "r")
		    if infile:
			string = infile.read()
			infile.close()
		    self.result.setText(string)
		    
	    elif self.RB_K.isChecked() and self.RB_drivelist.isChecked():
		datar =  self.RB_K.text()
		#self.resultlabelout.setText(datar)
		self.resultlabelout.setText(datar + ":\\")
		print datar
		datatextlist = (r"D:\LIST_DIRECTORY\LIST" + "\\" + datar + "_list.txt")
		print datatextlist
		self.namefile = str(datatextlist)
		
		infile = open(self.namefile, "r")
		if infile:
		    string = infile.read()
		    infile.close()
		self.result.setText(string)
		    
	    elif self.RB_K.isChecked() and self.RB_drivetree.isChecked():
		    datar =  self.RB_K.text()
		    #self.resultlabelout.setText(datar)
		    self.resultlabelout.setText(datar + ":\\")
		    print datar
		    datatexttree = (r"D:\LIST_DIRECTORY\TREE" + "\\" + datar + "_tree.txt")
		    print datatexttree
		    self.namefile = str(datatexttree)
		    
		    infile = open(self.namefile, "r")
		    if infile:
			string = infile.read()
			infile.close()
		    self.result.setText(string)
		    
	    elif self.RB_L.isChecked() and self.RB_drivelist.isChecked():
		datar =  self.RB_L.text()
		#self.resultlabelout.setText(datar)
		self.resultlabelout.setText(datar + ":\\")
		print datar
		datatextlist = (r"D:\LIST_DIRECTORY\LIST" + "\\" + datar + "_list.txt")
		print datatextlist
		self.namefile = str(datatextlist)
		
		infile = open(self.namefile, "r")
		if infile:
		    string = infile.read()
		    infile.close()
		self.result.setText(string)
		    
	    elif self.RB_L.isChecked() and self.RB_drivetree.isChecked():
		    datar =  self.RB_L.text()
		    #self.resultlabelout.setText(datar)
		    self.resultlabelout.setText(datar + ":\\")
		    print datar
		    datatexttree = (r"D:\LIST_DIRECTORY\TREE" + "\\" + datar + "_tree.txt")
		    print datatexttree
		    self.namefile = str(datatexttree)
		    
		    infile = open(self.namefile, "r")
		    if infile:
			string = infile.read()
			infile.close()
		    self.result.setText(string)
		    
	    elif self.RB_O.isChecked() and self.RB_drivelist.isChecked():
		datar =  self.RB_O.text()
		#self.resultlabelout.setText(datar)
		self.resultlabelout.setText(datar + ":\\")
		print datar
		datatextlist = (r"D:\LIST_DIRECTORY\LIST" + "\\" + datar + "_list.txt")
		print datatextlist
		self.namefile = str(datatextlist)
		
		infile = open(self.namefile, "r")
		if infile:
		    string = infile.read()
		    infile.close()
		self.result.setText(string)
		    
	    elif self.RB_O.isChecked() and self.RB_drivetree.isChecked():
		    datar =  self.RB_O.text()
		    #self.resultlabelout.setText(datar)
		    self.resultlabelout.setText(datar + ":\\")
		    print datar
		    datatexttree = (r"D:\LIST_DIRECTORY\TREE" + "\\" + datar + "_tree.txt")
		    print datatexttree
		    self.namefile = str(datatexttree)
		    
		    infile = open(self.namefile, "r")
		    if infile:
			string = infile.read()
			infile.close()
		    self.result.setText(string)
		    
	    elif self.RB_P.isChecked() and self.RB_drivelist.isChecked():
		datar =  self.RB_P.text()
		#self.resultlabelout.setText(datar)
		self.resultlabelout.setText(datar + ":\\")
		print datar
		datatextlist = (r"D:\LIST_DIRECTORY\LIST" + "\\" + datar + "_list.txt")
		print datatextlist
		self.namefile = str(datatextlist)
		
		infile = open(self.namefile, "r")
		if infile:
		    string = infile.read()
		    infile.close()
		self.result.setText(string)
		    
	    elif self.RB_P.isChecked() and self.RB_drivetree.isChecked():
		    datar =  self.RB_P.text()
		    #self.resultlabelout.setText(datar)
		    self.resultlabelout.setText(datar + ":\\")
		    print datar
		    datatexttree = (r"D:\LIST_DIRECTORY\TREE" + "\\" + datar + "_tree.txt")
		    print datatexttree
		    self.namefile = str(datatexttree)
		    
		    infile = open(self.namefile, "r")
		    if infile:
			string = infile.read()
			infile.close()
		    self.result.setText(string)
		    
	    elif self.RB_Q.isChecked() and self.RB_drivelist.isChecked():
		datar =  self.RB_Q.text()
		#self.resultlabelout.setText(datar)
		self.resultlabelout.setText(datar + ":\\")
		print datar
		datatextlist = (r"D:\LIST_DIRECTORY\LIST" + "\\" + datar + "_list.txt")
		print datatextlist
		self.namefile = str(datatextlist)
		
		infile = open(self.namefile, "r")
		if infile:
		    string = infile.read()
		    infile.close()
		self.result.setText(string)
		    
	    elif self.RB_Q.isChecked() and self.RB_drivetree.isChecked():
		    datar =  self.RB_Q.text()
		    #self.resultlabelout.setText(datar)
		    self.resultlabelout.setText(datar + ":\\")
		    print datar
		    datatexttree = (r"D:\LIST_DIRECTORY\TREE" + "\\" + datar + "_tree.txt")
		    print datatexttree
		    self.namefile = str(datatexttree)
		    
		    infile = open(self.namefile, "r")
		    if infile:
			string = infile.read()
			infile.close()
		    self.result.setText(string)
		
	    else:
		self.resultlabelout.setText("Please Select Type Format Of File")
	 
        except IOError, e:
		print e
	    
	except OSError, e:
		if e.errno == errno.ENOENT:
			print "\n Program tidak ditemukan \n"
		elif e.errno == errno.ENOEXEC:
			print "\n Program bukan program excutable ! \n"
    
		
    def addinfo2(self):
	try:
	    if self.combofile.currentIndex != "":
		data = str(self.combofile.currentText())
		dataz =  data.split("\n")
		datay = dataz[0].split(")")
		datax = datay[0].split("(")
		
		#self.combolabeladdinfo2.setText(datainfox4[-1])
		self.combolabeladdinfo2.setText(str(datax[1]))
		#print "testMe1 :", datainfox, "\n\n"
		#print "testMe2 :", datainfox4, "\n\n"
		#print "datainfo :", datainfox4[-1]
		print "datax = ", datax
	except IndexError, e:
	    self.combolabeladdinfo2.setText("")
					    
	

    def readerr(self):
	    msgre = QtGui.QMessageBox.question(self, 'Message', 'File tidak dapat dibaca , \nsilahkan cek hak akses File !', QtGui.QMessageBox.Close)
	    if msgre == QtGui.QMessageBox.Close:
		    self.destroy()
		    sys.exit()
	    else:
		return(1)
	    
    def checkerr(self):
	    msgre = QtGui.QMessageBox.question(self, 'Message', 'Jenis File Belum terpilib , \nsilahkan Pilih Jenis File yang akan ditampilkan !', QtGui.QMessageBox.Close)
	    if msgre == QtGui.QMessageBox.Close:
		    self.destroy()
	    else:
		return(1)
    
    def infoerr(self):
	    self.resultlabelout.setText("PLEASE SELECT A TYPE FORMAT OF FILE")
	    
    @staticmethod
    def updateComboBox(comboBox):
        if comboBox.findText(comboBox.currentText()) == -1:
            comboBox.addItem(comboBox.currentText())
	    
    def find(self):
	self.result.hide()
	#self.filesTable.show()
	
        self.filesTable.setRowCount(0)

        fileName = self.search.currentText()
        text = self.searchtext.currentText()
        path = QtCore.QDir.currentPath()

        self.updateComboBox(self.search)
        self.updateComboBox(self.searchtext)

        self.currentDir = QtCore.QDir(path)
        if fileName.isEmpty():
            fileName = "*"
        files = self.currentDir.entryList(QtCore.QStringList(fileName),
                QtCore.QDir.Files | QtCore.QDir.NoSymLinks)

        if not text.isEmpty():
            files = self.findFiles(files, text)
        self.showFiles(files)
	
    def findFiles(self, files, text):
	
        progressDialog = QtGui.QProgressDialog(self)

        progressDialog.setCancelButtonText(self.tr("&Cancel"))
        progressDialog.setRange(0, files.count())
        progressDialog.setWindowTitle(self.tr("Find Files"))

        foundFiles = QtCore.QStringList()

        for i in range(files.count()):
            progressDialog.setValue(i)
            progressDialog.setLabelText(self.tr("Searching file number %1 of %2...")
                                                .arg(i).arg(files.count()))
            QtGui.qApp.processEvents()

            if progressDialog.wasCanceled():
                break

            inFile = QtCore.QFile(self.currentDir.absoluteFilePath(files[i]))

            if inFile.open(QtCore.QIODevice.ReadOnly):
                line = QtCore.QString()
                stream = QtCore.QTextStream(inFile)
                while not stream.atEnd():
                    if progressDialog.wasCanceled():
                        break
                    line = stream.readLine()
                    if line.contains(text):
                        foundFiles << files[i]
                        break

        progressDialog.close()

        return foundFiles


    def showFiles(self, files):

        for i in range(files.count()):
            file = QtCore.QFile(self.currentDir.absoluteFilePath(files[i]))
            size = QtCore.QFileInfo(file).size()

            fileNameItem = QtGui.QTableWidgetItem(files[i])
            fileNameItem.setFlags(fileNameItem.flags() ^ QtCore.Qt.ItemIsEditable)
            sizeItem = QtGui.QTableWidgetItem(QtCore.QString("%1 KB").arg(int((size + 1023) / 1024)))
            sizeItem.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
            sizeItem.setFlags(sizeItem.flags() ^ QtCore.Qt.ItemIsEditable)

            row = self.filesTable.rowCount()
            self.filesTable.insertRow(row)
            self.filesTable.setItem(row, 0, fileNameItem)
            self.filesTable.setItem(row, 1, sizeItem)

        #self.filesFoundLabel.setText(self.tr("%1 file(s) found").arg(files.count()) + " (Double click on a file to open it)")
	self.resultlabelout.setText(self.tr("%1 file(s) found").arg(files.count()) + " (Double click on a file to open it)")

    
    def openFileOfItem(self, row, column):

        item = self.filesTable.item(row, 0)

        QtGui.QDesktopServices.openUrl(QtCore.QUrl(self.currentDir.absoluteFilePath(item.text())))

    def createFilesTable(self):
	#self.filesTable = QtGui.QTableWidget(0, 2)
        self.filesTable = QtGui.QTableWidget(self.wrk)
        self.filesTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)

        labels = QtCore.QStringList()
        labels << self.tr("File Name") << self.tr("Size")
        self.filesTable.setHorizontalHeaderLabels(labels)
        self.filesTable.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Stretch)
        self.filesTable.verticalHeader().hide()
        self.filesTable.setShowGrid(False)
	self.filesTable.setGeometry(10, 10, 500, 200)

        #self.filesTable.cellActivated.connect(self.openFileOfItem)
	
	self.connect(self.filesTable, QtCore.SIGNAL("cellActivated()"), self.openFileOfItem)
	
    def showdrive(self):
	self.Gbox4.show()
	self.RB_C.hide()
	self.RB_D.hide()
	self.RB_E.hide()
	self.RB_I.hide()
	self.RB_J.hide()
	self.RB_K.hide()
	self.RB_L.hide()
	self.RB_O.hide()
	self.RB_P.hide()
	self.RB_Q.hide()
	self.Gbox5.show()
	
    def showdrivebox4(self):
	self.Gbox4.show()
	self.RB_C.show()
	self.RB_D.show()
	self.RB_E.show()
	self.RB_I.show()
	self.RB_J.show()
	self.RB_K.show()
	self.RB_L.show()
	self.RB_O.show()
	self.RB_P.show()
	self.RB_Q.show()
	

        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    myapp = MainApp()
    myapp.show()
    sys.exit(app.exec_())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        