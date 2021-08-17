# recebe dois números inteiros correspondentes à largura e à altura de um retângulo,respectivamente.
# Imprimi, usando repetições encaixadas, uma cadeia de caracteres que represente o retângulo
# informado com caracteres '#' na saída.

larg= int(input("Digite a largura do retângulo: "))
alt= int(input("Digite a altura do retângulo: "))

x=1
y=1
while y <= alt:
    while x <= larg:
        if x > 1 and x < larg and y != 1 and y != alt:
            print(" ", end ="")
        else:    
            print("#", end= "")
        x = x + 1 
    print()
    y = y + 1
    x = 1

