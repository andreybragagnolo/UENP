# -*- coding: utf-8 -*-
"""
@author: andre
"""

import Lexema
from Token import nextToken
import Token
    

def match(char):
    global entrada
    global leitorPrevio
    global contador
    t = Token("", None, None)
    if leitorPrevio == char:
       leitorPrevio = t.nextToken()

    else:
       s = "Found " + leitorPrevio + " but expected " +char 
       print(s)

def operacaoComPrec():
    global leitorPrevio
    global contador
    global saida
    global resultado 
    global operador
    if leitorPrevio == '*':
        match('*') 
        digito()
        A = resultado.pop(len(resultado)-1)
        B = resultado.pop(len(resultado)-1)
        operador.valor = A.valor*B.valor
        operador.tipo = A.tipo
        resultado.append(operador)
        saida = saida.replace(saida, saida+'*') 
        operacaoComPrec()
        
    elif leitorPrevio == '/':
        match('/')
        digito()
        A = resultado.pop(len(resultado)-1)
        B = resultado.pop(len(resultado)-1)
        operador.valor = B.valor/A.valor
        operador.tipo = A.tipo
        resultado.append(operador)
        saida = saida.replace(saida, saida+'/')
        operacaoComPrec()

    else:
        return 
     
def termos():
    digito()
    operacaoComPrec()
 

    
    
def digito() :
    global leitorPrevio
    global contador
    global saida
    global total
    t2 = Token()
    total = 0
    while Lexema.NUMBER.__contains__(leitorPrevio):
        if leitorPrevio == '0':
            match('0')
            saida =saida.replace(saida, saida+'0')
            t2.tipo = Lexema.varType('0')
            total = Lexema.varValue(total, 0)
        elif leitorPrevio == '1':
            match('1')
            saida =saida.replace(saida, saida+'1')
            t2.tipo = Lexema.varType('1')
            total = Lexema.varValue(total ,1)
        elif leitorPrevio == '2':
            match('2')
            saida =saida.replace(saida, saida+'2')
            t2.tipo = Lexema.varType('2')        
            total = Lexema.varValue(total ,2)
        elif leitorPrevio == '3':
            match('3')
            saida =saida.replace(saida, saida+'3')
            t2.tipo = Lexema.varType('3')
            total = Lexema.varValue(total ,3)
        elif leitorPrevio == '4':
            match('4')
            saida =saida.replace(saida, saida+'4')
            t2.tipo = Lexema.varType('4')
            total = Lexema.varValue(total ,4)
        elif leitorPrevio == '5':
            match('5')
            saida =saida.replace(saida, saida+'5')
            t2.tipo = Lexema.varType('5')
            total = Lexema.varValue(total ,5)
        elif leitorPrevio == '6':
            match('6')
            saida =saida.replace(saida, saida+'6')
            t2.tipo = Lexema.varType('6')
            total= Lexema.varValue(total ,6)
        elif leitorPrevio == '7':
            match('7')
            saida =saida.replace(saida, saida+'7')
            t2.tipo = Lexema.varType('7')
            total = Lexema.varValue(total ,7)
        elif leitorPrevio == '8':
            match('8')
            saida =saida.replace(saida, saida+'8')
            t2.tipo = Lexema.varType('8')
            total = Lexema.varValue(total ,8)
        elif leitorPrevio == '9':
            match('9')
            saida =saida.replace(saida, saida+'9')
            t2.tipo = Lexema.varType('9')
            total = Lexema.varValue(total ,9)
            
        else :
            print('Erro, esperava-se Dígito em '+contador )
        
    t2.valor = total  
    resultado.append(t2)
    
    total = 0
        
def operacaoSemPrec():
    global leitorPrevio
    global contador
    global saida
    global resultado 
    global EOF
    if leitorPrevio =='-':
        match('-')
        termos()
        A = resultado.pop(len(resultado)-1)
        B = resultado.pop(len(resultado)-1)
        operador.valor = B.valor-A.valor
        operador.tipo = A.tipo
        resultado.append(operador)
        saida =saida.replace(saida, saida+'-')
        operacaoSemPrec()
    elif leitorPrevio =='+':
        match('+')
        termos()
        A = resultado.pop(len(resultado)-1)
        B = resultado.pop(len(resultado)-1)
        operador.valor = A.valor+B.valor
        operador.tipo = A.tipo
        resultado.append(operador)
        saida =saida.replace(saida, saida+'+')
        operacaoSemPrec()

    elif leitorPrevio == EOF:
       """ print ('Correto') """     
    else:
        print('SINTAX ERROR')

def expr():
    termos()
    operacaoSemPrec()

def var():
    global leitorPrevio
    global tabelaDeSimbolos
    match()
    entrada = None
    t =  Token("", None, None)

    while (leitorPrevio!=' '):
        entrada = entrada.replace(entrada, entrada+""+leitorPrevio)
        leitorPrevio.nextToken()
    leitorPrevio.nextToken()
    if leitorPrevio == '=':
        t.valor = expr()
        t.nome = entrada
    tabelaDeSimbolos.append(t)

        
def atribuicao():
    var()
    expr()

def EOL():
    global contadorLinhas
    global leitorPrevio
    if leitorPrevio==';':
        match(";")
        contadorLinhas +=1    
    else:
        print("Erro, esperava-se ; na posição:{} da linha {}".format(contador,contadorLinhas))


def openPar():
    global leitorPrevio
    global tabela
    if leitorPrevio == '(':
        match('(')
        tabela.append('(')    
        

def closePar():
    global leitorPrevio
    global tabela
    if leitorPrevio == ')':
        match(')')
        tabela.pop('(')

def impressao():
    openPar() 
    var() 
    closePar()

def stmt():
    global leitorPrevio
    valorEntrada = ""
    t = Token("", None,None)

    while (leitorPrevio!=' '):
        leitorPrevio = str(leitorPrevio)
        print(type(leitorPrevio))
        valorEntrada = valorEntrada+leitorPrevio
        leitorPrevio = t.nextToken()
    
    if Lexema.KEYWORD.__contains__(entrada):
        impressao() 
    else:
        atribuicao()

def programa():
    stmt()
    EOL() 
    linhas()

def linhas():
    programa()





if __name__=='__main__':
    global EOF
    global contadorLinha
    global tabela
    global tabelaDeSimbolos 
    contadorLinha = 0
    tabelaDeSimbolos = []
    tabela = []
    EOF = False
    t = Token()
    global resultado
    global operador
    operador = Token('',None,None)
    resultado = []
    entrada = input()
    saida =''
    contador = -1
    global leitorPrevio
    leitorPrevio = ""
    while contador != len(entrada) :
        if(contador <= len(entrada)):
            leitorPrevio = operador.nextToken()
            leitorPrevio = str(leitorPrevio)
            print(type(leitorPrevio))
            programa()        
    print (saida)


         

            
