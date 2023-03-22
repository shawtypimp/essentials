import csv
from datetime import datetime

oneToThreeHunna = list(range(1, 301))

current_datetime = datetime.now()

with open('rows_300.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter = ';', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    filewriter.writerow(oneToThreeHunna)
    filewriter.writerow(str(current_datetime))
    filewriter.writerow(str(current_datetime.second))
    filewriter.writerow(str(current_datetime.microsecond))





