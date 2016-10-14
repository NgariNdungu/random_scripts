""" Read the users .bash_history file and return command counts and 
percentages 
"""

import os

history_file = os.path.join(os.getenv('HOME'), ".bash_history")
commands = {}
command_count = 0
unique_command_count = 0 
with open(history_file, 'r') as history:
    for line in history.readlines():
        command_count += 1
        if len(line.split()) > 0: # handle blank lines
            if line.split()[0] == 'sudo': # handle super user commands
                command = "{0} {1}".format(line.split()[0], line.split()[1])
            else:    
                command = line.split()[0]
        if command not in commands.keys():
            commands[command] = 1
            unique_command_count += 1
        else:
            commands[command] += 1
 
for key in commands.keys():
    percentage = round(commands[key]/command_count * 100, 2)
    commands[key] = {
        "count": commands[key],
        "percentage": percentage
        }
        
print(commands)


    
