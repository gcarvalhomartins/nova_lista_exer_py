# 16.Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros 
# quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total

# primeira coisa, pedir metros quadrados.(ok)
# 1 litro de tinta é = a 3 metros 
# a loja só vende latas de 18 litros, que custam R$80,00
# ou seja, se eu colocar 3 metros, tem que dar o resultado de
# uma lata de tinta de 18 litros, que custa 80,00
# 3 metros é = 1 lata de tinta, no valor de 80,00
# 3 metros quadrados é igual a 9 metros.
# 9 metros é igual a 3 litros de tinta. 
# o objetivo: a quantidade de latas a serem compradas e o preço total. 

# pegar o valor em metros quadrados e dividir por 3 metros, vai dar o resultado da
# quantidade de litros de tinta 

receber_metros_quadrados = input("Digite os metros quadrados: ")
metros_quadrados = float(receber_metros_quadrados)

# Calcula a quantidade de litros necessários
litros_necessarios = metros_quadrados / 3

# Define o tamanho da lata de tinta em litros e o preço por lata
litros_por_lata = 18
preco_por_lata = 80.00

# Calcula a quantidade de latas necessárias
quantidade_latas = litros_necessarios / litros_por_lata

# Arredonda para cima para garantir que você compre latas suficientes
import math
quantidade_latas = math.ceil(quantidade_latas)

# Calcula o preço total
preco_total = quantidade_latas * preco_por_lata

# Exibe o resultado
print(f"Quantidade de latas necessárias: {quantidade_latas}")
print(f"Preço total: R${preco_total:.2f}")