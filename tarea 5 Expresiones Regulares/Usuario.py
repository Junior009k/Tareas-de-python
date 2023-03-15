import re

def registrarCorreo():
    i=0
    while(i!=1):
        correo=input("Ingrese un correo\n")
    #Creamos la condicional que nos validara que nuestro correo sea valido]
        if(re.match('[aA-zZ0-9._%+-]+@[aA-zZ0-9.-]+\.[aA-zZ]{2,}',correo)):
            print("El correo es valido")
            i=1
        else:
            print("el correo es invalido, intentelo de nuevo \n")   
    return correo

def registrarClave():
    i=0
    while(i!=1):
        clave=input("Ingrese su clave \n")
        i=1
        #Evaluaremos que tenga una letra mayuscula
        i=validarClave(re.findall(f"[A-Z]",clave),"No hay letra mayuscula en la contraseña \n",i)
        #Evaluaremos que tenga una letra minuscula
        i=validarClave(re.findall(f"[a-z]",clave),"No hay letra minuscula en la contraseña \n",i)
        #Evaluaremos que tenga una letra minuscula
        i=validarClave(re.findall(f"[0-9]",clave),"No hay numero en la contraseña \n",i)
        #Evaluaremos que tenga un caracter especial
        i=validarClave(re.findall(f"[._*%+-]",clave),"No hay caracter en la contraseña \n",i)
    return clave
 
 
def validarClave(resultado,texto,i):
    if(len(resultado)<1):
        print(texto)
        i=0
    return i

