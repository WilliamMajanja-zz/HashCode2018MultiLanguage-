# Distance and Energy
from Parse import *
from algo import *

def distance(pt1, pt2):
    return abs(pt1[0]-pt2[0]) + abs(pt1[1]-pt2[1])

def traj_distance(traj):
    return distance(traj[0],traj[1])

def energy(list_affect):
    E = 0
    for trajs in list_affect:
        pos = (0,0)
        k = 1
        depart = distance(pos,trajets[trajs[1]][0]) + dist_trajets[trajs[1]]
        E += depart
        pos = trajets[trajs[1]][1]
        tk = depart
        for traj in trajs[1:]:
            dist_k = distance(pos,trajets[trajs[k]][0]) + dist_trajets[trajs[k]]
            if (trajets[trajs[k]][3] >= tk + dist_k):
                pos = trajets[trajs[k]][1]
                dt = trajets[trajs[k]][2]-tk
                if (dist_k >  dt):
                    tk += dist_k
                    E += dist_trajets[trajs[k]]
                else:
                    tk = trajets[trajs[k]][2]
                    E += dist_trajets[trajs[k]] + features[4]
                    
            k+=1        
    return E

dist_trajets = list(map(traj_distance, trajets))

Etat = output
print(energy(Etat))
