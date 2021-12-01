import random
import animalHierarchy as ah
import numpy as np

def initialize_individual(traits_dict,species_id,i):
    if traits_dict["Is Predator"]:
        individual = ah.Predator(
            {"Species Name":species_id,"ID":i},
            random.randint(0,traits_dict["Age"]),
            traits_dict["Mating"],
            random.randint(0,traits_dict["Digestion"]),
            random.uniform(0,traits_dict["Hunting"]),
            random.uniform(0,traits_dict["Size"]),
            traits_dict["Maturity"],
            np.empty(traits_dict["Pack Size"],dtype=object)
        )
    else:
        individual = ah.Prey(
            {"Species Name":species_id,"ID":i},
            random.randint(0,traits_dict["Age"]),
            traits_dict["Mating"],
            random.randint(0,traits_dict["Digestion"]),
            random.uniform(0,traits_dict["Hunting"]),
            random.uniform(0,traits_dict["Size"]),
            traits_dict["Maturity"],
            np.empty(traits_dict["Pack Size"],dtype=object),
            random.uniform(0,traits_dict["Hiding"])
        )
    return individual

class Population:
    def __init__(self,pop_size,traits_dict,species_id):
        self.population = self.make_pop_array(pop_size,traits_dict,species_id)
        self.pop_size=pop_size
        self.species_id = species_id

    def make_pop_array(self,pop_size,traits_dict,species_id):
        pop_array=np.empty(pop_size,dtype=object)
        for i in range(pop_size):
            individual = initialize_individual(traits_dict,species_id,i)
            pop_array[i]=Pack(traits_dict["Pack Size"],individual)
        return pop_array
        
    def do_mating(self):
        return 0
    

class Pack:
    def __init__(self,pack_size,parent):
        self.pack_size = pack_size-2
        self.pack = np.empty(pack_size-2,dtype=object)
        self.curr_individuals = 1
        if(parent.sex=='Female'):
           self.mother = parent
           self.father = 0
        else:
            self.mother = 0
            self.father = parent
        self.isFamily = False


    def makeBaby(self,i):
        if self.father.is_predator == True:
            return ah.Predator(
                {"Species Name":self.father.individual_data["Species Name"],"ID":f"{self.father.individual_data['ID']}-'{i}'"},
                0,
                {}, #make mating stuff
                int((self.mother.digestion+self.father.digestion)/2),
                {},
                ((self.mother.size+self.father.size)/2),
                False,
                self.pack_size+2
            )
        else:
            return ah.Prey(
                {"Species Name":self.father.individual_data["Species Name"],"ID":f"{self.father.individual_data['ID']}-'{i}'"},
                0,
                {},
                int((self.mother.digestion+self.father.digestion)/2),
                {},
                ((self.mother.size+self.father.size)/2),
                False,
                self.pack_size+2,
                ((self.mother.hiding+self.father.hiding)/2),
            )

    def mate(self):
        averageLitter = int((self.mother.mating["Current Fertility"]+self.father.mating["Current Fertility"])/2)
        if averageLitter>self.pack_size:
            averageLitter=self.pack_size
        for i in range(random.randint(0,averageLitter-1)):
            self.pack[i] = self.makeBaby(i)
            self.curr_individuals+=1

    def makeFamily(self, otherParent):
        self.curr_individuals+=1
        if (self.mother == 0):
            self.mother = otherParent
        else:
            self.father = otherParent
        self.mate()
