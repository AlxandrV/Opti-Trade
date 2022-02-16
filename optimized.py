import csv

from prettytable import PrettyTable

BUDGET = 500
FILE_ACTION = 'actions.csv'

# Convert file CSV to array
with open(FILE_ACTION, 'r') as file:
    csvFile = csv.reader(file)
    header = next(csvFile)

    actionsList = [action for action in csvFile]
    for actions in actionsList:
        actions.append(round(float(actions[1]) * (float(actions[2]) / 100), 2))

actionsSorted = sorted(actionsList, key=lambda row: float(row[2]), reverse=True)

# Optimize the best combinations, sort by profits and if breakpoint sort by benefits
optimizeComb = []
for actions in actionsSorted:
    optimizeComb.append(actions)
    if sum([float(actions[1]) for actions in optimizeComb]) > BUDGET:
        optimizeComb.pop(-1)
        benefitsSorted = sorted(actionsSorted, key=lambda row: float(row[3]), reverse=True)
        for benef in benefitsSorted:
            if benef not in optimizeComb:
                optimizeComb.append(benef)
                if sum([float(actions[1]) for actions in optimizeComb]) > BUDGET:
                    optimizeComb.pop(-1)
        break
    
# Print all combinations
combsPrettyTable = PrettyTable(["Actions name", "Price (€)", "Profits (%)", "Benefits in 2 years (€)"])
for actions in optimizeComb:
    combsPrettyTable.add_row([elem for elem in actions])
print(combsPrettyTable)
print("Bénéfice total en 2 ans : " + str(round(sum([float(actions[3]) for actions in optimizeComb]), 2)) + "€\n"
    "Budget total : " + str(round(sum([float(actions[1]) for actions in optimizeComb]), 2)) + "€")