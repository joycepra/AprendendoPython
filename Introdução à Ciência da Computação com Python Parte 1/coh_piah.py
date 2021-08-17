import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def calcula_assinatura(textos):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    regex = r"(?<!\d)[.,;:](?!\d)"

    texto_no_punctuations = re.sub(regex,'',textos)
    
    palavras=separa_palavras(texto_no_punctuations)

    sum_pal=0    
    for i in range(len(palavras)):
        sum_pal = sum_pal + len(palavras[i])

    tam_medio_pal= sum_pal / len(palavras)

    type_token= n_palavras_diferentes(palavras)/len(palavras)

    Hapax_Legomana= n_palavras_unicas(palavras)/len(palavras)

    sentencas= separa_sentencas(textos)

    sum_car_sent = 0
    for j in range(len(sentencas)):
        sum_car_sent = sum_car_sent + (len(sentencas[j]))

    tam_medio_sent= sum_car_sent / len(sentencas)

    sum_n_frase = 0
    sum_car_frase = 0
    for k in range(len(sentencas)):
        frases= separa_frases(sentencas[k])
        sum_n_frase = sum_n_frase + len(frases)
        for m in range(len(frases)):
            sum_car_frase = sum_car_frase + (len(frases[m]))

    complexidade= sum_n_frase / len(sentencas)

    tam_medio_frase = sum_car_frase / sum_n_frase

    return(tam_medio_pal,type_token, Hapax_Legomana, tam_medio_sent, complexidade, tam_medio_frase)


def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    sum=0
    for m in range(len(as_a)):
        diferenca= abs(as_a[m] - as_b[m])
        sum = sum + diferenca
        sim = sum / 6
        
    return(sim)


def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    Assinaturas= []
    for i in range(len(textos)):
        Assinaturas.append(calcula_assinatura(textos[i]))

    similaridades= []
    for t in range(len(Assinaturas)):
        similaridades.append(compara_assinatura(Assinaturas[t],ass_cp))

    menor = similaridades[0]
    pos = 1
    for n in range(len(similaridades)):
        if similaridades[n] < menor:
            menor = similaridades[n]
            pos = n + 1     
    print ("O autor do texto", pos, "está infectado com COH-PIAH")
    return(pos)
    
     
  
def main():

    ass_cp = le_assinatura()

    textos = le_textos()

    avalia_textos(textos, ass_cp)

main()

 


    
