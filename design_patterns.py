import networkx as nx

mediator_pattern = nx.DiGraph()
mediator_pattern.add_edges_from([ (1, 2, {'type': "as"}), (3, 2, {'type': "as"}), (4, 1, {'type': "as"}), (4, 3, {'type': "as"}), (4, 2, {'type': "ge"}) ])

state_pattern = nx.DiGraph()
state_pattern.add_edges_from([ (1, 2, {'type': "as"}), (3, 2, {'type': "ge"}) ])

proxy_pattern = nx.DiGraph()
proxy_pattern.add_edges_from([ (2, 1, {'type': "ge"}), (3, 1, {'type': "ge"}), (2, 3, {'type': "as"}) ])


design_patterns = dict()

design_patterns["mediator"] = mediator_pattern
design_patterns["state"] = state_pattern
design_patterns["proxy"] = proxy_pattern