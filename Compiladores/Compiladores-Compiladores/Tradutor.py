# -*- coding: utf-8 -*-
"""
@author: andre
"""
import tabelaSimbolos
    
class token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor
    
def nextToken():
    global entrada
    global lookahead
    global contador
    global EOF
    global saida
    
    contador = contador+1

    if contador == len(entrada):
        EOF = True
        return EOF
    else:
        if entrada[contador]!=' ':
            return entrada[contador]
        else:
            return nextToken()
            
            
def match(char):
    global entrada
    global lookahead
    global contador

    if lookahead == char:
       lookahead = nextToken()

    else:
       s = "Found " + lookahead + " but expected " +char 
       print(s)

def operacao2():
    global lookahead
    global contador
    global saida
    global resultado 
    global operador
    if lookahead == '*':
        match('*') 
        digito()
        A = resultado.pop(len(resultado)-1)
        B = resultado.pop(len(resultado)-1)
        operador.valor = A.valor*B.valor
        operador.tipo = A.tipo
        resultado.append(operador)
        saida = saida.replace(saida, saida+'*') 
        operacao2()
        
    elif lookahead == '/':
        match('/')
        digito()
        A = resultado.pop(len(resultado)-1)
        B = resultado.pop(len(resultado)-1)
        operador.valor = B.valor/A.valor
        operador.tipo = A.tipo
        resultado.append(operador)
        saida = saida.replace(saida, saida+'/')
        operacao2()


    else:
        return 
     
def termos():
    digito()
    operacao2()
 

    
    
def digito() :
    global lookahead
    global contador
    global saida
    global total
    t2 = token('', None)
    total = 0
    while tabelaSimbolos.NUMBER.__contains__(lookahead):
        if lookahead == '0':
            match('0')
            saida =saida.replace(saida, saida+'0')
            t2.tipo = tabelaSimbolos.varType('0')
            total = tabelaSimbolos.varValue(total, 0)
        elif lookahead == '1':
            match('1')
            saida =saida.replace(saida, saida+'1')
            t2.tipo = tabelaSimbolos.varType('1')
            total = tabelaSimbolos.varValue(total ,1)
        elif lookahead == '2':
            match('2')
            saida =saida.replace(saida, saida+'2')
            t2.tipo = tabelaSimbolos.varType('2')        
            total = tabelaSimbolos.varValue(total ,2)
        elif lookahead == '3':
            match('3')
            saida =saida.replace(saida, saida+'3')
            t2.tipo = tabelaSimbolos.varType('3')
            total = tabelaSimbolos.varValue(total ,3)
        elif lookahead == '4':
            match('4')
            saida =saida.replace(saida, saida+'4')
            t2.tipo = tabelaSimbolos.varType('4')
            total = tabelaSimbolos.varValue(total ,4)
        elif lookahead == '5':
            match('5')
            saida =saida.replace(saida, saida+'5')
            t2.tipo = tabelaSimbolos.varType('5')
            total = tabelaSimbolos.varValue(total ,5)
        elif lookahead == '6':
            match('6')
            saida =saida.replace(saida, saida+'6')
            t2.tipo = tabelaSimbolos.varType('6')
            total= tabelaSimbolos.varValue(total ,6)
        elif lookahead == '7':
            match('7')
            saida =saida.replace(saida, saida+'7')
            t2.tipo = tabelaSimbolos.varType('7')
            total = tabelaSimbolos.varValue(total ,7)
        elif lookahead == '8':
            match('8')
            saida =saida.replace(saida, saida+'8')
            t2.tipo = tabelaSimbolos.varType('8')
            total = tabelaSimbolos.varValue(total ,8)
        elif lookahead == '9':
            match('9')
            saida =saida.replace(saida, saida+'9')
            t2.tipo = tabelaSimbolos.varType('9')
            total = tabelaSimbolos.varValue(total ,9)
            
        else :
            print('Erro, esperava-se Dígito em '+contador )
        
    t2.valor = total  
    resultado.append(t2)
    
    total = 0
        
def operacao1():
    global lookahead
    global contador
    global saida
    global resultado 
    global EOF
    if lookahead =='-':
        match('-')
        termos()
        A = resultado.pop(len(resultado)-1)
        B = resultado.pop(len(resultado)-1)
        operador.valor = B.valor-A.valor
        operador.tipo = A.tipo
        resultado.append(operador)
        saida =saida.replace(saida, saida+'-')
        operacao1()
    elif lookahead =='+':
        match('+')
        termos()
        A = resultado.pop(len(resultado)-1)
        B = resultado.pop(len(resultado)-1)
        operador.valor = A.valor+B.valor
        operador.tipo = A.tipo
        resultado.append(operador)
        saida =saida.replace(saida, saida+'+')
        operacao1()

    elif lookahead == EOF:
       """ print ('Correto') """     
    else:
        print('SINTAX ERROR')

def expr():
    termos()
    operacao1()

        
if __name__=='__main__':
    global EOF 
    EOF = False
    t = token('', None)
    global resultado
    global operador
    operador = token('',None)
    resultado = []
    entrada = input()
    saida =''
    contador = -1
    while contador != len(entrada) :
        if(contador <= len(entrada)):
            lookahead = nextToken()
            expr()        
    print (saida)
    for item in resultado:
            print (item.valor,item.tipo)

         

            