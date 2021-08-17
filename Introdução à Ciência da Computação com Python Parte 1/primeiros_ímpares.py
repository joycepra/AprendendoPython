#Receba um número inteiro positivo na entrada e imprima os n primeiros 
#números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.

n = int(input("Digite o valor de n: "))

i= 0
x= n*2 


while i < x:
    
    impars= i + 1
    print(impars)
    i= i + 2
 
    