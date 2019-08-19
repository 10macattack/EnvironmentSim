import random


def FunctionCounter(value):
    value += 1


def CreatureCreator(CURRENT_GENERATION, SPECIES):
    CREATURE = {}
    CREATURE_INIT_AGE = int(random.randint(1, 4))
    CREATURE_GENE = random.uniform(1, 100)
    CREATURE_GENDER = random.choice(GENDER)
    CREATURE_HUNGER = random.randint(1, 3)
    CREATURE = {'Species': SPECIES, 'Age': CREATURE_INIT_AGE, 'Survivability': CREATURE_GENE, 'Sex': CREATURE_GENDER,
                'Hunger': CREATURE_HUNGER, 'Dead': False, 'Generation': CURRENT_GENERATION, 'Infected': False, 'Maturity':'GEN'}
    return CREATURE


def Mating(CURRENT_GENERATION, SPECIES_LIST, SPECIES, RANGE_LOW, RANGE_HIGH, MATE_COUNTER):
    MATABLE = []
    for i in SPECIES_LIST:
        if i['Maturity'] == 'Adult':
            MATABLE.append(i)
            MATING_SEASON = True
    for i in MATABLE:
        if MATING_SEASON == True:
            OFFSPRING = random.randint(RANGE_LOW,RANGE_HIGH)
            for i in range(OFFSPRING):
                MATE_ONE = random.choice(MATABLE)
                MATE_TWO = random.choice(MATABLE)
                MATE_HUNGER = MATE_ONE['Hunger'] + MATE_TWO['Hunger']
                if MATE_HUNGER >= 3:
                    if MATE_ONE['Sex'] != MATE_TWO['Sex']:
                        BABY = CreatureCreator(CURRENT_GENERATION, SPECIES)
                        BABY['Age'] = 0
                        BABY['Survivability'] = (
                            MATE_ONE['Survivability']+MATE_TWO['Survivability'])/2
                        BABY.update({'Born': True})
                        SPECIES_LIST.append(BABY)
                        FunctionCounter(MATE_COUNTER)
    MATING_SEASON = False
    MATABLE = []


def OldAge(SPECIES_LIST, AGE_OF_DEATH):
    SPARE_LIST = []
    for i in SPECIES_LIST:
        if i['Age'] >= AGE_OF_DEATH:
            i.update({'Death Cause': 'Old Age'})
            i['Dead'] = True
            SPARE_LIST.append(i)
    for i in SPARE_LIST:
        SPECIES_LIST.remove(i)


def Aging(CREATURE_LIST):
    for i in CREATURE_LIST:
        i['Age'] += 1


def Hunting(PREDATOR, PREY, FORESTRY):
    SPARE_LIST = []
    for i in PREDATOR:
        if len(PREY) == 0:
            i['Hunger'] -= 10
        for j in PREY:
            if i['Hunger'] <= 10 and i['Hunger'] >= -10 and i['Maturity'] == 'Adult':
                FOUND_CHANCE = random.randint(1, 100)
                if FOUND_CHANCE < 50:
                    if j['Survivability'] < i['Survivability']:
                        i['Hunger'] = i['Hunger'] + 3
                        j['Dead'] = True
                        j.update({'Death Cause': 'Hunted'})
                        SPARE_LIST.append(j)
                    else:
                        i['Hunger'] -= 1
                else:
                    i['Hunger'] = - 1
    for i in SPARE_LIST:
        if i in PREY:
            PREY.remove(i)


def Eating(PREY, FORESTRY):
    for i in PREY:
        if FORESTRY >= 0:
            i['Hunger'] += 1
            FORESTRY -= 1
        else:
            i['Hunger'] -= 10
    return FORESTRY


def Hunger_Reset(Species):
    for i in Species:
        if i['Hunger'] >= 2:
            i['Hunger'] = 2


def Starvation(CreatureList):
    SPARE_LIST = []
    for i in CreatureList:
        if i['Hunger'] <= 0:
            i.update({'Death Age': i['Age']})
            i.update({'Death Cause': 'Starvation'})
            i['Dead'] = True
            SPARE_LIST.append(i)
    for i in SPARE_LIST:
        CreatureList.remove(i)


def Infection(CreatureList, Min_Pollution, MESSAGE, DISEASE):
    for i in CreatureList:
        INFECT_CHANCE = random.randint(Min_Pollution, 10000)
        if INFECT_CHANCE >= 9995:
            i['Infected'] = True
            DISEASE = True
            if MESSAGE == True:
                MESSAGE = False
        else:
            DISEASE = False


def InfectionSpread(CreatureList):
    SPREAD_CHANCE = random.randint(1, 3)
    for i in CreatureList:
        if i['Infected'] == True:
            for i in range(SPREAD_CHANCE):
                INFECTED = random.choice(CreatureList)
                INFECTED['Infected'] = True


def InfectionKill(CreatureList):
    SPARE_LIST = []
    for i in CreatureList:
        if i['Infected'] == True:
            DIE_CHANCE = random.randint(1, 20)
            if DIE_CHANCE == 2:
                SPARE_LIST.append(i)
    for i in SPARE_LIST:
        CreatureList.remove(i)

def Maturify(SPECIES_LIST,AGE):
    for a in SPECIES_LIST:
            if a['Age'] >= AGE:
                a['Maturity'] = 'Adult'
            else:
                a['Maturity'] = 'Child'

def Animal(SPECIES_LIST,MATURE_AGE,CURRENT_GENERATION,NAME,MIN_RANGE,MAX_RANGE,MATE,MIN_POLLUTION,MESSAGE,DISEASE):
    Hunger_Reset(SPECIES_LIST)
    Aging(SPECIES_LIST)
    Maturify(SPECIES_LIST,MATURE_AGE)
    Mating(CURRENT_GENERATION, SPECIES_LIST, NAME,MIN_RANGE,MAX_RANGE,MATE)
    Infection(FOX_LIST, MIN_POLLUTION, MESSAGE, DISEASE)
    InfectionSpread(SPECIES_LIST)

def AnimalDeath(SPECIES_LIST,AGE_OF_DEATH):
    Starvation(SPECIES_LIST)
    OldAge(SPECIES_LIST, AGE_OF_DEATH)
    InfectionKill(SPECIES_LIST)


MATING_VALUE = 0

Min_Pollution = random.randint(1, 2000)
print(f'Min Pollution:{Min_Pollution}')
MESSAGE = True
DISEASE = False
HUNTED_LIST = []
NUMBER = 1
FOX_MATE = 0
RABBIT_MATE = 0
FOX_LIST = []
RABBIT_LIST = []
ORIGINAL_FAVORABILITY = []
RABBIT = {}
FOX = {}
INIT_FOX_POP = 100
INIT_RABBIT_POP = 1000
FORESTRY = 250000
GENERATIONS = 16
GENDER = ('Male', 'Female')
x = 0

print('Initial Population Details:')

print(f'Original Fox Population: {INIT_FOX_POP}')
for i in FOX_LIST:
    ORIGINAL_FAVORABILITY.append(i['Survivability'])
if len(FOX_LIST) != 0:
    print(f'Original Fox Favorability:{sum(ORIGINAL_FAVORABILITY)/len(ORIGINAL_FAVORABILITY)}')

print(f'Original Rabbit Population: {INIT_RABBIT_POP}')
print(f'Original Forestry:{FORESTRY}')
print(f'Amount of Generations: {GENERATIONS}')
print('')

for i in range(INIT_FOX_POP):
    FOX_LIST.append(CreatureCreator(NUMBER, 'FOX'))

for i in range(INIT_RABBIT_POP):
    RABBIT_LIST.append(CreatureCreator(NUMBER, 'RABBIT'))

GENERATION_LIST = []
for i in range(GENERATIONS):
    CURRENT_GENERATION = i + 1
    TOTAL_RABBITS = len(RABBIT_LIST)
    TOTAL_FOXES = len(FOX_LIST)  
   
    Animal(FOX_LIST,3,CURRENT_GENERATION,'FOX',2,7,FOX_MATE,Min_Pollution,MESSAGE,DISEASE)
    Animal(RABBIT_LIST,2,CURRENT_GENERATION,'RABBIT',6,12,RABBIT_MATE,Min_Pollution,MESSAGE,DISEASE)


    Hunting(FOX_LIST, RABBIT_LIST, FORESTRY)
    FORESTRY = Eating(RABBIT_LIST, FORESTRY)

    AnimalDeath(RABBIT_LIST,4)
    AnimalDeath(FOX_LIST,6)

    FOREST_GROWTH = random.uniform(1, 2)

    if FORESTRY <= 2000:
        FORESTRY = FORESTRY + 750
    if FORESTRY <= 20000:
        FORESTRY = int(FORESTRY * FOREST_GROWTH)

    NET_FOX_CHANGE = len(FOX_LIST)-TOTAL_FOXES
    NET_RABBIT_CHANGE = len(RABBIT_LIST)-TOTAL_RABBITS

    print(f'there is {TOTAL_FOXES} foxes in generation {CURRENT_GENERATION}')
    print(f'there is {TOTAL_RABBITS} rabbits in generation {CURRENT_GENERATION}')


    print(f'There is {FORESTRY} forestry')
    
    RABBIT_HUNGER_LIST = []
    FOX_HUNGER_LIST = []
    for l in FOX_LIST:
        FOX_HUNGER_LIST.append(l['Hunger'])
    for p in RABBIT_LIST:
        RABBIT_HUNGER_LIST.append(p['Hunger'])
    print('')

    print(f'Net change in foxes = {NET_FOX_CHANGE}')
    print(f'Net change in rabbits = {NET_RABBIT_CHANGE}')
    print('')
    RABBIT_HUNGER_LIST = []
    FOX_HUNGER_LIST = []
    HUNTED_LIST = []


RABBIT_HUNGER_LIST = []
FOX_HUNGER_LIST = []
FOX_FAVORABILITY_LIST = []

print('')
print(f'The final amount of foxes is: {len(FOX_LIST)}')
print(f'The final amount of rabbits is: {len(RABBIT_LIST)}')
for l in FOX_LIST:
    FOX_HUNGER_LIST.append(l['Hunger'])
    FOX_FAVORABILITY_LIST.append(l['Survivability'])
for p in RABBIT_LIST:
    RABBIT_HUNGER_LIST.append(p['Hunger'])
if FOX_LIST and RABBIT_LIST:
    print(f'the final average hunger of foxes  is : {sum(FOX_HUNGER_LIST)/len(FOX_HUNGER_LIST)}')
    print(f'the final average hunger of rabbits is : {sum(RABBIT_HUNGER_LIST)/len(RABBIT_HUNGER_LIST)}')
    print(f'Final Fox Favorability = {sum(FOX_FAVORABILITY_LIST)/len(FOX_FAVORABILITY_LIST)}')
    print(f'The amount of Rabbit\'s born is :{RABBIT_MATE}')
    print(f'The amount of Foxes\'s born is {FOX_MATE}')

ANIMAL_LIST = FOX_LIST + RABBIT_LIST

PICKING = True
while PICKING:
    CHOICE_ONE = input('Would you like to sort through the Animals? ')
    if CHOICE_ONE == 'YES':
        CHOICE_TWO = input('Which Animal? ')
        if CHOICE_TWO == 'Fox':
            while CHOICE_TWO != 'Back':
                CHOICE = input(
                    f'What animal do you want to examine? we have {len(FOX_LIST)} options ')
                print(FOX_LIST[int(CHOICE) - 1])
        else:
            while CHOICE_TWO != 'Back':
                CHOICE_TWO = input(
                    f'What animal do you want to examine? we have {len(RABBIT_LIST)} options ')
                print(RABBIT_LIST[int(CHOICE_TWO) - 1])
    else:
        PICKING = False
