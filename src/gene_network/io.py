from pathlib import Path

def read_edge_list(path) -> list[tuple[str, str]]:
    """Reads an edge list from a file and returns it as a list of tuples."""
    filetype = Path(path).suffix.lower()
    if filetype == ".csv":
        return _read_csv_edge_list(path)
    elif filetype == ".tsv":
        return _read_tsv_edge_list(path)
    else:
        raise ValueError(f"Unsupported file type: {filetype}")

def _read_csv_edge_list(path) -> list[tuple[str, str]]:
    edges = []
    with open(path, 'r') as file:
        for line in file:
            if line.startswith('#') or not line.strip():
                continue
            if line.count(',') != 1:
                raise ValueError(f"Invalid CSV format in line: {line.strip()}")
            src, dst = line.strip().split(',')
            edges.append((src.strip().upper(), dst.strip().upper()))
    return edges

def _read_tsv_edge_list(path) -> list[tuple[str, str]]:
    edges = []
    with open(path, 'r') as file:
        for line in file:
            if line.startswith('#') or not line.strip():
                continue
            if line.count('\t') != 1:
                raise ValueError(f"Invalid TSV format in line: {line.strip()}")
            src, dst = line.strip().split('\t')
            edges.append((src.strip().upper(), dst.strip().upper()))
    return edges

def write_graphml(graph, path) -> None:
    """Writes a NetworkX graph to a GraphML file."""
    import networkx as nx
    nx.write_graphml(graph, path)

def graph_to_edge_list(graph) -> list[tuple[str, str]]:
    """Converts a NetworkX graph to an edge list."""
    return sorted([(str(u).upper(), str(v).upper()) for u, v in graph.edges()])

def write_edge_list(edges: list[tuple[str, str]], path) -> None:
    """Writes an edge list to a file in CSV or TSV format based on the file extension."""
    filetype = Path(path).suffix.lower()
    delimiter = ',' if filetype == '.csv' else '\t' if filetype == '.tsv' else None
    if delimiter is None:
        raise ValueError(f"Unsupported file type: {filetype}")
    
    with open(path, 'w') as file:
        for src, dst in edges:
            file.write(f"{src}{delimiter}{dst}\n")