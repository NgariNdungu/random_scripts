""" Test implementation of the graph data structure in python
Done following tutorial at https://interactivepython.org/runestone/static/pythonds/Graphs/toctree.html
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
        
    def getNeighbours(self):
        return self.neighbours
    
