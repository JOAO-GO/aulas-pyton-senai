'''
Titulo: Estudo 'if' usando calculo aumento de salario
Autor: Joao Santos
Data: 26/09/2024
Descrição: 8.	Escreva um programa que leia a idade de um indivíduo e escreva a faixa etária a que pertence, de acordo com a tabela abaixo;
'''
# ctrl + shift + alt + (cima/baico/direita/esquerda)
#entrada de dados
idade = int(input('Qual a faixa Etaria?:'))
#processamento de dados
if idade <= 12: 
    faixa_etaria = 'criança'
elif idade >=13 and faixa_etaria <=17:
    faixa_etaria = 'adolecente'
elif idade >=18 and faixa_etaria <=59: 
    faixa_etaria = 'adulo'
elif idade >= 60: 
    faixa_etaria = 'especialista'
#saida de dados    
print (faixa_etaria)
