#Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas. 

n= int(input("Digite um número inteiro:"))

dig= (n // 10) % 10

print("O dígito das dezenas é", dig)