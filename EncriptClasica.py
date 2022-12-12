import time

#Se establece punto de entrada para conteo del tiempo en ejecucion
TiempoInicio= time.time() 
#Recibir archivo de texto plano
my_text = r'C:\Users\hidal\Desktop\python-course\Encriptacion\Texto_E1.txt'
with open (my_text) as file_object:
    leer = file_object.read()

#Funcion para encriptar por sustitucion 
caracter_elegido = "@"
def encriptar (frase,caracter):
    encriptada = ""
    for letra in frase:
        if letra.lower() in "aeiouáéíóú":
            if letra.isupper():
                encriptada = encriptada + caracter.upper()
            else:
             encriptada = encriptada + caracter
        else:
            encriptada = encriptada + letra
    return encriptada

#Llamada de la funcion de sustitucion 
mensaje_encriptado = encriptar(leer,caracter_elegido)
print('Este es el mensaje encriptado por sustitucion: ', mensaje_encriptado)
print('--------------------------------')
print('Mensaje en texto entendible:', leer)
print('--------------------------------------')
tiempoFinal= time.time()
tiempoTotal= tiempoFinal - TiempoInicio
print('Tiempo de ejecución es: ', tiempoTotal)