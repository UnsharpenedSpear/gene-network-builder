import pytest
import networkx as nx
from gene_network.io import (
    return_edge_list,
    write_graphml,
    graph_to_edge_list,
    write_edge_list,
)

UNSPEC = "unspecified"


# ---------- return_edge_list (CSV / TSV) ----------

def test_csv_two_columns_defaults(tmp_path):
    f = tmp_path / "edges.csv"
    f.write_text("a,b\n")

    edges = return_edge_list(f)

    assert edges == [("A", "B", UNSPEC, UNSPEC)]


def test_csv_four_columns_preserved(tmp_path):
    f = tmp_path / "edges.csv"
    f.write_text("a,b,physical,BioGRID\n")

    edges = return_edge_list(f)

    assert edges == [("A", "B", "physical", "BioGRID")]


def test_tsv_two_columns_defaults(tmp_path):
    f = tmp_path / "edges.tsv"
    f.write_text("a\tb\n")

    edges = return_edge_list(f)

    assert edges == [("A", "B", UNSPEC, UNSPEC)]


def test_comments_and_blank_lines_ignored(tmp_path):
    f = tmp_path / "edges.csv"
    f.write_text(
        "# comment\n"
        "\n"
        "a,b\n"
    )

    edges = return_edge_list(f)

    assert edges == [("A", "B", UNSPEC, UNSPEC)]


def test_invalid_column_count_raises(tmp_path):
    f = tmp_path / "edges.csv"
    f.write_text("a,b,c,d,e\n")

    with pytest.raises(ValueError):
        return_edge_list(f)


def test_unsupported_extension_raises(tmp_path):
    f = tmp_path / "edges.txt"
    f.write_text("a,b\n")

    with pytest.raises(ValueError):
        return_edge_list(f)


# ---------- graph_to_edge_list ----------

def test_graph_to_edge_list_basic():
    G = nx.Graph()
    G.add_edge("a", "b")
    G.add_edge("c", "d")

    edges = graph_to_edge_list(G)

    assert edges == [("A", "B"), ("C", "D")]


def test_graph_to_edge_list_sorted():
    G = nx.Graph()
    G.add_edge("c", "d")
    G.add_edge("a", "b")

    edges = graph_to_edge_list(G)

    assert edges == [("A", "B"), ("C", "D")]


# ---------- write_edge_list ----------

def test_write_edge_list_csv(tmp_path):
    edges = [("A", "B"), ("C", "D")]
    out = tmp_path / "out.csv"

    write_edge_list(edges, out)

    assert out.read_text() == "A,B\nC,D\n"


def test_write_edge_list_tsv(tmp_path):
    edges = [("A", "B"), ("C", "D")]
    out = tmp_path / "out.tsv"

    write_edge_list(edges, out)

    assert out.read_text() == "A\tB\nC\tD\n"


def test_write_edge_list_unsupported_extension(tmp_path):
    edges = [("A", "B")]
    out = tmp_path / "out.txt"

    with pytest.raises(ValueError):
        write_edge_list(edges, out)


# ---------- write_graphml ----------

def test_write_graphml_creates_file(tmp_path):
    G = nx.Graph()
    G.add_edge("A", "B")

    out = tmp_path / "graph.graphml"
    write_graphml(G, out)

    assert out.exists()
    assert out.stat().st_size > 0
