# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 20:02:59 2018

@author: Maxime
"""

from algo import *
from random import *
from Parse import *


R, C, F, N, B, T = features

def dist(start,finish):
    return abs(start[0]-finish[0]) + abs(start[1]-finish[1])

def voiture_alea(Etat):
    return randint(0, F-1)


def indice_changement_valide(Etat, vi):
    nb_Courses_vi =  Etat[vi][0]
    return randint(0 , nb_Courses_vi - 1)

def Voisinage(Etat, vi, vj, ci, cj):
    courses_vi = Etat[vi][1:]
    courses_vj = Etat[vj][1:]
    
    
    
    # insertion de cj dans vi à la place dans l'ordre chronologique:
    # ordre = 
    pos_vi = [0,0]
    t = 0
    inser = 0
    course_i = trajets[ courses_vj[inser] ]
    # Tant que le temps de début maximal du prochain trajet de la
    # voiture i est avant le temps de début maximal de cj, on va au
    # delà.
    # Le temps de début maximal est le temps de fin maximal
    start_i = course_i.pt_start
    end_i = course_i.pt_end
    temps_min_course_0 = course_0.latest_end - 
    while machin_cj > course_k:
        temps_max = trajets[f] - dist
        
        
        
        inser += 1
    Etat.insert(inser,cj)  
        
    return Etat