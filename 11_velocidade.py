'''
Titulo: Estudo 'if' usando calculo aumento de salario
Autor: Joao Santos
Data: 01/10/2024
Descrição:9.	Faça um programa para exibir a ocupação de um funcionário a partir de seu código de profissão, de acordo com a tabela abaixo;

Escreva um programa que leia a velocidade máxima permitida em uma avenida e velocidade com que o motorista estava dirigindo nela e calcule a multa que uma pessoa vai receber;

Siga a tabela de multas
Velocidade Ultrapassada	Valor da Multa
Até 10 km/h	R$ 50,00
11 a 30 km/h	R$ 100,00
Mais 31 km/h	R$ 200,00
Exemplo: 
	Limite: 50 km/h
	Velocidade: 59 km/h
	Multa: R$ 50,00
'''
# ctrl + shift + alt + (cima/baico/direita/esquerda)
#entrada de dados
velocidade_ultrapassada = int(input('Qual a Profissão?:'))
#processamento de dados

if velocidade_ultrapassada <= 10:
    print('MULTA 50,00')
if velocidade_ultrapassada > 11 and <= 30:
    print('MULTA 100,00')
