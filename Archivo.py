nombre = "mariana"
edad = 17

print("nombre:", nombre)
print("edad:", edad)

if edad >= 18:
    print(nombre, "es mayor de edad")
else:
    print(nombre, 'es menor de edad')

def saludar(nombre):
    return "hola, " + nombre
mensaje = saludar(nombre)
print(mensaje)
