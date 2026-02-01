import networkx as nx

def build_graph_from_edges(edges: list[tuple[str, str]]) -> nx.Graph:
    """Builds a NetworkX graph from a list of edges."""

    G = nx.Graph()
    G.add_edges_from(edges)

    return G

def remove_self_loops(G: nx.Graph) -> nx.Graph:
    """Removes self edges from graph."""

    self_edges = list(nx.selfloop_edges(G))
    G.remove_edges_from(self_edges)
    
    return G

def graph_summary(G: nx.Graph) -> dict:
    """Returns a summary of the graph including number of nodes and edges."""

    return {
        "num_nodes": G.number_of_nodes(),
        "num_edges": G.number_of_edges(),
    }


