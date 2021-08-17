#recebe como argumento um número inteiro maior ou igual a 2  
#devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).


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

    

def n_primos(x):
    fator=2
    n=1
    while x > 2:
        while éPrimo(x)==False:
            x = x - 1   
        n = n + 1
        x = x -1
    return(n)
            
