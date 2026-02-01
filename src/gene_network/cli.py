import argparse
from gene_network.io import read_edge_list
from gene_network.io import write_graphml
from gene_network.builder import build_graph_from_edges
from gene_network.annotate import annotate_graph_with_degree

def parse_args():
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
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    
    # Read edge list from input file
    edges = read_edge_list(args.input)
    
    # Build graph from edge list
    graph = build_graph_from_edges(edges)
    
    # Annotate graph with degree information
    annotate_graph_with_degree(graph)
    
    # Write annotated graph to output file
    write_graphml(graph, args.output)