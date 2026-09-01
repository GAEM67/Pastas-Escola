import os
os.system("cls")

# 1. Retorne o maior entre 3 numeros
# x = maior3n(4, 7, 5) # x valerá 7

def maior3n(n1: float, n2: float, n3: float) -> float:
    maior = n1
    if maior > n2:
        return maior
    elif n2 > n3:
        maior = n2 
        return maior
    elif n3 > maior:
        maior = n3
        return maior
  
# PROGRAMA PRINCIPAL !!
x = maior3n(30, 40, 51)
print (f"Maior numero é: {x}")

# 2. Retorne a somatoria de 5 numeros
# x = maior3n(4, 7, 5, 3, 1) # x valerá 20
def soma5n(n1: float, n2: float, n3: float, n4: float, n5: float) -> float:
    soma_x = n1 + n2 + n3 + n4 + n5
    return soma_x

# PROGRAMA PRINCIPAL !!
soma = soma5n(4, 7, 5, 3, 1)
print (f"Soma total: {soma}")


# 3. Retorne o numero intermediário entre 3 passados
# x = intermediario(4, 2, 9) # x valerá 4
def intermediario(n1: float, n2: float, n3: float) -> float:
    if n1 > n2 and n1 < n3:
        return n1
    elif n2 > n1 and n2 < n3:
        return n2
    elif n3 > n1 and n3 < n2:
        return n3
inter = intermediario(4, 2, 9)
print(f"O intermediario eh: {inter}")   

# PROGRAMA PRINCIPAL !!
intX= intermediario(4, 2, 9)

# 4. Exiba 3 numeros passados em ordem crescente
# ordem_crescente(6,2,3) # exibirá 2 3 6
def cresc(n1: float, n2: float, n3: float) -> float:
    maiorn = n1
    menon = n2
    if menon < n2 and n1 < n3:
        return menon 
    elif maiorn > menon:
        return maiorn
# PROGRAMA PRINCIPAL !!