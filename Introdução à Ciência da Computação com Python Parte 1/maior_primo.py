#Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro 
# e devolve o maior número primo menor ou igual ao número passado à função.

def éPrimo(x):
    i = 2
    if x == 2:
        return True
    
    while x % i != 0 and i <= x/2:
        i = i + 1
    if x % i == 0:
        return False    
    else:
        return True

def maior_primo(x):
    while x > 2 and éPrimo(x) == False:
        x = x - 1   
    return (x)