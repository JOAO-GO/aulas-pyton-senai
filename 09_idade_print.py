'''
Titulo: Estudo 'if' usando calculo aumento de salario
Autor: Joao Santos
Data: 26/09/2024
Descrição: 8.	Escreva um programa que leia a idade de um indivíduo e escreva a faixa etária a que pertence, de acordo com a tabela abaixo;
'''
# ctrl + shift + alt + (cima/baico/direita/esquerda)
#entrada de dados
faixa_etaria = float(input('Qual a faixa Etaria?:'))
#processamento de dados
if faixa_etaria <= 12:
    print('CRIANÇA')
if faixa_etaria >=13 and faixa_etaria <=17:
    print('ADOLECENTE')
if faixa_etaria >=18 and faixa_etaria <=59:
    print('ADULTO')
if faixa_etaria >= 60:
    print('IDOSO')
