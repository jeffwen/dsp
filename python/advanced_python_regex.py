
import pandas as pd
import re
from collections import defaultdict

#Preprocessing
data = pd.read_csv('faculty.csv',skipinitialspace = True)
data['degree'] = data['degree'].str.replace('.','')

#Q1. Find how many different degrees there are, and their frequencies: Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.
def num_degrees(dataframe):
    degrees = list(set(dataframe['degree']))
    all_degrees = ' '.join(list(dataframe['degree'])).split(' ')
    count_dict = defaultdict(int)
    for i in all_degrees:
        count_dict[i] += 1
    print "There are {} different degrees. (note that '0' is counted as not having a degree)".format(len(degrees))
    return count_dict

#Q2. Find how many different titles there are, and their frequencies: Ex: Assistant Professor, Professor
def num_titles(dataframe):
    raw_titles = list(dataframe['title'])
    titles = []
    for title in raw_titles:
        titles += re.findall(r'.*[\w+\sP]rofessor', title)
    titles_count_dict = defaultdict(int)
    for title in titles:
        titles_count_dict[title] += 1
    print "There are {} different titles.".format(len(set(titles)))
    return titles_count_dict

#Q3. Search for email addresses and put them in a list. Print the list of email addresses.
def email_addresses(dataframe):
    emails = list(dataframe['email'])
    return emails

#Q4. Find how many different email domains there are (Ex: mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.). Print the list of unique email domains.
def email_domains(dataframe):
    emails = email_addresses(dataframe)
    domains = []
    for email in emails:
        domains += re.findall(r'@(.*)', email)
    print "There are {} different email domains.".format(len(list(set(domains))))
    return list(set(domains))
