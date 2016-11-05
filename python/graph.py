""" Test implementation of the graph data structure in python

Done following tutorial at https://interactivepython.org/runestone/static/pythonds/Graphs/toctree.html

"""

class Vertex(object):
    """ Create new vertex 
    
    Methods:
        addNeighbour
        getConnections
        getId
        getWeight
        __str__
    """
    
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
        return "{0} connected to {1}".format(self.name, [nbr.getId() for nbr in self.neighbours])
    
class Graph(object):
    """ Create new Graph 
    
    Methods:
        addVertex
        getVertex
        __contains__
        addEdge
        getVertices
        __iter__
    """
    
    def __init__(self):
        self.vertList = {} # map vertex id to vertex objects
        self.numVertices = 0
        
    def addVertex(self,key):
        """ create new vertex, add to vertex list and return new vertex """
        
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        self.numVertices += 1
        return newVertex
        
    def getVertex(self,key):
        """ check if vertex is in vertList and return it """
        
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None
    
    def addEdge(self, f, to, weight=0):
        """ create a new edge
        
        add neighbour for existing vertex or create new vertex and add neighbour
        """
        
        if f not in self.vertList:
            self.addVertex(f)
        if to not in self.vertList:
            self.addVertex(to)
        self.vertList[f].addNeighbour(self.vertList[to], weight)
        
    def getVertices(self):
        """ return a list of all vertices in the graph """
        
        return self.vertList.keys()
        
    def __contains__(self, key):
        return key in self.vertList
    
    def __iter__(self):
        return iter(self.vertList.values())
        
