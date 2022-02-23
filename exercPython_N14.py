'''Exercício 14 - digitar um número, verificar se é par, impar, ou primo e
executar a soma dos números primos entre 1 e o número digitado, conforme opção
desejada'''

# -*- coding: utf-8 -*-

import sys
import os
import time

numero=0
contdiv=0
menu=0
itemMenu=0
somaPrimos=0

def lerNumN(): # opção 1
    try:
        numN = int(input('\nDigite um número inteiro positivo: '))
        while numN < 0:
            numN = int(input('\nNúmero inválido!! Digite um número inteiro positivo: '))
        return numN
    except ValueError:
        print ('Valor inválido!! Deve-se digitar apenas números.')
    time.sleep(5)
    os.system ('cls')
    sys.exit()

def numeroParImpar( numero ): # opção 2
    if numero % 2==0:
        return True
    else:
        return False

def numeroPrimo ( numero ): #opção 3
    contdiv = 0
    for i in range (1,numero+1,1):
        if numero % i == 0:
            contdiv += 1 
    if contdiv == 2:
        return True
    else:
        return False

def somaNumPrimo (numero): #opção 4 - função soma
    somaPrimos=0
    j=1
    for j in range (j, numero+1, 1):
        verificarPrimo=numeroPrimo(j)
        if verificarPrimo== True:
            somaPrimos += j
    return(somaPrimos)       

def exibir(numero,somaPrimos): #opção 4 - processo exibir soma
    somaPrimos=somaNumPrimo(numero)
    print (f'\nA soma dos números primos entre 1 e {numero} é: {somaPrimos}')
    time.sleep(6)
    os.system('cls')
    
def controle():
    menu='\nOpção 1 - Digitar um número inteiro positivo '
    menu+='\nOpção 2 - Verificar se o número é PAR ou é ÍMPAR'
    menu+='\nOpção 3 - Verificar se o número é PRIMO ou não'
    menu+='\nOpção 4 - Exibir a SOMA dos números PRIMOS de 1 até o número digitado'
    menu+='\nOpção 5 - Encerrar o programa\n'
    menu+='\nDigite a opção desejada: '
       
    while True:
        os.system('cls')
        itemmenu = int(input(menu))
        if itemmenu == 1: # ler um número interio
            numero = lerNumN()
            time.sleep(4)
        
        elif itemmenu ==2: # verificar se o número é par ou ímpar
            ehPar = numeroParImpar( numero )
            if ehPar == True:
                print(f'\nO número {numero} é par!')
            else:
                print(f'\nO número {numero} é ímpar!')
            time.sleep(4)
            os.system('cls')

        elif itemmenu ==3: # verificar se o número é primo ou não
            ehPrimo = numeroPrimo( numero )
            if ehPrimo == True:
                print(f'\nO número {numero} é primo!')
            else:
                print(f'\nO número {numero} não é primo!')
            time.sleep(4)
            os.system('cls')
            
        elif itemmenu ==4: # exibir a soma dos números primos de 1 até o número digitado
            exibir(numero,somaPrimos)
            
        elif itemmenu ==5: # finalizar programa
            print ('\nO Programa foi finalizado!!!!')
            time.sleep(4)
            os.system('cls')
            sys.exit()

        else:
            print('\nErro!!! Opção inválida!!!')
            time.sleep(4)
            os.system('cls')
           
controle()
