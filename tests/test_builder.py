import networkx as nx
from gene_network.builder import (
    build_graph_from_edges,
    remove_self_loops,
    graph_summary,
)

# ---------- build_graph_from_edges ----------

def test_build_graph_single_edge():
    edges = [("X", "Y")]
    G = build_graph_from_edges(edges)

    assert isinstance(G, nx.Graph)
    assert G.number_of_nodes() == 2
    assert G.number_of_edges() == 1
    assert set(G.nodes) == {"X", "Y"}
    assert set(G.edges) == {("X", "Y")}


def test_build_graph_duplicate_edges():
    edges = [("A", "B"), ("A", "B"), ("B", "A")]
    G = build_graph_from_edges(edges)

    assert G.number_of_nodes() == 2
    assert G.number_of_edges() == 1
    assert G.has_edge("A", "B")


def test_build_graph_with_self_loops():
    edges = [("A", "A"), ("A", "B")]
    G = build_graph_from_edges(edges)

    # build_graph_from_edges does NOT remove self-loops
    assert ("A", "A") in G.edges
    assert ("A", "B") in G.edges


def test_build_graph_empty_edge_list():
    G = build_graph_from_edges([])

    assert G.number_of_nodes() == 0
    assert G.number_of_edges() == 0


# ---------- remove_self_loops ----------

def test_remove_self_loops_removes_only_self_edges():
    edges = [("A", "A"), ("A", "B"), ("B", "B")]
    G = build_graph_from_edges(edges)

    G = remove_self_loops(G)

    assert ("A", "A") not in G.edges
    assert ("B", "B") not in G.edges
    assert ("A", "B") in G.edges


def test_remove_self_loops_no_self_loops():
    edges = [("A", "B"), ("B", "C")]
    G = build_graph_from_edges(edges)

    G2 = remove_self_loops(G)

    assert set(G2.edges) == {("A", "B"), ("B", "C")}


def test_remove_self_loops_empty_graph():
    G = nx.Graph()

    G = remove_self_loops(G)

    assert G.number_of_nodes() == 0
    assert G.number_of_edges() == 0


# ---------- graph_summary ----------

def test_graph_summary_basic():
    edges = [("A", "B"), ("B", "C")]
    G = build_graph_from_edges(edges)

    summary = graph_summary(G)

    assert summary == {
        "num_nodes": 3,
        "num_edges": 2,
    }


def test_graph_summary_after_self_loop_removal():
    edges = [("A", "A"), ("A", "B")]
    G = build_graph_from_edges(edges)

    G = remove_self_loops(G)
    summary = graph_summary(G)

    assert summary["num_nodes"] == 2
    assert summary["num_edges"] == 1


def test_graph_summary_empty_graph():
    G = nx.Graph()

    summary = graph_summary(G)

    assert summary["num_nodes"] == 0
    assert summary["num_edges"] == 0
