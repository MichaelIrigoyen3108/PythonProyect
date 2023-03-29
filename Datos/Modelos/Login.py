from Datos.BaseDeDatos import BaseDeDatos


class usuario():

    def __init__(self, nombre, contrasena):
        self.nombre = nombre
        self.contrasena = contrasena
        self.conectado = False
        self.intentos = 7

    def conectar(self):
        myPass = input("Ingrese su contraseña: ")
        if myPass == self.contrasena:
            print("Se ha conectado correctamente")
            self.conectado = True
        else:
            self.intentos -= 1
            if self.intentos > 0:
                print("Contraseña incorrecta, intente de vuelta...")
                print("Intentos restantes: ", self.intentos)
                self.conectar()
            else:
                print("Error, no se pudo conectar")
                self.conectado = False

    def desconectar(self):
        if self.conectado:
            print("Se ha cerrado sesion")
            self.conectado = False
        else:
            print("Error")

    def __str__(self):
        if self.conectado:
            conect = "conectado"
        else:
            conect = "desconectado"
        return f"Mi nombre de usuario es: {self.nombre} y estoy {conect}"


    bd = BaseDeDatos()


