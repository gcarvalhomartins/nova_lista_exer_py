# 6.	Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# a fórmula para calcular a área de um raio é: A = pi.r r= ao quadrado 

#primeiro defino minha constante
pi = 3.1415

# agora recebo o raio 
r = input("Digite o raio do circulo: ")
raio_recebido = float(r)
#realizo o calculo
A = pi * raio_recebido **2

print(f"a area do circulo é: {A} ")