import socket
import time
import pickle
import threading
from cryptography.fernet import Fernet


#Класс, реализующий сервер на socket
class Server():
    def __init__(self, ip, port):
        self.port = port
        self.ip = ip
        self.symetricKey = None
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen(0)
        self.allClients = []
        print("Сервер запущен!")
        #self.checkNewJoined()
        threading.Thread(target=self.checkNewJoined).start()
    
    #Проверка на подключение к чату
    def checkNewJoined(self):
        while True:
            user, road = self.server.accept()
            if user not in self.allClients:    #Проверка на наличие пользователя в чате
                self.allClients.append(user)
                self.newKey()
                answer = ["200_OK", "Успешное подключение к чату", self.symetricKey] #Успешное подключение к чату
                user.send(pickle.dumps(answer))
                print(f"{road} - joined the chat")
                #self.checkMassage(user)
                threading.Thread(target=self.checkMassage, args=(user, )).start()
            time.sleep(2)
    
    #Генератор симметричного шифра
    def newKey(self):
        if self.symetricKey is None:
            self.symetricKey = Fernet.generate_key()

    #Проверка на наличие новых сообщений    
    def checkMassage(self, user):
        while True:
            #Попытка принять сообщение от пользователя
            try:
                message = user.recv(1024)
                decodeMassege = pickle.loads(message)
                print(decodeMassege)
            
            #В случае неудачи, оборвать с ним соединение
            except:
                self.allClients.remove(user)
                break
            
            #Отправка сообщения в чат
            if decodeMassege[0] == "100_CONTINUE":
                for client in self.allClients:
                    if client != user:
                        client.send(message)
                        
            #Участник покинул чат
            elif decodeMassege[0] == "500_INTERNAL_SERVER_ERROR":
                print(f"{decodeMassege[1]} - left the chat")
                self.allClients.remove(user)
                break
            
            elif decodeMassege[0] == "EXIT":
                print(f"{decodeMassege[1]} +  - Разорвал соединение")
                self.allClients.remove(user)
                break
            
            time.sleep(1)
    
        
if __name__ == "__main__":
    newServer = Server("127.0.0.1", 1234)
        