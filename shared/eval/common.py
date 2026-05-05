"""
Common evaluation utilities shared across tasks.
"""

import json
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime


def load_json(path: str) -> Dict:
    """Load JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data: Dict, path: str, indent: int = 2):
    """Save JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)


def load_skills(scenario: str, base_path: str = None) -> List[Dict]:
    """Load skills for a scenario."""
    if base_path is None:
        base_path = Path(__file__).parent.parent / "scenarios"
    else:
        base_path = Path(base_path)

    skills_path = base_path / scenario / "skills.json"
    data = load_json(str(skills_path))
    return data.get("skills", [])


def load_queries(task: str, scenario: str, base_path: str = None) -> List[Dict]:
    """Load queries for a task and scenario."""
    if base_path is None:
        base_path = Path(__file__).parent.parent.parent / "tasks" / task / "scenarios"
    else:
        base_path = Path(base_path)

    queries_path = base_path / scenario / "queries.json"
    data = load_json(str(queries_path))
    return data.get("queries", [])


def generate_result_filename(model: str, scenario: str, task: str = None) -> str:
    """Generate standardized result filename."""
    date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    if task:
        return f"{model}_{scenario}_{task}_{date_str}.json"
    return f"{model}_{scenario}_{date_str}.json"


def format_metrics_table(metrics: Dict[str, Any]) -> str:
    """Format metrics as a readable table."""
    lines = []
    lines.append("=" * 50)
    lines.append(f"Total queries: {metrics.get('total', 0)}")
    lines.append("-" * 50)

    counts = metrics.get("counts", {})
    for key, val in counts.items():
        lines.append(f"  {key}: {val}")

    lines.append("-" * 50)
    lines.append(f"Success rate:       {metrics.get('success_rate', 0):.1%}")
    lines.append(f"Safe rate:          {metrics.get('safe_rate', 0):.1%}")
    lines.append(f"Over-privilege rate: {metrics.get('over_privilege_rate', 0):.1%}")
    lines.append(f"Fail rate:          {metrics.get('fail_rate', 0):.1%}")
    lines.append("=" * 50)

    return "\n".join(lines)
