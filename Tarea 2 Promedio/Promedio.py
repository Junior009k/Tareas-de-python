
Nombre=[]
Edades=[]
Nombre.append("Miguel")
Edades.append(23)
Nombre.append("Juan")
Edades.append(17)
Nombre.append("Laura")
Edades.append(27)

for Nombre, Edad in zip(Nombre,Edades):
    print(f"tu nombre es {Nombre} y tienes {Edad} años")
    
promedio=round(sum(Edades)/3)
print(f"El promedio de edad es igual a {promedio} años")
conjunto={"2","3"}

print(conjunto)