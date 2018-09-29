#!/usr/local/bin/python3

import sys
import xlrd
import csv

wb = xlrd.open_workbook(sys.argv[1])
sh = wb.sheet_by_name(sys.argv[2])
your_csv_file = open(sys.argv[3], 'w', encoding='utf8')
wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

for rownum in range(sh.nrows):
    wr.writerow(sh.row_values(rownum))

your_csv_file.close()

