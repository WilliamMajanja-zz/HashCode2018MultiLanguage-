# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 21:57:49 2018

@author: Maxime
"""
import random as rd
from Parse import *
from algo import *
from energy import *
from math import exp
filename = "out_c.in"
data = []
output = []
with open(filename, 'r') as csvfile:
    Reader = csv.reader(csvfile, delimiter=' ')
    for row in Reader: 
        data.append(row)


for l in data:
    output.append(list(map(int, l[:-1])))
    
Etat = output

T = 100
Tf = 1
k = 0
while (T>Tf):
    k+=1
    T *= 0.999
    Ener = energy(Etat)
    v1 = voiture_alea(Etat)
    v2 = voiture_alea(Etat)
    c1 = indice_changement_valide(Etat,v1)
    c2 = indice_changement_valide(Etat,v2)
    Etat1 = Voisinage(Etat,v1,v2,c1,c2)
    Ener1 = energy(Etat1)
    r = rd.random()
    k += 1
    if (Ener1 > Ener):
        Etat = Etat1
        Ener = Ener1
        print(Ener)
    if (k==100):
        k=0
        write_output(Etat, "out_c.in")
        
write_output(Etat, "out_c.in")