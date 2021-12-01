import random
from math import e,pi
SEX = ('Male', 'Female')

def update_fertility(current_age,peak_fertile_age,max_fertility,fertile_len):
    exp = -1/2*(((current_age-peak_fertile_age)/fertile_len)**2)
    const = max_fertility*(1/(fertile_len*2*pi))
    return const * (e**exp)

class Animal:
    def __init__(self,individual_data,age,mating,digestion,hunting,size,mature,pack):
        self.species_id=individual_data["Species Name"]
        self.individual_id=individual_data["ID"]
        self.age = age
        self.sex = random.choice(SEX)
        self.mating = mating
        self.digestion = digestion
        self.infected = False
        self.hunting = hunting
        self.size = size
        self.mature = mature
        self.pack = pack
    def quick_data(self):
        return f"<Species: {self.species_id}, ID:{self.individual_id}>"
    def update_mating(self):
        if self.mature:
            self.mating["Current Fertility"] = update_fertility(self.age,self.mating["Peak Fertile Age"],self.mating["Max Fertility"],self.mating["Fertile Length"])
    def update_traits(self):
        self.update_mating()
        
        

class Predator(Animal):
    def __init__(self,individual_data,age,mating,digestion,hunting,size,maturity,pack):
        super().__init__(individual_data,age,mating,digestion,hunting,size,maturity,pack)
        self.is_predator = True
    def __str__(self):
        str_indv = f""
        str_indv = f"{str_indv}Animal Type: Predator\n"
        str_indv = f"{str_indv}Age: {self.age}\n"
        str_indv = f"{str_indv}Mating: {self.mating}\n"
        str_indv = f"{str_indv}Digestion: {self.digestion}\n"
        str_indv = f"{str_indv}Hunting: {self.hunting}\n"
        str_indv = f"{str_indv}Pack: {self.pack}\n"
        return str_indv


class Prey(Animal):
    def __init__(self,individual_data,age,mating,digestion,hunting,size,maturity,pack,hiding):
        super().__init__(age,individual_data,mating,digestion,hunting,size,maturity,pack)
        self.is_predator = False
        self.hiding = hiding
    def __str__(self):
        str_indv = f""
        str_indv = f"{str_indv}Animal Type: Predator\n"
        str_indv = f"{str_indv}Age: {self.age}\n"
        str_indv = f"{str_indv}Mating: {self.mating}\n"
        str_indv = f"{str_indv}Digestion: {self.digestion}\n"
        str_indv = f"{str_indv}Hunting: {self.hunting}\n"
        str_indv = f"{str_indv}Pack: {self.pack}\n"
        return str_indv

