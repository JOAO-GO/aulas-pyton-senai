'''
Titulo: Estudo 'if elif' usando calculo aumento de salario
Autor: Joao Santos
Data: 01/10/2024
Descrição:9.	Faça um programa para exibir a ocupação de um funcionário a partir de seu código de profissão, de acordo com a tabela abaixo;
'''
# ctrl + shift + alt + (cima/baico/direita/esquerda)
#entrada de dados
profissao = int(input('Qual a Profissão?:'))
#processamento de dados
if profissao == 1:
    codigo = 'MATEMATICO'
elif profissao == 2:
    codigo = 'ANALISTA DE SISTEMA'
elif profissao == 3:
    codigo = 'FISICO'
elif profissao == 4:
    codigo = 'ARQUITETO'
elif profissao == 5:
    codigo = 'PILOTO DE AERONAVES'
print (codigo)