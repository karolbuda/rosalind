import sys
file = sys.argv[1]
with open(file, 'r') as file:
    s = file.readline()

print(s.count('A'), s.count('C'), s.count('G'), s.count('T'))