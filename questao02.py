
precoProduto = float(input("Digite o preço do produto: R$ ").strip())

# Preço com desconto 
preco_com_desconto = 0.9 *precoProduto


preco_com_desconto = round(preco_com_desconto, 2)


print("O preço do produto com 10 porcento de desconto é igual a: R$",(preco_com_desconto))