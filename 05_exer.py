# 5.	Faça um Programa que converta metros para centímetros.

# entendendo problema: 1m = 10cm então, pensando que toda unidade de centimetro será colocada em poonto flutuante
# e que todo prineiro valor será apenas de centimetros
# podemos realizar o seguinte calculo = Valor_inserido pelo usuário * 10
valor_metro = input("Digite o valor de centimetros: ")

conversor_centimeto = float(valor_metro) * 10

print(f"o valor de {valor_metro}m, em centimetos é: {conversor_centimeto}cm ")
