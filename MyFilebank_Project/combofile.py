

def main(name):
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
    
    
    if self.combofilelist.isChecked() + name.isChecked():
        self.addinfo2
        self.connect(self.combofilelist, QtCore.SIGNAL("clicked()"), self.windowfilelist)
    if self.combofiletree.isChecked() + name.isChecked():
        self.addinfo2
        self.connect(self.combofiletree, QtCore.SIGNAL("clicked()"), self.windowfiletree)