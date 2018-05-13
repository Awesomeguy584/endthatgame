import os
import subprocess
import csv

if os.name == 'nt':
    with open('games.csv', 'r') as games:
        gamesreader = csv.reader(games)
        for line in gamesreader:
            subprocess.run(['taskkill', '/f', '/im', line])

input()
