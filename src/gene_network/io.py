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


if __name__ == "__main__":
    edges = read_edge_list("example.csv")