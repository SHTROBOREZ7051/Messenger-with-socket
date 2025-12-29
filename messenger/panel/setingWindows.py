from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt
import json
import sys
import re
import os
import io


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QFrame" name="frame">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>9</y>
     <width>381</width>
     <height>281</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">QFrame{
    border-radius: 10px;
	background-color: #1B1D23;
}</string>
   </property>
   <property name="frameShape">
    <enum>QFrame::StyledPanel</enum>
   </property>
   <property name="frameShadow">
    <enum>QFrame::Raised</enum>
   </property>
   <widget class="QFrame" name="frame_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>361</width>
      <height>191</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QFrame{
    border-radius: 10px;
	background-color: #3d3a59;
}</string>
    </property>
    <property name="frameShape">
     <enum>QFrame::StyledPanel</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Raised</enum>
    </property>
    <widget class="QLabel" name="label">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>0</y>
       <width>161</width>
       <height>31</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QLabel{
    font: 22pt &quot;Sitka Small&quot;;
     color: rgb(250, 250, 250);
}</string>
     </property>
     <property name="text">
      <string>Введите:</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="lineEdit">
     <property name="geometry">
      <rect>
       <x>72</x>
       <y>50</y>
       <width>281</width>
       <height>31</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QLineEdit{
	border-radius: 15px;
	background-color: #fff;
    font: 12pt &quot;Sitka Small&quot;;
}</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="lineEdit_2">
     <property name="geometry">
      <rect>
       <x>72</x>
       <y>100</y>
       <width>281</width>
       <height>31</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QLineEdit{
	border-radius: 15px;
	background-color: #fff;
    font: 12pt &quot;Sitka Small&quot;;
}</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="lineEdit_3">
     <property name="geometry">
      <rect>
       <x>72</x>
       <y>149</y>
       <width>281</width>
       <height>31</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QLineEdit{
	border-radius: 15px;
	background-color: #fff;
    font: 12pt &quot;Sitka Small&quot;;
}</string>
     </property>
    </widget>
    <widget class="QLabel" name="label_2">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>42</y>
       <width>47</width>
       <height>41</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QLabel{
    font: 12pt &quot;Sitka Small&quot;;
     color: rgb(250, 250, 250);
}</string>
     </property>
     <property name="text">
      <string>Имя</string>
     </property>
    </widget>
    <widget class="QLabel" name="label_3">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>100</y>
       <width>47</width>
       <height>31</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QLabel{
    font: 12pt &quot;Sitka Small&quot;;
     color: rgb(250, 250, 250);
}</string>
     </property>
     <property name="text">
      <string>Ip</string>
     </property>
    </widget>
    <widget class="QLabel" name="label_4">
     <property name="geometry">
      <rect>
       <x>16</x>
       <y>149</y>
       <width>51</width>
       <height>31</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QLabel{
    font: 12pt &quot;Sitka Small&quot;;
     color: rgb(250, 250, 250);
}</string>
     </property>
     <property name="text">
      <string>Port</string>
     </property>
    </widget>
   </widget>
   <widget class="QPushButton" name="pushButtonCancel">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>220</y>
      <width>171</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
	font: 12pt &quot;Sitka Small&quot;;
    border: none;
    border-radius: 10px;
	background-color:  #3d3a59;
    color: rgb(250, 250, 250);
}
QPushButton:hover{
	background-color: #4a3c73;
}
QPushButton:pressed{
	background-color: #604d94;
}
</string>
    </property>
    <property name="text">
     <string>Отменить</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButtonConfirm">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>220</y>
      <width>171</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
	font: 12pt &quot;Sitka Small&quot;;
    border-radius: 10px;
	background-color:  #3d3a59;
    color: rgb(250, 250, 250);
    border:50px;
    border-color: rgb(250, 250, 250)
}
QPushButton:hover{
	background-color: #4a3c73;
}
QPushButton:pressed{
	background-color: #604d94;
}
</string>
    </property>
    <property name="text">
     <string>Подтвердить</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class SetWindows(QWidget):
    def __init__(self, parent=None, signal=None):
        self.nickName = None
        self.port = None
        self.ip = None
        self.signal = signal
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.setWindowModality(2)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()
        try:
            self.pushButtonConfirm.clicked.connect(self.confirm)
        except:
            print("Error")
        if os.path.exists(os.path.join("Information", "aboutUser.json")):
            with open(os.path.join("Information", "aboutUser.json")) as f:
                information = json.load(f)
                self.lineEdit.setText(information["nickName"])
                self.lineEdit_2.setText(information["ip"])
                self.lineEdit_3.setText(information["port"])        
    
    def center(self):
            qr = self.frameGeometry()
            cp = QtWidgets.QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())
    
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
    
    def mouseMoveEvent(self, event):
        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except AttributeError:
            pass
        
    def confirm(self):
        self.nickName = self.lineEdit.text()
        self.ip = self.lineEdit_2.text()
        port = self.lineEdit_3.text()
        sampleIp = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        
        self.lineEdit.setStyleSheet("border-radius: 7px; font: 12pt 'Sitka Small';")
        self.lineEdit_2.setStyleSheet("border-radius: 7px; font: 12pt 'Sitka Small';")
        self.lineEdit_3.setStyleSheet("border-radius: 7px; font: 12pt 'Sitka Small';")        
        
        if 4 <= len(self.nickName) < 15:
            if not re.match(sampleIp, self.ip) is None:
                if port.isdecimal() and int(port) <= 65535:
                    
                    if not os.path.exists(os.path.join("Information", "aboutUser.json")):
                    
                        with open(os.path.join("Information", "aboutUser.json"), "w") as f:
                            information = {"nickName": self.nickName, "ip": self.ip, "port": port}
                            json.dump(information, f, indent=6)
                    else:
                        with open(os.path.join("Information", "aboutUser.json"), "w") as f:
                            information = {"nickName": self.nickName, "ip": self.ip, "port": port}
                            json.dump(information, f, indent=6)
                            
                    self.close()
                    self.signal.emit(['Update configuration'])
                else:
                    self.lineEdit_3.setStyleSheet("border: 2px solid red; border-radius: 7px; font: 12pt 'Sitka Small';")
                    self.lineEdit_3.setText("Некорректный ввод PORT")
            else:
                self.lineEdit_2.setStyleSheet("border: 2px solid red; border-radius: 7px; font: 12pt 'Sitka Small';")
                self.lineEdit_2.setText("Некорректный ввод IP")
        else:
            self.lineEdit.setStyleSheet("border: 2px solid red; border-radius: 7px; font: 12pt 'Sitka Small';")
            self.lineEdit.setText("Слишком длинный либо слишком короткий ник")

        

    
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = SetWindows()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())    
