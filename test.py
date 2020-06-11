import networkx
from networkx.algorithms import isomorphism

if __name__=="__main__":
    G1 = networkx.DiGraph([(1,2), (2,4), (5,6), (6,8)])
    networkx.set_edge_attributes(G1, {(1, 2):{"type":"inh"}, (2,4):{"type":"ass"}})
    networkx.set_edge_attributes(G1, {(5, 6): {"type": "inh"}, (6, 8): {"type": "ass"}})
    G2 = networkx.DiGraph([("asghar","akbar"), ("akbar","ali")])
    networkx.set_edge_attributes(G2, {(1, 2):{"type":"inh"}, (2,4):{"type":"ass"}})
    x = isomorphism.DiGraphMatcher(G1, G2)
    print(list(x.subgraph_isomorphisms_iter()))
    print(G1)