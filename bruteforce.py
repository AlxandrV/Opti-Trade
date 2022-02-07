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


# Determine minimum entry for budget
actionsSorted = sorted(actionsList, key=lambda row: int(row[1]))
minRes = []
for actions in actionsSorted:
    if sum(minRes) >= BUDGET:
        break
    else:
        minRes.append(int(actions[1]))
        if sum(minRes) > BUDGET:
            minRes.pop(-1)


# Generate all combinations of actions
combsActions = []
for i in range(len(minRes), len(actionsList)+1):
    for comb in combinations(actionsList, i):
        actionsPrice = []
        for actions in comb:
            actionsPrice.append(int(actions[1]))
        if sum(actionsPrice) <= BUDGET:
            # print(sum(actionsPrice))
            combsActions.append(comb)

# Print all combinations
for i in range(1, len(combsActions)+1):
    print("Combinaison possible n°" + str(i) + " :")
    combsPrettyTable = PrettyTable(["Actions name", "Price (€)", "Profits (%)", "Profits en 2 ans (€)"])
    # actionsPrice = [actions for actions in comb]
    for actions in combsActions[i-1]:
        actions.append(actions[1] / 100 * actions[2])
        combsPrettyTable.add_row([elem for elem in actions])
        # actionsPrice.append(int(actions[1]))
    print(combsPrettyTable)

