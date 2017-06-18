import unittest
import graph

class TestGraph(unittest.TestCase):

    def test_graph_has_vertex_class(self):
        """ graph should have a vertex class """
        self.assertTrue(hasattr(graph, 'Vertex'), "graph should have a vertex")

    def test_graph_has_graph_class(self):
        """ graph should have a Graph class """
        self.assertTrue(hasattr(graph, 'Graph'), "it isn't a graph if there's no Graph")

    def test_can_create_empty_graph(self):
        """ it should be possible to initialize an empty graph """
        gr = graph.Graph()
        self.assertIsInstance(gr, graph.Graph)
        self.assertTrue(gr.vertList == {})
        self.assertTrue(gr.numVertices == 0)

if __name__ == "__main__":
    unittest.main()
