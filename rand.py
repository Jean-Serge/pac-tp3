# -*- coding:utf-8 -*-

"""
TP3 - PAC
Partie rand

Ce TP a pour but de comprendre les défauts de la fonction 
'rand' utilisée en C.
"""



# ----------------------------------------------------------------------------
# Initialisation 
# -------------------------
from client import *

URL = 'http://pac.bouillaguet.info/TP3/rand/'

server = Server(URL)

# ----------------------------------------------------------------------------
# Fonctions Utiles
# -------------------------
def chercher_next(x, y):
    """
    Décomposition de next :
    ______________________________________
    |a|________b_______|_________c________|
    
    b = IV[0]
    """

    # Partie b
    next = 0x7FFF << 16
    print(x)
    print(next)
    next = next and x
    print(next)
    for i in range (1 << 17):   
        next = next or i
        for j in range (2):
            next = next or (j << 31)
            # print(next)
            
    return None
    
# ----------------------------------------------------------------------------
# Récupération du Challenge 
# -------------------------
response = server.query('challenge/monbailly')
print(response)

# Vecteur d'initialisation utilisé pour chiffrer
IV = response['IV']


print(chercher_next(IV[0], IV[1]))
