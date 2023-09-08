# 7.	Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

# lembrando que estamos na linha de pensamento do quadrado de lados iguais. 
# a formula é: A = L²

receber_lados = input("Digite a área do quadrado: ")
area = int(receber_lados)**2
dobro_area = int(receber_lados)**2 * 2
print(f"a área do quadrado é: {area}, e o dobro é: {dobro_area}")


