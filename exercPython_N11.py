'''Exercício 11 - Digitado um valor para montante e período em meses, obter
o capital que foi investido e o valor do juros recebido a uma taxa de 5%
ao mês'''

#-*- coding: utf-8 -*-
import os
import sys
import math
import time

def lerMontante():
    mont=float(input('\nDigite o valor do Montante: R$ '))
    return mont

def lerPeriodo():
    per=float(input('\nDigite o período da aplicação (meses): '))
    return per

def calValorCapital(mont,per):    
    cap=mont/(1+0.05*per)
    return cap

def calJuros(cap,per):    
    juros=cap*0.05*per
    return juros
    
def exibir (mont,per,cap,juros):  
    print(f'\nPara obter o Montante de R${mont:8.2f}, ao final de um período de {per} meses')
    print(f'a uma taxa de juros de 5% ao mês, foi aplicado o Capital de R${cap:8.2f},')
    print(f'que rendeu R${juros:5.2f}.')
    time.sleep(6)
    os.system('cls')
     
def controle():
     menu='\n### Programa para calculo de capital investido e respectivo juros ###\n'
     menu+='\nOpção 1 - Leitura do valor do Montante e do período'
     menu+='\nOpção 2 - Cálculo do Capital e do Juros a taxa de 5% ao mês'
     menu+='\nOpção 3 - Exibir Montante, Capital, Juros, Taxa e Período'
     menu+='\nOpção 4 - Sair do programa\n'
     menu+='\nDigite a opção desejada: '

     while True:
      itemMenu=int(input(menu))
        
      if itemMenu==1:
           mont = lerMontante()
           per=lerPeriodo()
                                            
      elif itemMenu==2:
           cap=calValorCapital(mont,per)
           juros=calJuros(cap,per)
           print('\n### CALCULANDO ###')
           time.sleep(6)
           os.system('cls')

      elif itemMenu==3:
           exibir(mont,per,cap,juros)
           
      elif itemMenu==4:
           print('O programa foi finalizado!!!')
           time.sleep(6)
           os.system('cls')
           break

      else:
           print('Selecione uma opção válida!!!')
           time.sleep(6)
           os.system('cls')

controle()
