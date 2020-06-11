import networkx as nx

design_patterns = dict()

design_patterns["abstract_factory"] = nx.DiGraph()
design_patterns["abstract_factory"].add_nodes_from(["ConcreteFactory", "AbstractFactory", ""])