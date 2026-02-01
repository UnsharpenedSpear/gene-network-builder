import pytest
import networkx as nx
from gene_network.builder import (
    build_graph_from_edges,
    remove_self_loops,
    graph_summary,
)

UNSPEC = "unspecified"


# ---------- build_graph_from_edges ----------

def test_build_graph_single_edge():
    edges = [("A", "B", UNSPEC, UNSPEC)]

    G = build_graph_from_edges(edges)

    assert isinstance(G, nx.Graph)
    assert G.number_of_nodes() == 2
    assert G.number_of_edges() == 1
    assert G.has_edge("A", "B")
    assert G.edges["A", "B"]["interaction_type"] == UNSPEC
    assert G.edges["A", "B"]["source"] == UNSPEC


def test_build_graph_multiple_edges():
    edges = [
        ("A", "B", "physical", "BioGRID"),
        ("B", "C", "genetic", "STRING"),
    ]

    G = build_graph_from_edges(edges)

    assert G.number_of_nodes() == 3
    assert G.number_of_edges() == 2
    assert G.edges["A", "B"]["interaction_type"] == "physical"
    assert G.edges["B", "C"]["source"] == "STRING"


def test_build_graph_duplicate_edges():
    edges = [
        ("A", "B", UNSPEC, UNSPEC),
        ("A", "B", UNSPEC, UNSPEC),
    ]

    G = build_graph_from_edges(edges)

    assert G.number_of_edges() == 1


def test_build_graph_rejects_non_4_tuple():
    edges = [("A", "B")]

    with pytest.raises(ValueError):
        build_graph_from_edges(edges)


def test_build_graph_empty_edge_list():
    G = build_graph_from_edges([])

    assert G.number_of_nodes() == 0
    assert G.number_of_edges() == 0


# ---------- remove_self_loops ----------

def test_remove_self_loops_removes_only_self_edges():
    edges = [
        ("A", "A", UNSPEC, UNSPEC),
        ("A", "B", UNSPEC, UNSPEC),
    ]

    G = build_graph_from_edges(edges)
    G = remove_self_loops(G)

    assert ("A", "A") not in G.edges
    assert ("A", "B") in G.edges


def test_remove_self_loops_no_self_loops_present():
    edges = [
        ("A", "B", UNSPEC, UNSPEC),
        ("B", "C", UNSPEC, UNSPEC),
    ]

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
    edges = [
        ("A", "B", UNSPEC, UNSPEC),
        ("B", "C", UNSPEC, UNSPEC),
    ]

    G = build_graph_from_edges(edges)
    summary = graph_summary(G)

    assert summary == {
        "num_nodes": 3,
        "num_edges": 2,
    }


def test_graph_summary_after_self_loop_removal():
    edges = [
        ("A", "A", UNSPEC, UNSPEC),
        ("A", "B", UNSPEC, UNSPEC),
    ]

    G = build_graph_from_edges(edges)
    G = remove_self_loops(G)

    summary = graph_summary(G)

    assert summary["num_nodes"] == 2
    assert summary["num_edges"] == 1


def test_graph_summary_empty_graph():
    G = nx.Graph()

    summary = graph_summary(G)

    assert summary == {
        "num_nodes": 0,
        "num_edges": 0,
    }
