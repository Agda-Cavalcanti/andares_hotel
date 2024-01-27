# Precisamos imprimir um número para cada andar de um hotel de 20 andares. 
# Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

#Escreva um código que imprima todos os números exceto o número 13.
#Escreva mais um código que resolva o mesmo problema, mas dessa vez usando o laço de repetição 'while'.

#Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

print("\nESTES SÃO OS ANDARES DO PRÉDIO\n")

for i in range(1,21): # Com o comando FOR
    if i == 13:
        i = i + 1
    else:
        print("Andar", i)


print("\nESTES SÃO OS ANDARES DO PRÉDIO\n")

i = 1
while i <= 20:   # Com o comando WHILE
    if i == 13:
        i = i + 1
        continue
    else:
        print("Andar", i)
    i += 1

print("\nESTES SÃO OS ANDARES DO PRÉDIO EM ORDEM DECRESCENTE \n")

i = 20
while i > 0:     # Com o comando WHILE
    if i == 13:
        i -= 1
        continue
    else:
        print("Andar", i)
    i -= 1

print("\nESTES SÃO OS ANDARES DO PRÉDIO EM ORDEM DECRESCENTE \n")

for i in range(20,0, -1): # Com o comando FOR
    if i == 13:
        i = i - 1
    else:
        print("Andar", i)    
    i -= 1    