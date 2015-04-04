#-*- coding:utf-8 -*-

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
from math import floor

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
    #print(next)
    next = next & x
    #print(next)
    for i in range (1 << 17):   
        next = next | i
        for j in range (2):
            next = next | (j << 31)
            # print(next)
            next = next - 12345
            #next = floor(next)
            next = next / 1103515245

    return next
    
# ----------------------------------------------------------------------------
# Récupération du Challenge 
# -------------------------
response = server.query('challenge/monbailly')
print(response)

# Vecteur d'initialisation utilisé pour chiffrer
IV = response['IV']


# print(chercher_next(IV[0], IV[1]))

i = 0
while True:
    n1 = (IV[1] + i * 32768) * 65536
    for j in range (65536):
        tmp = n1 + j
        n0 = floor((tmp - 12345) / 1103515245)
        # print(n0)
        if((n0 / 65536) % 32768 == IV[0]):
            print("Trouvé")
    i += 1

