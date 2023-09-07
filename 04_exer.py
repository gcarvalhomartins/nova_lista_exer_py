# 4.	Faça um Programa que peça as 4 notas bimestrais e mostre a média.
primeira_nota = input("Digite a nota do primeiro Bimestre: ")
segunda_nota = input("Digite a nota do Segundo Bimestres: ")
terceira_nota = input("Digite a nota do Terceiro Bimestres: ")
quarta_nota = input("Digite a nota do Quarto Bimestres: ")

media = (float(primeira_nota) + float(segunda_nota) + float(terceira_nota) + float(quarta_nota)) / 4

print(f"Sua Média é: {media}")
