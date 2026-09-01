import os
os.system("cls")

# 01
def cont_carac(frase):
    return len(frase)

# 02
def contar_vogais(frase):
    vogais = "aeiouAEIOUáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙãÃÕõâÂêÊÎîôÔÛû"
    contador = 0
    for letra in frase:
        if letra in vogais:
            contador += 1
    return contador

# 03
def qtd_frase (frase):
    palavra = frase.split()
    return len(palavra)

# 04 
def trocar_digitos (frase):
    nova = ""
    for c in frase:
        if c >= '0' and c <= '9':
            nova += "?"
        else:
            nova += c
    return nova

# 05 
def revert (frase):
    return frase[::-1]

# 06
def pegar_range(frase):
    while True:
        inicio = int(input("Digite o início: "))
        fim = int(input("Digite o fim: "))

        if inicio < 0 or fim > len(frase) or inicio >= fim:
            print("Range inválido! Tente novamente.")
        else:
            print("Resultado:", frase[inicio:fim])
            break

# 07
def palavras_curta(frase):
    lista = []
    palavras = frase.split()

    for p in palavras:
        if len(p) <= 4:
            lista.append(p)

    return lista



# PROGRAMA PRINCIPAL

frase = input("Digite uma frase: ")

print (f"Quantidade de caracteres eh: ", cont_carac(frase))
print (f"Quantidade de vogais eh: ", contar_vogais(frase))
print (f"Quantidade de palavras eh: ", qtd_frase(frase))
print (f"Troca de Digitos: ", trocar_digitos(frase))
print (f"Frase inversa: ", revert(frase))
pegar_range(frase)

print("6. Palavras com até 4 letras:", palavras_curta(frase))
