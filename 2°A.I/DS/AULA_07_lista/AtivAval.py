import os
os.system('cls')

#Erick Martis e Gustavo Andrews 2ºAI

# Pedir um valor ao usuário 

lista1 = [34, 78, 56, 34, 12]
print (lista1)
while True:
    valor = int(input("Digite um valor: "))
    for i in range (0, 6, 1):
     if valor == lista1[i]:
        print ("1 ocorrência")
     else:
        print("0 ocorrências")

        


    
    
    
    
   
      

'''for i in range (0, 6, 1):
        if valor == lista1[i]:
            print ("Existe!!")
        else:'''