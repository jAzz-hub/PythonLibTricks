import datetime

#Mostrando idade em meses e anos

#Dados do usuário:
print('====BirthDate====')
dia=int(input('Dia: '))
mês=int(input('Mês: '))
Ano=int(input('Ano: '))

#Dados do tempo real:
now=datetime.datetime.now()

#Filtrando os dados de agora:
dayN=now.day
monthN=now.month
yearN=now.year

#Montando as variáveis completas de cada dado:
Today=datetime.date(yearN,monthN,dayN)
Bfday=datetime.date(Ano,mês,dia)

#desconstruindo as variáveis para subtração:
td=Today.year
tdm=Today.month

bfd=Bfday.year
bfdm=Bfday.month

#Subtraindo Anos e meses:
ageY=(td-bfd)
ageM=tdm-bfdm


print(ageY)
print(ageM)

print(f'{dayN}/{monthN}/{yearN}')
