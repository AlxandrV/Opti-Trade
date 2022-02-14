import csv

from itertools import combinations
from prettytable import PrettyTable

BUDGET = 500
FILE_ACTION = 'actions.csv'

# Convert file CSV to array
with open(FILE_ACTION, 'r') as file:
    csvFile = csv.reader(file)
    header = next(csvFile)

    actionsList = [action for action in csvFile]
    for actions in actionsList:
        actions.append(float(actions[1]) * (float(actions[2]) / 100))

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
                # print(sum(budgetComb))
                combsActions.append(comb)

print('Combinaisons possibles : ' + str(len(combsActions)))

for comb in combsActions:
    benefComb = [float(actions[3]) for actions in comb]
    print(sum(benefComb))

# Print all combinations
# for i in range(1, len(combsActions)+1):
#     print("Combinaison possible n°" + str(i) + " :")
#     combsPrettyTable = PrettyTable(["Actions name", "Price (€)", "Profits (%)", "Profits in 2 years (€)"])
#     for actions in combsActions[i-1]:
#         if len(actions) == 4:
#             actions.pop(-1)
#         actions.append(round(int(actions[1]) / 100 * int(actions[2]), 2))
#         combsPrettyTable.add_row([elem for elem in actions])
#     # print(combsPrettyTable)