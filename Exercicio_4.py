char = input("Escolha um caracter: ")
qtd_dgraus = int(input("Escolha a quantidade de degraus: "))

count = 0

while count <= qtd_dgraus:
    print(char * count)
    count +=1       