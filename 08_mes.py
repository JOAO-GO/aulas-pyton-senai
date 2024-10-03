'''
Titulo: Estudo 'if' usando calculo aumento de salario
Autor: Joao Santos
Data: 26/09/2024
Descrição: 7.	Faça um programa que receba o mês em número e apresente-o por extenso.
'''
# ctrl + shift + alt + (cima/baico/direita/esquerda)
#entrada de dados
mes = int(input('Qual o mes?:'))
#processamento de dados
if mes == 1:
    print('JANEIRO')
if mes == 2:
    print('FEVEREIRO')
if mes == 3:
    print('MARÇO')
if mes == 4:
    print('ABRIL')
if mes == 5:
    print('MAIO')
if mes ==  6:
    print('JUNHO')
if mes == 7:
    print('JULHO')
if mes == 8:
    print('AGOSTO')
if mes == 9:
    print('SETEMBRO')
if mes == 10:
    print('OUTUBRO')
if mes == 11:
    print('NOVEMBRO')
if mes == 12:
    print('DEZEMBRO')
if mes > 12 or mes < 1:
    print('MES NAO EXISTE')
