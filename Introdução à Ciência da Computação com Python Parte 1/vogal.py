#Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for 
# uma vogal e False se for uma consoante.

def vogal(letra):
    vogal = ['a','e', 'i', 'o', 'u', 'A','E', 'I', 'O', 'U']
    if letra in vogal:
        return True
    else:
        return False
        