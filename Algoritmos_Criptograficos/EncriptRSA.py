import time
import Crypto #Importamos la libreria Crypto 
import binascii #libreria para conversion de binario a ASCII

#Utilizaremos el algoritmo RSA
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP #Metodo de cifrado

#Tiempo en leer un archivo con el texto a cifrar
InicioArchivo= time.time() 
#Obtenemos un mensaje de un archivo externo
my_text = r'C:\Users\hidal\Desktop\python-course\Algoritmos_Criptograficos\Texto_1.txt' #Destino del archivo
#Guardamos informacion del archivo en mensaje
with open(my_text, 'r', encoding='utf-8') as fichero:
    mensaje = fichero.read()
mensaje = mensaje.encode() #Se codifica el mensaje
FinalArchivo= time.time()


#Tiempo en generar y/o imprimir la(las) claves de cifrado
InicioClave= time.time()
#Generacion de numeros de manera aleatoria de forma segura
random = Crypto.Random.new().read
#Se genera las llaves privada y publica
clave_privada = RSA.generate(2048) #(1024,tamaño de la clave)
clave_publica = clave_privada.publickey() #De una llave priva se crea la publica
print('Se muestran las claves creadas: ')
print(clave_privada)
print(clave_publica)
print('---------------------------------------')
FinalClave= time.time()


#Tiempo en cifrar e imprimir el texto cifrado
InicioCifrado= time.time()
#Se decodifica las llaves para poder leer
clave_privada = clave_privada.export_key(format='DER') #Exportamos las llaves
clave_publica = clave_publica.export_key(format='DER')
#CaNVERTIMOS a codigo ASCCI
clave_privada = binascii.hexlify(clave_privada).decode('utf8')
clave_publica = binascii.hexlify(clave_publica).decode('utf8')
print('Clave privada:'+clave_privada)
print(' ')
print('Clave publica:'+clave_publica)
print('-------------------------------------')

#Proceso inverso obteniendo objetos para codificar los mensajes
clave_privada = RSA.import_key(binascii.unhexlify(clave_privada))
clave_publica = RSA.import_key(binascii.unhexlify(clave_publica))


#Ciframos el texto
cifrar = PKCS1_OAEP.new(clave_publica) #Para cifrar se necesita la llave publica
mensaje_encriptado = cifrar.encrypt(mensaje)

#Se guarda el mensaje encriptado y se muestra
print('Mensaje encriptado: ')
print(mensaje_encriptado)
print('--------------------------------------')
FinalCifrado= time.time()


#Tiempo en descifrar e imprimir el texto cifrado
InicioDescifrado= time.time()
#Desciframos el texto
cifrar = PKCS1_OAEP.new(clave_privada) #Llve que permite descifrar
mensaje1 = cifrar.decrypt(mensaje_encriptado)
print('Mensaje desencriptado: ')
print(mensaje1)
print('--------------------------------------')
FinalDescifrado= time.time()

#Resultados de tiempos obtenidos
TotalArchivos= FinalArchivo - InicioArchivo
TotalClave= FinalClave - InicioClave
TotalCifrado= FinalCifrado - InicioCifrado
TotalDescifrado= FinalDescifrado - InicioDescifrado
print('Tiempo de ejecución de lectura de archivos es: ', TotalArchivos)
print('Tiempo en generar y/o imprimir claves de cifrado: ', TotalClave)
print('Tiempo de ejecución de cifrado e imprimir resultado es: ', TotalCifrado)
print('Tiempo de ejecución de descifrado e imprimir resultado es: ', TotalDescifrado)
