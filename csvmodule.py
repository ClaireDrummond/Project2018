# Claire Drummond 2018-03-26
# Ref: Iris Data Set Exercise 5 Programming and Scripting Assessments

# ref: https://en.wikipedia.org/wiki/Iris_flower_data_set
# ref: https://pyformat.info/

import csv #importing the csv module

with open("data/iris.csv", "r") as f: #opens the data file Iris and closes it again once command has been executed
  reader = csv.reader(f) # creating a variable reader
  for line in reader:
    print(line)

with open("data/iris.csv", "r") as f:
  reader = csv.reader(f) # creating a variable reader
  for line in reader:
    print(line[4]) # this prints the 5th Varaiable of each row

with open("data/iris.csv") as f: #importing of the Iris Data Set
  for line in f:
     data = line.split(',') #creating space between the data
     print('{0[0]:12} {0[1]:12} {0[2]:12} {0[3]:12} {0[4]:12}'.format(data))

 # the formatting of the data   