class FaultWeb:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, node, fault_probability):
        self.nodes[node] = fault_probability

    def add_edge(self, node1, node2, fault_probability):
        if node1 not in self.edges:
            self.edges[node1] = {}
        self.edges[node1][node2] = fault_probability

    def get_fault_web(self):
        return {
            'nodes': self.nodes,
            'edges': self.edges
        }