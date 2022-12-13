import time

from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
inicio2=time.time()
#Generacion de claves
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()
# Crear archivos de las claves publica y privada
file_out = open("private.pem", "wb")
file_out.write(private_key)
file_out.close()

file_out = open("receiver.pem", "wb")
file_out.write(public_key)
file_out.close()
#Salida de pantalla
print(public_key)
print(private_key)
fin2=time.time()



inicio3 = time.time()
#Lectura del archivo
my_text = r'C:\Users\hidal\Desktop\python-course\Algoritmos_Criptograficos\Texto_5.txt' #Destino del archivo
data = open(my_text, "rb").read()
with open (my_text, "r", encoding="utf-8") as m:
   lectura = m.read()
print("\nLectura del archivo ")
print(lectura)
fin3 = time.time()


inicio = time.time()
file_out = open("encrypted_data.bin", "wb")

recipient_key = RSA.import_key(open("receiver.pem").read())
session_key = get_random_bytes(16)


cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_session_key = cipher_rsa.encrypt(session_key)


cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)
[file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
file_out.close()


#leer el archivo binario y luegi imprimir
file_in = open("encrypted_data.bin", "rb")
with open("encrypted_data.bin", "rb") as f:
   variable = f.read()
   print("Informacion cifrada")
   print(variable)

fin = time.time()


inicio1 = time.time()
private_key = RSA.import_key(open("private.pem").read())


enc_session_key, nonce, tag, ciphertext = \
   [file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]


#Desencriptar
cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)


cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)
print("\nInformacion descifrada")
print(data.decode("utf-8")) # imprimir el texto decodificado
fin1 = time.time()

print("TDescifrado "+str(fin1-inicio1))
print("Gene "+ str(fin2-inicio2) )
print("Lect "+ str(fin3-inicio3))
print("T_Cifrado "+ str(fin-inicio))