# Cifrado basado en la propiedad de monticulo minimo y maximo

global I

# funciones necesarias
get_ar = lambda t: [I.index(i) for i in t]
get_cad = lambda A: ''.join([I[i] for a in A for i in a])
get_cad_1 = lambda A: ''.join([I[a] for a in A])
parent = lambda i: int((i/2)-1) if i%2 == 0 else int((i-1)/2)  
left = lambda i: 2*i+1
right = lambda i: 2*(i+1)

def swap(A, i, j):
    A[i],A[j] = A[j],A[i]

def cifrado(texto_plano, llave):
    global I
    texto = get_ar(texto_plano)
    if (len(texto)%2 == 0):     #<------------- Si la longitud del texto es par
        for i in range(1, len(texto), 2): 
            swap(texto, i-1, i) #<------------ [a,b,c,d,e,f,...] -> [b,a,d,c,f,e,...]
    else:                       # sino
        for i in range(1, len(texto)-1, 2): 
            swap(texto, i - 1, i) #<------------ [a,b,c,d,e,f,...,z] -> [b,a,d,c,f,e,...,z]
    monticulos = []
    llave_1 = llave[0] #<-----------------------  Montículos
    llave_2 = llave[1] #<----------------------- '-' montículos mínimos / '+' máximos
    for l in llave_1:  #<-----------------------  Para cada montículo
        monticulo = []
        for n in l:
            monticulo.append(n)
            i = len(monticulo)-1
            f = parent(i)
            if (llave_2 == '-'):   #<------------- Si son montículos mínimos
                while ((monticulo[f] > monticulo[i]) and (f > -1)):
                    swap(monticulo, f, i)
                    i, f = f, parent(f)
            elif (llave_2 == '+'): #<------------- Si son montículos máximos
                while ((monticulo[f] < monticulo[i]) and (f > -1)):
                    swap(monticulo, f, i)
                    i, f= f, parent(f)
            else:
                raise TypeError("El parámetro debe ser '-' para montículos mínimos o '+' para montículos máximos")
        monticulos.append(monticulo)

    j, criptograma_t, llave_descifrado, pos, lon = 0, [], [], -1, -1
    for n in texto:
        mon = monticulos[j]+[n] #<------------------- Incluimos el carácter para mezclarlo
        i = len(mon)-1
        f = parent(i)
        if (llave_2 == '-'):   #<-------------------- Si son montículos mínimos
            while ((mon[f] > mon[i]) and (f > -1)):
                swap(mon, f, i)
                i, f = f, parent(f)
        else:                  #<-------------------- Si son montículos máximos
            while ((mon[f] < mon[i]) and (f >   -1)):
                swap(mon, f, i)
                i, f = f, parent(f)
        pos, lon = i, len(mon)
        criptograma_t.append(mon)
        llave_descifrado.append([lon, pos])
        j = 0 if j+1 == len(monticulos) else j+1
    criptograma = get_cad(criptograma_t)
    return criptograma, llave_descifrado

def descifrado(criptograma, llave):
    crip, texto_1, j = get_ar(criptograma), [], 0
    for l in llave:
        i = l[1]+j
        n = crip[i]
        j = l[0]+j
        texto_1.append(n)
    if (len(texto_1)%2 == 0):
        for i in range(1, len(texto_1), 2):
            swap(texto_1, i - 1, i)
    else:
        for i in range(1, len(texto_1) - 1, 2):
            swap(texto_1, i - 1, i)
    texto = get_cad_1(texto_1)
    return texto



# Alfabeto (lista que se le entrega al programa)
I = ['%', 'x', 'A', '}', 'z', '>', 'B', '-', '8', '[', 'y', '!', 'C', '_', 'D', 'w', 'E', 'ó', '$', 'v', '6',
     'F', ')', '1', 'u', 'G', 't', 'H', 's', '|', 'I', 'r', 'J', '/', 'q', '3', '*', 'K', 'p', 'L', '°',
     'o', '^', 'M', 'ñ', '5', 'í', '@', 'N', 'n', 'á', 'Ñ', 'm', 'O', '¬', 'l', 'P', 'k', 'Q', 'j', 'R', 'i', '?',
     'S', '¨', 'h','T', '#', 'g', '4', 'U', '(', 'f', 'V', 'e', 'é', '=', 'W', '<', 'd', 'X', 'ú', '9', 'c', 'Y',
     '0', 'b', 'Z', 'a','.', '7', ',', ']', '¡', ';', '2', '+', '{', '¿', '&']


###########
# EJEMPLO #
###########

texto = 'Texto_de_prueba'
print(len(I))
#Entre 0 y 100

llave_cifrado = llave_cifrado = ([[11, 37, 24, 94, 0, 100, 32, 64, 28, 56], [73, 87, 1, 2, 3, 8, 93, 22, 54, 48, 47], [33, 25, 17, 58, 59, 5, 3, 4, 47, 46, 83]], '-')
criptograma, llave_descifrado = cifrado(texto, llave_cifrado)
texto_descifrado = descifrado(criptograma, llave_descifrado)
print('Texto plano original: ' + texto)
print('Criptograma: ' + criptograma)
print('Texto descifrado: ' + texto_descifrado)