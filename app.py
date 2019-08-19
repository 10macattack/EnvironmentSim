import random


def FunctionCounter(value):
    value += 1


def CreatureCreator(CURRENT_GENERATION, SPECIES):
    CREATURE = {}
    CREATURE_INIT_AGE = int(random.randint(1, 4))
    CREATURE_GENE = random.randint(1, 10)
    CREATURE_GENDER = random.choice(GENDER)
    CREATURE_HUNGER = random.randint(1, 3)
    CREATURE = {'Species': SPECIES, 'Age': CREATURE_INIT_AGE, 'Survivability': CREATURE_GENE, 'Sex': CREATURE_GENDER,
                'Hunger': CREATURE_HUNGER, 'Dead': False, 'Generation': CURRENT_GENERATION, 'Infected': False, 'Maturity':'GEN'}
    return CREATURE


def Mating(CURRENT_GENERATION, SPECIES_LIST, SPECIES,):
    MATABLE = []
    for i in SPECIES_LIST:
        if i['Maturity'] == 'Adult':
            MATABLE.append(i)
            MATING_SEASON = True
    for i in MATABLE:
        if MATING_SEASON == True:
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
    MATING_SEASON = False
    MATABLE = []


def OldAge(SPECIES_LIST, AGE_OF_DEATH, VALUE):
    SPARE_LIST = []
    for i in SPECIES_LIST:
        FunctionCounter(VALUE)
        if i['Age'] >= AGE_OF_DEATH:
            i.update({'Death Cause': 'Old Age'})
            i['Dead'] = True
            SPARE_LIST.append(i)
    for i in SPARE_LIST:
        SPECIES_LIST.remove(i)


def Aging(CREATURE_LIST):
    for i in CREATURE_LIST:
        i['Age'] += 1


def Hunting(PREDATOR, PREY):
    SPARE_LIST = []
    for i in PREDATOR:
        if len(PREY) == 0:
            i['Hunger'] -= 10
        for j in PREY:
            if i['Hunger'] <= 10 and i['Hunger'] >= -10 and i['Maturity'] == 'Adult':
                FOUND_CHANCE = random.randint(1, 1000)
                if FOUND_CHANCE < 16:
                    KILLED_CHANCE = random.uniform(1, 10)
                    if KILLED_CHANCE < i['Survivability']:
                        i['Hunger'] = i['Hunger'] + 300
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
    SPREAD_CHANCE = random.randint(0, 5)
    for i in CreatureList:
        if i['Infected'] == True:
            for u in range(SPREAD_CHANCE):
                INFECTED = random.choice(CreatureList)
                INFECTED['Infected'] = True


def InfectionKill(CreatureList):
    SPARE_LIST = []
    for i in CreatureList:
        if i['Infected'] == True:
            DIE_CHANCE = random.randint(1, 2)
            if DIE_CHANCE == 2:
                SPARE_LIST.append(i)
    for i in SPARE_LIST:
        CreatureList.remove(i)


MATING_VALUE = 0

Min_Pollution = random.randint(1, 2000)
print(f'Min Pollution:{Min_Pollution}')
MESSAGE = True
DISEASE = False
HUNTED_LIST = []
NUMBER = 1
FOX_LIST = []
RABBIT_LIST = []
FINAL_HUNTED_LIST = []
RABBIT = {}
FOX = {}
INIT_FOX_POP = 20
INIT_RABBIT_POP = 10
FORESTRY = 10000
GENERATIONS = 2
GENDER = ['Male', 'Female']
x = 0

print('Initial Population Details:')
print(f'Original Fox Population: {INIT_FOX_POP}')
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
    for NUMERO in range(5):
        for g in RABBIT_LIST:
            if g['Dead'] == True:
                x += 1
    for NUMERO in range(5):
        for f in FOX_LIST:
            if f['Dead'] == True:
                FOX_LIST.remove(f)

    Hunger_Reset(FOX_LIST)
    Hunger_Reset(RABBIT_LIST)
    GENERATION_INFO = {}
    CURRENT_GENERATION = i + 1
    # Foxes
    TOTAL_RABBITS = len(RABBIT_LIST)
    TOTAL_FOXES = len(FOX_LIST)
    Aging(FOX_LIST)

    for a in FOX_LIST:
        if a['Age'] >= 4:
            a.update({'Maturity': 'Adult'})
        else:
            a.update({'Maturity': 'Child'})

    for b in FOX_LIST:
        if b['Hunger'] >= 2:
            FOX_OFFSPRING_NUM = random.randint(3, 6)
            for b in range(FOX_OFFSPRING_NUM):
                Mating(CURRENT_GENERATION, FOX_LIST, 'FOX')

    # Rabbits
    # MatureClear(RABBIT_LIST,MATURE_RABBIT_LIST)

    for d in RABBIT_LIST:
        RABBIT_OFFSPRING_NUM = random.randint(1, 16)
        for d in range(RABBIT_OFFSPRING_NUM):
            Mating(CURRENT_GENERATION, RABBIT_LIST, 'RABBIT')
    Aging(RABBIT_LIST)
    Infection(FOX_LIST, Min_Pollution, MESSAGE, DISEASE)
    Infection(RABBIT_LIST, Min_Pollution, MESSAGE, DISEASE)
    InfectionSpread(FOX_LIST)
    InfectionSpread(RABBIT_LIST)

    Hunting(FOX_LIST, RABBIT_LIST)
    FORESTRY = Eating(RABBIT_LIST, FORESTRY)
    Starvation(RABBIT_LIST)
    Starvation(FOX_LIST)
    OldAge(FOX_LIST, 7, MATING_VALUE)
    OldAge(RABBIT_LIST, 4, MATING_VALUE)
    InfectionKill(FOX_LIST)
    InfectionKill(RABBIT_LIST)
    for f in FOX_LIST:
        if f['Dead'] == True:
            FOX_LIST.remove(f)

    for g in RABBIT_LIST:
        if g['Dead'] == True:
            RABBIT_LIST.remove(g)

    FOREST_GROWTH = random.uniform(1, 3)

    if FORESTRY <= 50000:
        FORESTRY = FORESTRY + 750
        FORESTRY = int(FORESTRY * FOREST_GROWTH)

    # Data
    NET_FOX_CHANGE = len(FOX_LIST)-TOTAL_FOXES
    NET_RABBIT_CHANGE = len(RABBIT_LIST)-TOTAL_RABBITS

    print(f'there is {TOTAL_FOXES} foxes in generation {CURRENT_GENERATION}')
    print(
        f'there is {TOTAL_RABBITS} rabbits in generation {CURRENT_GENERATION}')
    print(f'There is {FORESTRY} forestry')
    RABBIT_HUNGER_LIST = []
    FOX_HUNGER_LIST = []
    for l in FOX_LIST:
        FOX_HUNGER_LIST.append(l['Hunger'])
    for p in RABBIT_LIST:
        RABBIT_HUNGER_LIST.append(p['Hunger'])
    if FOX_LIST and RABBIT_LIST:
        print(
            f'The average hunger of foxes in generation {CURRENT_GENERATION} is : {sum(FOX_HUNGER_LIST)/len(FOX_HUNGER_LIST)}')
        print(
            f'The average hunger of rabbits in generation {CURRENT_GENERATION} is : {sum(RABBIT_HUNGER_LIST)/len(RABBIT_HUNGER_LIST)}')
        print(
            f'The number of rabbits hunted in generation {CURRENT_GENERATION} is {len(HUNTED_LIST)}')

    print('')

    print(f'Net change in foxes = {NET_FOX_CHANGE}')
    print(f'Net change in rabbits = {NET_RABBIT_CHANGE}')
    print('')
    RABBIT_HUNGER_LIST = []
    FOX_HUNGER_LIST = []
    # FINAL_HUNTED_LIST.append(sum(HUNTED_LIST))
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
    print(
        f'the final average hunger of foxes  is : {sum(FOX_HUNGER_LIST)/len(FOX_HUNGER_LIST)}')
    print(
        f'the final average hunger of rabbits is : {sum(RABBIT_HUNGER_LIST)/len(RABBIT_HUNGER_LIST)}')
    print(f'the final number of rabbits hunted is {sum(FINAL_HUNTED_LIST)}')
    print(
        f'Final Fox Favorability = {sum(FOX_FAVORABILITY_LIST)/len(FOX_FAVORABILITY_LIST)}')
ANIMAL_LIST = FOX_LIST + RABBIT_LIST
# print(FOX_LIST)
PICKING = True
while PICKING:
    CHOICE_ONE = input('Would you like to sort through the Animals? ')
    if CHOICE_ONE == 'Yes' or CHOICE_ONE == 'yes':
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
