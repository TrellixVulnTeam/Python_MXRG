str = 'X-DSPM-Confidence: 0.8475'

ipos = str.find(':')
print(ipos)

piced = str[ipos+2:]
print(piced)

value = float(piced)
print(value)
# print(value+42)
print(piced+42)

