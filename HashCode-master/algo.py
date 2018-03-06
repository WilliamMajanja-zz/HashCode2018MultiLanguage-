import os
import inspect
path = os.path.dirname(inspect.getfile(inspect.currentframe()))
os.chdir(path)

# Importation des données parsées
from Parse import features, trajets

# Résolution

#comment
# Ecriture des résultats en output A VOIR

def time_travel(end, start):
    return abs(end[0]-start[0]) + abs(end[1]-start[1])
    
class travel:
    def __init__(self, infos, compt):
        self.index = compt
        
        self.pt_start=infos[0]
        self.pt_end=infos[1]
        self.earliest_start= infos[2]
        self.latest_end = infos[3]
        
        self.length=time_travel(self.pt_end, self.pt_start)
        
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
        self.time_avail+=time_travel(self.pos, travel.pt_start)
        travel.time_start=self.time_avail
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
        self.list=[0]
    
    def reset(self):
        self.list=[]
        
    def affect(self, travel):
        self.list[0]+=1
        self.list.append(travel.index)
        
    def __str__(self):
        return str(self.list)


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
    return best_car
            

def assign_random(cars, travels):
    for travel in travels:
        car = soonest_available(cars)
        
        car.assign_travel(travel)


def get_output(cars):
    affects=[]
    for car in cars:
        affects.append(car.affectations.list)
    return affects


def write_output(list_affect, namefile):
    with open(namefile, 'w') as outp:
        for l in list_affect:
            for k in l:
                outp.write(str(k)+' ')
            outp.write('\n')
        outp.close()


def sort_travel(travels):
    n = len(travels)
    for i in range(1, n):
        current = travels[i]
        j= i
        while j>0 and travels[j-1].earliest_start>current.earliest_start:
            travels[j]=travels[j-1]
            j-=1
        travels[j]=current

    
def tri_insertion(tableau):
    for i in range(1,len(tableau)):
        en_cours = tableau[i]
        j = i
        #décalage des éléments du tableau }
        while j>0 and tableau[j-1]>en_cours:
            tableau[j]=tableau[j-1]
            j = j-1
        #on insère l'élément à sa place
        tableau[j]=en_cours

# print(features)
# prinat(trajets)

travels=[]
index=0
for trajet in trajets:
    travels.append(travel(trajet, index))
    index+=1

# print(travels)
#sort_travel(travels)
# print(travels)

#cars=[]
#for i in range(features[2]):
#    cars.append(car())
#
##assign_random(cars, travels)
#
##output=get_output(cars)
#
## print( "Output :")
## for out in output:
##     print(out)
#
#write_output(output, "out_e.in")



