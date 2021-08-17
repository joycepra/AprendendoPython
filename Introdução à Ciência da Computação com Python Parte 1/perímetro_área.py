#Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um 
#quadrado, calcule e imprima (saída de dados) seu perímetro e sua área.

lado= int(input("Digite o valor correspondente ao lado de um quadrado:"))

x= lado*4
y= lado*lado

print("perímetro:", x, "- área:", y)