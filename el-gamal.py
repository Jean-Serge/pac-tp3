#-*- coding:utf-8 -*-

"""
TP3 - PAC
Partie chiffrement ElGamal
"""

# ----------------------------------------------------------------------------
# Initialisation 
# -------------------------
from client import *

URL = 'http://pac.bouillaguet.info/TP3/ElGamal-encryption/'
server = Server(URL)

x = 1 # Valeur utilisée pour le chiffrement

def xgcd(a,b):
    """
    Calcul de XGCD(a, b) récupéré sur internet
    """
    prevx, x = 1, 0;  prevy, y = 0, 1
    while b:
        q, r = divmod(a,b)
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
        a, b = b, r
    return a, prevx, prevy
                                                

def inverse_mod(x, y):
    """
    Calcul de l'inverse modulaire de x par rapport à y.
    Revient à calculer le XGCD(x, y)
    """
    a,b,c = xgcd(x, y)
    return b

# ----------------------------------------------------------------------------
# Récupération des champs p et q
# -------------------------
response = server.query('parameters/monbailly') # contient p et g

g = response['g']
p = response['p']
h = pow(g, x, p)


# ----------------------------------------------------------------------------
# Récupération du challenge 
# -------------------------
dic = {'h':h}
response = server.query('challenge/monbailly', dic)

c1 = response['ciphertext'][0]
c2 = response['ciphertext'][1]


# ----------------------------------------------------------------------------
# Déchiffrement du message  
# -------------------------
c1x = pow(c1, x, p)
inv = inverse_mod(c1x, p)

cipher = (c2 * inv) % p
print(cipher)


# ----------------------------------------------------------------------------
# Envoi du message
# -------------------------
dic = {'plaintext':cipher}
response = server.query('validate/monbailly', dic)
print(response) # status : OK
