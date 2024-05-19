# hash-bip39

¿Por que escribí el código (Con ayuda del robot)?

En un futuro cercano, habrá muchas seedphrase generadas por los usuarios, la seguridad fisica de esas 12 palabras se volverán un target relevante, por lo cual, la ofuscación de esas palabras será vital para evitar un robo (cuando un ratero llegue a tu casa mientrás estás de vacaciones y se lleve tu placa con tus palabras, no querrás que las pueda leer, tampoco cuando tu persona de "cofianza" decida que tomarle una foto a tu frase es buena idea, no querras haber escrito de manera legible tu frase) 

¿Cómo funciona?

GENERACIÓN DE LISTA DUPLAS PALABRA BIP39-NUMERO - hash-gen-lista-py

(NOTA: ESTE CODIGO NO GENERA SEEDPHRASES)

La forma de ofuscar tu seedphrase es simple, en lugar de escribir tu seedphrase con palabras que son legibles, será a través de la creación de un mapa de palabras del BIP-39-números. El usuario en vez de almacenar su seedphrase con palabras, almacenará números, escritos en donde quiera y piense es prudente.

Este codigo propone funciona creando una lista aleatoria de duplas palabra-numero de la lista de palabras del bip 39 de bitcoin, la lista se genera de manera aleatoria utilizando la libreria secrets de python como generador generador de aleatoriedad, para generar la semilla de entropía del modulo secrets se realiza lo siguiente:

Al correr el código del archivo hash-gen-lista.py, se generará un primer timestamp, que pasará por una función de hash-256, este hash nos ayudará para dos cosas:

La primera es crear el nombre de tu lista aleatoria de duplas palabra-numero (se crea un archivo .csv llamado "lista_********.csv" y un archivo .txt del cual hablaremos después) el archivo .csv, el nombre se compone de un código alfanumérico de 8 posiciones.

La segunda es para crear un segundo timestamp aleatorio dentro de los 21 segundos posteriores, ese timestamp se corre en una función hash-256 y el hash se utilizará como semilla para crear la aleatoriedad de la lista de duplas.

El usuario al final de este primer proceso, obtendrá el archivo CSV, que podrá usar para ver de manera fácil la lista de duplas palabra-numero, el ususario podrá apuntar los numeros correspondientes a su seedphrase, esto se deberá hacer de manera manual, explorando la lista, y por supuesto, de manera privada. Nadie debería saber que tienes esta lista en especifico. Y la lista en CSV, que es legible, puede ser desechada ya que podrá ser re generada posteriormente.

Este archivo es generado de la siguiente manera:

Se corre una función de hash con el algoritmo sha-256 de cada una de las filas de la lista de duplas palabra-numero, es decir, si a la palabra "abandon", se le asigno de manera aleatoria el número "2021", el programa hace un hash de esa combinación palabra-numero y se entrega el hash en la primera fila del documento .txt,

Todas las palabras de la lista generan un hash y al final, se generá un hash probatorio de la lista, combinando todos los hashes y obteniendo un hash de toda la lista. Este será necesario para comprobar la autenticidad y fidelidad de la lista cuando un usuario quiera recuperar su lista a partir de este archivo .txt, es decir, este archivo es el que el usuario debe asegurarse de tener tantos back ups como sea posible.

REGENERACIÓN DE LISTA DUPLAS PALABRA BIP39-NUMERO - hash-dir-hashes.py + hash-recover-txt.py

Por otro lado, cuando el usuario necesite recuperar su lista, deberá correr dos archivos en el siguiente orden. 

1.- hash-dir-hashes.py

Este código crea de manera local un directorio llamado hashes, este directorio contendrá 2048 archivos txt, cada uno correspondiente a una palabra del BIP-39.

Cada archivo de cada palabra, por ejemplo la palabra "abandon", contendrá 2048 hashes, correspondientes a la combinación de palabra-número, por ejemplo

abandon-1: 0a223f00b0835ecdec4d759ed13adc12457b52c106a2c923601a9b6d47fc7bda
abandon-2: bd65c9a5d076d56cccf98cf3704c9c280eb349d269bff858d11cc4bfd217d4d7
abandon-3: f120c8cf1c7fde3e4e0049d392fa095edfe0d5b129945be5c99f3070b7c03f98
...
abandon-2047: dc63733649d79b7225355b18b2e97ffc74b8a022a2f72e3f8847bb9b6368e5a4
abandon-2048: 40349602743d445c5ba6bcead70da03c9f8e1507c19afa1384c3637d949f47d9

Este código prepara el camino para la recuperación de la lista de los usuarios. Se utilizará para comparar los hashes del archivo creado con anterioridad cuando se creo la lista, (y que el usuario debió asegurarse de guardar bien)

2.- hash-recover-txt.py

El usuario deberá tener a la mano su archivo hashes.txt generado al crear la lista de duplas palabras-numero listo en la computadora y correr el código.

El archivo pedirá la ubicación del directorio hashes (que contiene los txt con todos los hashes posibles de número-palabra)

Posteriormente deberá ingresar el archivo hashes.txt que contiene su lista y el hash probatorio.

El código comparará todos los hashes y verificará por medio del hash validatorio si la lista es correcta. Si es correcta, creará el archivo hash_comprobatorio.txt, este arc
