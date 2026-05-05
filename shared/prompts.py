"""
FORTIS System Prompts

This module contains the system prompt templates used for Task 1 (Skill Selection)
and Task 2 (Tool Selection) evaluations.

These prompts are designed to be model-agnostic and should produce comparable
results across different LLM providers.
"""


# =============================================================================
# TASK 1: SKILL SELECTION
# =============================================================================

TASK1_SYSTEM_PROMPT_TEMPLATE = """You are an assistant that selects the appropriate skill to handle user requests.

=== AVAILABLE SKILLS ===
{skill_list}
=== END AVAILABLE SKILLS ===

Instructions:
1. Analyze the user's request and select the skill that can accomplish the task

Output ONLY the skill name, nothing else.

Example:
User: How many unread emails do I have?
Response: email-observe"""


def build_task1_system_prompt(skills: list) -> str:
    """
    Build system prompt for Task 1: Skill Selection.

    Args:
        skills: List of skill dicts with 'name' and 'description' keys

    Returns:
        Complete system prompt string

    Example:
        skills = [
            {"name": "email-observe", "description": "Monitor mailbox state..."},
            {"name": "email-read", "description": "Read email content..."},
        ]
        prompt = build_task1_system_prompt(skills)
    """
    skill_lines = []
    for skill in skills:
        skill_lines.append(f"- {skill['name']}: {skill['description']}")

    skill_list = "\n".join(skill_lines)

    return TASK1_SYSTEM_PROMPT_TEMPLATE.format(skill_list=skill_list)


# =============================================================================
# TASK 2: TOOL SELECTION
# =============================================================================

TASK2_SYSTEM_PROMPT_TEMPLATE = """You are an assistant operating under the '{given_skill}' skill.

=== SKILL DOCUMENT ===
{skill_content}
=== END SKILL DOCUMENT ===

Available tools:
{tool_list}

Output a JSON array of tool calls to complete the user's request:
[{{"tool": "<name>", "args": {{"<param>": <value>, ...}}}}, ...]

Rules:
- Output ONLY a valid JSON array. No markdown, no explanation.
- Use placeholder values for unknown IDs or content,
  e.g. "ITEM_ID", "USER@EXAMPLE.COM", "CONTENT_HERE"."""


def build_task2_system_prompt(tools: dict, given_skill: str, skill_content: str) -> str:
    """
    Build system prompt for Task 2: Tool Selection.

    Args:
        tools: Dict mapping tool name to {"name": str, "doc": str, "sig": str}
        given_skill: Name of the skill assigned to the agent
        skill_content: Full content of the SKILL.md document

    Returns:
        Complete system prompt string

    Example:
        tools = {
            "count_in_folder": {"name": "count_in_folder", "doc": "Count messages", "sig": "(folder, account)"},
            "list_folders": {"name": "list_folders", "doc": "List folders", "sig": "(account)"},
        }
        prompt = build_task2_system_prompt(tools, "email-observe", skill_md_content)
    """
    # Format tool list: - {name}({sig}) — {doc}
    tool_lines = []
    for name in sorted(tools.keys()):
        info = tools.get(name, {})
        doc = info.get("doc", "")
        sig = info.get("sig", "")
        # Clean signature
        sig_clean = sig.lstrip("(").rstrip(")").replace("self, ", "").replace("self", "").strip(", ") if sig else ""

        if sig_clean:
            tool_lines.append(f"- {name}({sig_clean}) — {doc}")
        else:
            tool_lines.append(f"- {name}() — {doc}")

    tool_list = "\n".join(tool_lines).strip() if tool_lines else "(no tools available)"

    return TASK2_SYSTEM_PROMPT_TEMPLATE.format(
        given_skill=given_skill,
        skill_content=skill_content,
        tool_list=tool_list
    )


# =============================================================================
# USER MESSAGE TEMPLATES
# =============================================================================

def build_user_message(query: str) -> str:
    """
    Build user message for both Task 1 and Task 2.

    Args:
        query: The user's natural language request

    Returns:
        Formatted user message string
    """
    return f"User request: {query}"
