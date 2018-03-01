import os
import inspect

os.chdir(os.path.dirname(inspect.getfile(inspect.currentframe())))

# Importation des données parsées
from Parse import features, trajets

# Résolution


# Ecriture des résultats en output A VOIR

def time_travel(end, start):
    return abs(end[0]-start[0]) + abs(end[1]-start[1])
    
class travel:
    def __init__(self, infos):
        self.index = compt
        
        self.pt_start=infos[0]
        self.pt_end=infos[1]
        self.earliest_start= infos[2]
        self.latest_end = infos[3]
        
        self.length=time_travel(pt_end, pt_start)
        
        self.time_start=-1
        self.time_finish=-1
        
        self.done= False
        self.bonus=False
    
    def reset(self):
        self.done = False
        self.bonus = False 
        self.time_start= -1
        self.time_finish = -1


class car:
    def __init__(self):
        self.pos=(0 , 0)
        self.time_avail = 0
        self.affectations = affectation()
    
    
    def assign_travel(self, travel):
        self.time_spent+=time_travel(self.pos, travel.start)
        travel.time_start=self.time_spent
        self.time_avail+=travel.length
        travel.time_finish = self.time_avail
        self.pos= travel.pt_end
        
        travel.done=True
        if travel.time_start==travel.earliest_start:
            travel.bonus= True
        
        self.affectations.affect(travel)
    
    
    def reset(self):
        self.pos= (0,0)
        self.time_avail=0


class affectation:
    def __init__(self):
        list=[0]
    
    def reset(self):
        affectations=[]
        
    def affect(self, travel):
        self.list[0]+=1
        self.list.append(travel.index)


def reset_all():
    for travel in travels:
        travel.reset()
    for car in cars:
        car.reset()


def soonest_available(cars):
    min = 1000000000
    for car in cars:
        if car.time_avail<=min:
            best_car= car
            min = car.time_avail
    return car
            

def assign_random(cars, travels):
    for travel in travels:
        car = soonest_available(cars)
        car.assign_travel(travel)

        


    