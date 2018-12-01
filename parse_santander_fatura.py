#!/usr/bin/python3

import re

pattern = re.compile("(\s*(\d{2}\/\d{2})\s+(([\w\*-]+\s?)+)\b\s+(PARC\s+(\d{2}\/\d{2}))?\s+([\d,\-]+))")
#((\d{2}\/\d{2})\s+([\w\*]+)\s+(PARC\s+(\d{2}\/\d{2}))?\s+([\d,\-]+))+

fatura_txt = open("fatura.txt", "r")

line = fatura_txt.readline()
while line:
    print line
    print pattern.match(line)
    line = fatura_txt.readline()
fatura_txt.close()
