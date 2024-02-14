from PyQt5.QtWidgets import QWidget
from PyQt5 import uic, QtWidgets, QtCore
import json
import re
import os


class SetWindows(QWidget):
    def __init__(self, parent=None, signal=None):
        self.nickName = None
        self.port = None
        self.ip = None
        self.signal = signal
        super().__init__()
        uic.loadUi("templates/setWindow.ui", self)
        self.setWindowTitle("Настройки")
        self.setWindowModality(2)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()
        self.pushButtonConfirm.clicked.connect(self.confirm)
        self.pushButtonCancel.clicked.connect(lambda: self.close())
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
