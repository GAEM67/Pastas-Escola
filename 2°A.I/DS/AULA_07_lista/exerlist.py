import os
os.system('cls')

# Pedir para o usuario preencher uma lista.
lista = []

while True:
    elem = int(input("Digite um numero para a lista: "))
    if elem == "0":
        lista.append(elem) 
    else:
        print (lista)
        break

print ("Lista original: ", lista)

listacresc = lista.copy()
listacresc.sort()
print ("Ordem crescente: ", lista)

listadecresc = lista.copy()
listadecresc.sort (reverse = True)
print("Ordem decrescente: ", listadecresc)

listarevert = lista.copy()
listarevert.reverse ()
print("Ordem reversa: ", listarevert)