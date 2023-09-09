# 14.	João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos 
# além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.

# 50 quilos é o limite, o excesso disso é multa de = R$4,00
# ele quer uma variavel peso que verifique o peso e o excesso
# na variavel multa, o valor que ele ira pagar

# 1. verificar o limite de peso, que é 50
# 2. calcular o excesso do peso.

get_peso_peixe = input("Digite o peso do Peixe: ")
peso_peixe = float(get_peso_peixe)

multa = 4.00
limite = 50.00



if peso_peixe > limite:
    excesso = peso_peixe - limite
    valor_multa = excesso * multa
    print(f"O valor da multa é: R$ {valor_multa}")

