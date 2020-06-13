import networkx as nx
from networkx.algorithms import isomorphism
class DesignPatternMatcher:
    def __init__(self,modulde_graph=nx.DiGraph(), design_patterns= dict()):
        self.design_patterns = design_patterns
        self.graph = modulde_graph
        self.match_result = None

    def set_graph(self, graph):
        self.graph = graph

    def add_design_pattern(self, name:str, pattern_graph):
        if self.design_patterns is not None:
            self.design_patterns[name] = pattern_graph
        else:
            self.design_patterns = {name: pattern_graph}

    @classmethod
    def match(cls, graph, design_pattern):
        dgm = isomorphism.DiGraphMatcher(graph, design_pattern)
        return list(dgm.subgraph_isomorphisms_iter())

    def match_all(self):
        self.match_result = {name: None for name in self.design_patterns.keys()}
        for d_p in self.design_patterns:
            self.match_result[d_p] = DesignPatternMatcher.match(self.graph, self.design_patterns[d_p])
        return self.match_result

    def get_quality_value(self):
        all_classes = len(self.graph.nodes)
        values = list(self.match_result.values())
        flatten = lambda l: [item for sublist in l for item in sublist]
        values = flatten(values)
        classes = list(map(lambda x: set(x.keys()), values))
        classes_used_in_design_pattern = len(set().union(*classes))
        return classes_used_in_design_pattern / all_classes
