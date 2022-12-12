import time
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

TiempoInicio= time.time() 
#Generamos las claves 
while True:
    try:
        key = DES3.adjust_key_parity(get_random_bytes(48))
        break
    except ValueError:
        pass
print('Clave:')
print(key)
print('------------------------')

#Funciones de encriptar y desencriptar
def encrypt(msg):
    cipher = DES3.new(key, DES3.MODE_EAX)
    nonce = cipher.nonce
    ciphertext = cipher.encrypt(msg.encode('ascii'))
    return nonce, ciphertext

def decrypt(nonce, ciphertext):
    cipher = DES3.new(key, DES3.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode('ascii')

#Obtenemos un mensaje de un archivo externo
my_text = r'C:\Users\hidal\Desktop\python-course\Encriptacion\Texto_E2.txt' #Destino del archivo
#Guardamos informacion del archivo en mensaje
with open(my_text, 'r', encoding='utf-8') as fichero:
    mensaje = fichero.read()

#GUardamos informacion 
nonce, ciphertext = encrypt(mensaje)
plaintext = decrypt(nonce, ciphertext)
print(f'Texto Cifrado: {ciphertext}')
print('------------------------------')
print(f'Texto Descifrado : {plaintext}')
tiempoFinal= time.time()
tiempoTotal= tiempoFinal - TiempoInicio
print('------------------------------')
print('Tiempo de ejecución es: ', tiempoTotal)