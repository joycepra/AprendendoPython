#Reescreva o programa contaSegundos para imprimir também a quantidade de dias, ou seja, 
#faça um programa em Python que, dada a quantidade de segundos, "quebre" esse valor em dias, 
#horas, minutos e segundos. A saída deve estar no formato: a dias, b horas, c minutos e d segundos.

segundos= int(input("Por favor, entre com o número de segundos que deseja converter:"))

dias= segundos//(24*(60*60))
horas= (segundos - (dias*24*60*60))//(60*60)
minutos= (segundos - (dias*24*60*60)- (horas*60*60))//60
seg= (segundos - (dias*24*60*60)- (horas*60*60) - (minutos*60))


print(dias, "dias,", horas, "horas,", minutos, "minutos e", seg, "segundos.")