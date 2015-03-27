BB#-*- coding:utf-8 -*-

"""
TP3 - PAC
Partie chiffrement ElGamal
"""

from client import *

URL = 'http://pac.bouillaguet.info/TP3/ElGamal-encryption/'

server = Server(URL)

response = server.query('parameters/monbailly') # contient p et g
print(response)
