'''1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
'''

reais = 100.00
dolar = 5.20
euro = 6.15
valorDolar = reais / dolar
valorEuro = reais / euro

print( f"Valor convertido de Reais para Dolar é de US$ {valorDolar:.2f}")
print(f"Valor convertido de Reais para Euro é de € {valorEuro:.2f}")