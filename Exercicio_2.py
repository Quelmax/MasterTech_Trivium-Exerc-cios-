dic = {
    1 : 'Domingo',
    2 : 'Segunda',
    3 : 'Terça',
    4 : 'Quarta',
    5 : 'Quinta',
    6 : 'Sexta',
    7 : 'Sabádo'
}

num = int(input("Escolha um número de 1 a 7: "))

if num > 0 and num <= 7:
    print('\nNúmero  ','Dia da Semana' )
    print(' ', num, '       ',   dic[num])