#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

import sys
import random
from collections import defaultdict

# first function takes the input argument and parses the text file to create a dictionary with tuples of 2 adjacent words as keys and the following word as values
def markov(input_file):
    '''
    input_file: .txt file that will be parsed
    returns a dictionary with tuple of adjacent words as keys and the follow words as values
    '''
    with open(input_file, 'r') as myfile:
        data_file = myfile.read().replace('\n', '')
    data_split = data_file.split()
    markov_dict = defaultdict()
    # go through the text file and create key value pairs
    for i in range(2, len(data_split)):
        if (data_split[i-2], data_split[i-1]) not in markov_dict.keys():
            markov_dict[(data_split[i-2], data_split[i-1])] = [data_split[i]]
        else:
            markov_dict[(data_split[i-2], data_split[i-1])].append(data_split[i])
    return markov_dict

# this function generates sentences from the previously generated dictionary
def sentence_gen(markov_dict, num_words):
    '''
    markov_dict: the input dictionary of a parsed text file 
    num_words: number of words desired for the output 
    returns a sentence with num_words number of words
    '''
    # only start with words that are capitalized and do not have a period following the first word (abbreviations)
    start = [key for key in markov_dict.keys() if key[0][0].isupper() and key[0][-1] != '.']

    # randomly select the starting pair of words
    sent_list = list(random.choice(start))

    # continue to randomly append words to the sentence if the sentence length is less than the number of words desired
    while len(sent_list) < num_words:
        try:
            # use the two preceding words as keys to look up the next word that should follow
            sent_list.append(random.choice(markov_dict[(sent_list[-2], sent_list[-1])]))
        except KeyError:
            sent_list += list(random.choice(markov_dict.keys()))
    print ' '.join(sent_list)

    
if __name__ == "__main__":
    markov_dict = markov(sys.argv[1])
    sentence_gen(markov_dict, int(sys.argv[2]))

## sample output
## $ python markov.py story.txt 40
## I that caught Nag by the hood last night in the morning he will tell the garden will be empty, and Rikki-tikki heard a scream from Teddy's mother. His father ran out with a whack on the rubbish-heap this morning,
