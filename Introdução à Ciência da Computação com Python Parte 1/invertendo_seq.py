
n=1
seq= []
while n != 0:
    n= int(input("Digite o número: "))
    seq.append(n)
    x=len(seq)- 2

while x >= 0:
    print(seq[x])
    x = x - 1


