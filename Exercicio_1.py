import datetime as dt

def calcular_dias(d,m,a):
    user_date = dt.date(year=a, month=m, day=d)
    tday_date = dt.date.today()
    result =  user_date - tday_date
    return result

dia = int(input("Digite um dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

res = calcular_dias(dia,mes,ano)

print(res, type(res))
