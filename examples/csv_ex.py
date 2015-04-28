import csv

with open('data.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader, None)
    for row in reader:
        print row[0] + " is " + row[1] + " and likes the color " + row[2]