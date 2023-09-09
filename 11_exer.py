# 11.	Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# 1.	o produto do dobro do primeiro com metade do segundo .
# 2.	a soma do triplo do primeiro com o terceiro.
# 3.	o terceiro elevado ao cubo.

# 1. o produto do dobro do primeiro = multiplicar o primeiro numero por 2
# a metdade do segundo = dividir o segundo número por 2
# depois realizar a soma. 

receber_primeiro_valor = input("Digite o Primeiro Valor: ")
pri_valor = int(receber_primeiro_valor)

receber_segundo_valor = input("Digite o segundo valor: ")
segu_valor = int(receber_segundo_valor)

pri_resultado = (pri_valor * 2) + ( segu_valor / 2)


#vou logo resolver o terceiro 
receber_terceiro_valor = input("Digite o terceiro valor: ")
terc_elevado_ao_cubo = float(receber_terceiro_valor) **3


segun_resultado = (pri_valor * 3) + terc_elevado_ao_cubo


print(f"Os resultados são")
print(f"Primeiro Resultado:{pri_resultado}")
print(f"Segundo Resultado:{segun_resultado}")
print(f"Terceiro Resultado:{terc_elevado_ao_cubo}")



