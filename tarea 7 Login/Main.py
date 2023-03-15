#import SerieFibonacci
import Menu   
import os  
i=0
Menu=Menu.Menu()
while(i!=3):  
    print("Que desea realizar? ")
    print("1.Registrar un usuario ")
    print("2.Iniciar la serie Fibonacci")
    print("3.Salir")
    opcion=input()  
    if (opcion=="1"):
        Menu.menuRegistrarUsuario()
    if (opcion=="2"):
        Menu.menuIniciarFibonacci()
    if (opcion=="3"):
        i=3
    opcion=input()
    os.system("cls")    

