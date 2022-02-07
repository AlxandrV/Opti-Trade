import csv

BUDGET = 500
FILE_ACTION = 'actions.csv'

with open(FILE_ACTION, 'r') as file:
    csvFile = csv.reader(file)
    header = next(csvFile)

    actionList = [action for action in csvFile]

# print(sum([int(price[1]) for price in actionList]))

