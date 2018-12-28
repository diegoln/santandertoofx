#!/usr/bin/python3

import csv
from datetime import datetime
import re

transaction_pattern = re.compile("(\s*(\d{2}\/\d{2})\s+([\w\s\*\-]{25})\s+(PARC\s+(\d{2}\/\d{2}))?\s+([\d,\-\.]+))")

with open('ynab_input.csv', mode='w') as ynab_input, open("fatura.txt", "r") as fatura_txt:
    ynab_writer = csv.writer(ynab_input, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    ynab_writer.writerow(['Date', 'Payee', 'Memo','Outflow','Inflow'])

    for line in fatura_txt:
        for match in transaction_pattern.finditer(line):
            date = datetime.strptime(match.group(2), '%d/%m').strftime('%m/%d/') + datetime.today().strftime('%Y')
            payee = match.group(3).strip()
            transaction_value = match.group(6).replace(".","").replace(",",".")
            installment = match.group(4)
            ynab_writer.writerow([date, payee, installment, transaction_value,''])
