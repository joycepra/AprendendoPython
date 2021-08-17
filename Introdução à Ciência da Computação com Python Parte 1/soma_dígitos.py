#Escreva um programa que receba um número inteiro na entrada, calcule 
#e imprima a soma dos dígitos deste número na saída

valor = int(input("Digite o valor de n: "))
soma = 0
valor1= valor

while valor1 > 0:
    valor2 = valor1 % 10
    valor1 = valor1 // 10
    soma = soma + valor2
    
print(soma)