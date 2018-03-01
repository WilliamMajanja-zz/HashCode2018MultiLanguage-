import numpy as np
import csv

# Working directory
wd = 'C:/Users/Bastien/Desktop/Hashcode/'
# Input name
filename = wd + 'example.in'

# Lecture du csv
data = []
with open(filename, 'r') as csvfile:
    Reader = csv.reader(csvfile, delimiter=' ')
    for row in Reader: 
        data.append(row)

# Traitement des données 
# A MODIFIER EN FONCTION DU FORMAT DES DONNEES
features = data[0]
[R, C, L, H] = map(int, features)
data[1:] = map(lambda a: a[0], data[1:])


        

