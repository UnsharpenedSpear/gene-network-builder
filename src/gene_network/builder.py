import networkx as nx

def build_graph_from_edges(edges: list[tuple[str, str, str, str]]) -> nx.Graph:
    """Builds a NetworkX graph from a list of edges."""

    
    G = nx.Graph()
    for edge in edges:
        if len(edge) != 4:
            raise ValueError("Edges must be (src, dst, interaction_type, source)")
        G.add_edge(edge[0], edge[1])
        G.edges[list(G.edges)[-1]]['interaction_type'] = edge[2]
        G.edges[list(G.edges)[-1]]['source'] = edge[3]
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


