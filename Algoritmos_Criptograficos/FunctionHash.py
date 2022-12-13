import hashlib
import time

def compute_sha256(file_name):
    hash_sha256 = hashlib.sha256()
    with open(file_name, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

#Tiempo en leer un archivo con el texto a cifrar
InicioArchivo= time.time()
my_text = r'C:\Users\hidal\Desktop\python-course\Algoritmos_Criptograficos\Texto_5.txt'
FinalArchivo= time.time()

# Tiempo de cifrado y muesta
InicioCifrado= time.time()
print('Mensaje cifrado: ')
print(compute_sha256(my_text))
print('--------------------------------')
FinalCifrado= time.time()


#Resultados de tiempos obtenidos
TotalArchivos= FinalArchivo - InicioArchivo
TotalCifrado= FinalCifrado - InicioCifrado
print('Tiempo de ejecución de lectura de archivos es: ', TotalArchivos)
print('Tiempo de ejecución de cifrado e imprimir resultado es: ', TotalCifrado)
