#		    if (self.combofilelist.isChecked()):
			
#			self.combofiletree.setChecked(False)
#				    
#			dataid = os.popen("dir /b e:\CD_DVD_LIST\\P*list*").readlines()
#			print dataid, "\n"
#			print "Len dataid = ", len(dataid)
#				    
#			if (os.path.isfile('e:\CD_DVD_LIST\\zresult.dat') == True):
#			    os.remove('e:\CD_DVD_LIST\\zresult.dat')
#			    dataresult = open("e:\CD_DVD_LIST\\zresult.dat", "w")
#					
#			    for i in range(0, len(dataid)):
#					datacek = dataid[i].split("\n")
#					#print "datacek[0] = ", datacek[0]
#					#print os.path.isfile(datacek[0])
#					datacheck = open("e:\CD_DVD_LIST\\" + datacek[0], "r").readlines()
#					#print datacheck
#					for j in range(0, len(datacheck)):
#					        
#						datafile = self.search.currentText()
#						if str(datafile) in datacheck[j]:
#						    
#						    datarecord = " " + datacek[0] + " : " + "\n" + "\t Line : " + str(j) + ". " + datacheck[j]
#						    dataresult04 = open("e:\CD_DVD_LIST\\zresult.dat", "a").write(datarecord)
#						    dataresult05 = open("e:\CD_DVD_LIST\\zresult.dat", "r").read()
#						    print dataresult05
#						    self.result.setText(dataresult05 + "\n\n")
#						    
#						    
#						else:
#						    pass
#						
#						self.progress.show()
#						self.progress.setRange(0, len(datacheck))
#						self.progress.setValue(j + 1)
#						
#			    time.sleep(1)
#			    self.progress.setValue(0)
#			    self.progress.hide()
#						
#						
#			else:
#			    
#			    dataresult = open("e:\CD_DVD_LIST\\zresult.dat", "w")
#					
#			    for i in range(0, len(dataid)):
#					for j in range(0, len(dataid[i])):
#						datacheck = open(dataid[i], "r").readlines()
#							
#						if datafile in datacheck[j]:
#							datarecord = " " + datacek[0] + " : " + "\n" + "\t Line : " + str(j) + ". " + datacheck[j]
#							dataresult04 = open("e:\CD_DVD_LIST\\zresult.dat", "a").write(datarecord)
#							dataresult05 = open("e:\CD_DVD_LIST\\zresult.dat", "r").read()
#							self.result.setText(dataresult05 + "\n\n")
#							
#								
#						else:
#						    pass
#						
#						self.progress.show()
#						self.progress.setRange(0, len(datacheck))
#						self.progress.setValue(j + 1)
#						
#					time.sleep(1)
#					self.progress.setValue(0)
#					self.progress.hide()
#						
#		    elif (self.combofiletree.isChecked()):
#			
#				self.combofilelist.setChecked(False)
#				
#				dataid = os.popen("dir /b e:\CD_DVD_LIST\\P*tree*").readlines()
#				print dataid, "\n"
#				print "Len dataid = ", len(dataid)
#				
#				if (os.path.isfile('e:\CD_DVD_LIST\\zresult.dat') == True):
#					os.remove('e:\CD_DVD_LIST\\zresult.dat')
#					dataresult = open("e:\CD_DVD_LIST\\zresult.dat", "w")
#					
#					for i in range(0, len(dataid)):
#						for j in range(0, len(dataid[i])):
#							datacheck = open(dataid[i], "r").readlines()
#							
#							if datafile in datacheck[j]:
#								datarecord = " " + datacek[0] + " : " + "\n" + "\t Line : " + str(j) + ". " + datacheck[j]
#								dataresult04 = open("e:\CD_DVD_LIST\\zresult.dat", "a").write(datarecord)
#								dataresult05 = open("e:\CD_DVD_LIST\\zresult.dat", "r").read()
#								
#								self.result.setText(dataresult05 + "\n\n")
#								
#							
#							else:
#							    pass
#							
#							self.progress.show()
#							self.progress.setRange(0, len(datacheck))
#							self.progress.setValue(j + 1)
#							
#					time.sleep(1)
#					self.progress.setValue(0)
#					self.progress.hide()
#								
#				else:
#						
#					dataresult = open("e:\CD_DVD_LIST\\zresult.dat", "w")
#					
#					for i in range(0, len(dataid)):
#						for j in range(0, len(dataid[i])):
#							datacheck = open(dataid[i], "r").readlines()
#							
#							if datafile in datacheck[j]:
#								datarecord = " " + datacek[0] + " : " + "\n" + "\t Line : " + str(j) + ". " + datacheck[j]
#								dataresult04 = open("e:\CD_DVD_LIST\\zresult.dat", "a").write(datarecord)
#								dataresult05 = open("e:\CD_DVD_LIST\\zresult.dat", "r").read()
#								self.result.setText(dataresult05 + "\n\n")
#								
#							
#							else:
#							    pass
#							
#							self.progress.show()
#							self.progress.setRange(0, len(datacheck))
#							self.progress.setValue(j + 1)
#							
#					time.sleep(1)
#					self.progress.setValue(0)
#					self.progress.hide()
#		    
#