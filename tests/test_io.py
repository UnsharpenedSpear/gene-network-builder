import pytest
from gene_network.io import read_edge_list


# ---------- CSV TESTS ----------

def test_read_csv_basic(tmp_path):
    f = tmp_path / "edges.csv"
    f.write_text("a,b\nc,d\n")

    edges = read_edge_list(f)

    assert edges == [("A", "B"), ("C", "D")]


def test_csv_ignores_comments_and_blank_lines(tmp_path):
    f = tmp_path / "edges.csv"
    f.write_text(
        "# comment\n"
        "\n"
        "a,b\n"
    )

    edges = read_edge_list(f)

    assert edges == [("A", "B")]


def test_csv_strips_whitespace_and_uppercases(tmp_path):
    f = tmp_path / "edges.csv"
    f.write_text("  a  ,  b  \n")

    edges = read_edge_list(f)

    assert edges == [("A", "B")]


def test_csv_invalid_format_raises(tmp_path):
    f = tmp_path / "edges.csv"
    f.write_text("a,b,c\n")

    with pytest.raises(ValueError):
        read_edge_list(f)


# ---------- TSV TESTS ----------

def test_read_tsv_basic(tmp_path):
    f = tmp_path / "edges.tsv"
    f.write_text("a\tb\nc\td\n")

    edges = read_edge_list(f)

    assert edges == [("A", "B"), ("C", "D")]


def test_tsv_invalid_format_raises(tmp_path):
    f = tmp_path / "edges.tsv"
    f.write_text("a\tb\tc\n")

    with pytest.raises(ValueError):
        read_edge_list(f)


# ---------- GENERAL BEHAVIOR ----------

def test_empty_file_returns_empty_list(tmp_path):
    f = tmp_path / "edges.csv"
    f.write_text("")

    edges = read_edge_list(f)

    assert edges == []


def test_comment_only_file_returns_empty_list(tmp_path):
    f = tmp_path / "edges.tsv"
    f.write_text("# comment\n# another\n")

    edges = read_edge_list(f)

    assert edges == []


def test_unsupported_filetype_raises(tmp_path):
    f = tmp_path / "edges.txt"
    f.write_text("a,b\n")

    with pytest.raises(ValueError):
        read_edge_list(f)
