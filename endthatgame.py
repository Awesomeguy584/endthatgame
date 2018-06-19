import os
import subprocess
import csv

print('EndThatGame V1.0\n')

if os.name == 'nt':
    with open('games.csv', 'r') as games:
        gamesreader = csv.reader(games)
        for line in gamesreader:
            subprocess.run(['taskkill', '/f', '/im', line])
else:
    print('OS not supported.')
