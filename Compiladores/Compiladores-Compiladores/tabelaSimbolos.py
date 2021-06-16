# -*- coding: utf-8 -*-
"""
@author: andre
"""

SYMBOL = ['+', '-', '*', '/', '(', ')']
NUMBER = ['0','1','2','3','4','5','6','7','8','9']

def varType(charEntrada):
    global SYMBOL
    if SYMBOL.__contains__(charEntrada):
        return "SYMBOL"
    elif NUMBER.__contains__(charEntrada):
        return "NUMBER" 
    else:
        return "Invalid token"

def varValue(total, valorEntrada):
    total = total*10+valorEntrada
    return total
    
    