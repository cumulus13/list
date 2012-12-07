import sys, os
from PyQt4 import QtGui, QtCore

class DialogData(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(DialogData, self).__init__(parent)
        
        self.setFixedSize(400, 400)

	self.setWindowTitle("Import Data List")
	
	#tooltip
	self.setToolTip('Import List Data')
        QtGui.QToolTip.setFont(QtGui.QFont('Arial', 10))
        self.statusBar().showMessage('Main Application')
	
	#make screen On center Windows
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 3, (screen.height() - size.height()) / 3)
        
        self.Box1 = QtGui.QGroupBox(self)
	self.Box1.setTitle('Category')
        self.Box1.setGeometry(20, 20, 360, 200)
        self.Box1.setToolTip('Category Of Data File')
        self.Box1.setStatusTip('Category Of Data File')
	
        self.Box2 = QtGui.QGroupBox(self)
	#self.Box2.setTitle('File')
        self.Box2.setGeometry(20, 225, 360, 130)
        self.Box2.setToolTip('File Choice')
        self.Box2.setStatusTip('File Choice')
        
        
        #Radio Button For Box1
        self.RB_winfile = QtGui.QRadioButton(self.Box1)
        self.RB_winfile.setText('Programming Soft')
        self.RB_winfile.setGeometry(10, 20, 120, 20)
        self.RB_winfile.setToolTip('Programming Soft')
        self.RB_winfile.setStatusTip('Programming Soft')
	self.connect(self.RB_winfile, QtCore.SIGNAL("clicked()"), self.CodeWinFile)
	self.connect(self.RB_winfile, QtCore.SIGNAL("clicked()"), self.hidelistdrive)
        
        self.RB_linfile = QtGui.QRadioButton(self.Box1)
        self.RB_linfile.setText('Linux Programs')
        self.RB_linfile.setGeometry(10, 40, 120, 20)
        self.RB_linfile.setToolTip('Linux Programs')
        self.RB_linfile.setStatusTip('Linux Programs')
	self.connect(self.RB_linfile, QtCore.SIGNAL("clicked()"), self.CodeLinFile)
	self.connect(self.RB_linfile, QtCore.SIGNAL("clicked()"), self.hidelistdrive)
        
        self.RB_winmaster = QtGui.QRadioButton(self.Box1)
        self.RB_winmaster.setText('Windows Master')
        self.RB_winmaster.setGeometry(10, 60, 120, 20)
        self.RB_winmaster.setToolTip('Windows Master')
        self.RB_winmaster.setStatusTip('Windows Master')
	self.connect(self.RB_winmaster, QtCore.SIGNAL("clicked()"), self.CodeWinMaster)
	self.connect(self.RB_winmaster, QtCore.SIGNAL("clicked()"), self.hidelistdrive)
        
        self.RB_linmaster = QtGui.QRadioButton(self.Box1)
        self.RB_linmaster.setText('Linux Master')
        self.RB_linmaster.setGeometry(10, 80, 120, 20)
        self.RB_linmaster.setToolTip('Linux Master')
        self.RB_linmaster.setStatusTip('Linux Master')
	self.connect(self.RB_linmaster, QtCore.SIGNAL("clicked()"), self.CodeLinMaster)
	self.connect(self.RB_linmaster, QtCore.SIGNAL("clicked()"), self.hidelistdrive)
	
        
        self.RB_music = QtGui.QRadioButton(self.Box1)
        self.RB_music.setText('Music Master')
        self.RB_music.setGeometry(10, 100, 130, 20)
        self.RB_music.setToolTip('Music Master')
        self.RB_music.setStatusTip('Music Master')
	self.connect(self.RB_music, QtCore.SIGNAL("clicked()"), self.CodeMusic)
	self.connect(self.RB_music, QtCore.SIGNAL("clicked()"), self.hidelistdrive)
        
        self.RB_driverstudio = QtGui.QRadioButton(self.Box1)
        self.RB_driverstudio.setText('Driver Studio')
        self.RB_driverstudio.setGeometry(10, 120, 120, 20)
        self.RB_driverstudio.setToolTip('Driver Studio')
        self.RB_driverstudio.setStatusTip('Driver Studio')
	self.connect(self.RB_driverstudio, QtCore.SIGNAL("clicked()"), self.CodeDriverStudio)
	self.connect(self.RB_driverstudio, QtCore.SIGNAL("clicked()"), self.hidelistdrive)
        
        self.RB_ebookfile = QtGui.QRadioButton(self.Box1)
        self.RB_ebookfile.setText('Ebooks')
        self.RB_ebookfile.setGeometry(10, 140, 120, 20)
        self.RB_ebookfile.setToolTip('Ebooks')
        self.RB_ebookfile.setStatusTip('Ebooks')
	self.connect(self.RB_ebookfile, QtCore.SIGNAL("clicked()"), self.CodeEbookFile)
	self.connect(self.RB_ebookfile, QtCore.SIGNAL("clicked()"), self.hidelistdrive)
        
        self.RB_netsoft = QtGui.QRadioButton(self.Box1)
        self.RB_netsoft.setText('Networking Soft')
        self.RB_netsoft.setGeometry(10, 160, 120, 20)
        self.RB_netsoft.setToolTip('Networking Soft')
        self.RB_netsoft.setStatusTip('Networking Soft')
	self.connect(self.RB_netsoft, QtCore.SIGNAL("clicked()"), self.CodeNetSoft)
	self.connect(self.RB_netsoft, QtCore.SIGNAL("clicked()"), self.hidelistdrive)
        
        self.RB_hddbck = QtGui.QRadioButton(self.Box1)
        self.RB_hddbck.setText('Harddisk Backup')
        self.RB_hddbck.setGeometry(140, 20, 120, 20)
        self.RB_hddbck.setToolTip('Harddisk Backup')
        self.RB_hddbck.setStatusTip('Harddisk Backup')
	self.connect(self.RB_hddbck, QtCore.SIGNAL("clicked()"), self.CodeHddBCK)
	self.connect(self.RB_hddbck, QtCore.SIGNAL("clicked()"), self.hidelistdrive)
        
        self.RB_hackersoft = QtGui.QRadioButton(self.Box1)
        self.RB_hackersoft.setText('Hacker Soft')
        self.RB_hackersoft.setGeometry(140, 40, 120, 20)
        self.RB_hackersoft.setToolTip('Hacker Soft')
        self.RB_hackersoft.setStatusTip('Hacker Soft')
	self.connect(self.RB_hackersoft, QtCore.SIGNAL("clicked()"), self.CodeHackerSoft)
	self.connect(self.RB_hackersoft, QtCore.SIGNAL("clicked()"), self.hidelistdrive)
        
        self.RB_gamesoft = QtGui.QRadioButton(self.Box1)
        self.RB_gamesoft.setText('Gamers')
        self.RB_gamesoft.setGeometry(140, 60, 120, 20)
        self.RB_gamesoft.setToolTip('Gamers')
        self.RB_gamesoft.setStatusTip('Gamers')
	self.connect(self.RB_gamesoft, QtCore.SIGNAL("clicked()"), self.CodeGameSoft)
	self.connect(self.RB_gamesoft, QtCore.SIGNAL("clicked()"), self.hidelistdrive)
        
        self.RB_bootsoft = QtGui.QRadioButton(self.Box1)
        self.RB_bootsoft.setText('Booting Soft')
        self.RB_bootsoft.setGeometry(140, 80, 120, 20)
        self.RB_bootsoft.setToolTip('Booting Soft')
        self.RB_bootsoft.setStatusTip('Booting Soft')
	self.connect(self.RB_bootsoft, QtCore.SIGNAL("clicked()"), self.CodeBootSoft)
	self.connect(self.RB_bootsoft, QtCore.SIGNAL("clicked()"), self.hidelistdrive)
        
        self.RB_databck = QtGui.QRadioButton(self.Box1)
        self.RB_databck.setText('Data Backup')
        self.RB_databck.setGeometry(140, 100, 120, 20)
        self.RB_databck.setToolTip('Data Backup')
        self.RB_databck.setStatusTip('Data Backup')
	self.connect(self.RB_databck, QtCore.SIGNAL("clicked()"), self.CodeDataBck)
	self.connect(self.RB_databck, QtCore.SIGNAL("clicked()"), self.hidelistdrive)
	
	self.RB_datadrive = QtGui.QRadioButton(self.Box1)
        self.RB_datadrive.setText('Data Drive')
        self.RB_datadrive.setGeometry(140, 120, 120, 20)
        self.RB_datadrive.setToolTip('Data Drive')
        self.RB_datadrive.setStatusTip('Data Drive')
	self.connect(self.RB_datadrive, QtCore.SIGNAL("clicked()"), self.showdrive)
	self.connect(self.RB_datadrive, QtCore.SIGNAL("clicked()"), self.CodeDataDrive)
	
	self.Gbox4 = QtGui.QGroupBox(self.Box1)
	self.Gbox4.setTitle("Drive : ")
	self.Gbox4.setGeometry(123, 140, 234, 55)
	self.Gbox4.setFont(QtGui.QFont('Arial', 8))
	
	self.RB_C = QtGui.QRadioButton(self.Gbox4)
	self.RB_C.setGeometry(5, 15, 28, 13)
	self.RB_C.setText("C")
	self.RB_C.setToolTip("Drive C")
	self.RB_C.setStatusTip("Drive C")
	#textme = self.RB_C.text()
	#self.connect(self.RB_C, QtCore.SIGNAL("clicked()"), self.fileOpen2)
	
	self.RB_D = QtGui.QRadioButton(self.Gbox4)
	self.RB_D.setGeometry(5, 35, 28, 13)
	self.RB_D.setText("D")
	self.RB_D.setToolTip("Drive D")
	self.RB_D.setStatusTip("Drive D")
	#self.connect(self.RB_D, QtCore.SIGNAL("clicked()"), self.fileOpen2)
	
	self.RB_E = QtGui.QRadioButton(self.Gbox4)
	self.RB_E.setGeometry(34, 15, 28, 13)
	self.RB_E.setText("E")
	self.RB_E.setToolTip("Drive E")
	self.RB_E.setStatusTip("Drive E")
	#self.connect(self.RB_E, QtCore.SIGNAL("clicked()"), self.fileOpen2)
	
	self.RB_F = QtGui.QRadioButton(self.Gbox4)
	self.RB_F.setGeometry(34, 35, 28, 13)
	self.RB_F.setText("F")
	self.RB_F.setToolTip("Drive F")
	self.RB_F.setStatusTip("Drive F")
	#self.connect(self.RB_F, QtCore.SIGNAL("clicked()"), self.fileOpen2)
	
	self.RB_G = QtGui.QRadioButton(self.Gbox4)
	self.RB_G.setGeometry(63, 15, 28, 13)
	self.RB_G.setText("G")
	self.RB_G.setToolTip("Drive G")
	self.RB_G.setStatusTip("Drive G")
	#self.connect(self.RB_G, QtCore.SIGNAL("clicked()"), self.fileOpen2)
	
	self.RB_H = QtGui.QRadioButton(self.Gbox4)
	self.RB_H.setGeometry(63, 35, 28, 13)
	self.RB_H.setText("H")
	self.RB_H.setToolTip("Drive H")
	self.RB_H.setStatusTip("Drive H")
	#self.connect(self.RB_H, QtCore.SIGNAL("clicked()"), self.fileOpen2)
	
	self.RB_I = QtGui.QRadioButton(self.Gbox4)
	self.RB_I.setGeometry(92, 15, 28, 13)
	self.RB_I.setText("I")
	self.RB_I.setToolTip("Drive I")
	self.RB_I.setStatusTip("Drive I")
	#self.connect(self.RB_I, QtCore.SIGNAL("clicked()"), self.fileOpen2)
	
	self.RB_M = QtGui.QRadioButton(self.Gbox4)
	self.RB_M.setGeometry(92, 35, 28, 13)
	self.RB_M.setText("M")
	self.RB_M.setToolTip("Drive M")
	self.RB_M.setStatusTip("Drive M")
	#self.connect(self.RB_M, QtCore.SIGNAL("clicked()"), self.fileOpen2)
	
	self.RB_N = QtGui.QRadioButton(self.Gbox4)
	self.RB_N.setGeometry(121, 15, 28, 13)
	self.RB_N.setText("N")
	self.RB_N.setToolTip("Drive N")
	self.RB_N.setStatusTip("Drive N")
	#self.connect(self.RB_N, QtCore.SIGNAL("clicked()"), self.fileOpen2)
	
	self.RB_O = QtGui.QRadioButton(self.Gbox4)
	self.RB_O.setGeometry(121, 35, 28, 13)
	self.RB_O.setText("O")
	self.RB_O.setToolTip("Drive O")
	self.RB_O.setStatusTip("Drive O")
	#self.connect(self.RB_O, QtCore.SIGNAL("clicked()"), self.fileOpen2)
	
	self.Gbox5 = QtGui.QGroupBox(self.Gbox4)
	self.Gbox5.setTitle("Type : ")
	self.Gbox5.setFont(QtGui.QFont('Arial', 7))
	self.Gbox5.setGeometry(150, 7, 81, 45)
	
	self.RB_drivelist = QtGui.QRadioButton(self.Gbox5)
	self.RB_drivelist.setGeometry(3, 12, 40, 13)
	self.RB_drivelist.setText("List")
	self.RB_drivelist.setToolTip("List Type Drive")
	self.RB_drivelist.setStatusTip("List Type Drive")
	self.connect(self.RB_drivelist, QtCore.SIGNAL("clicked()"), self.showdrivebox4)
	self.connect(self.RB_drivelist, QtCore.SIGNAL("clicked()"), self.clearDrive)
	
	self.RB_drivetree = QtGui.QRadioButton(self.Gbox5)
	self.RB_drivetree.setGeometry(3, 27, 40, 13)
	self.RB_drivetree.setText("Tree")
	self.RB_drivetree.setToolTip("Tree Type Drive")
	self.RB_drivetree.setStatusTip("Tree Type Drive")
	self.connect(self.RB_drivetree, QtCore.SIGNAL("clicked()"), self.showdrivebox4)
	self.connect(self.RB_drivetree, QtCore.SIGNAL("clicked()"), self.clearDrive)
        
	self.RB_driveAll = QtGui.QRadioButton(self.Gbox5)
	self.RB_driveAll.setGeometry(46, 20, 40, 13)
	self.RB_driveAll.setText("All")
	self.RB_driveAll.setToolTip("All Drive")
	self.RB_driveAll.setStatusTip("All Drive")
	self.connect(self.RB_driveAll, QtCore.SIGNAL("clicked()"), self.showdrivebox4)
	self.connect(self.RB_driveAll, QtCore.SIGNAL("clicked()"), self.clearDrive)
	
	self.Code1_Label = QtGui.QLabel(self.Box2)
	self.Code1_Label.setText("Code : ")
	self.Code1_Label.setFont(QtGui.QFont('Arial', 10))
	self.Code1_Label.setGeometry(140, 11, 38, 30)
	
	self.Code1_Label_Prefix = QtGui.QLabel(self.Box2)
	#self.Code1_Label_Prefix.setText("M")
	self.Code1_Label_Prefix.setFont(QtGui.QFont('Arial', 18))
	#self.Code1_Label_Prefix.setGeometry(200, 11, 38, 30)
	
	self.Code1_Label = QtGui.QLabel(self.Box2)
	self.Code1_Label.setText("+")
	self.Code1_Label.setFont(QtGui.QFont('Arial', 10))
	self.Code1_Label.setGeometry(230, 10, 30, 30)
	
	self.Code1_LabelInfo = QtGui.QLabel(self.Box2)
	self.Code1_LabelInfo.setText("(Code + Number Code)")
	self.Code1_LabelInfo.setFont(QtGui.QFont('Arial', 8))
	self.Code1_LabelInfo.setGeometry(230, 30, 150, 30)
	
	self.Code1_Input = QtGui.QLineEdit(self.Box2)
	self.Code1_Input.setGeometry(250, 13, 70, 22)
	self.Code1_Input.setToolTip("Please Insert The Number Code")
	self.Code1_Input.setStatusTip("Please Insert The Number Code")
	self.Code1_Input.setFixedSize(70, 22)
	Font = QtGui.QFont("Arial", 11)
	self.Code1_Input.setFont(Font)
	
	self.Code1_list = QtGui.QCheckBox(self.Box2)
	self.Code1_list.setGeometry(190, 70, 70, 22)
	self.Code1_list.setText("List")
	self.Code1_list.setToolTip("List Type Drive")
	self.Code1_list.setStatusTip("List Type Drive")
	self.connect(self.Code1_list, QtCore.SIGNAL("clicked()"), self.clearCheckOne)
	
	self.Code1_tree = QtGui.QCheckBox(self.Box2)
	self.Code1_tree.setGeometry(230, 70, 70, 22)
	self.Code1_tree.setText("Tree")
	self.Code1_tree.setToolTip("Tree Type Drive")
	self.Code1_tree.setStatusTip("Tree Type Drive")
	self.connect(self.Code1_tree, QtCore.SIGNAL("clicked()"), self.clearCheckOne)
        
	self.Code1_All = QtGui.QCheckBox(self.Box2)
	self.Code1_All.setGeometry(275, 70, 100, 22)
	self.Code1_All.setText("All (Default)")
	self.Code1_All.setToolTip("All Drive")
	self.Code1_All.setStatusTip("All Drive")
	self.connect(self.Code1_All, QtCore.SIGNAL("clicked()"), self.clearCheckAll)
	
	self.Box3 = QtGui.QGroupBox(self.Box2)
	self.Box3.setTitle("Info")
	self.Box3.setGeometry(5, 3, 125, 120)
	self.Box3.setToolTip("Info About Data List")
	self.Box3.setStatusTip("Info About Data List")
	
	self.lastfile = QtGui.QLabel(self.Box3)
	self.lastfile.setText("Last File       : ")
	self.lastfile.setGeometry(5, 18, 70, 10)
	
	self.createfile = QtGui.QLabel(self.Box3)
	self.createfile.setText("Create at     : ")
	self.createfile.setGeometry(5, 36, 70, 10)
	
	self.lastupdate = QtGui.QLabel(self.Box3)
	self.lastupdate.setText("Last Update : ")
	self.lastupdate.setGeometry(5, 54, 70, 10)
	
	self.Gbox4.hide()
	
        self.show()
	
    def CodeWinFile(self):
	self.Code1_Label_Prefix.setText("P")
	self.Code1_Label_Prefix.setGeometry(200, 11, 38, 30)
	
    def CodeLinFile(self):
	self.Code1_Label_Prefix.setText("L")
	self.Code1_Label_Prefix.setGeometry(200, 11, 38, 30)
	
    def CodeWinMaster(self):
	self.Code1_Label_Prefix.setText("W")
	self.Code1_Label_Prefix.setGeometry(200, 11, 38, 30)
	
    def CodeLinMaster(self):
	self.Code1_Label_Prefix.setText("LM")
	self.Code1_Label_Prefix.setGeometry(190, 11, 38, 30)
    
    def CodeMusic(self):
	self.Code1_Label_Prefix.setText("M")
	self.Code1_Label_Prefix.setGeometry(200, 11, 38, 30)
	
    def CodeDriverStudio(self):
	self.Code1_Label_Prefix.setText("D")
	self.Code1_Label_Prefix.setGeometry(200, 11, 38, 30)
    
    def CodeEbookFile(self):
	self.Code1_Label_Prefix.setText("E")
	self.Code1_Label_Prefix.setGeometry(200, 11, 38, 30)
	
    def CodeNetSoft(self):
	self.Code1_Label_Prefix.setText("N")
	self.Code1_Label_Prefix.setGeometry(200, 11, 38, 30)
	
    def CodeHddBCK(self):
	self.Code1_Label_Prefix.setText("HD")
	self.Code1_Label_Prefix.setGeometry(190, 11, 38, 30)
	
    def CodeHackerSoft(self):
	self.Code1_Label_Prefix.setText("HCK")
	self.Code1_Label_Prefix.setGeometry(180, 11, 50, 30)
	
    def CodeGameSoft(self):
	self.Code1_Label_Prefix.setText("G")
	self.Code1_Label_Prefix.setGeometry(200, 11, 38, 30)
	
    def CodeBootSoft(self):
	self.Code1_Label_Prefix.setText("B")
	self.Code1_Label_Prefix.setGeometry(200, 11, 38, 30)
	
    def CodeDataBck(self):
	self.Code1_Label_Prefix.setText("BCK")
	self.Code1_Label_Prefix.setGeometry(180, 11, 50, 30)
	
    def CodeDataDrive(self):
	self.Code1_Label_Prefix.setText("D")
	self.Code1_Label_Prefix.setGeometry(200, 11, 38, 30)
	
    def showdrive(self):
	self.Gbox4.show()
	self.RB_C.hide()
	self.RB_D.hide()
	self.RB_E.hide()
	self.RB_F.hide()
	self.RB_G.hide()
	self.RB_H.hide()
	self.RB_I.hide()
	self.RB_M.hide()
	self.RB_N.hide()
	self.RB_O.hide()
	self.Gbox5.show()
	
    def showdrivebox4(self):
	self.Gbox4.show()
	self.RB_C.show()
	self.RB_D.show()
	self.RB_E.show()
	self.RB_F.show()
	self.RB_G.show()
	self.RB_H.show()
	self.RB_I.show()
	self.RB_M.show()
	self.RB_N.show()
	self.RB_O.show()
	
    def clearCheckAll(self):
	if self.Code1_list.isChecked and self.Code1_tree.isChecked:
	    self.Code1_list.setChecked(False)
	    self.Code1_tree.setChecked(False)
	    
    def clearCheckOne(self):
	if self.Code1_All.isChecked:
	    self.Code1_All.setChecked(False)
        
    def clearDrive(self):
	if self.RB_drivelist.isChecked and self.RB_drivetree.isChecked and self.RB_driveAll.isChecked:
	    self.RB_C.setChecked(False)
	    self.RB_D.setChecked(False)
	    self.RB_E.setChecked(False)
	    self.RB_F.setChecked(False)
	    self.RB_G.setChecked(False)
	    self.RB_H.setChecked(False)
	    self.RB_I.setChecked(False)
	    self.RB_M.setChecked(False)
	    self.RB_N.setChecked(False)
	    self.RB_O.setChecked(False)
	    
    def hidelistdrive(self):
	self.Gbox4.hide()
	    
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    TApp = DialogData()
    TApp.show()
    sys.exit(app.exec_())