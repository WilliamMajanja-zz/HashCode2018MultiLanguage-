
import os
import inspect
path = os.path.dirname(inspect.getfile(inspect.currentframe()))
os.chdir(path)

# Importation des données parsées
from Parse import *

# Résolution

#comment
# Ecriture des résultats en output A VOIR

def time_travel(end, start):
    return abs(end[0]-start[0]) + abs(end[1]-start[1])
    
class travel:
    def __init__(self, infos):
        self.pt_start=infos[0]
        self.pt_end=infos[1]
        self.earliest_start= infos[2]
        self.latest_end = infos[3]
        
        self.length=time_travel(pt_end, pt_start)
        
        self.time_start=-1
        self.time_finish=-1
        
        self.done= False
        self.bonus=False


    
class voiture:
    def __init__(self):
        self.pos=(0 , 0)
        self.time_avail = 0
    
    
    def assign_travel(self, travel):
        self.time_spent+=time_travel(self.pos, travel.start)
        travel.time_start=self.time_spent
        self.time_avail+=travel.length
        travel.time_finish = self.time_avail
        self.pos= travel.pt_end
        
        travel.done=True
        if travel.time_start=travel.earliest_start:
            travel.bonus= True
        


    