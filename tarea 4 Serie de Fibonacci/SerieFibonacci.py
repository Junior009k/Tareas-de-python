#Declaramos la funcion que nos ayudara a generar la serie de fibonacci
def generarSerie(numero):
    #declaramos nuestro arreglao que contendra la serie
    serie=[0]
    #Declaramos la variables auxiliares
    a=0
    b=1     
    for numeros in range(numero):
        print(f"{a}+{b}={b}")
        b=a+b
        a=serie[numeros]
        serie.append(b)
    return serie,numero
