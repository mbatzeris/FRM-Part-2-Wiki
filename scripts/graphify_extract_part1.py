#!/usr/bin/env python3
"""
Graphify Part 1: Extract framework tags, distractor archetypes, domains, readings, LOs, propositions, and error archetypes.
"""

import json
from pathlib import Path

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

nodes, edges = [], []

# 1. Framework tags
nodes.extend([
    N('framework_reg', '[REG] Regulatory Framework', type='framework', description='Regulatory and compliance perspective'),
    N('framework_eco', '[ECO] Economic Framework', type='framework', description='Economic and financial perspective'),
    N('framework_ops', '[OPS] Operational Framework', type='framework', description='Operational and implementation perspective'),
    N('framework_the', '[THE] Theoretical Framework', type='framework', description='Theoretical and academic perspective'),
])

# 2. Distractor archetypes
nodes.extend([
    N('distractor_absolute', 'Absolute Statement Trap', type='distractor', description='Uses always/never language'),
    N('distractor_true_irrelevant', 'True-Irrelevant Distractor', type='distractor', description='Factually true but irrelevant to LO'),
    N('distractor_inverse', 'Inverse Intuition', type='distractor', description='Reverses expected direction'),
    N('distractor_reg_eco_flip', 'REG vs ECO Flip', type='distractor', description='Switches between regulatory and economic perspectives'),
])

# 3. Exam domains
nodes.extend([
    N('domain_credit_risk', 'Credit Risk', type='domain', book='Book 2'),
    N('domain_market_risk', 'Market Risk', type='domain', book='Book 3'),
    N('domain_operational_risk', 'Operational Risk', type='domain', book='Book 4'),
    N('domain_risk_mgmt', 'Risk Management', type='domain', book='Book 5'),
    N('domain_investment_mgmt', 'Investment Management', type='domain', book='Book 6'),
    N('domain_current_issues', 'Current Issues', type='domain', book='Book 7'),
])

# 4. Readings (R30 and R31 as examples)
nodes.extend([
    N('reading_r30', 'R30 — Credit Risk (Hull Ch 25)', type='reading', domain='credit_risk'),
    N('reading_r31', 'R31 — Credit Derivatives (Hull Ch 26)', type='reading', domain='credit_risk'),
])

# 5. Learning Objectives from LO tracker
lo_file = Path('wiki/_LO_TRACKER.md')
if lo_file.exists():
    content = lo_file.read_text(encoding='utf-8')
    for line in content.split('\n'):
        if line.startswith('| LO ') and '|' in line[1:]:
            parts = [p.strip() for p in line.split('|')[1:]]
            if len(parts) >= 6 and parts[0]:
                lo_id = parts[0].replace(' ', '_').replace('.', '_').lower()
                lo_title = parts[1]
                readiness = parts[4] if parts[4] else 'N/A'
                nodes.append(N(f'lo_{lo_id}', lo_title, type='lo', readiness=readiness))
                
                # Link LO to its domain based on reading number
                if '30.' in parts[0]:
                    edges.append(E(f'lo_{lo_id}', 'domain_credit_risk', 'belongs_to', conf='INFERRED', score=1.0))
                elif '31.' in parts[0]:
                    edges.append(E(f'lo_{lo_id}', 'domain_credit_risk', 'belongs_to', conf='INFERRED', score=1.0))

# 6. Propositions from readings
for reading_file in [Path('wiki/Book 2 - Credit Risk/R30_Credit_Risk.md'), Path('wiki/Book 2 - Credit Risk/R31_Credit_Derivatives.md')]:
    if reading_file.exists():
        content = reading_file.read_text(encoding='utf-8')
        lines = content.split('\n')
        reading_num = '30' if 'R30' in reading_file.name else '31'
        
        for i, line in enumerate(lines):
            if line.startswith('**P') and '.' in line[:5]:
                prop_id = f"prop_{reading_num}_{line.split('.')[0][2:]}"
                prop_title = line.replace('**', '').strip()
                nodes.append(N(prop_id, prop_title, type='proposition', reading=f'R{reading_num}'))
                edges.append(E(f'reading_r{reading_num}', prop_id, 'contains', conf='EXTRACTED', score=1.0))

# 7. Error archetypes
nodes.extend([
    N('archetype_a1', 'A1: Sign Flip', type='error_archetype', description='Positive/negative sign reversal'),
    N('archetype_a2', 'A2: Conditional Confusion', type='error_archetype', description='Joint vs conditional probability confusion'),
    N('archetype_a3', 'A3: Framework Flip', type='error_archetype', description='REG vs ECO perspective switch'),
    N('archetype_a4', 'A4: Inverse Intuition', type='error_archetype', description='Direction reversal intuition'),
    N('archetype_a5', 'A5: Absolute Statement Trap', type='error_archetype', description='Always/never language trap'),
    N('archetype_a6', 'A6: True-Irrelevant Distractor', type='error_archetype', description='True but irrelevant fact'),
    N('archetype_a7', 'A7: Measure Confusion', type='error_archetype', description='Q vs P measure confusion'),
    N('archetype_a8', 'A8: Formula Misapplication', type='error_archetype', description='Incorrect formula application'),
    N('archetype_a9', 'A9: Scope Creep', type='error_archetype', description='LO boundary violation'),
    N('archetype_a10', 'A10: Recovery Rate Blindspot', type='error_archetype', description='Ignoring recovery assumptions'),
    N('archetype_a11', 'A11: Correlation Direction Flip', type='error_archetype', description='Correlation sign reversal'),
    N('archetype_a12', 'A12: Time Horizon Mismatch', type='error_archetype', description='Conditional vs marginal PD timing'),
])

# Link error archetypes to distractor types
mapping = [
    ("a1",  "inverse"),
    ("a2",  "true_irrelevant"),
    ("a3",  "reg_eco_flip"),
    ("a4",  "inverse"),
    ("a5",  "absolute"),
    ("a6",  "true_irrelevant"),
    ("a7",  "reg_eco_flip"),        # Q vs P is a framework flip
    ("a11", "inverse"),
]
for aid, did in mapping:
    edges.append(E(f"archetype_{aid}", f"distractor_{did}", "semantically_similar_to", conf="INFERRED", score=0.85))

print(f"Part 1: {len(nodes)} nodes, {len(edges)} edges so far")

# Create output directory if it doesn't exist
Path('graphify-out').mkdir(exist_ok=True)

# Save partial state for part 2 to append
Path('graphify-out/.graphify_partial.json').write_text(json.dumps({'nodes': nodes, 'edges': edges}, indent=2))
print("Partial state saved to graphify-out/.graphify_partial.json")
