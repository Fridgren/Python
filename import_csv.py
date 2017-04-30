import csv

exampleFile = open('/Users/Cedric/Desktop/Python/automate_online-materials/example.csv')
exampleReader = csv.reader(exampleFile)

for row in exampleReader:
        print('Row #' + str(exampleReader.line_num) + ' ' + str(row))