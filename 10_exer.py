# 10.Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

receber_temperatura = input("Digite uma temperatura em °C: ")

converter_em_fahrenheit =  (int(receber_temperatura) * 1.8 + 32) 

print(f"o valor de °C:{receber_temperatura} em fahrenheit é °F:{converter_em_fahrenheit}")
