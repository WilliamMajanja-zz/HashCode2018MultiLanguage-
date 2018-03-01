import numpy as np
import csv
import os
import inspect

# Working directory
wd = os.path.dirname(inspect.getfile(inspect.currentframe()))+'/'

# Input name
filename = wd + 'e_high_bonus.in'

# Lecture du csv
data = []
with open(filename, 'r') as csvfile:
    Reader = csv.reader(csvfile, delimiter=' ')
    for row in Reader: 
        data.append(row)

# Traitement des données 
# A MODIFIER EN FONCTION DU FORMAT DES DONNEES
features = list(map(int, data[0]))
trajets = []
for l in data[1:]:
    traj = []
    traj.append((int(l[0]), int(l[1])))
    traj.append((int(l[2]), int(l[3])))
    traj.append(int(l[4]))
    traj.append(int(l[5]))
    trajets.append(traj)




        

