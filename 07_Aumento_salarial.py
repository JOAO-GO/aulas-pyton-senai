'''
Titulo: Estudo 'if' usando calculo aumento de salario
Autor: Joao Santos
Data: 26/09/2024
Descrição: 6.	Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se que:
Salário < R$ 1000,00 aumento de 25%.
Salário >= R$ 1000,00 e < R$ 2000,00 aumento de 15%.
Salário >= R$ 2000,00 aumento de 10%.
'''
# ctrl + shift + alt + (cima/baico/direita/esquerda)
#entrada de dados
salario = int(input('Qual o Valor do Salario?:'))
#processamento de dados
if salario < 1000:
    salario_reajuste = salario * 1.25
if salario >= 1000 and salario < 2000:
    reajuste = salario * 0.15
    salario_reajuste = salario + reajuste
if salario >= 2000:
    salario_reajuste = salario  * 1.1
#saida de dados
print('Seu Novo Salario:', salario_reajuste)
