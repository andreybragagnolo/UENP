# -*- coding: utf-8 -*-
"""
@author: andre
"""
import re

KEYWORD = ['PRINT','print','Print']
SYMBOL = ['+', '-', '*', '/', '(', ')',';', '|s|','=',"/n/"]
NUMBER = ['0','1','2','3','4','5','6','7','8','9']
CARACTERES = re.compile('[A-z]*')
DECIMAL = re.compile(r'[0-9]*[.]?[0-9]*')
INTEIRO = re.compile('[0-9]*')


def varType(Entrada):
    global SYMBOL
    if SYMBOL.__contains__(Entrada):
        return "SYMBOL"
    elif INTEIRO.match(Entrada):
        return "NUMBER"
    elif KEYWORD.__contains__(Entrada):
        return "KEYWORD"
    elif DECIMAL.match(Entrada):
        return "DECIMAL"
    elif CARACTERES.match(Entrada):
        return "CARACTER" 

    else:
        return "Invalid token"

def varValue(total, valorEntrada):
    total = total*10+valorEntrada
    return total

def varValueDec(total, valorEntrada,contagens):
    
    total = total+valorEntrada/10**(contagens+1)
    return total
    
    
    
