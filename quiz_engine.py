#!/usr/bin/env python3
"""
FRM Part 2 Quiz Engine
Parses questions from the Drill Bank, quizzes interactively,
tracks scores, implements Leitner spaced repetition, and logs errors.
"""

import json
import re
import random
import os
import sys
import textwrap
from datetime import datetime

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DRILL_BANK = os.path.join(BASE_DIR, "ops", "06_DRILL_BANK.md")
CONSTRAINT_DRILLS = os.path.join(BASE_DIR, "ops", "11_CONSTRAINT_LAYERING_DRILLS.md")
STATE_FILE = os.path.join(BASE_DIR, "ops", "quiz_state.json")
ERROR_LOG = os.path.join(BASE_DIR, "ops", "07_ERROR_LOG.md")

# ── Domain map ─────────────────────────────────────────────────────────────────
DOMAIN_NAMES = {
    1: "Market Risk",
    2: "Credit Risk",
    3: "Operational Risk",
    4: "Liquidity Risk",
    5: "Investment Management",
    6: "Current Issues",
    7: "Cross-Domain Boundary Events",
}

DOMAIN_Q_RANGES = {
    1: range(1, 11),
    2: range(11, 21),
    3: range(21, 31),
    4: range(26, 36),
    5: range(31, 41),
    6: range(41, 46),
    7: range(46, 53),
}

# ── ANSI colours ───────────────────────────────────────────────────────────────
GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

def c(color, text):
    return f"{color}{text}{RESET}"

def hr(char="─", width=60):
    return char * width

def wrap(text, width=70, indent="  "):
    return textwrap.fill(text, width=width, subsequent_indent=indent)


# ── Markdown parser ────────────────────────────────────────────────────────────

def parse_questions(filepath):
    """Return list of question dicts parsed from a markdown file."""
    with open(filepath, encoding="utf-8") as f:
        raw_lines = f.readlines()

    # Build a map of line_index -> domain by scanning ## Domain headers
    section_domain = {}  # line_index -> domain int
    current_domain = 0
    for i, line in enumerate(raw_lines):
        dom_match = re.match(r'^## (?:Domain (\d)|BE-|.*Boundary)', line)
        if dom_match:
            current_domain = int(dom_match.group(1)) if dom_match.group(1) else 7
        section_domain[i] = current_domain

    content = "".join(raw_lines)

    questions = []
    seen_ids = set()

    # Split on any ### header
    blocks = re.split(r'\n(?=### )', content)

    for block in blocks:
        # Skip pure section-descriptor headers (no question tag)
        header_line = block.strip().split('\n')[0]
        if not re.match(r'^### (?:Q[\d]+|BE-\d+)', header_line):
            continue

        # Check for twin-pair (Q6–Q7 or Q8-Q9 format)
        twin_match = re.match(r'^### (Q(\d+)[–-]Q(\d+))\s*(.*)', header_line)
        if twin_match:
            parsed_twins = parse_twin_block(block)
            for q in parsed_twins:
                key = (q['id'], q['type'])
                if key in seen_ids:
                    continue
                seen_ids.add(key)
                q['domain'] = _domain_from_context(block, content, section_domain, raw_lines)
                questions.append(q)
            continue

        q = parse_block(block)
        if not q:
            continue
        key = (q['id'], q['type'])
        if key in seen_ids:
            continue
        seen_ids.add(key)
        q['domain'] = _domain_from_context(block, content, section_domain, raw_lines)
        questions.append(q)

    return questions


def parse_twin_block(block):
    """Parse a twin-pair block (Q6–Q7) into two separate question dicts."""
    questions = []
    header_line = block.strip().split('\n')[0]
    tags = re.findall(r'\[([^\]]+)\]', header_line)
    archetype = _detect_archetype(tags)

    # Extract shared vignette (text before the first Q6/Q7 sub-question)
    vignette_match = re.search(r'(?<=\n)\*\*Vignette:\*\*\s*(.*?)(?=\n\*\*Q\d)', block, re.DOTALL)
    vignette = vignette_match.group(1).strip() if vignette_match else ""

    # Find each sub-question
    sub_blocks = re.split(r'(?=\n\*\*Q(\d+)\s*\()', block)
    for sub in sub_blocks:
        q_num_match = re.search(r'\*\*Q(\d+)\s*\([^)]+\):\*\*\s*(.*)', sub)
        if not q_num_match:
            continue
        q_num = q_num_match.group(1)
        stem = q_num_match.group(2).strip()

        options = re.findall(r'^- ([A-D]\).*)', sub, re.MULTILINE)
        ans_match = re.search(r'\*\*Q' + q_num + r'\s*(?:\([^)]+\))?\s*Answer:\*\*\s*([A-D])', sub)
        if not ans_match:
            ans_match = re.search(r'Answer:\*\*?\s*([A-D])', sub)

        why_match = re.search(r'(?:Answer:\*\*\s*[A-D]\s*[—–-]\s*)(.*?)(?:\n\n|\Z)', sub, re.DOTALL)
        explanation = why_match.group(1).strip() if why_match else ""

        if options and ans_match:
            questions.append({
                "id": f"Q{q_num}",
                "type": "mcq",
                "domain": 0,
                "archetype": archetype,
                "tags": tags,
                "vignette": vignette + ("\n" + stem if stem else ""),
                "stem": stem,
                "options": options,
                "answer": ans_match.group(1).upper(),
                "explanation": explanation,
            })
    return questions


def _domain_from_context(block, full_content, section_domain, raw_lines):
    """Find which domain section this block falls in by its byte offset."""
    # Find the first line of the block in raw_lines
    first_line = block.strip().split('\n')[0].strip()
    for i, raw in enumerate(raw_lines):
        if first_line and first_line[:40] in raw:
            # Walk back to find nearest domain header
            for j in range(i, -1, -1):
                dm = re.match(r'^## .*Domain (\d)', raw_lines[j])
                be = re.match(r'^## .*(?:Boundary|Cross)', raw_lines[j], re.IGNORECASE)
                if dm:
                    return int(dm.group(1))
                if be:
                    return 7
    return 0


def parse_block(block):
    """Parse a single question block into a dict."""
    block = block.strip()
    if not block:
        return None

    # Header line
    header_match = re.match(r'^### (Q[\d\-]+|BE-\d+)\s*(.*)', block)
    if not header_match:
        return None

    q_id = header_match.group(1)
    tags_raw = header_match.group(2)

    # Parse tags from header: [Domain] [Archetype] [Constraint]
    tags = re.findall(r'\[([^\]]+)\]', tags_raw)
    domain = _detect_domain(q_id, tags)
    archetype = _detect_archetype(tags)

    # Determine if MCQ (has A) B) C) D) options)
    options = re.findall(r'^- ([A-D]\).*)', block, re.MULTILINE)
    answer_match = re.search(r'\*\*(?:Q\d+ )?Answer:\*?\*?\s*([A-D])', block)
    if not answer_match:
        answer_match = re.search(r'\*\*Answer:\*\*\s*\*?\*?([A-D])', block)

    # Extract explanation (Why: or line after answer)
    why_match = re.search(r'\*\*Why:\*\*\s*(.*?)(?:\n\n|\Z)', block, re.DOTALL)
    explanation = why_match.group(1).strip() if why_match else ""

    if options and answer_match:
        # Full MCQ format
        # Extract vignette: text between header and first option
        vignette_raw = re.split(r'- A\)', block)[0]
        # Remove header line
        vignette_raw = re.sub(r'^### .*\n', '', vignette_raw).strip()
        # Strip markdown bold
        vignette = re.sub(r'\*\*([^*]+)\*\*', r'\1', vignette_raw)
        # Get question stem if separate
        stem_match = re.search(r'\*\*([^*]+\?[^*]*)\*\*', vignette_raw)
        stem = stem_match.group(1).strip() if stem_match else ""

        # Clean options
        cleaned_options = []
        for opt in options:
            opt_clean = re.sub(r'`[^`]+`', lambda m: m.group().strip('`'), opt)
            cleaned_options.append(opt_clean)

        return {
            "id": q_id,
            "type": "mcq",
            "domain": domain,
            "archetype": archetype,
            "tags": tags,
            "vignette": vignette.strip(),
            "stem": stem,
            "options": cleaned_options,
            "answer": answer_match.group(1).upper(),
            "explanation": explanation,
        }
    else:
        # Concept card format — whole block is the content
        content = re.sub(r'^### .*\n', '', block).strip()
        content = re.sub(r'\*\*([^*]+)\*\*', r'\1', content)
        # Try to extract an embedded answer keyword
        return {
            "id": q_id,
            "type": "card",
            "domain": domain,
            "archetype": archetype,
            "tags": tags,
            "content": content,
            "answer": None,
            "explanation": "",
        }


def _detect_domain(q_id, tags):
    """Fallback domain detection from tags (used when context fails)."""
    if q_id.startswith("BE"):
        return 7
    for t in tags:
        t_l = t.lower()
        if "market" in t_l: return 1
        if "credit" in t_l: return 2
        if "oprisk" in t_l or "operational" in t_l: return 3
        if "liquidity" in t_l: return 4
        if "invmgmt" in t_l or "investment" in t_l: return 5
        if "current" in t_l: return 6
    return 0


def _detect_archetype(tags):
    archetypes = ["REG-ECO FLIP", "INVERSE INTUITION", "TRUE-IRRELEVANT", "ABSOLUTE"]
    for t in tags:
        for a in archetypes:
            if a in t.upper():
                return a
    return "OTHER"


# ── State / Leitner ────────────────────────────────────────────────────────────

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, encoding="utf-8") as f:
            return json.load(f)
    return {"boxes": {}, "history": [], "error_count": 0}


def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)


def get_box(state, q_id):
    return state["boxes"].get(q_id, 1)


def update_box(state, q_id, correct):
    current = get_box(state, q_id)
    if correct:
        state["boxes"][q_id] = min(current + 1, 5)
    else:
        state["boxes"][q_id] = 1


def leitner_weight(box):
    """Lower box = higher probability of being selected."""
    return {1: 10, 2: 5, 3: 3, 4: 2, 5: 1}.get(box, 1)


def select_questions(questions, state, n=10, domain=None, archetype=None, review_only=False):
    pool = questions
    if domain:
        pool = [q for q in pool if q["domain"] == domain]
    if archetype:
        a_upper = archetype.upper()
        pool = [q for q in pool if a_upper in q.get("archetype", "").upper()]
    if review_only:
        pool = [q for q in pool if get_box(state, q["id"]) == 1]

    if not pool:
        return []

    weights = [leitner_weight(get_box(state, q["id"])) for q in pool]
    k = min(n, len(pool))
    return random.choices(pool, weights=weights, k=k)


# ── Error log export ───────────────────────────────────────────────────────────

def append_error_log(q, session_errors):
    """Append wrong MCQ answers to 07_ERROR_LOG.md."""
    if not session_errors:
        return
    with open(ERROR_LOG, "a", encoding="utf-8") as f:
        for entry in session_errors:
            q_obj = entry["question"]
            state = entry["state_ref"]
            state["error_count"] = state.get("error_count", 0) + 1
            n = state["error_count"]
            date = datetime.now().strftime("%Y-%m-%d")
            domain_name = DOMAIN_NAMES.get(q_obj["domain"], "Unknown")
            f.write(f"\n#### Entry #{n}\n")
            f.write(f"- **Date:** {date}\n")
            f.write(f"- **Source:** Drill Bank {q_obj['id']}\n")
            f.write(f"- **Domain:** {domain_name}\n")
            f.write(f"- **Distractor Archetype:** {q_obj.get('archetype', 'OTHER')}\n")
            f.write(f"- **My Answer:** {entry['given']}\n")
            f.write(f"- **Correct Answer:** {q_obj['answer']}\n")
            if q_obj.get("explanation"):
                f.write(f"- **Antigravity Autopsy Result:** {q_obj['explanation'][:200]}\n")
            f.write(f"- **Prevention Rule:** (fill in)\n")


# ── Display helpers ────────────────────────────────────────────────────────────

def display_mcq(q, number, total):
    print()
    print(hr())
    print(c(CYAN, f"  Question {number}/{total}  │  {DOMAIN_NAMES.get(q['domain'], '?')}  │  {q['archetype']}  │  {q['id']}"))
    print(hr())
    print()
    # Vignette
    vignette = q["vignette"]
    for para in vignette.split("\n"):
        if para.strip():
            print(wrap(para.strip(), width=70, indent="  "))
    print()
    # Options
    for opt in q["options"]:
        print(f"  {opt}")
    print()


def display_card(q, number, total):
    print()
    print(hr())
    print(c(CYAN, f"  Concept Card {number}/{total}  │  {DOMAIN_NAMES.get(q['domain'], '?')}  │  {q['archetype']}  │  {q['id']}"))
    print(hr())
    print()
    content = q.get("content", "")
    # Hide bold keywords that are answers — show as [???]
    masked, reveals = mask_answers(content)
    for line in masked.split("\n"):
        if line.strip():
            print(wrap(line.strip(), width=70, indent="  "))
    print()
    print(c(YELLOW, "  Try to recall the key answer before pressing Enter."))
    input("  [Press Enter to reveal] ")
    print()
    # Show original with highlights
    for line in content.split("\n"):
        if line.strip():
            highlighted = re.sub(r'\b(INCORRECT|Incorrect|Correct|correct|incorrect|CORRECT|treat|Treat|transfer|Transfer|Inappropriate|Appropriate|inappropriate|appropriate)\b',
                                  lambda m: c(BOLD + GREEN, m.group()), line)
            print(wrap(highlighted, width=70, indent="  "))
    print()


def mask_answers(text):
    """Replace key answer words in concept cards."""
    reveals = []
    def replacer(m):
        reveals.append(m.group())
        return "[???]"
    masked = re.sub(r'\b(INCORRECT|Incorrect|Treat|Transfer|Inappropriate|Appropriate|inappropriate|appropriate|increases|decreases)\b', replacer, text)
    return masked, reveals


# ── Stats ──────────────────────────────────────────────────────────────────────

def print_stats(state, questions):
    print()
    print(c(BOLD, hr("═")))
    print(c(BOLD, "  PERFORMANCE DASHBOARD"))
    print(c(BOLD, hr("═")))

    history = state.get("history", [])
    if not history:
        print("  No sessions recorded yet.")
        return

    # Domain breakdown
    domain_correct = {}
    domain_total = {}
    archetype_correct = {}
    archetype_total = {}

    for entry in history:
        d = entry.get("domain", 0)
        a = entry.get("archetype", "OTHER")
        correct = entry.get("correct", False)
        domain_correct[d] = domain_correct.get(d, 0) + (1 if correct else 0)
        domain_total[d] = domain_total.get(d, 0) + 1
        archetype_correct[a] = archetype_correct.get(a, 0) + (1 if correct else 0)
        archetype_total[a] = archetype_total.get(a, 0) + 1

    print()
    print(c(BOLD, "  By Domain:"))
    for d in sorted(domain_total):
        name = DOMAIN_NAMES.get(d, "Unknown")
        tot = domain_total[d]
        cor = domain_correct.get(d, 0)
        pct = 100 * cor // tot if tot else 0
        bar = ("█" * (pct // 10)).ljust(10)
        color = GREEN if pct >= 70 else (YELLOW if pct >= 50 else RED)
        print(f"  {name:<30} {c(color, bar)} {cor}/{tot} ({pct}%)")

    print()
    print(c(BOLD, "  By Distractor Archetype:"))
    for a in sorted(archetype_total):
        tot = archetype_total[a]
        cor = archetype_correct.get(a, 0)
        pct = 100 * cor // tot if tot else 0
        color = GREEN if pct >= 70 else (YELLOW if pct >= 50 else RED)
        print(f"  {a:<25} {cor}/{tot} ({c(color, str(pct) + '%')})")

    print()
    # Leitner box distribution
    boxes = state.get("boxes", {})
    box_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for b in boxes.values():
        box_counts[b] = box_counts.get(b, 0) + 1

    print(c(BOLD, "  Leitner Boxes (1=weak → 5=mastered):"))
    for b in range(1, 6):
        cnt = box_counts[b]
        bar = ("■" * cnt).ljust(20)
        print(f"  Box {b}: {c(YELLOW if b == 1 else GREEN, bar)} {cnt} questions")

    print()


# ── Main quiz loop ─────────────────────────────────────────────────────────────

def run_quiz(questions, state, n=10, domain=None, archetype=None, review_only=False):
    selected = select_questions(questions, state, n=n, domain=domain,
                                archetype=archetype, review_only=review_only)
    if not selected:
        print(c(RED, "  No questions match your filter. Try a different selection."))
        return

    session_errors = []
    session_history = []
    correct_count = 0
    total = len(selected)

    print()
    print(c(BOLD, f"  Starting quiz: {total} questions"))
    print(c(YELLOW, "  Type your answer (A/B/C/D) or 's' to skip, 'q' to quit."))

    for i, q in enumerate(selected, 1):
        if q["type"] == "mcq":
            display_mcq(q, i, total)
            while True:
                raw = input(c(BOLD, "  Your answer: ")).strip().upper()
                if raw in ("A", "B", "C", "D", "S", "Q"):
                    break
                print("  Enter A, B, C, D, s (skip) or q (quit).")

            if raw == "Q":
                print(c(YELLOW, "  Quiz ended early."))
                break
            if raw == "S":
                print(c(YELLOW, f"  Skipped. Correct answer: {q['answer']}"))
                continue

            correct = raw == q["answer"]
            update_box(state, q["id"], correct)
            session_history.append({"domain": q["domain"], "archetype": q["archetype"],
                                    "correct": correct, "id": q["id"]})

            if correct:
                correct_count += 1
                print(c(GREEN, f"\n  ✓ Correct!"))
            else:
                print(c(RED, f"\n  ✗ Wrong. Correct answer: {q['answer']}"))
                session_errors.append({"question": q, "given": raw, "state_ref": state})

            # Always show explanation
            if q.get("explanation"):
                print()
                exp = q["explanation"].replace("\n", " ").strip()
                print(wrap(c(YELLOW, "  Why: ") + exp, width=72, indent="       "))
            input(c(CYAN, "\n  [Enter for next] "))

        else:  # card
            display_card(q, i, total)
            raw = input(c(BOLD, "  Did you get it right? (y/n/q): ")).strip().lower()
            if raw == "q":
                print(c(YELLOW, "  Quiz ended early."))
                break
            correct = raw == "y"
            update_box(state, q["id"], correct)
            session_history.append({"domain": q["domain"], "archetype": q["archetype"],
                                    "correct": correct, "id": q["id"]})
            if correct:
                correct_count += 1
                print(c(GREEN, "  ✓ Marked correct."))
            else:
                print(c(RED, "  ✗ Marked wrong — will resurface sooner."))
            input(c(CYAN, "  [Enter for next] "))

    # Session summary
    state.setdefault("history", []).extend(session_history)
    save_state(state)

    attempted = len(session_history)
    pct = 100 * correct_count // attempted if attempted else 0
    color = GREEN if pct >= 70 else (YELLOW if pct >= 50 else RED)

    print()
    print(hr("═"))
    print(c(BOLD, "  SESSION COMPLETE"))
    print(hr("═"))
    print(f"  Score: {c(color, f'{correct_count}/{attempted} ({pct}%)')}")

    if session_errors:
        print(c(RED, f"  {len(session_errors)} error(s) logged to Error Log."))
        append_error_log(None, session_errors)
    print()


# ── Interactive menu ───────────────────────────────────────────────────────────

def main_menu(questions, state):
    while True:
        print()
        print(c(BOLD, hr("═")))
        print(c(BOLD, "  FRM Part 2 — Quiz Engine"))
        print(c(BOLD, hr("═")))
        print()
        print("  Select a section to drill:")
        print()
        for k, name in DOMAIN_NAMES.items():
            q_count = sum(1 for q in questions if q["domain"] == k)
            box1 = sum(1 for q in questions if q["domain"] == k and get_box(state, q["id"]) == 1)
            weak_indicator = c(RED, f" [{box1} weak]") if box1 > 0 else ""
            print(f"  {k}. {name:<35} ({q_count} questions){weak_indicator}")
        print()
        print(f"  8. All questions (random)")
        print(f"  9. Review wrong answers only")
        print(f"  0. View stats dashboard")
        print(f"  q. Quit")
        print()

        choice = input(c(BOLD, "  > ")).strip().lower()

        if choice == "q":
            print(c(YELLOW, "  Goodbye. Keep drilling!"))
            break
        elif choice == "0":
            print_stats(state, questions)
        elif choice == "8":
            n = _ask_num_questions()
            run_quiz(questions, state, n=n)
        elif choice == "9":
            run_quiz(questions, state, n=20, review_only=True)
        elif choice in [str(k) for k in DOMAIN_NAMES]:
            domain = int(choice)
            _domain_submenu(questions, state, domain)
        else:
            print(c(RED, "  Invalid choice."))


def _domain_submenu(questions, state, domain):
    domain_qs = [q for q in questions if q["domain"] == domain]
    print()
    print(c(BOLD, f"  {DOMAIN_NAMES[domain]} — {len(domain_qs)} questions available"))
    print()
    print("  a. All questions in this domain")
    print("  b. Filter by distractor archetype")
    print("  c. Review wrong answers only")
    print("  x. Back")
    print()
    choice = input(c(BOLD, "  > ")).strip().lower()

    if choice == "a":
        n = _ask_num_questions(max_n=len(domain_qs))
        run_quiz(questions, state, n=n, domain=domain)
    elif choice == "b":
        arch = _ask_archetype()
        n = _ask_num_questions()
        run_quiz(questions, state, n=n, domain=domain, archetype=arch)
    elif choice == "c":
        run_quiz(questions, state, n=20, domain=domain, review_only=True)
    elif choice == "x":
        return


def _ask_num_questions(max_n=None):
    default = min(10, max_n) if max_n else 10
    raw = input(c(CYAN, f"  How many questions? (default {default}): ")).strip()
    try:
        n = int(raw)
        if max_n:
            n = min(n, max_n)
        return max(1, n)
    except ValueError:
        return default


def _ask_archetype():
    archetypes = ["REG-ECO FLIP", "INVERSE INTUITION", "TRUE-IRRELEVANT", "ABSOLUTE"]
    print()
    for i, a in enumerate(archetypes, 1):
        print(f"  {i}. {a}")
    raw = input(c(CYAN, "  Pick archetype (1-4): ")).strip()
    try:
        return archetypes[int(raw) - 1]
    except (ValueError, IndexError):
        return None


# ── Entry point ────────────────────────────────────────────────────────────────

def main():
    import argparse
    parser = argparse.ArgumentParser(description="FRM Part 2 CLI Quiz Engine")
    parser.add_argument("--domain", type=int, help="Filter by domain (1-7)")
    parser.add_argument("--archetype", type=str, help="Filter by distractor archetype")
    parser.add_argument("--chapter", type=str, help="Filter by chapter tag e.g. R42")
    parser.add_argument("--review", action="store_true", help="Review wrong answers only")
    parser.add_argument("--stats", action="store_true", help="Show stats dashboard")
    parser.add_argument("--n", type=int, default=10, help="Number of questions (default 10)")
    args = parser.parse_args()

    # Load questions
    questions = []
    for filepath in [DRILL_BANK, CONSTRAINT_DRILLS]:
        if os.path.exists(filepath):
            questions.extend(parse_questions(filepath))

    if not questions:
        print(c(RED, f"No questions found. Check that {DRILL_BANK} exists."))
        sys.exit(1)

    # Filter by chapter tag if specified
    if args.chapter:
        tag = args.chapter.upper()
        questions = [q for q in questions if tag in " ".join(q.get("tags", [])).upper()]
        if not questions:
            print(c(YELLOW, f"No questions tagged with {args.chapter}. Running all questions."))
            questions = parse_questions(DRILL_BANK)

    state = load_state()

    if args.stats:
        print_stats(state, questions)
        return

    if args.domain or args.archetype or args.review:
        run_quiz(questions, state, n=args.n, domain=args.domain,
                 archetype=args.archetype, review_only=args.review)
    else:
        main_menu(questions, state)


if __name__ == "__main__":
    main()
