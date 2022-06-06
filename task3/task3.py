lookup = {
'A': 'T',
'T': 'A',
'C': 'G',
'G': 'C'
}

import sys
file = sys.argv[1]
with open(file, 'r') as file:
    s = file.readline().strip()

sout = []
for i in s[::-1]:
    sout.append(lookup[i])

print(''.join(sout))