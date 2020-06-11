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
        return list(isomorphism.DiGraphMatcher(graph, design_pattern))

    def match_all(self):
        self.match_result = {name: None for name in self.design_patterns.keys()}
        for d_p in self.design_patterns:
            self.match_result[d_p] = DesignPatternMatcher.match(self.graph, self.design_patterns[d_p])
        return self.match_result

    def get_quality_value(self):
        all_classes = (self.graph.nodes)
        classes_used_in_design_pattern = 0
        return classes_used_in_design_pattern / all_classes
