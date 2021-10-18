"""
1.5,1.7,1.8,1.9,2.1,
3.3,3.4,4.1-4.6, 4.9
4.10, 5.2 a)
"""

#Exercicio 1.1
def comprimento(lista):
    if lista == []:
        return 0
    return 1 + comprimento(lista[1:])

#Exercicio 1.2
def soma(lista):
    if lista == []:
        return 0
    return lista[0] + soma(lista[1:])

#Exercicio 1.3
def existe(lista, elem):
	if lista == []:
		return False
	if lista[0] == elem:
		return True
	return existe(lista[1:], elem)

#Exercicio 1.4
def concat(l1, l2):
    if l1 == []:
        return l2
    if l2 == []:
        return l1
    l1.append(l2[0])
    return concat(l1, l2[1:])

#Exercicio 1.5
def inverte(lista):
	if lista == []:
		return []
	return [lista[-1]] + inverte(lista[0:-1])

#Exercicio 1.6
def capicua(lista):
    if lista == []:
        return True
    if lista[0] == lista[-1]:
        return capicua(lista[1:-1])
    else:
        return False

#Exercicio 1.7
def explode(lista):
    if lista == []:
        return []
    return lista[0] + explode(lista[1:]) 

#Exercicio 1.8
def substitui(lista, original, novo):
    if lista == []:
        return []
    if lista[0] == original:
        lista[0] = novo
    return [lista[0]] + substitui(lista[1:], original, novo)
    
#Exercicio 1.9
def junta_ordenado(lista1, lista2):
    if lista1 == []:
        return lista2
    elif lista2 == []:
        return lista1
    else:
        if lista1[0] < lista2[0]:
            return [lista1[0]] + junta_ordenado(lista1[1:], lista2)
        else:
            return [lista2[0]] + junta_ordenado(lista1, lista2[1:])

#Exercicio 2.1
def separar(lista):
    if lista == []:
        return [], []
    an, bn = lista[0]                     #ir buscar o primeiro e o segundo elemento do par
    lista_a, lista_b = separar(lista[1:]) #ir ao par seguinte e retirar o primeiro e segundo elemento desse par
    return [an] + lista_a, [bn] + lista_b #juntar os elementos 

#Exercicio 2.2
def remove_e_conta(lista, elem):
    if lista == []:
        return [], 0
    resto_lista, counter = remove_e_conta(lista[1:], elem)
    if lista[0] == elem:
        lista.pop(0)
        return resto_lista, counter + 1
    return [lista[0]] + resto_lista, counter 

#Exercicio 3.1
def cabeca(lista):
    if lista == []:
        return None
    return lista[0]

#Exercicio 3.2
def cauda(lista):
    if lista == [] or len(lista) == 1:
        return None
    return lista[-1]

#Exercicio 3.3
def juntar(l1, l2):
    if l1 == [] or l2 == []:
        return []
    if len(l1) != len(l2):
        return None
    return [(l1[0], l2[0])] + juntar(l1[1:], l2[1:])

#Exercicio 3.4
def menor(lista):
    if lista == []:
        return None
    menor_num = menor(lista[1:])
    if menor_num ==  None or lista[0] < menor_num:
        return lista[0]
    else:
        return menor_num    

#Exercicio 3.6
def max_min(lista):
    if lista == []:
        return None
    
    par_min_max = max_min(lista[1:])
   
    if par_min_max == None:         #caso inicial, o min_ e o max_ sao o primeiro valor da lista
        return lista[0], lista[0]
    
    min_ = lista[0]
    max_ = lista[0]
    
    if par_min_max[0] < min_:
        min_ = par_min_max[0]
    if par_min_max[1] > max_:
        max_ = par_min_max[1]
    return min_, max_
    
    
if __name__ == '__main__':    
    print("Exercicio 1.1: ", comprimento([1,2,2,1]))
    print("Exercicio 1.2: ", soma([1,2,2,1]))
    print("Exercicio 1.3: ", existe([1,2,2,1], 2))
    print("Exercicio 1.4: ", concat([1,2,2,1], [1,2,2,1]))
    print("Exercicio 1.5: ", inverte([1,2,2,1]))
    print("Exercicio 1.6: ", capicua([1,2,2,1]))
    print("Exercicio 1.7: ", explode([[1,2,2,1], [1,2,2,1]]))
    print("Exercicio 1.8: ", substitui([1,2,2,1], 1, 2))
    print("Exercicio 1.9: ", junta_ordenado([1,2,3,4], [2,3,4,5]))

    print("\nExercicio 2.1: ", separar([(1,2), (3,4)]))
    print("Exercicio 2.2: ", remove_e_conta([1,2,2,1,3,4,5,3,2,2,1], 2))

    print("\nExercicio 3.1: ", cabeca([1,2,2,1]))
    print("Exercicio 3.2: ", cauda([1,2,3,4]))
    print("Exercicio 3.3: ", juntar([1,2,3,4], [1,2,3,4]))
    print("Exercicio 3.4: ", menor([1,2,2,1]))
    print("Exercicio 3.6: ", max_min([1,2,3,2,1]))