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

S = 1 # Valeur utilisée pour le chiffrement

# ----------------------------------------------------------------------------
# Récupération des champs p et q
# -------------------------
response = server.query('parameters/monbailly') # contient p et g

g = response['g']
p = response['p']
h = pow(g, S, p)


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
invC1 = pow(c1, p-2)

cipher = c2 * invC1
print(cipher)

# ----------------------------------------------------------------------------
# Envoi du message
# -------------------------
dic = {'plaintext':cipher}
response = server.query('validate/monbailly', dic)
print(response)
