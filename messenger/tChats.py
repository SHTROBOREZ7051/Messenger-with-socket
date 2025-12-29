class User:
    def __init__(self, name, socket_address):
        self.name = name
        self.socket_address = socket_address
        
    def __repr__(self):
        return f"User({self.name}, {self.socket_address})"

    def __str__(self):
        return f"User({self.name}, {self.socket_address})"
    

class OrdinarChat():
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.userList = []
        
    def password_isCorrect(self, password):
        return password == self.password
    
    def chatname_isCorrect(self, name):
        return name == self.name
    
    def user_includeChat(self, user_name):
        for user in self.userList:
            if user.name == user_name:
                return True
        return False
        
    def get_userList(self):
        return self.userList
    
    def add_user(self, user: User):
        self.userList.append(user)
    
    def del_user(self, user_name):        
        for index in range(len(self.userList)):
            if self.userList[index].name == user_name:
                del self.userList[index]
            
    def __repr__(self):
        return f"OrdinarChat({self.name},{self.password},{self.userList})"
    
    def __str__(self):
        return f"OrdinarChat({self.name},{self.password},{self.userList})"
    
    def __bool__(self):
        return True
        
    