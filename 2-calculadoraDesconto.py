"""2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes."""

produto = "Camiseta"
preco = 50.00
desconto = 0.2

valorDesconto = preco * desconto
valorFinal = preco - valorDesconto


print(f"Valor final do produto: {produto}, com desconto de 20% que equivalente a R$ {valorDesconto:.2f}, é de R$ {valorFinal:.2f}")