import os
os.system('cls')

# + -> Junta as listas na ordem que foram colocadas

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2


# extend() ->Adiciona uma lista no final da outra
os.system('cls')

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista2.extend(lista1)
print(lista1)
print(lista2)
print(lista3)

os.system('cls')
x = 6
y = 5
x = y
print("x =",x,"y =", y)
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1 = l2

print("l1 =", l1, "l2 = ", l2)

l1.append(7)
l2.append (8)

print("l1 =", l1, "l2 = ", l2)

# copy() -> faz uma cópia de uma lista (objeto)

lista1 = [1, 2, 3]
lista2 = lista1.copy()
print (lista1, lista2)

lista1.append(7)
lista2.append(8)

print (lista1, lista2)

# sort() -> ordena uma lista numerica
os.system('cls')
lista = [45, 34, 98, 23, 12, -5]
print (lista)
lista.sort ()
print (lista)
lista.sort (reverse = True)
print (lista)

lista5 = ["Abc", "Rfjeste", "gdgg"]
lista5.sort()
print(lista5)

lista6 = [ 1, 2, 111, 1101]
lista5.sort()
print(lista6)

# reverse() -> Inverte a ordem dos elementos 
os.system('cls')
lista = [4, False, 98.7, "Edson", 12, -5]
print (lista)
lista.reverse()
print(lista)