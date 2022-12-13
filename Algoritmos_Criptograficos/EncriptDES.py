import time
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

#Tiempo en leer un archivo con el texto a cifrar
InicioArchivo= time.time() 
#Obtenemos un mensaje de un archivo externo
my_text = r'C:\Users\hidal\Desktop\python-course\\Algoritmos_Criptograficos\Texto_2.txt' #Destino del archivo
#Guardamos informacion del archivo en mensaje
with open(my_text, 'r', encoding='utf-8') as fichero:
    mensaje = fichero.read()
FinalArchivo= time.time()


#Tiempo en generar y/o imprimir la(las) claves de cifrado
InicioClave= time.time()
#Generamos las claves 
while True:
    try:
        key = DES3.adjust_key_parity(get_random_bytes(24))
        break
    except ValueError:
        pass
print('Clave:')
print(key)
print('------------------------')
FinalClave= time.time()


#Tiempo en cifrar e imprimir el texto cifrado
InicioCifrado= time.time()
#Funciones de cifrar
def encrypt(msg):
    cipher = DES3.new(key, DES3.MODE_EAX)
    nonce = cipher.nonce
    ciphertext = cipher.encrypt(msg.encode('ascii'))
    return nonce, ciphertext

nonce, ciphertext = encrypt(mensaje)
print(f'Texto Cifrado: {ciphertext}')
print('------------------------------')
FinalCifrado= time.time()


#Tiempo en descifrar e imprimir el texto cifrado
InicioDescifrado= time.time()
#Funciones de cifrar
def decrypt(nonce, ciphertext):
    cipher = DES3.new(key, DES3.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode('ascii')

plaintext = decrypt(nonce, ciphertext)
print(f'Texto Descifrado : {plaintext}')
print('------------------------------')
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