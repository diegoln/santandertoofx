#!/usr/bin/python3

import csv
from datetime import datetime
import ntpath
import os
import re
import sys

if len(sys.argv) != 2:
    sys.exit('Missing argument: Santander PDF file.')

input_basename = ntpath.basename(sys.argv[1])

password = raw_input('Enter password for file ' + input_basename + '\n')

input_basename = re.sub('\.pdf', '', input_basename, flags=re.IGNORECASE)

text_file = ('/tmp/' + input_basename + '.txt')

os.system('pdftotext -layout -upw ' + password + ' ' + sys.argv[1] + ' ' + text_file)

transaction_pattern = re.compile("(\s*(\d{2}\/\d{2})\s+([\w\s\*\-]{25})\s+(PARC\s+(\d{2}\/\d{2}))?\s+([\d,\-\.]+))")

output_file = 'ynab_' + input_basename + '.csv'

with open(output_file, mode='w') as ynab_output, open(text_file, "r") as fatura_txt:
    ynab_writer = csv.writer(ynab_output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    ynab_writer.writerow(['Date', 'Payee', 'Memo', 'Outflow', 'Inflow'])

    for line in fatura_txt:
        for match in transaction_pattern.finditer(line):
            date = datetime.strptime(match.group(2), '%d/%m').strftime('%m/%d/') + datetime.today().strftime('%Y')
            payee = match.group(3).strip()
            transaction_value = match.group(6).replace(".", "").replace(",", ".")
            installment = match.group(4)
            ynab_writer.writerow([date, payee, installment, transaction_value, ''])