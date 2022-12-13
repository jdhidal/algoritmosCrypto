import time

#Tiempo en leer un archivo con el texto a cifrar
InicioArchivo= time.time() 
#Recibir archivo de texto plano
my_text = r'C:\Users\hidal\Desktop\python-course\Algoritmos_Criptograficos\Texto_1.txt'
with open (my_text) as file_object:
    leer = file_object.read()
FinalArchivo= time.time()


# Tiempo de cifrado y muesta
InicioCifrado= time.time()
# #Funcion para encriptar por sustitucion
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
FinalCifrado= time.time()

#Tiempo en descifrar e imprimir el texto claro
InicioDescifrado= time.time()
print('Mensaje en texto entendible:', leer)
print('--------------------------------------')
FinalDescifrado= time.time()

#Resultados de tiempos obtenidos
TotalArchivos= FinalArchivo - InicioArchivo
TotalCifrado= FinalCifrado - InicioCifrado
TotalDescifrado= FinalDescifrado - InicioDescifrado
print('Tiempo de ejecución de lectura de archivos es: ', TotalArchivos)
print('Tiempo de ejecución de cifrado e imprimir resultado es: ', TotalCifrado)
print('Tiempo de ejecución de descifrado e imprimir resultado es: ', TotalDescifrado)