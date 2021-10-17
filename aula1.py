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
    if lista1 == [] and lista2 != []:
        return lista2
    elif lista1 != [] and lista2 == []:
        return lista1
    elif lista1 == [] and lista2 == []:
        return []
    else:
        if lista1[0] < lista2[0]:
            return [lista1[-1]] + [lista2[-1]] + junta_ordenado(lista1[:-1], lista2[:-1])
        else:
            return [lista2[-1]] + [lista1[-1]] + junta_ordenado(lista1[:-1], lista2[:-1])

#Exercicio 2.1
def separar(lista):
	pass

#Exercicio 2.2
def remove_e_conta(lista, elem):
	pass

#Exercicio 3.1
def cabeca(lista):
	pass

#Exercicio 3.2
def cauda(lista):
	pass

#Exercicio 3.3
def juntar(l1, l2):
    pass

#Exercicio 3.4
def menor(lista):
	pass

#Exercicio 3.6
def max_min(lista):
	pass

if __name__ == '__main__':
    lista = [1,2,2,1]
    
    print("Exercicio 1.1: ", comprimento(lista))
    print("Exercicio 1.2: ", soma(lista))
    print("Exercicio 1.3: ", existe(lista, 2))
    print("Exercicio 1.4: ", concat(lista, lista))
    print("Exercicio 1.5: ", inverte(lista))
    print("Exercicio 1.6: ", capicua(lista))
    print("Exercicio 1.7: ", explode([lista,lista, lista]))
    print("Exercicio 1.8: ", substitui(lista, 1, 2))
    print("Exercicio 1.9: ", junta_ordenado(lista, lista))

    #print("Exercicio 2.1: ", separar(lista))
    #print("Exercicio 2.2: ", remove_e_conta(lista, 2))

    #print("Exercicio 3.1: ", cabeça(lista))
    #print("Exercicio 3.2: ", cauda(lista))
    #print("Exercicio 3.3: ", juntar(lista, lista))
    #print("Exercicio 3.4: ", menor(lista))
    #print("Exercicio 3.6: ", max_min(lista))
