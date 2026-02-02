# Gene–Gene Network Builder

A lightweight Python tool for constructing **biologically annotated gene–gene interaction networks** from simple edge lists, with a focus on **network biology workflows** and **interoperability** (e.g. Cytoscape).

---

## What This Tool Does

Given a simple edge list, this tool:

1. Constructs an **undirected gene–gene network**
2. Annotates edges with:
   - **interaction type** (e.g. physical, regulatory, pathway)
   - **evidence/source** (e.g. BioGRID, STRING)
3. Annotates nodes with basic network metrics:
   - degree (number of interactions)
4. Exports the network in **GraphML** (Cytoscape-ready)

---

## Input Format

The primary input is a tab- or comma-separated edge list.

### Minimal format

geneA geneB
TP53 BRCA1
BRCA1 RAD51

### Annotated format (recommended)

- geneA geneB interaction_type source
- TP53 BRCA1 physical BioGRID
- TP53 MDM2 regulatory Reactome
- BRCA1 RAD51 pathway KEGG

### Notes
- `interaction_type` is optional (default: `unspecified`)
- `source` is optional but strongly encouraged
- Gene symbols are normalized by trimming whitespace and uppercasing
- Self-edges are ignored

---

## Output

### 1. GraphML (Primary Output)
- Compatible with Cytoscape
- Preserves node and edge attributes

---

## Example Usage

- gene-network --input examples/real_edges.tsv --output network.graphml

### Load network.graphml directly into Cytoscape to explore:
- interaction types
- evidence sources
- node degree

## Biological Assumptions & Limitations

This tool makes several explicit assumptions:
- Edges represent hypotheses supported by evidence, not absolute biological truth
- Interaction types are user-provided and not inferred
- Gene identifier normalization is minimal (no alias resolution)
- The network is undirected by design for simplicity
- These choices are intentional to avoid introducing incorrect biological inferences.

## Future Extensions

Directional edges for regulatory networks

Confidence weighting based on evidence

Integration with pathway or expression datasets

Identifier mapping (HGNC ↔ Ensembl)
