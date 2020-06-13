import networkx as nx
def read_graph(file):
    g = nx.DiGraph()
    g_file = open(file, "r")
    for line in g_file:
        line_list = line.split(",")
        g.add_edge(line_list[0], line_list[1])
        nx.set_edge_attributes(g, {(line_list[0], line_list[1]): {"type" : line_list[2][:2].lower()}})
    return g