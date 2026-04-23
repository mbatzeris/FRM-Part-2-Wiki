#!/usr/bin/env python3
"""
Graphify Part 2: Extract concepts, boundary tensions, scenarios, meta nodes, and merge with part 1.
"""

import json
from pathlib import Path

# Load partial state from part 1
partial = json.loads(Path('graphify-out/.graphify_partial.json').read_text())
nodes, edges = partial['nodes'], partial['edges']

# Node and edge helpers
def N(id, label, **kw):
    node = {'id': id, 'label': label, **kw}
    for k, v in list(node.items()):
        if v is None:
            del node[k]
    return node

def E(src, tgt, rel, **kw):
    edge = {'source': src, 'target': tgt, 'relation': rel, **kw}
    for k, v in list(edge.items()):
        if v is None:
            del edge[k]
    return edge

# 8. Key concepts from readings
concept_map = {
    'cva': 'Credit Valuation Adjustment (CVA)',
    'dva': 'Debit Valuation Adjustment (DVA)',
    'pd_spread': 'PD from credit spreads',
    'netting': 'Netting agreements',
    'collateral': 'Collateralization',
    'triggers': 'Downgrade triggers',
    'central_clearing': 'Central clearing',
    'credit_var': 'Credit VaR',
    'vasicek': 'Vasicek/WCDR model',
    'cds': 'Credit Default Swap',
    'cds_valuation': 'CDS valuation',
    'risk_neutral_pd': 'Risk-neutral vs real-world PD',
}

for cid, title in concept_map.items():
    nodes.append(N(f'concept_{cid}', title, type='concept'))
    # Link to relevant domain
    edges.append(E(f'concept_{cid}', 'domain_credit_risk', 'belongs_to', conf='INFERRED', score=0.9))

# 9. Boundary tensions between domains
nodes.extend([
    N('boundary_credit_market', 'Credit-Market Risk Boundary', type='boundary_tension', 
      description='CVA bridges credit and market risk'),
    N('boundary_credit_ops', 'Credit-Operational Risk Boundary', type='boundary_tension',
      description='Operational risk affects credit outcomes'),
    N('boundary_reg_eco', 'Regulatory-Economic Perspective Tension', type='boundary_tension',
      description='Different views on risk management'),
])

# Link boundary tensions to domains
edges.extend([
    E('boundary_credit_market', 'domain_credit_risk', 'tension_between', conf='INFERRED', score=0.8),
    E('boundary_credit_market', 'domain_market_risk', 'tension_between', conf='INFERRED', score=0.8),
    E('boundary_credit_ops', 'domain_credit_risk', 'tension_between', conf='INFERRED', score=0.8),
    E('boundary_credit_ops', 'domain_operational_risk', 'tension_between', conf='INFERRED', score=0.8),
])

# 10. Scenario nodes for stress testing
nodes.extend([
    N('scen_2008', '2008 Financial Crisis', type='scenario', domain='credit_risk'),
    N('scen_covid', 'COVID-19 Market Stress', type='scenario', domain='market_risk'),
    N('scen_rate_hike', 'Rapid Rate Hike Scenario', type='scenario', domain='market_risk'),
    N('scen_default_wave', 'Corporate Default Wave', type='scenario', domain='credit_risk'),
])

# 11. Meta-document nodes
meta_nodes = [
    ('_LO_TRACKER', 'Learning Objective Tracker', 'system'),
    ('_READINESS_DASHBOARD', 'Readiness Dashboard', 'system'),
    ('_EVENT_LOG', 'Event Log', 'system'),
    ('_ERROR_ARCHETYPES', 'Error Archetypes', 'system'),
    ('_boundary_events', 'Boundary Events', 'system'),
    ('_TEMPLATE_Reading', 'Reading Template', 'template'),
    ('_ANKI_GUIDE', 'Anki Integration Guide', 'guide'),
    ('drill_workflow', 'Drill Session Workflow', 'workflow'),
    ('reading_workflow', 'Reading Conversion Workflow', 'workflow'),
    ('system_prompt', 'AI System Prompt', 'system'),
]

for nid, title, cat in meta_nodes:
    nodes.append(N(f'meta_{nid.lower()}', title, type='meta', category=cat))

# 12. Roadmap concepts
roadmap_concepts = [
    ('phase1', 'Phase 1: Core Concept Mastery'),
    ('phase2', 'Phase 2: Application Practice'),
    ('phase3', 'Phase 3: Exam Simulation'),
    ('leitner', 'Leitner System'),
    ('spaced_repetition', 'Spaced Repetition'),
    ('readiness_formula', 'Readiness Formula'),
    ('priority_engine', 'Priority Engine'),
    ('event_logging', 'Event Logging'),
    ('boundary_thinking', 'Boundary Thinking'),
]

for rid, title in roadmap_concepts:
    nodes.append(N(f'rm_{rid}', title, type='roadmap_concept'))

# Add cross-references from readings to concepts
edges.extend([
    E('reading_r30', 'concept_cva', 'references', conf='EXTRACTED', score=1.0),
    E('reading_r30', 'concept_dva', 'references', conf='EXTRACTED', score=1.0),
    E('reading_r30', 'concept_pd_spread', 'references', conf='EXTRACTED', score=1.0),
    E('reading_r30', 'concept_netting', 'references', conf='EXTRACTED', score=1.0),
    E('reading_r30', 'concept_credit_var', 'references', conf='EXTRACTED', score=1.0),
    E('reading_r31', 'concept_cds', 'references', conf='EXTRACTED', score=1.0),
    E('reading_r31', 'concept_cds_valuation', 'references', conf='EXTRACTED', score=1.0),
    E('reading_r31', 'concept_risk_neutral_pd', 'references', conf='EXTRACTED', score=1.0),
])

# Link error archetypes to relevant domains
edges.extend([
    E('archetype_a7', 'domain_credit_risk', 'conceptually_related_to', conf='INFERRED', score=0.7),
    E('archetype_a10', 'domain_credit_risk', 'conceptually_related_to', conf='INFERRED', score=0.7),
    E('archetype_a11', 'domain_credit_risk', 'conceptually_related_to', conf='INFERRED', score=0.7),
    E('archetype_a4', 'domain_credit_risk', 'conceptually_related_to', conf='INFERRED', score=0.7),
])

# Create hyperedges for complex relationships
hyperedges = [
    {
        'id': 'he_credit_frameworks',
        'type': 'framework_application',
        'nodes': ['domain_credit_risk', 'framework_reg', 'framework_eco'],
        'description': 'Credit risk analyzed through both regulatory and economic frameworks'
    },
    {
        'id': 'he_error_patterns',
        'type': 'error_clustering',
        'nodes': ['archetype_a4', 'archetype_a7', 'archetype_a11'],
        'description': 'Common error patterns in credit risk questions'
    },
]

# Final graph structure
graph = {
    'nodes': nodes,
    'edges': edges,
    'hyperedges': hyperedges,
    'input_tokens': 0,
    'output_tokens': 0,
}

# Save all outputs
Path('graphify-out').mkdir(exist_ok=True)
Path('graphify-out/.graphify_extract.json').write_text(json.dumps(graph, indent=2))
Path('graphify-out/.graphify_semantic.json').write_text(json.dumps(graph, indent=2))
Path('graphify-out/.graphify_chunk_01.json').write_text(json.dumps(graph, indent=2))
Path('graphify-out/.graphify_ast.json').write_text(json.dumps([], indent=2))  # Empty - no code files

print("Final extraction:")
print(f"  nodes: {len(nodes)}")
print(f"  edges: {len(edges)}")
print(f"  hyperedges: {len(hyperedges)}")
print("  files written:")
print("    graphify-out/.graphify_chunk_01.json")
print("    graphify-out/.graphify_semantic.json")
print("    graphify-out/.graphify_extract.json")
print("    graphify-out/.graphify_ast.json (empty — no code)")
