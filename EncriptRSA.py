import time
import Crypto #Importamos la libreria Crypto 
import binascii #libreria para conversion de binario a ASCII

#Utilizaremos el algoritmo RSA
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP #Metodo de cifrado

#Se establece punto de entrada para conteo del tiempo en ejecucion
TiempoInicio= time.time() 
#Generacion de numeros de manera aleatoria de forma segura
random = Crypto.Random.new().read
#Se genera las llaves privada y publica
clave_privada = RSA.generate(2048, random) #(1024,tamaño de la clave)
clave_publica = clave_privada.publickey() #De una llave priva se crea la publica
print('Se muestran las claves creadas: ')
print(clave_privada)
print(clave_publica)
print('---------------------------------------')

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

#Obtenemos un mensaje de un archivo externo
my_text = r'C:\Users\hidal\Desktop\python-course\Encriptacion\Texto_E2.txt' #Destino del archivo
#Guardamos informacion del archivo en mensaje
with open(my_text, 'r', encoding='utf-8') as fichero:
    mensaje = fichero.read()

mensaje = mensaje.encode() #Se codifica el mensaje

#Ciframos el texto
cifrar = PKCS1_OAEP.new(clave_publica) #Para cifrar se necesita la llave publica
mensaje_encriptado = cifrar.encrypt(mensaje)
#Se guarda el mensaje encriptado y se muestra
print('Mensaje encriptado: ')
print(mensaje_encriptado)
print('--------------------------------------')

#Desciframos el texto
cifrar = PKCS1_OAEP.new(clave_privada) #Llve que permite descifrar
mensaje1 = cifrar.decrypt(mensaje_encriptado)
print('Mensaje desencriptado: ')
print(mensaje1)
print('--------------------------------------')
tiempoFinal= time.time()
tiempoTotal= tiempoFinal - TiempoInicio
print('Tiempo de ejecución es: ', tiempoTotal)