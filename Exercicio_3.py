import random as rd

lista = []

num = int(input("Quantos números deseja ter na lista? "))
count = 0;

while count < num:
    n = rd.randint(1,100)
    lista.append(n)
    count += 1

print("\nlista:", lista, "\nMaior número:", max(lista), "\nMenor número:", min(lista))