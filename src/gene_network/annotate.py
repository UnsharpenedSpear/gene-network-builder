import networkx as nx

def annotate_graph_with_degree(graph: nx.Graph) -> None:
    for node in graph.nodes():
        graph.nodes[node]['degree'] = graph.degree(node)