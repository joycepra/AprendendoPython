#Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, 
#verifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista 
#correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.

def remove_repetidos(lista):
    lista=sorted(lista)
    lista2=[]
    for i in range(len(lista)):
        if lista[i] != lista[i-1]:
            lista2.append(lista[i])
    return(lista2)
           

         
   
            
                
  
    
