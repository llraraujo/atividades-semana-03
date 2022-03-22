
anos = int(input("Digite o tempo de serviço (em Anos): ").strip())

valor_por_ano = int(input("Valor do bônus por ano: R$ ").strip())

bonus = anos * valor_por_ano

print("Bônus de R$ %5.2f" %bonus)