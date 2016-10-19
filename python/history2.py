""" Read the users .bash_history file and return command counts and 
percentages

A class based implementation of history.py
This is WIP. Any oversights and ugliness are solely to be blamed on the
author, and will be corrected in due time. 
"""

import os

class Commands(object):
    def __init__(self):
        """ Create and populate class variables """
        self.history_file = os.path.join(os.getenv('HOME'), ".bash_history")
        self.commands = {}
        self.command_count = 0
        self.unique_command_count = 0
        self.populateData()
        
    def populateData(self):
        """ Open history file and populate command dictionary"""
        with open(self.history_file, 'r') as history:
            for line in history.readlines():
                self.command_count += 1
                if len(line.split()) > 0: # handle blank lines
                    if line.split()[0] == 'sudo': # handle super user commands
                        command = "{0} {1}".format(line.split()[0], line.split()[1])
                    else:    
                        command = line.split()[0]
                if command not in self.commands.keys():
                    self.commands[command] = 1
                    self.unique_command_count += 1
                else:
                    self.commands[command] += 1
        
        for key in self.commands.keys():
            percentage = round(self.commands[key]/self.command_count * 100, 2)
            self.commands[key] = {
                "count": self.commands[key],
                "percentage": percentage
                }
                
    def getCount(self, com="", limit=None):
        """ Print specified command count or limit printed lines to limit"""
        if not com == "" and limit==None:
            try:
                print("{0} used {1} time(s)".format(com, self.commands[com]['count']))
            except:
                print("You don't know that command yet!")
        elif not limit==None and com=="":
            for key in self.commands:
                print("{0} used {1} time(s)".format(key, self.commands[key]['count']))
                limit = limit-1
                if limit == 0:
                    break
        else:
            print("Ignored... either command or limit, not both!")
            for key in self.commands:
                print("{0} used {1} time(s)".format(key, self.commands[key]['count']))
    
    def getPercentage(self, com):
        """ Return command usage as a percentage of the total """
        try:
            return self.commands[com]['percentage']
        except:
            return "You don't know that command yet!"
            
        
if __name__=="__main__":
    th = Commands()
    th.getCount('ls')
    print(th.getPercentage('ls'))
        



    
