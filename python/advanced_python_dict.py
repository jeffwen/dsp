
import pandas as pd
import re
from collections import OrderedDict

def data_table(path):
    data = pd.read_csv(path,skipinitialspace = True)
    return data

def names_func(dataframe):
    names = list(dataframe['name'])
    names = [name.split(' ') for name in names]
    first_name = []
    last_name = []
    for name in names:
        last_name.append(name[-1])
        if len(name[0]) < 3:
            first_name.append(name[1])
        elif name[1][0] == '(':
            first_name.append(name[0] + name[1])
        else:
            first_name.append(name[0])
    return first_name, last_name

def titles_func(dataframe):
    raw_titles = list(dataframe['title'])
    titles = []
    for title in raw_titles:
        titles += re.findall(r'.*[\w+\sP]rofessor', title)
    return titles

def emails_func(dataframe):
    emails = dataframe['email']
    return list(emails)

# Q6.  Create a dictionary in the below format:
def q6_dict(dataframe):
    first_names, last_names = names_func(dataframe)
    titles = titles_func(dataframe)
    emails = emails_func(dataframe)
    degrees = list(dataframe['degree'])
    faculty_dict = {}
    for i in range(len(last_names)):
        faculty_dict[last_names[i]] = faculty_dict.get(last_names[i], []) + [[degrees[i], titles[i], emails[i]]]
    return faculty_dict
    

# Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:
def q7_dict(dataframe):
    first_names, last_names = names_func(dataframe)
    titles = titles_func(dataframe)
    emails = emails_func(dataframe)
    degrees = list(dataframe['degree'])
    professor_dict = {}
    for i in range(len(first_names)):
        professor_dict[(first_names[i],last_names[i])] = professor_dict.get((first_names[i],last_names[i]),[]) + [degrees[i], titles[i], emails[i]]
    return professor_dict

# Q8.  It looks like the current dictionary is printing by first name.  Sort by last name and print the first 3 key and value pairs.
data = data_table('faculty.csv')
professor_dict = q7_dict(data)
ordered_prof_dict = OrderedDict(sorted(professor_dict.items(), key = lambda x: x[0][1]))


# Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)
