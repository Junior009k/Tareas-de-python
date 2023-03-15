import Usuario  
import SerieFibonacci

class Menu:
    #Creacion del objeto
    Usuario=Usuario.Usuario()
     
    def menuRegistrarUsuario(self):
        
        
        #Metodos del objeto
        self.Usuario.registrarCorreo()
        self.Usuario.registrarClave()    
        print("Estoy en opcion 1")
        #Salida
        print(f"Su correo es {self.Usuario.correo} y su clave es {self.Usuario.contraseña}")

    
    #esto hara de login
    def menuIniciarFibonacci(self):    
        if(self.Usuario.correo==""):
            print("Debe de haber registrado un correo")
            return 0
        if(self.Usuario.correo!=""):
            i=2
            while(i!=3):  
                print("inserte el correo")
                correo="Junior@gmail.com"         
                print("inserte la contraseña")
                clave="Junior@gmail.com123"
                bandera=self.Usuario.validarUsuario(correo,clave)
                if (bandera):
                    print("Bienvenido a la serie de fibonacci, indique un numero para generarla")
                    n=int(input())  
                    SerieFibonacci.generarSerie(n)
                    i=2
                else:
                    print("Usuario incorrecto")