import networkx as nx
from gene_network.cli import main


def test_cli_happy_path(tmp_path, monkeypatch):
    # --- prepare fake input file ---
    input_file = tmp_path / "edges.csv"
    input_file.write_text("A,B\n")

    output_file = tmp_path / "graph.graphml"

    # --- mock dependencies ---
    def mock_return_edge_list(path):
        assert path == str(input_file)
        return [("A", "B", "unspecified", "unspecified")]

    def mock_build_graph(edges):
        G = nx.Graph()
        G.add_edge("A", "B")
        return G

    def mock_annotate_graph(graph):
        graph.nodes["A"]["degree"] = 1
        graph.nodes["B"]["degree"] = 1

    def mock_write_graphml(graph, path):
        assert path == str(output_file)
        assert graph.has_edge("A", "B")
        path_obj = tmp_path / "graph.graphml"
        path_obj.write_text("dummy graphml")

    monkeypatch.setattr(
        "gene_network.cli.return_edge_list", mock_return_edge_list
    )
    monkeypatch.setattr(
        "gene_network.cli.build_graph_from_edges", mock_build_graph
    )
    monkeypatch.setattr(
        "gene_network.cli.annotate_graph_with_degree", mock_annotate_graph
    )
    monkeypatch.setattr(
        "gene_network.cli.write_graphml", mock_write_graphml
    )

    # --- run CLI ---
    main([
        "--input", str(input_file),
        "--output", str(output_file),
    ])

    # --- verify output ---
    assert output_file.exists()
