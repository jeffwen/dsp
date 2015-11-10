#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


import csv
import os
import pandas as pd

suffix = os.getcwd()
os.chdir(suffix + '/python')

# One solution (less elegant?)
def read_data(data):
    reader = csv.reader(open(data,'rb'))
    data = []
    for row in reader:
        data.append([row[0],row[-3],row[-2]])
    return data[1:]

def get_min_score_difference(parsed_data):
    min_score_diff = abs(int(parsed_data[0][1])-int(parsed_data[0][2]))
    team = parsed_data[0]
    for team in parsed_data:
        if min_score_diff > abs(int(team[1])-int(team[2])):
            min_score_diff = abs(int(team[1])-int(team[2]))
            min_team = team[0]
    return min_team, min_score_diff

# Maybe better solution
def get_min_team(filename):
    data = pd.read_csv(filename)
    data['Difference'] = abs(data['Goals'] - data['Goals Allowed'])
    return data['Team'].ix[data['Difference'].idxmin()]
