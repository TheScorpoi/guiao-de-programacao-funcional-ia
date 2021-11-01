import math

#Exercicio 4.1
impar = lambda x : True if (x % 2 != 0) else False

#Exercicio 4.2
positivo = lambda x : True if (x > 0) else False

#Exercicio 4.3
comparar_modulo = lambda x, y : True if (abs(x) < abs(y)) else False

#Exercicio 4.4
#https://www.w3schools.com/python/ref_math_atan2.asp
cart2pol = lambda x, y : (math.sqrt(x**2 + y**2), (math.atan2(y, x)))

#Exercicio 4.5
def ex5(f, g, h):
    return lambda x, y, z: h(f(x,y), g(y, z)) 
 
#Exercicio 4.6
def quantificador_universal(lista, f):
    for i in lista:
        if f(i) == False:
            return False
    return True

#Exercicio 4.7
def quantificador_existencial(lista, f):
    for i in lista:
        if f(i) == True:
            return True
    return False

#Exercicio 4.9
def ordem(lista, f):
    if len(lista) == 1:
        return lista[0]
    m = ordem(lista[1:], f)
    
    return lista[0] if f(lista[0], m) else m

#Exercicio 4.10
def filtrar_ordem(lista, f):
    if len(lista) == 1:
        return lista[0], []
    m, l = filtrar_ordem(lista[1:], f)
    return (lista[0], lista[1:]) if f(lista[0], m) else (m, [lista[0]] + l)

#Exercicio 5.2
def ordenar_seleccao(lista, ordem):
    if len(lista) == 1:
        return lista
    m, l = filtrar_ordem(lista, ordem)
    return [m] + ordenar_seleccao(l, ordem)

if __name__ == '__main__':
    print("Exercicio 4.1: ", impar(3))
    print("Exercicio 4.2: ", positivo(3))
    print("Exercicio 4.3: ", comparar_modulo(4,-3))
    print("Exercicio 4.4: ", cart2pol(3, -2))
    #print("Exercicio 4.5: ", impar(3))
    #print("Exercicio 4.6: ", impar(3))
    print("Exercicio 4.9: ", ordem([1,-1-4-0], lambda x,y: x < y))
    
    