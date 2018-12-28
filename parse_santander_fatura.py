#!/usr/bin/python3

import csv
import datetime
import re

transaction_pattern = re.compile("(\s*(\d{2}\/\d{2})\s+([\w\s\*-]+)\s+(PARC\s+(\d{2}\/\d{2}))?\s+([\d,\-\.]+))")
installment_pattern = re.compile("(\d{2})\/\d{2}")

fatura_txt = open("fatura.txt", "r")

with open('ynab_input.csv', mode='w') as ynab_input:
    ynab_writer = csv.writer(ynab_input, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    ynab_writer.writerow(['Date', 'Payee', 'Memo','Outflow','Inflow'])

    line = fatura_txt.readline()
    while line:
        for match in transaction_pattern.finditer(line):
            transaction_date = match.group(2)
            transaction_payee = match.group(3).strip()
            transaction_value = match.group(6).replace(".","").replace(",",".")
            installment = match.group(5)
	    if (bool(installment)):
                transaction_installment = "Installment " + installment_pattern.match(installment).group(1)
            ynab_writer.writerow([transaction_date, transaction_payee, '',transaction_value,''])
        line = fatura_txt.readline()
    fatura_txt.close()
