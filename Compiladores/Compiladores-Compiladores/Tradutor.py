# -*- coding: utf-8 -*-
"""
@author: andre
"""
import Lexema
    
class token:
    def __init__(self, tipo, valor, nome):
        self.tipo = tipo
        self.valor = valor
        self.nome = nome
    
def nextToken():
    global entrada
    global lookahead
    global contador
    global EOF
    global saida
    
    contador = contador+1

    if contador >= len(entrada):
        EOF = True
        return EOF
    else:
        if entrada[contador]!=' ':
            return entrada[contador]
        else:
            return "|s|"
            
            
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
    global EOF
    global EOL
    global sToken
    global tabelaParenteses
    global pointerVar
    global contadorLinhas
    global tabelaSimbolo
    EOL = False
    operador = token(sToken,None,None)
    while lookahead == '|s|':
        lookahead = nextToken()
    if lookahead ==')':
        tok = token("SYMBOL", ")", "clsPar")
        tabelaSimbolo.append(tok)
        closePar()
    while(lookahead == '|s|'):
        lookahead = nextToken()
    
    if lookahead == '*':
        match('*')
        tok = token("SYMBOL", "*", "OpMult")
        tabelaSimbolo.append(tok)
        while lookahead == '|s|':
            lookahead = nextToken()
        if Lexema.NUMBER.__contains__(lookahead):
            digito()
        else:
            var()
        A = resultado.pop(len(resultado)-1)
        B = resultado.pop(len(resultado)-1)
        operador.valor = A.valor*B.valor
        operador.tipo = A.tipo
        resultado.append(operador)
        saida = saida.replace(saida, saida+'*') 
        operacao2()
        
    elif lookahead == '/':
        match('/')
        tok = token("SYMBOL", "/", "OpDiv")
        tabelaSimbolo.append(tok)
        while lookahead == '|s|':
            lookahead = nextToken()
        if Lexema.NUMBER.__contains__(lookahead):
            digito()
        else:
            var()
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
    global lookahead
    global sToken
    global pointerVar
    sToken = ""
    while lookahead=='|s|':
        lookahead=nextToken()
    
    if Lexema.NUMBER.__contains__(lookahead):
        digito()
        operacao2()
        
    elif lookahead=='(':
        tok = token("SYMBOL", "(", "OpPar")
        tabelaSimbolo.append(tok)
        openPar()
        t = expr()
        resultado.append(t)
        closePar()
        
    else:
        var()
        operacao2()

        

    
    
def digito() :
    global lookahead
    global contador
    global saida
    global total
    while lookahead=='|s|':
        lookahead = nextToken()
    t2 = token('', None,'')
    total = 0
    contagem_decimal = 0
    decimal = False
    while Lexema.NUMBER.__contains__(lookahead) or lookahead == '.':
        if lookahead == '.':
            lookahead = nextToken()
            decimal = True
        elif lookahead == '0':
            match('0')
            saida =saida.replace(saida, saida+'0')
            t2.tipo = Lexema.varType('0')
            if decimal == True:
                total = Lexema.varValueDec(total,0,contagem_decimal)
                contagem_decimal = contagem_decimal + 1
            else:
                total = Lexema.varValue(total, 0)
        elif lookahead == '1':
            match('1')
            saida =saida.replace(saida, saida+'1')
            t2.tipo = Lexema.varType('1')
            if decimal == True:
                total = Lexema.varValueDec(total,1,contagem_decimal)
                contagem_decimal = contagem_decimal + 1
            else:
                total = Lexema.varValue(total, 1)
        elif lookahead == '2':
            match('2')
            saida =saida.replace(saida, saida+'2')
            t2.tipo = Lexema.varType('2')        
            if decimal == True:
                total = Lexema.varValueDec(total,2,contagem_decimal)
                contagem_decimal = contagem_decimal + 1
            else:
                total = Lexema.varValue(total, 2)
        elif lookahead == '3':
            match('3')
            saida =saida.replace(saida, saida+'3')
            t2.tipo = Lexema.varType('3')
            if decimal == True:
                total = Lexema.varValueDec(total,3,contagem_decimal)
                contagem_decimal = contagem_decimal + 1
            else:
                total = Lexema.varValue(total, 3)
        elif lookahead == '4':
            match('4')
            saida =saida.replace(saida, saida+'4')
            t2.tipo = Lexema.varType('4')
            if decimal == True:
                total = Lexema.varValueDec(total,4,contagem_decimal)
                contagem_decimal = contagem_decimal + 1
            else:
                total = Lexema.varValue(total, 4)
        elif lookahead == '5':
            match('5')
            saida =saida.replace(saida, saida+'5')
            t2.tipo = Lexema.varType('5')
            if decimal == True:
                total = Lexema.varValueDec(total,5,contagem_decimal)
                contagem_decimal = contagem_decimal + 1
            else:
                total = Lexema.varValue(total, 5)
        elif lookahead == '6':
            match('6')
            saida =saida.replace(saida, saida+'6')
            t2.tipo = Lexema.varType('6')
            if decimal == True:
                total = Lexema.varValueDec(total,6,contagem_decimal)
                contagem_decimal = contagem_decimal + 1
            else:
                total = Lexema.varValue(total, 6)
        elif lookahead == '7':
            match('7')
            saida =saida.replace(saida, saida+'7')
            t2.tipo = Lexema.varType('7')
            if decimal == True:
                total = Lexema.varValueDec(total,7,contagem_decimal)
                contagem_decimal = contagem_decimal + 1
            else:
                total = Lexema.varValue(total, 7)
        elif lookahead == '8':
            match('8')
            saida =saida.replace(saida, saida+'8')
            t2.tipo = Lexema.varType('8')
            if decimal == True:
                total = Lexema.varValueDec(total,8,contagem_decimal)
                contagem_decimal = contagem_decimal + 1
            else:
                total = Lexema.varValue(total, 8)
        elif lookahead == '9':
            match('9')
            saida =saida.replace(saida, saida+'9')
            t2.tipo = Lexema.varType('9')
            if decimal == True:
                total = Lexema.varValueDec(total,9,contagem_decimal)
                contagem_decimal = contagem_decimal + 1
            else:
                total = Lexema.varValue(total, 9)
            
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
    global EOL
    global sToken
    global tabelaParenteses
    EOL = False
    operador = token(sToken,None,None)
    while lookahead == '|s|':
        lookahead = nextToken()
    if lookahead =='-':
        tok = token("SYMBOL", "-", "OpSub")
        tabelaSimbolo.append(tok)
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
        tok = token("SYMBOL", "+", "OpSum")
        tabelaSimbolo.append(tok)
        match('+')
        termos()
        A = resultado.pop(len(resultado)-1)
        B = resultado.pop(len(resultado)-1)
        operador.valor = A.valor+B.valor
        operador.tipo = A.tipo
        resultado.append(operador)
        saida =saida.replace(saida, saida+'+')
        operacao1()
    elif lookahead == '(':
        print("Abri (")
        openPar()
        t = expr()
        resultado.append(t)
        if lookahead ==')':
            tok = token("SYMBOL", ")", "clsPar")
            tabelaSimbolo.append(tok)
            closePar()
    if lookahead == ';':
        EOL = True
    if EOL == True or EOF == True:
        global tokenRetorno
        if len(resultado)>0:
            tokenRetorno = resultado.pop()
            return tokenRetorno
        else:
            if len(tabelaParenteses)>0:
                print("Erro no balanceamento de parênteses")
            else:
                return tokenRetorno





def expr():
    termos()
    t = token("",None, None)
    t = operacao1()
    return t

def var():
    global lookahead
    global sToken 
    global EOF
    global pointerVar
    sToken = ""
    while (lookahead != "|s|"):
        if (not Lexema.SYMBOL.__contains__(lookahead) and EOF != True):
            sToken = sToken+lookahead
            lookahead = nextToken()
        else:
            break
    for item in tabelaSimbolo:
        if item.nome == sToken:
            resultado.append(item)
            pointerVar = False
            break
            
    return sToken

def openPar():
    global contador
    global tabelaParenteses
    global lookahead
    global tabelaParenteses 
    if lookahead == '(': 
        tabelaParenteses.append('(')
        lookahead = nextToken()
        return lookahead
    else:
        print("Parenteses ( ausente em: "+str(contador))
                    
def closePar():
    global lookahead
    global contador
    global tabelaParenteses 
    if lookahead == ')': 
        if len(tabelaParenteses)!=0:
            tabelaParenteses.pop()
            lookahead = nextToken()
            return lookahead
        else:
            print("Parenteses ) ausente em: "+contador)
    
def impressao():
    global EOF
    global lookahead
    global sToken
    lookahead = nextToken()
    openPar()
  
    var()
    
    if len(tabelaSimbolo)!=0:
        for item in tabelaSimbolo:
            if item.nome == sToken:
                closePar()
                print("<"+str(item.nome)+", "+str(item.valor)+", "+str(item.tipo)+" >")
    else:
        print("Variavel "+sToken+" não encontrada")
        
def EndOfLine():
    global lookahead
    global contadorLinhas 
    global EOF
    tok = token("SYMBOL", ";", "EOL")
    tabelaSimbolo.append(tok)
    while lookahead == '|s|':
        lookahead = nextToken()
    if lookahead ==';' and EOF == False:
        contadorLinhas+=1
        lookahead = nextToken()
    else: 
        print("Erro, ; esperado na linha", contadorLinhas)
    
def lines():
    global lookahead
    global enter 
    enter = ''
    while lookahead=='|s|':
        lookahead = nextToken()
        
    while lookahead!='|s|' and lookahead != True and enter != '\en':
        enter = enter+lookahead
        lookahead = nextToken()


    global EOF
    if EOF == True:
        return
    else:
        programa()
        
def programa():
    global EOF
    stmt()
    EndOfLine()
    if EOF == False:
      lines()
    

            
def atribuicao():
    global lookahead
    global sToken 
    global tabelaSimbolo
    global EOL
    sToken = ""
    copia =""
    armazenado = bool
    global EOF
    if EOF == False:
        while lookahead == '|s|':
            lookahead = nextToken()
        while  Lexema.SYMBOL.__contains__(lookahead)!= True and EOF == False:
            sToken = sToken+lookahead
            lookahead=nextToken()
            copia = sToken
            if Lexema.SYMBOL.__contains__(lookahead)==True:
                while lookahead != True:
                    if lookahead =='=':
                        match('=')
                        t = token("",None,None)
                        t = expr()
                        t.nome = copia
                        if len(tabelaSimbolo)!=0:
                            for item in tabelaSimbolo:
                                if item.nome == t.nome:
                                    item.valor = t.valor
                                    item.tipo = Lexema.varType(str(t.valor))
                                    item.nome = t.nome
                                    armazenado = True
                                    break
                                
                            if armazenado == True:
                                print("--------------")
                                
                            else:
                                t.tipo = Lexema.varType(str(t.valor))
                                tabelaSimbolo.append(t)
                            
                        else:                          
                            t.tipo = Lexema.varType(str(t.valor))
                            tabelaSimbolo.append(t)
                    elif lookahead == '|s|':
                        lookahead = nextToken()
                    
                    else:
                        if lookahead == ';':
                            return
                        else:
                            lookahead = nextToken()
            
                    
    else:
        print('fim do arquivo')
    
def stmt():
    contadorBackup = 0
    global contador
    global lookahead
    global TokenStmt
    global EOF
    contadorBackup = contador
    TokenStmt = ""
    first = lookahead
    if first != True:
        while (first != True):
            if (not Lexema.SYMBOL.__contains__(first)):
                TokenStmt = TokenStmt+first
                first = nextToken()
            else:
                break
        
    if(TokenStmt.upper()=="PRINT"):
        contador = contador-1
        impressao()
    elif EOF!=True:
        contador = contadorBackup
        atribuicao()
    else: 
        print("unexpected end of line/file")
    

    
if __name__=='__main__':
    global contadorLinhas
    global entrada
    contadorLinhas = 1
    global EOF 
    global pointerVar 
    pointerVar = False
    EOF = False
    t = token('', None,"")
    global resultado
    global operador
    operador = token('',None,"")
    resultado = []
    global tabelaParenteses 
    tabelaParenteses= []
    global tabelaSimbolo
    tabelaSimbolo = []
    entrada = input()
    saida =''
    contador = -1
    while contador != len(entrada) :
        if(contador <= len(entrada)):
            lookahead = nextToken()
            if EOF == False:
                programa()   
    for item in tabelaSimbolo:
        print("Tokens armazenados =<", item.nome,",", item.valor,",",item.tipo,">")
#testes = 
#x = 2 - 2 + 2/5;\eny = 2 * 10 + 1;\enz = (x + y) * 5;\enprint(z);
#x = 2 - 2 + 2/5;\eny = 2 * 10 + 1;\enz = (x + y) + 5;\enprint(z);\enprintador = x * z;
#x = 2 - 2 + 2/5;\eny = 2 * 10 + 1;\enz = (x + y) + 5;\enp = (x + z) * 3 + (3 * 2);\enprint(z);\enp = 3.14;
