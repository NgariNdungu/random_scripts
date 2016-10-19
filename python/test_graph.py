import unittest
import graph

class TestGraph(unittest.TestCase):
    
    def test_graph_has_vertex_class(self):
        """ graph should have a vertex class"""
        self.assertTrue(hasattr(graph, 'Vertex'), "graph should have a vertex")
        

if __name__ == "__main__":
    unittest.main()
