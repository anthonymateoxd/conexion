class Movie():
    
    def __init__(self, id_user, username=None,email=None,contraseña=None)->None:
        self.id_user = id_user
        self.username = username
        self.email = email
        self.contraseña = contraseña
    
    def to_JSON(self):
        return{
            'id_user': self.id_user,
            'username': self.username,
            'email': self.email,
            'contraseña': self.contraseña
        }