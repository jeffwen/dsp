# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

1. Python lists and tuples are both types of Python data structures that can be used to store information. However, while lists are mutable (can be changed), tuples are immutable (cannot be changed).
2. Only tuples work as dictionary keys because dictionary keys must be immutable. Imagine a scenario if the keys can be changed and are changed to the same key, Python would probably have difficulty figuring out which values are actually the correct ones. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

1. Lists and sets are similar in that both are used to store information.
   * Use sets to remove duplicates or check membership
   * Use list to iterate over elements 
2. Lists are ordered and can repeat while sets are unordered and unique.
3. Sets are faster for checking membership (for example, x in aSet)
   * Sets are faster than lists for finding an element because it uses an underlying hash table as its data structure while lists are arrays.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

1. Lambda expressions (or lambda forms) can be used to create anonymous functions that can be used to define functions needed on the fly. It takes any number of arguments and returns the value of a single expression.
2. Examples:

```python
In [8]: aList = [(1,'a'),(2,'c'),(3,'b')]
In [9]: sorted(aList, key = lambda x:x[1])
Out[9]:[(1, 'a'), (3, 'b'), (2, 'c')]
```

```python
In [10]: (lambda x: x**2 + 3)(3)
Out[10]: 12
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

####List Comprehension
List comprehension is a quick way to create lists. Usually it is used in situations where an operation is applied to each element of another sequence.

```python
In [12]: aStr = "hello, what is your name?"
In [13]: ' '.join([x.upper() for x in aStr.split()])
Out[13]: 'HELLO, WHAT IS YOUR NAME?'
```

```python
In [12]: values = range(10)
In [13]: [x for x in values if x %% 2 == 0]
Out[13]: [0, 2, 4, 6, 8]
```
####Filter
Filter will take a function and arguments and return only elements for which the function evaluates as `True`.

```python
In [14]: filter(lambda x: x % 2 == 0, values)
Out[14]: [0, 2, 4, 6, 8]
```
####Map
Map will take a function and arugments and call the function for each element in the argument.

```python
In [15]: map(lambda x: x % 2 == 0, values)
Out[15]: [True, False, True, False, True, False, True, False, True, False]
```
####Set Comprehension

```python
In [16]: {x for x in range(2,51) if all(x%y for y in range(2,x))}
Out[16]: {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}
```
####Dictionary Comprehension

```python
In [17]: {x: x**2 for x in range(5)}
Out[17]:  {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

```python
Out[5]: 937
```

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

```python
Out[5]: 513
```

c.
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

```python
Out[5]: 7850
```

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





