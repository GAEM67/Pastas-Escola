import os
os.system('cls')

def verificar_valor_a(a: int) -> bool:
    if a == 0:
       print("Erro!! Valor inválido")
    return 



delta = 0
while True:
 a = int(input("Digite o valor de a: "))
 b = int(input("Digite o valor de b: "))
 c = int(input("Digite o valor de c: "))

 delta = (b ** 2) - 4 * a * c
 if delta < 0:
    print("Impossivel realizar conta, digite outros valores!!")
 else:
    print(f"Delta = {delta}")

 if delta >= 0: 
    x1 = (-b + delta ** 0.5) / 2 * a
    x2 = (-b - delta ** 0.5) / 2 * a
    print(f"X1 = {x1:.3f} ; X2 = {x2:.3f}")

 else:
    print("Sem Delta para conta") 
    continue