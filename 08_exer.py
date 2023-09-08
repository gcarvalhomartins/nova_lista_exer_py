# 8.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

receber_salario = input("Digite quanto ganha por Hora: ")
receber_horas_trabalhadas = input("Digite quantas horas trabalha por MÊS: ")

calcular_salario = float(receber_salario) * float(receber_horas_trabalhadas)

print(f"Seu salário é: R${calcular_salario} ")
