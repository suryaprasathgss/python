import re
import csv

data_in = '''
12/15/21\t09:16:56\ttest control: left: 23.2 right: 54.7 test input:85.3 distance:49.5 XY1:15.0 XY2:22.8 ZX1:25.0 ZX2:28.8 MN1:18.7 MN2:18.8 PN1:26.0 PN2:84.5 test speed: 23.2
04/30/21\t11:20:38\ttest control: left: 36.2 right: 88.7 test input:87.4 distance:26.8 XY1:53.0 XY2:85.9 ZX1:95.0 ZX2:78.8 MN1:32.7 MN2:96.8 PN1:52.0 PN2:79.5 test speed: 23.2
'''

def parseRow(row):
    el = row.split("\t")
    sub_el = [item for item in re.split(":| ", el[2]) if item]
    return [
        el[0],
        el[1],
        float(sub_el[3]),
        float(sub_el[5]),
        float(sub_el[8]),
        float(sub_el[10]),
        float(sub_el[12]),
        float(sub_el[14]),
        float(sub_el[16]),
        float(sub_el[18]),
        float(sub_el[20]),
        float(sub_el[22]),
        float(sub_el[24]),
        float(sub_el[26]),
        float(sub_el[29]),
    ]

with open('output.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(parseRow(row) for row in data_in.split("\n") if row)