# 9.Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# o	C = 5 * ((F-32) / 9).

receber_temperatura = input("Digite a temperatura em °F: ")

converter_em_celsius = 5 * ((int(receber_temperatura)-32 ) / 9)

print(f"o Valor em °F é: {receber_temperatura}, convertido em °C é: {converter_em_celsius}")
