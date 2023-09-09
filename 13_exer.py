# 13.	Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
# o	Para homens: (72.7*h) - 58
# o	Para mulheres: (62.1*h) - 44.7

print("Você é Home ou Mulher ?")
print("Digite 1 - Para Homem")
print("Digite 2 - Para Mulher")
get_gener = input("Digite aqui: ")
get_heigth = input("Digite sua Altura: ")

peso_man = (72.7 * float(get_heigth) - 58)
peso_woman = (62.1 * float(get_heigth) - 44.7)

match get_gener:
    case "1":
         print(f"Peso ideal para Homem é:{peso_man}")
    case "2":
         print(f"Peso ideal para Mulheres é:{peso_woman}")

