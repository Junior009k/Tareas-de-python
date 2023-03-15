#import SerieFibonacci
import Usuario     

#Creacion del objeto
Usuario=Usuario.Usuario()

#Metodos del objeto
Usuario.registrarCorreo()
Usuario.registrarClave()    

#Salida
print(f"Su correo es {Usuario.correo} y su clave es {Usuario.contraseña}")