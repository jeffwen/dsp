## Advanced Python    

###Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference. 

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

###Part I - Regular Expressions  


####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.
```python
In [5]: num_degrees(data)
There are 7 different degrees. (note that '0' is counted as not having a degree)
Out[5]: 
defaultdict(int,
            {'0': 1,'BSEd': 1,'JD': 1,'MA': 1,'MD': 1,'MPH': 2,'MS': 2,'PhD': 31,'ScD': 6})
```

####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

```python
In [6]: num_titles(data)
There are 3 different titles.
Out[6]: 
defaultdict(int,
            {'Assistant Professor': 12,'Associate Professor': 12,'Professor': 13})
```

####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

```python
def email_addresses(dataframe):
    emails = list(dataframe['email'])
    return emails
```
	
```python
Out[492]: 
['bellamys@mail.med.upenn.edu','warren@upenn.edu','bryanma@upenn.edu','jinboche@upenn.edu','sellenbe@upenn.edu','jellenbe@mail.med.upenn.edu','ruifeng@upenn.edu','bcfrench@mail.med.upenn.edu','pgimotty@upenn.edu','wguo@mail.med.upenn.edu','hsu9@mail.med.upenn.edu','rhubb@mail.med.upenn.edu','whwang@mail.med.upenn.edu','mjoffe@mail.med.upenn.edu','jrlandis@mail.med.upenn.edu','liy3@email.chop.edu','mingyao@mail.med.upenn.edu','hongzhe@upenn.edu','rlocalio@upenn.edu','nanditam@mail.med.upenn.edu','knashawn@mail.med.upenn.edu','propert@mail.med.upenn.edu','mputt@mail.med.upenn.edu','sratclif@upenn.edu','michross@upenn.edu','jaroy@mail.med.upenn.edu','msammel@cceb.med.upenn.edu','shawp@upenn.edu','rshi@mail.med.upenn.edu','hshou@mail.med.upenn.edu','jshults@mail.med.upenn.edu','alisaste@mail.med.upenn.edu','atroxel@mail.med.upenn.edu','rxiao@mail.med.upenn.edu','sxie@mail.med.upenn.edu','dxie@upenn.edu','weiyang@mail.med.upenn.edu']
```

####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

```python
In [240]: email_domains(data)
There are 4 different email domains.
Out[240]: ['email.chop.edu', 'upenn.edu', 'cceb.med.upenn.edu', 'mail.med.upenn.edu']
```

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

###Part II - Write to CSV File

####Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

---

### Part III - Dictionary

####Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [\
              ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
              ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']
                            ],
              'Li': [\
              ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
              ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
              ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
                            ]
							}
```
			
```python
In [321]: faculty_dict
Out[321]: 
{'Bellamy': [['Sc.D.', 'Associate Professor', 'bellamys@mail.med.upenn.edu']],
 'Bilker': [['Ph.D.', 'Professor', 'warren@upenn.edu']],
 'Bryan': [['PhD', 'Assistant Professor', 'bryanma@upenn.edu']]...}
```
 
####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'],\
                ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'],\
                ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'],\
                ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'],\
                ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']
            }
```

```python
In [21]: professor_dict
Out[21]: 
{('Alisa', 'Stephens'): ['Ph.D.','Assistant Professor','alisaste@mail.med.upenn.edu'],
 ('Andrea', 'Troxel'): ['ScD', 'Professor', 'atroxel@mail.med.upenn.edu'],
 ('Benjamin', 'French'): ['PhD','Associate Professor','bcfrench@mail.med.upenn.edu']...}
```

####Q8.  It looks like the current dictionary is printing by first name.  Sort by last name and print the first 3 key and value pairs.  

```python
In [37]: ordered_prof_dict
Out[37]: 
OrderedDict([(('Scarlett', 'Bellamy'),
              ['Sc.D.', 'Associate Professor', 'bellamys@mail.med.upenn.edu']),
             (('Warren', 'Bilker'),
              ['Ph.D.', 'Professor', 'warren@upenn.edu']),
             (('Matthew', 'Bryan'),
              ['PhD', 'Assistant Professor', 'bryanma@upenn.edu']),
```
			  
Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

