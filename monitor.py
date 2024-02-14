import PyQt5.QtCore
from PyQt5 import QtCore
from cryptography.fernet import Fernet
import pickle
import socket


class ThreadMonitor(QtCore.QThread):
    getSignal = QtCore.pyqtSignal(list)
    serverSocket = None
    symetricKey = None
    
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        
    def run(self):
        print(f"The server was started {self.serverSocket}")
        while True:
            if self.serverSocket != None:
                message = self.serverSocket.recv(1024)
                decodeMessage = pickle.loads(message)
                if decodeMessage[0] == "200_OK":
                    
                    self.symetricKey = decodeMessage[-1]
                    self.cipher = Fernet(self.symetricKey)
                    self.getSignal.emit(decodeMessage)
                    
                elif decodeMessage[0] == "100_CONTINUE":
                    decryptedMessage = self.cipher.decrypt(decodeMessage[-1]).decode()
                    decryptedload = ["100_CONTINUE", decodeMessage[1], decryptedMessage]
                    self.getSignal.emit(decryptedload)
                    
            time.sleep(2)
                        
    def send_encrypt(self, information):
        if information[0] == "100_CONTINUE":
            encryptMessage = self.cipher.encrypt(information[-1])
            pickLoad = ["100_CONTINUE", information[1], encryptMessage]
            self.serverSocket.send(pickle.dumps(pickLoad))
            
        elif information[0] == "EXIT":
            encryptMessage = self.cipher.encrypt(information[-1])
            pickLoad = ["EXIT", information[1], encryptMessage]
            self.serverSocket.send(pickle.dumps(pickLoad))