#Bienvenido al archivo de configuracion de la app flask

class DevelopmentConfig():
    DEBUG = True
    HOST = "0.0.0.0"
    PORT = 5000
    
#Aqui voy a tener las configuraciones del proyectos
config = {
    'development': DevelopmentConfig
}