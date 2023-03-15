import re
#Creacion de la clase 
class Usuario:
    #Declaracion de variables
    correo=""
    contraseña=""
    
 
    def registrarCorreo(self):
        i=0
        while(i!=1):
            #self.correo=input("Ingrese un correo\n")
            self.correo=("Junior@gmail.com")
        #Creamos la condicional que nos validara que nuestro correo sea valido]
            if(re.match('[aA-zZ0-9._%+-]+@[aA-zZ0-9.-]+\.[aA-zZ]{2,}',self.correo)):
                print("El correo es valido")
                i=1
            else:
                print("el correo es invalido, intentelo de nuevo \n")   
    
    def registrarClave(self):
        i=0
        while(i!=1):
            #self.contraseña=input("Ingrese su clave \n")
            self.contraseña=("Junior@gmail.com123")
            i=1
            #Evaluaremos que tenga una letra mayuscula
            i=validarClave(re.findall(f"[A-Z]",self.contraseña),"No hay letra mayuscula en la contraseña \n",i)
            #Evaluaremos que tenga una letra minuscula
            i=validarClave(re.findall(f"[a-z]",self.contraseña),"No hay letra minuscula en la contraseña \n",i)
            #Evaluaremos que tenga una letra minuscula
            i=validarClave(re.findall(f"[0-9]",self.contraseña),"No hay numero en la contraseña \n",i)
            #Evaluaremos que tenga un caracter especial
            i=validarClave(re.findall(f"[._*%+-]",self.contraseña),"No hay caracter en la contraseña \n",i)
    
    def validarUsuario(self,correo,contraseña):
        if(correo==self.correo and contraseña==self.contraseña):
            return True
        else:
            return False
        
            
    def cambiar(self):
        self.correo=4
        self.contraseña=3
        
def validarClave(resultado,texto,i):
      if(len(resultado)<1):
          print(texto)
          i=0
      return i  
