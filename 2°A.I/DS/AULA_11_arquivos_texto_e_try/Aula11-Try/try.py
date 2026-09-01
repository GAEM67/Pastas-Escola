import os
os.system('cls')
print("teste")



try: # rotina a ser executada
    n1 = int(input("Numero 1: "))
    n2 = int(input("Numero 2: "))
    resp = n1/n2
    
except ValueError:# erro de valor
    print("\033[1;33m"+"Digite um valor numérico!"  + "\033[0m")
except ZeroDivisionError: # erro de divisão por zero
    print("\033[1;31m"+"Não há divisão por zero!!" + "\033[0m")
except: # encontra os demais erros
    print("\033[1;34m" + "Erro! Chame a NASA" + "\033[0m")
else: # executa se não há falha
    print("\033[1;36m" + f"Resultado de divisão: {resp}" + "\033[0m")
finally: # executa se houver falha ou não
    print("\033[1;30m" + "Obrigado por usar o nosso sistema" + "\033[0m")