# 12.	Tendo como dados de entrada a altura de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

get_altura = input("Digite sua Altura: ")
calc_weigth = (72.7 * float(get_altura) - 58)
print(f"seu peso ideal: {calc_weigth} Kg")

