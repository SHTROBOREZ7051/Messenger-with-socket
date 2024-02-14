from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QWidget
from PyQt5 import uic, QtGui, QtWidgets, QtCore
from PyQt5.QtCore import Qt
import PyQt5.QtCore
import sys
import socket
import time
import io
import json
import os

from monitor import ThreadMonitor
from selection_menu import SetWindows
from addInformation import AdditionalInformation
from translator import TranslatorWindows


class UserInterface(QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.initui()
        self.nickName = None
        self.ip = None
        self.port = None
        self.AbilityToConnect = False
        self.connectMonitor = ThreadMonitor()
        self.connectMonitor.getSignal.connect(self.signalHandler)
        
    def initui(self):
        uic.loadUi("templates/mainWindow.ui", self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) 
        self.center()
        self.pushButton_7.move(745, 5)
        self.pushButton_8.move(709, 5)
        icon = QtGui.QIcon()
        icon1 = QtGui.QIcon()
        icon2 = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("button_Icon\mn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(r"button_Icon\x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(r"button_Icon\-.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(40, 64))
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QtCore.QSize(20, 20))          
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setIconSize(QtCore.QSize(25, 20))
        self.pushButton.clicked.connect(self.configure)
        self.pushButton_2.clicked.connect(self.join)
        self.pushButton_3.clicked.connect(self.translate)
        self.pushButton_6.clicked.connect(lambda: self.listWidget.clear())
        self.pushButton_5.clicked.connect(self.sendMessage)
        self.pushButton_7.clicked.connect(lambda: self.close())
        self.pushButton_8.clicked.connect(lambda: self.showMinimized())
        self.pushButton_4.clicked.connect(self.getInfo)
        self.setWindowTitle("Чат-мессенджер")
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
            
    def mouseMoveEvent(self, event):
        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except AttributeError:
            pass
            
    def mousePressEvent(self, event):
            self.oldPos = event.globalPos()
            
    def updateConfigure(self):
        if os.path.exists(os.path.join("Information", "aboutUser.json")):
            with open(os.path.join("Information", "aboutUser.json")) as file:
                data = json.load(file)
                self.nickName = data['nickName']
                self.ip = data['ip']
                self.port = int(data['port'])    
    
    def sendMessage(self):
        
        if self.AbilityToConnect:
            messageText = self.lineEdit.text()
            if len(messageText) > 0:
                pickLoad = ["100_CONTINUE", self.nickName, messageText.encode()]
                print(pickLoad)
                self.connectMonitor.send_encrypt(pickLoad)
                
                item = QtWidgets.QListWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignLeft)
                item.setText(f"{self.nickName} (ВЫ):\n{messageText}")
                self.listWidget.addItem(item)
                self.lineEdit.setText("")
            else:
                message = "Проверьте соединение с сервером"
                QtWidgets.QMessageBox.about(self, "Оповещение", message)            
    
    def signalHandler(self, value:list):
        if value[0] == 'Update configuration':
            self.updateConfigure()
        
        elif value[0] == "200_OK":
            self.AbilityToConnect = True
            cellMessage = QtWidgets.QListWidgetItem()
            cellMessage.setTextAlignment(QtCore.Qt.AlignHCenter)
            cellMessage.setText(f"Server{value[1]}\n")
            self.listWidget.addItem(cellMessage)
            print(value)            
    
        elif value[0] == "100_CONTINUE":
            cellMessage = QtWidgets.QListWidgetItem()
            cellMessage.setTextAlignment(QtCore.Qt.AlignRight)
            cellMessage.setText(f"{value[1]}:\n {value[-1]}")
            self.listWidget.addItem(cellMessage)
            print(value)            
    
    def getInfo(self):
        self.info = AdditionalInformation()
        self.info.show()
    
    def configure(self):
        self.setWn = SetWindows(self, self.connectMonitor.getSignal)
        self.setWn.show()     
    
    def join(self):
        self.updateConfigure()
        if self.nickName != None:
            try:
                self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client.connect((self.ip, self.port))
                self.connectMonitor.serverSocket = self.client
                self.connectMonitor.start()
            except Exception as error:
                message = "Проверьте соединение с сервером: 'Ошибка с соединением'"
                QtWidgets.QMessageBox.about(self, "Оповещение", message)            
        else:
            message = "Введите имя во фкладке 'Настройки'!"
            QtWidgets.QMessageBox.about(self, "Оповещение", message)
    
    def translate(self):
        self.tr = TranslatorWindows()
        self.tr.show()
    
    def closeEvent(self, value:QtGui.QCloseEvent):
        try:
            payload = ["EXIT", f"{self.nickName}".encode()]
            self.connectMonitor.send_encrypt(payload)
            self.hide()
            time.sleep(3)
            self.client.close()
            self.close()
        except Exception as err:
            print(err)
    
    
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = UserInterface()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())