#Cifrado basado en la propiedad de monticulo minimo y maximo

def get_ar(t):
    global I
    A = []
    for c in t:
        A.append(I.index(c))
    return A

def get_cad(A):
    global I
    cad = ''
    for l in A:
        for n in l:
            cad = cad + I[n]
    return cad


def get_cad_1(A):
    global I
    cad = ''
    for n in A:
        cad = cad + I[n]
    return cad

def swap(A, i, j):
    t = A[i]
    A[i] = A[j]
    A[j] = t
    
def parent(i):
    if (i%2 == 0):
        return int((i/2) - 1)
    else:
        return int((i - 1)/2)
    
def left(i):
    return 2*i + 1

def right(i):
    return 2*(i + 1)

def cifrado(texto_plano, llave):
    global I
    texto = get_ar(texto_plano)
    if (len(texto)%2 == 0):
        for i in range(1, len(texto), 2):
            swap(texto, i - 1, i)
    else:
        for i in range(1, len(texto) - 1, 2):
            swap(texto, i - 1, i)
    monticulos = []
    llave_1 = llave[0]
    llave_2 = llave[1]
    if (llave_2 == '-'):
        for l in llave_1:
            monticulo = []
            for n in l:
                monticulo.append(n)
                i = len(monticulo) - 1
                f = parent(i)
                while ((monticulo[f] > monticulo[i]) and (f > -1)):
                    swap(monticulo, f, i)
                    i = f
                    f = parent(i)
            monticulos.append(monticulo)
        j = 0
        criptograma_t = []
        llave_descifrado = []
        pos = -1
        lon = -1
        for n in texto:
            mon = []
            for m in monticulos[j]:
                mon.append(m)
            mon.append(n)
            i = len(mon) - 1
            f = parent(i)
            while ((mon[f] > mon[i]) and (f > -1)):
                swap(mon, f, i)
                i = f
                f = parent(i)
            pos = i
            lon = len(mon)
            criptograma_t.append(mon)
            llave_descifrado.append([lon, pos])
            j += 1
            if (j == len(monticulos)):
                j = 0
    elif (llave_2 == '+'):
        for l in llave_1:
            monticulo = []
            for n in l:
                monticulo.append(n)
                i = len(monticulo) - 1
                f = parent(i)
                while ((monticulo[f] < monticulo[i]) and (f > -1)):
                    swap(monticulo, f, i)
                    i = f
                    f = parent(i)
            monticulos.append(monticulo)
        j = 0
        criptograma_t = []
        llave_descifrado = []
        pos = -1
        lon = -1
        for n in texto:
            mon = []
            for m in monticulos[j]:
                mon.append(m)
            mon.append(n)
            i = len(mon) - 1
            f = parent(i)
            while ((mon[f] < mon[i]) and (f > -1)):
                swap(mon, f, i)
                i = f
                f = parent(i)
            pos = i
            lon = len(mon)
            criptograma_t.append(mon)
            llave_descifrado.append([lon, pos])
            j += 1
            if (j == len(monticulos)):
                j = 0
    criptograma = get_cad(criptograma_t)
    return criptograma, llave_descifrado

def descifrado(criptograma, llave):
    crip = get_ar(criptograma)
    texto_1 = []
    j = 0
    for l in llave:
        i = l[1] + j
        n = crip[i]
        texto_1.append(n)
        j = l[0] + j
    if (len(texto_1)%2 == 0):
        for i in range(1, len(texto_1), 2):
            swap(texto_1, i - 1, i)
    else:
        for i in range(1, len(texto_1) - 1, 2):
            swap(texto_1, i - 1, i)
    texto = get_cad_1(texto_1)
    return texto

I = [' ', 'A', 'z', 'B', 'y', 'C', 'x', 'D', 'w', 'E', 'v', 'F', 'u', 'G', 't', 'H', 's', 'I', 'r', 'J',
      'q', 'K', 'p', 'L', 'o', 'M', 'ñ', 'N', 'n', 'Ñ', 'm', 'O', 'l', 'P', 'k', 'Q', 'j', 'R', 'i','S',
      'h','T', 'g', 'U', 'f', 'V', 'e', 'W', 'd', 'X', 'c', 'Y', 'b', 'Z', 'a', '.', ',', ';']

texto = 'Este es un texto plano largo de prueba para, valga la redundancia, probar la efectividad del cifrado basado en la propiedad de monticulo minimo y maximo; haber que sucede.'
#Entre 0 y 57
llave_cifrado = ([[1, 2, 3, 47, 21, 33], [57, 56, 55, 4, 8, 23], [2, 4, 8, 16, 32], [3, 9, 27, 30, 1, 2], [1, 7, 9, 27, 29, 23, 39, 33, 31]], '-')
criptograma, llave_descifrado = cifrado(texto, llave_cifrado)
texto_descifrado = descifrado(criptograma, llave_descifrado)
print('Texto plano original: ' + texto)
print('Criptograma: ' + criptograma)
print('Texto descifrado: ' + texto_descifrado)