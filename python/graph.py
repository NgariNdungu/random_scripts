""" Test implementation of the graph data structure in python

Done following tutorial at https://interactivepython.org/runestone/static/pythonds/Graphs/toctree.html

Methods:
    addNeighbour
    getConnections
    getId
    getWeight
    __str__
"""

class Vertex(object):
    """ Create new vertex """
    
    def __init__(self, name):
        """ Create new named Vertex """
        
        self.name = name
        self.neighbours = {}
        
    def addNeighbour(self, neighbour, weight):
        self.neighbours[neighbour] = weight
        return "New neighbour {} added".format(neighbour)
        
    def getConnections(self):
        return self.neighbours.keys()
        
    def getId(self):
        return self.name 
        
    def getWeight(self, neighbour):
        return self.neighbours[neighbour]
        
    def __str__(self):
        return "{0} connected to {1}".format(self.name, [nbr for nbr in self.neighbours])
    
