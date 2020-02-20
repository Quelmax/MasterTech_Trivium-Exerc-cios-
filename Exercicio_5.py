import math

pi = math.pi

def entrada_usuario():
    i = 0
    while i == 0:
        try:
            r = float(input('Digite um raio: '))
        except ValueError:
            print ('\nVocê não digitou um número, por favor entre com um número\n')
        else: 
            i = 1
    return r

def calculo_area(r):
    area = pi * (r * r)
    return area

def calculo_comprimento(r):
    comp = 2 * (pi * r)
    return comp

r = entrada_usuario()
area = calculo_area(r)
comp = calculo_comprimento(r)
print("\nA area de uma circunferência com raio",r, "é de", area, ",e o comprimento é de {}.".format(comp))
