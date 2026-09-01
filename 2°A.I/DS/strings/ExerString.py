import os
os.system("cls")

# 1. peça para o usuário digitar uma frase etrnasforme todas as vogais 
# minusculas me maiúsculas
"""
frase = str(input(" "))
frase = (frase.replace("a", "A"))
frase = (frase.replace("é", "É"))
frase = (frase.replace("e", "E"))
frase = (frase.replace("i", "I"))
frase = (frase.replace("o", "O"))
frase = (frase.replace("u", "U"))
print (frase)"""

# 2. dada uma frase, mostre quantos caracteres e quantas palavras existem
# nesta frase
"""
frase2 = str(input(" "))

qtd = len(frase2)
print(f"a frase tem {qtd} caracteres!!")
frase2_lista = frase2.split()
qtd2 = len(frase2_lista)
print (f"Sua frase tem {qtd2} palavras!!")"""

# 3. dada uma frase conte quantos digitos e quantas letras existem nesta frase

frase3 = str(input(" "))
l = 0
dig = 0
alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
for c in frase3:
    if c in alfabeto:
        l = l + 1
    elif c in numeros:
        dig += 1
print(f"quantidade de letras:{l}")
print(f"quantidade de digitos:{dig}")

# 4. dada uma frase e um conteúdo, informe se este conteúdo existe na frase.
frase4 = str(input(" "))


