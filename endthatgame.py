import os

task = input()

if os.name == 'nt':
    os.system('taskkill /f /im ' + task)

input()
