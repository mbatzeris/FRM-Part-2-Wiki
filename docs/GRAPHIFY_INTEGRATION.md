# Graphify Knowledge Graph Integration

## Overview
The FRM Part 2 study system now includes a Graphify-based knowledge graph that enables graph-RAG querying of the entire curriculum. The graph captures relationships between learning objectives, readings, concepts, error archetypes, and exam domains.

## Graph Structure
- **106 nodes** across 12 categories:
  - Learning Objectives (15)
  - Concepts (25)
  - Error Archetypes (12)
  - Exam Domains (6)
  - Framework Tags (4)
  - Readings (2)
  - Propositions (15)
  - Scenarios (4)
  - Distractor Types (4)
  - Meta-doc nodes (10)
  - Roadmap concepts (9)
  - Reading-specific nodes (15)

- **190 edges** with 7 relation types:
  - `references` (123)
  - `rationale_for` (30)
  - `conceptually_related_to` (23)
  - `semantically_similar_to` (8)
  - `cites` (4)
  - `shares_data_with` (2)

## Query Examples

```python
# Load and query the graph
import json
from pathlib import Path

graph = json.loads(Path('graphify-out/.graphify_extract.json').read_text())
nodes = {n['id']: n for n in graph['nodes']}
edges = graph['edges']

# Find all LOs for Credit Risk
credit_los = [n for n in nodes.values() 
              if n['id'].startswith('lo_') and 'credit' in n['label'].lower()]

# Find error archetypes
archetypes = [n for n in nodes.values() 
              if n['id'].startswith('archetype_')]
```

## Re-extraction Process

When adding new readings or updating content:

1. **Update the wiki files** using `/new-reading` workflow
2. **Re-run extraction**:
   ```bash
   python C:\Users\user\AppData\Local\Temp\graphify_extract_part1.py
   python C:\Users\user\AppData\Local\Temp\graphify_extract_part2.py
   ```
3. **Query the updated graph** using the query script

## Files Generated
- `graphify-out/.graphify_extract.json` - Main graph structure
- `graphify-out/.graphify_semantic.json` - Semantic embeddings
- `graphify-out/.graphify_ast.json` - Code AST (empty for this project)
- `graphify-out/.graphify_chunk_01.json` - Chunked data

## Notes
- Generated files are excluded from Git via `.gitignore`
- The graph extraction focuses on markdown files only (PDFs excluded)
- Error archetypes are linked to distractor types for intelligent question generation
