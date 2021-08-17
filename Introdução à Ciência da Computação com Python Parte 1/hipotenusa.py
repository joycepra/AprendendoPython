# Escreva uma função soma_hipotenusas que receba como parâmetro um número inteiro positivo 
#n e devolva a soma de todos os inteiros entre 1 e n que são comprimento da hipotenusa de algum 
#triângulo retângulo com catetos inteiros. 

def é_hipotenusa(n):
    i=1
    j=1
    while i <= n:
        while j <= n:
            if (n * n) == (i * i) + (j * j):
                return True
            else:
                j = j + 1
        j = 1
        i = i + 1    

def soma_hipotenusas(n):
    i=1
    z=0
    while i <= n:
        if é_hipotenusa(i)== True:
            z = z + i
            i = i + 1
        else:
            z = z
            i = i + 1
    return(z)
            
            
        
