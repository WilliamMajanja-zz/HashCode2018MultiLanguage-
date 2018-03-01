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
    
    course_ci = trajets[ ci ]
    course_cj = trajets[ cj ]
    
    start_ci = course_ci.pt_start
    end_ci = course_ci.pt_end
    
    start_cj = course_cj.pt_start
    end_cj = course_cj.pt_end
    
    # insertion de cj dans vi à la place dans l'ordre chronologique:
    # ordre = 
    pos_vi = (0,0)
    inser = 0
    course_i = trajets[ courses_vi[inser] ]
    # Tant que le temps de début maximal du prochain trajet de la
    # voiture i est avant le temps de début maximal de cj, on va au
    # delà.
    # Le temps de début maximal est le temps de fin maximal
    start_i = course_i.pt_start  # ce qui dépend de vi
    end_i = course_i.pt_end
    temps_min_course_i = course_i.latest_end - dist(start_i,end_i) - dist(pos_vi,start_i)
    temps_min_cj = course_cj.latest_end - dist(start_cj,end_cj) - dist(pos_vi,start_cj)
    while temps_min_cj > temps_min_course_i:
        pos_vi = end_i
        inser += 1
        course_i = trajets[ courses_vi[inser] ]
        start_i = course_i.pt_start
        end_i = course_i.pt_end
        temps_min_course_i = course_i.latest_end - dist(start_i,end_i) - dist(pos_vi,start_i)
        temps_min_cj = course_cj.latest_end - dist(start_cj,end_cj) - dist(pos_vi,start_cj)
    Etat.insert(inser,cj)  

    # insertion de ci dans vj

    pos_vj = (0,0)
    inser = 0
    course_j = trajets[ courses_vj[inser] ]
    # Tant que le temps de début maximal du prochain trajet de la
    # voiture i est avant le temps de début maximal de cj, on va au
    # delà.
    # Le temps de début maximal est le temps de fin maximal
    start_j = course_j.pt_start
    end_j = course_j.pt_end
    temps_min_course_j = course_j.latest_end - dist(start_j,end_j) - dist(pos_vj,start_j)
    temps_min_ci = course_ci.latest_end - dist(start_ci,end_ci) - dist(pos_vj,start_ci)
    while temps_min_ci > temps_min_course_j:
        pos_vj = end_j
        inser += 1
        course_j = trajets[ courses_vj[inser] ]
        start_j = course_j.pt_start
        end_j = course_j.pt_end
        temps_min_course_j = course_j.latest_end - dist(start_j,end_j) - dist(pos_vj,start_j)
        temps_min_ci = course_ci.latest_end - dist(start_ci,end_ci) - dist(pos_vj,start_ci)
    Etat.insert(inser,ci)
    
    
    return Etat






