import csv

from itertools import combinations
from prettytable import PrettyTable

BUDGET = 500
FILE_ACTION = 'actions.csv'

# Convert file CSV to array
with open(FILE_ACTION, 'r') as file:
    csvFile = csv.reader(file)
    header = next(csvFile)

    actionsList = [action for action in csvFile if float(action) > 0]
    for actions in actionsList:
        actions.append(round(float(actions[1]) * (float(actions[2]) / 100), 2))

# Determine minimum entry for budget
actionsSorted = sorted(actionsList, key=lambda row: float(row[1]), reverse=True)
combMin = []
for actions in actionsSorted:
    if sum(combMin) >= BUDGET:
        break
    else:
        combMin.append(float(actions[1]))
        if sum(combMin) > BUDGET:
            combMin.pop(-1)

# Generate all combinations of actions
combsActions = []
for i in range(len(combMin), len(actionsList)+1):
    for comb in combinations(actionsSorted, i):
        budgetComb = [float(actions[1]) for actions in comb]
        nameComb = [actions[0] for actions in comb]
        if sum(budgetComb) <= BUDGET:
            i = []
            for elementInit in actionsList:
                if nameComb.count(elementInit[0]) == 0 and float(elementInit[1]) + sum(budgetComb) <= BUDGET:
                    i.append(True)
            if len(i) == 0:
                combsActions.append({'combinations': comb, 'benefits': round(sum([float(actions[3]) for actions in comb]), 2)})

print('Combinaisons possibles : ' + str(len(combsActions)))

# Return the index of the combinations where the benefits are maximal
benefits = [combination.get('benefits') for combination in combsActions]
maxBenef = max(benefits)
indexBenef = [(index, value) for index, value in enumerate(benefits) if value == maxBenef]

# Print all combinations
for index in indexBenef:
    combsPrettyTable = PrettyTable(["Actions name", "Price (€)", "Profits (%)", "Benefits in 2 years (€)"])
    for actions in combsActions[index[0]].get('combinations'):
        combsPrettyTable.add_row([elem for elem in actions])
    print(combsPrettyTable)
    print("Bénéfice total en 2 ans : " + str(combsActions[index[0]].get('benefits')) + "€\n"
        "Budget total : " + str(sum([float(actions[1]) for actions in combsActions[index[0]].get('combinations')])) + "€")