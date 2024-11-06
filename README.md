# Criptografía

## Algoritmo
Este es un nuevo e innovador algoritmo criptográfico que utiliza la propiedad de los montículos del Heapsort para poder encriptar los mensajes carácter por carácter en un montículo, asumiendo una llave 'pública' (en realdidad es una llave desechable), que es una tupla compuesta por una lista de montículos y un signo. 

  * Montículos: para esconder cada caracter de cada parte del texto plano, de manera que cada montículo de la lista es como una especie de llave y el mecanismod de utilización de los montículos es un poco como el sistema del vigenere, pues, cada caracter requiere de un montículo distinto hasta que se acaben y se comience de nuevo.
  * Signo: Este indica si la propiedad del montículo será máxima: + (Más); o mínima: -  (Menos).

A su vez, este algoritmo retorna el criptograma en forma de una cadena de caracteres y la llave privada, que se utilizará para el descifrado. 

  * Llave privada: es una n-lista de tuplas donde n es la cantidad de caracteres del mensaje original y cada tupla (i,j) expresa la cantidad de elementos del k-esimo montículo y j es la posición del caracter que pertenece al texto plano.
