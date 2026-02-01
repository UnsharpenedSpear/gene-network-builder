import argparse
from gene_network.io import return_edge_list, write_graphml
from gene_network.builder import build_graph_from_edges
from gene_network.annotate import annotate_graph_with_degree

def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Gene Network Builder CLI")
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Path to the input edge list file (CSV or TSV format).",
    )
    parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="Path to save the output annotated graph.",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)

    edges = return_edge_list(args.input)
    graph = build_graph_from_edges(edges)
    annotate_graph_with_degree(graph)
    write_graphml(graph, args.output)

if __name__ == "__main__":
    main()