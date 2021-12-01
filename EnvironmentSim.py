import random
import numpy as np
import animalHierarchy as ah
import populations as pop

GENDER = ('Male', 'Female')

def make_traits_dict(age_factor,mating_traits,digestion_factor,hunting_factor,size_factor,max_pack_size,is_predator=True,is_mature=True,unique_traits=[]):
    traits_dict = dict({
        "Is Predator":is_predator,
        "Age":age_factor,
        "Mating":mating_traits,
        "Maturity":is_mature,
        "Digestion":digestion_factor,
        "Hunting":hunting_factor,
        "Size":size_factor,
        "Pack Size":max_pack_size
        })
    if is_predator==False:
        traits_dict["Hiding"]=unique_traits[0]
    return traits_dict

def main():
    fox_traits = make_traits_dict(12,{"Attractiveness":.5,"Fertility":1.2,"Offspring":4},5,1.3,1,2)
    fox_population=pop.Population(50,fox_traits,"Foxes")
    rabbit_traits = make_traits_dict(12,{"Attractiveness":.5,"Fertility":1.2,"Offspring":4},5,1.3,1,3)
    rabbit_population=pop.Population(5,rabbit_traits,"Rabbits")
    print(fox_population)
    print(rabbit_population)
main()
