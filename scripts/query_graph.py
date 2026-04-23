#!/usr/bin/env python3
"""
Demo script to query the extracted FRM knowledge graph.
This demonstrates the graph-RAG capability using the extracted JSON.
"""

import json
from pathlib import Path
from collections import defaultdict

# Load the extracted graph
graph = json.loads(Path('graphify-out/.graphify_extract.json').read_text())
nodes = {n['id']: n for n in graph['nodes']}
edges = graph['edges']

print("=== FRM Knowledge Graph Query Demo ===\n")

# Helper functions
def find_nodes_by_prefix(prefix):
    """Return all nodes with ID starting with given prefix."""
    return [n for n in nodes.values() if n['id'].startswith(prefix)]

def find_connected(node_id, relation=None, direction='both'):
    """Find nodes connected to the given node."""
    connected = []
    for e in edges:
        if relation and e.get('relation') != relation:
            continue
        if direction in ('out', 'both') and e.get('source') == node_id:
            connected.append((e.get('target'), e.get('relation')))
        if direction in ('in', 'both') and e.get('target') == node_id:
            connected.append((e.get('source'), e.get('relation')))
    return connected

# Query 1: Show all Learning Objectives
print("Query 1: All Learning Objectives in the System")
print("-" * 50)
los = find_nodes_by_prefix('lo_')
for lo in los[:10]:  # Show first 10
    print(f"  • {lo['label']}")
if len(los) > 10:
    print(f"  ... and {len(los) - 10} more")
print()

# Query 2: Find all propositions for R30 Credit Risk
print("Query 2: Propositions in R30 Credit Risk Reading")
print("-" * 50)
r30_id = 'reading_r30'
if r30_id in nodes:
    props = find_connected(r30_id, relation='contains', direction='out')
    for prop_id, _ in props:
        if prop_id.startswith('prop_'):
            prop = nodes[prop_id]
            print(f"  • {prop['label'][:80]}...")
print()

# Query 3: Show framework tags
print("Query 3: Framework Tags")
print("-" * 50)
frameworks = find_nodes_by_prefix('framework_')
for fw in frameworks:
    print(f"  • {fw['label']}")
print()

# Query 4: Find error archetypes
print("Query 4: Error Archetypes")
print("-" * 50)
archetypes = find_nodes_by_prefix('archetype_')
for arch in archetypes:
    print(f"  • {arch['label']}")
print()

# Query 5: Show connections for Credit Risk domain
print("Query 5: Connections for Credit Risk Domain")
print("-" * 50)
credit_id = 'domain_credit_risk'
if credit_id in nodes:
    connected = find_connected(credit_id, direction='both')
    for node_id, relation in connected[:10]:  # Show first 10
        if node_id in nodes:
            print(f"  • {nodes[node_id]['label']} ({relation})")
    if len(connected) > 10:
        print(f"  ... and {len(connected) - 10} more connections")
print()

# Summary statistics
print("\n=== Graph Statistics ===")
print(f"Total nodes: {len(nodes)}")
print(f"Total edges: {len(edges)}")
print("\nNode types by prefix:")
prefix_counts = defaultdict(int)
for n in nodes.values():
    prefix = n['id'].split('_')[0]
    prefix_counts[prefix] += 1
for prefix, count in sorted(prefix_counts.items()):
    print(f"  {prefix}: {count}")

print("\nEdge relations:")
relation_counts = defaultdict(int)
for e in edges:
    relation_counts[e.get('relation', 'unknown')] += 1
for relation, count in sorted(relation_counts.items()):
    print(f"  {relation}: {count}")
