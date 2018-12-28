#!/usr/bin/python3

import re

transaction_pattern = re.compile("(\s*(\d{2}\/\d{2})\s+([\w\s\*-]+)\s+(PARC\s+(\d{2}\/\d{2}))?\s+([\d,\-\.]+))")
installment_pattern = re.compile("(\d{2})\/\d{2}")

fatura_txt = open("fatura.txt", "r")

line = fatura_txt.readline()
while line:
    for match in transaction_pattern.finditer(line):
        print "---"
        print line
        print "============"
        transaction_date = match.group(2)
        transaction_payee = match.group(3)
        transaction_value = match.group(6)
        print "Date: " + transaction_date
        print "Payee: " + transaction_payee
        print "Value: " + transaction_value
        installment = match.group(5)
	if (bool(installment)):
            transaction_installment = installment_pattern.match(installment).group(1)
            print "Installment: " + transaction_installment
        print "============"
    line = fatura_txt.readline()
fatura_txt.close()
