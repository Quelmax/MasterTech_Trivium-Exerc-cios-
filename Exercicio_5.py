import math

pi = math.pi

i = 0

while i == 0:
  try:
      r = float(input('Digite um raio: '))
  except:
      print ('\nVocê não digitou um número, por favor entre com um número\n')
  else: 
    i = 1
  
area = pi * (r * r)
comp = 2 * (pi * r)

print("\nA area de uma circunferência com raio",r, "é de", area, ",e o comprimento é de {}.".format(comp))


