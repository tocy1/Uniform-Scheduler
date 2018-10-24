# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 13:27:34 2018

@author: Uzoma
"""
from PyQt5.QtWidgets import QMainWindow,QApplication,QProgressBar,QPushButton,QComboBox,QAction,QCheckBox,QLineEdit,QVBoxLayout,QWidget,QGridLayout,QLabel
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
import itertools
import threading

class Example(QMainWindow,QWidget):
        a=[]
        cos=[]
        def __init__(self):
            QMainWindow.__init__(self)
            self.setWindowIcon(QIcon("cc.png"))
            self.setWindowTitle("Uniform Scheduler")
            
            self.Label=['','','','']
            
            self.main()
            
        def main(self):
            
            menu= QAction(QIcon("menu.png"),"&Menu",self)
            menu.setShortcut("Ctrl+Q")
            menu.setStatusTip("Menu")
            menu.triggered.connect(self.close)
            self.Quickschedule= QAction(QIcon("Z.png"),"&Quick Schedule",self)
            self.Quickschedule.setStatusTip("Have a quick schedule")
            
            self.Quickschedule.triggered.connect(self.enable)
            
           
            Exit= QAction(QIcon("exit"),"&Exit",self)
            Exit.setShortcut("Ctrl+X")
            Exit.setStatusTip("Exit this App")
            Exit.triggered.connect(self.close)
            self.statusBar()
            menubar= self.menuBar()
            Homemenu= menubar.addMenu("Menu")
            Homemenu.addAction(menu)
            Homemenu.addAction(self.Quickschedule)
            Aboutmenu= menubar.addMenu("about")
            tipsmenu= menubar.addMenu("Tips")
            close=menubar.addMenu("exit")
            close.addAction(Exit)
            
            
            
            self.shirtbutton= QPushButton("Tops",self)
            self.shirtbutton.setIcon(QIcon("tops.png"))
            #shirtbutton.setIconSize(QSize(24,24))
            self.shirtbutton.clicked.connect(self.newwin)
            self.shirtbutton.move(50,50)
            self.shirtbutton.setVisible(False)
            
            self.downbutton= QPushButton("Down",self)
            self.downbutton.setIcon(QIcon("down.png"))
            self.downbutton.setIconSize(QSize(24,24))
            self.downbutton.clicked.connect(self.newwin1)
            self.downbutton.move(750,450)
            self.downbutton.setVisible(False)
            self.GETbutton= QPushButton("GET",self) 
            self.GETbutton.clicked.connect(self.scheduling)
            self.GETbutton.move(500,200)
            self.GETbutton.setVisible(False)
            
                #self.Label[i].setText("aaa")
           
            self.show()
                    
        def newwin1(self):
            self.wi= UI_TopDialog1(self) 
            self.wi.show()
        def enable(self):
            self.shirtbutton.setVisible(True)  
            self.downbutton.setVisible(True)  
            self.GETbutton.setVisible(True)  
            #self.shirtbutton.show()
        def newwin(self):
            self.w = UI_TopDialog(self) 
            self.w.show()
        def scheduling(self):
            self.m=UI_TopDialog1()
            self.y=UI_TopDialog()
            #print(list(self.m.p))
            self.comb=list(itertools.product(self.m.p,self.y.z))
            #cos=self.comb[:]
            #self.show2()
            #print(self.comb[1])
              
            self.mm= UI_TopDialog2(self.comb) 
            #self.mm.p=self.comb[:]
            if self.comb!=[]:
            #print(self.mm.p)
                self.mm.show()
           # for i in comb:
                

class UI_TopDialog(QWidget):
        z=[]
        def __init__(self,parent=None):
            super().__init__()
            self.listx=[]
            QApplication.processEvents()
            self.listCheckBox=["Red","Green","Yellow","Black","Lemon green",
            "Purple","White","Sky blue","Pink","Orange"]
            self.grid=QGridLayout()
            self.setWindowIcon(QIcon("top.png"))
            self.setWindowTitle("Top")
            for i,v in enumerate(self.listCheckBox):
                self.listCheckBox[i]=QCheckBox(v)
                self.grid.addWidget(self.listCheckBox[i],i,0)
            self.button=QPushButton("Proceed")
            self.button.clicked.connect(self.checkboxChanged)
            self.edit= QLineEdit(self)
            self.edit.resize(50,50)
            self.push1=QPushButton("OK",self)
            self.push1.clicked.connect(self.ok)
            self.grid.addWidget(self.edit,len(self.listCheckBox)+len(self.listx),0)
            self.grid.addWidget(self.push1,len(self.listCheckBox)+len(self.listx),1)
            self.grid.addWidget(self.button,len(self.listCheckBox)+1+len(self.listx),0,1,2)
            
            self.setLayout(self.grid)
            
        def checkboxChanged(self):
           
            for i,v in enumerate(self.listCheckBox):
                if self.listCheckBox[i].isChecked():
                    self.z.append(str(v.text()))
            for i,v in enumerate(self.listx):
                if self.listx[i].isChecked():
                    self.z.append(str(v.text()))
            print(self.z) 
            
            self.close()
        def ok(self):
            if str(self.edit.text()) != "":
                self.listx.append(str(self.edit.text()))
                
                
                self.z.append(str(self.edit.text()))
                print(str(self.edit.text()))
                for i,_i in enumerate(self.listx):
                    self.listx[i]=QCheckBox(_i)
                    self.grid.addWidget(self.listx[i],len(self.listx)-1,((len(self.listx)-1)//10)+1)
                    QApplication.processEvents()
                QApplication.processEvents()
            print(self.z)
            self.edit.clear()
            #self.show()
class UI_TopDialog1(QWidget):
        p=[]
        
        def __init__(self,parent=None):
            
            super().__init__()
            self.listx=[]
            self.listCheckBox=["Red","Green","Yellow","Black","Lemon green",
            "Purple","White","Sky blue","Pink","Orange"]
            self.grid=QGridLayout()
            self.setWindowTitle("Down")
            self.setWindowIcon(QIcon("down.png"))
            for i,v in enumerate(self.listCheckBox):
                self.listCheckBox[i]=QCheckBox(v)
                self.grid.addWidget(self.listCheckBox[i],i,0)
            self.button=QPushButton("Proceed")
            self.button.clicked.connect(self.checkboxChanged)
            self.edit1= QLineEdit("enter",self)
            self.edit1.resize(50,50)
            #self.edit1.setText("Enter ANOTHER")
            self.push1=QPushButton("OK",self)
            self.push1.clicked.connect(self.ok)
            self.grid.addWidget(self.edit1,len(self.listCheckBox),0)
            self.grid.addWidget(self.push1,len(self.listCheckBox),1)
            self.grid.addWidget(self.button,len(self.listCheckBox)+1,0,1,2)
            self.setLayout(self.grid)
            QApplication.processEvents()
        def checkboxChanged(self):
            
            for i,v in enumerate(self.listCheckBox):
                if self.listCheckBox[i].isChecked():
                    self.p.append(str(v.text()))
           
            for i,v in enumerate(self.listx):
                if self.listx[i].isChecked():
                    self.p.append(str(v.text()))
            print(self.p[:]) 
            self.close()
            QApplication.processEvents()
        def ok(self):
            #print("ok")
            if str(self.edit1.text()) != "":
                self.listx.append(str(self.edit1.text()))
                #self.p.append(str(self.edit1.text()))
                print(str(self.edit1.text()))
                for i,_i in enumerate(self.listx):
                    self.listx[i]=QCheckBox(_i)
                    self.grid.addWidget(self.listx[i],len(self.listx)-1,((len(self.listx)-1)//10)+1)
                    QApplication.processEvents()
                QApplication.processEvents()
            print(self.p)
            self.edit.clear()
            
class UI_TopDialog2(QWidget):
    #p=[]
    
    def __init__(self,comb,parent=None):
        super().__init__()
        grid=QGridLayout()
        self.setWindowTitle("Result")
        self.a=comb
        self.p=self.a[:]
        
        #self.u=Example(mn
        #self.p=self.u.cos[:]
       
        #QApplication.processEvents()
        print(self.p)
        self.list1=[]
        self.list2=[]
        self.list3=[""]
        self.listing=[]
        for i,n in enumerate(self.p):
            
            print(str(self.p[i]))
            self.list1.append("")
            self.list2.append("")
            self.list1[i]= QLabel(self)
            self.list2[i]=QPushButton("",self)
            self.list2[i].setIcon(QIcon("delete.png"))
            self.list2[i].clicked.connect(self.calldrop(i))
            
            
            #self.Label.append("")
            grid.addWidget(self.list1[i], i,0)
            grid.addWidget(self.list2[i],i,1)
        self.proceedbutton = QPushButton("Proceed",self)
        self.proceedbutton.clicked.connect(self.solve)
        grid.addWidget(self.proceedbutton,len(self.list1),0)
        #for i in range(len(self.u.cos)):
            
            #self.Label[i].move(300,i*100)
           
        self.setLayout(grid)
        #self.show
        
        for i,n in enumerate(self.p):
           print(n[0])
           self.list1[i].setText("Top:"+n[1]+" Down:"+n[0])
           print(str(self.p[i]))
        #tghreading.Thread(self).start(self)
    def calldrop(self,i):
        #listing=self.p[:]        
        def drop():
            #del self.listing[i]
            self.list1[i].deleteLater()
            self.list2[i].deleteLater()
            self.listing.append(self.p[i])
            print(self.listing)   
            QApplication.processEvents()
            QApplication.processEvents()
            if len(self.listing)==len(self.p):
                self.close()
            print("finished")
         
        return drop
    def solve(self):
        for i,n in enumerate(self.listing):
            print(self.listing)
            if self.listing[i] in self.p:
               self.p.remove(self.listing[i])
        print (self.p)
        self.close()        
                
    #threading.Timer(1.0,UI_TopDialog2).start()        
           
if __name__=='__main__':
            app=QApplication(sys.argv)
            ex=Example()
            
            sys.exit(app.exec_())
             