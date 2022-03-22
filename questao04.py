
minutos = int(input("Digite a quantidade de minutos: ").strip())
horas = 0

while minutos >= 60:
    horas += 1
    minutos -= 60

if minutos == 0:
    print(f'\n{horas}h\n')
else:
    print(f'\n{horas}h e {minutos} min\n')