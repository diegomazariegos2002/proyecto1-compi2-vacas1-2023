#Bienvenido al archivo de configuracion de la app flask

class DevelopmentConfig():
    DEBUG = False
    #HOST = "0.0.0.0"
    HOST = "18.119.102.248"
    PORT = 4000
    
#Aqui voy a tener las configuraciones del proyectos
config = {
    'development': DevelopmentConfig
}