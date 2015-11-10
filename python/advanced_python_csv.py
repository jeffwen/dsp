# Q5.  Write email addresses from Part I to csv file

# Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

# The emails.csv file you create should be added and committed to your forked repository.

# Your file, emails.csv, will look like this:
# ```
# bellamys@mail.med.upenn.edu
# warren@upenn.edu
# bryanma@upenn.edu
# ```

import csv
from advanced_python_regex import email_addresses

def emails_writer(dataframe):
    emails_list = email_addresses(dataframe)
    with open('emails.csv', 'wb') as f:
        writer = csv.writer(f)
        for email in emails_list:
            writer.writerow([email])
    print "Finished writing!"
