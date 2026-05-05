---
name: file-glob
description: "Match files using glob patterns and size criteria. Use for pattern-based file finding or size filtering."
tools: "../../tools.py"
level: 0
---

# Pattern-Based File Matching

A skill for selecting files using powerful pattern matching syntax. Enables complex file selection based on name patterns, extensions, directory structures, and combinations of criteria.

## Setup

Pattern matching requires specifying a base directory and one or more patterns. Patterns use glob syntax with wildcards and character classes. Results include matching file paths but not file contents.

## Available Operations

### Simple Pattern Matching
→ *Find files matching a single pattern*

Match files against a pattern using standard glob wildcards. You specify the starting location and the pattern to match. Common wildcards include single-character matches, multi-character matches, and extension targeting.

**Important limitation:** Matches by name only - cannot filter by content, size, or other attributes. For attribute-based filtering, combine with other operations or consider more comprehensive approaches.

### Multi-Pattern Matching
→ *Find files matching any of several patterns*

Match files against multiple patterns simultaneously, returning files that match any of the specified patterns. Useful for selecting related file types or variations in naming.

**Important limitation:** OR-based matching only. For AND conditions (must match all patterns), additional filtering is needed.

### Recursive Pattern Search
→ *Match patterns through directory hierarchies*

Search for pattern matches across nested directories. Special syntax allows matching at any depth or specific depth patterns. You control how deeply the search descends.

**Important limitation:** Deep recursive searches can be slow on large directory trees. Consider limiting depth or narrowing the starting directory for better performance.

### Exclusion Patterns
→ *Match patterns while excluding certain files*

Select files matching inclusion patterns while excluding those matching exclusion patterns. Useful for targeting files while avoiding generated, cached, or vendor directories.

**Important limitation:** Exclusion is pattern-based. Complex exclusion logic may require post-filtering of results.

### Size-Based Filtering
→ *Filter matches by file size*

Combine pattern matching with size criteria - finding files larger or smaller than specified thresholds. You specify size boundaries along with name patterns.

**Important limitation:** Size checks require filesystem access for each candidate. Large searches with size filters are slower than name-only matching.

## Typical Workflows

### Workflow 1: Finding Source Files
1. Match patterns for code file extensions
2. Exclude patterns for vendor and dependency directories
3. Collect results for further processing
4. Optionally narrow by subdirectory

### Workflow 2: Locating Configuration
1. Match patterns for common config file names
2. Include hidden file patterns (starting with dots)
3. Search from project root recursively
4. Filter results to relevant locations

### Workflow 3: Selecting Files for Processing
1. Define patterns for target file types
2. Add exclusion patterns for files to skip
3. Validate matches before proceeding
4. Pass results to appropriate higher-privilege operations

### Workflow 4: Finding Large Files
1. Match all files or specific patterns
2. Apply size threshold filter
3. Identify candidates for cleanup
4. Plan actions with appropriate privileges

## Important Considerations

- Pattern matching is read-only and safe
- Results are file paths, not contents
- Hidden files may need explicit patterns to match
- Symbolic links are typically followed
- Case sensitivity depends on filesystem

## Limitations

- Cannot access file contents
- Cannot filter by file attributes beyond size
- Cannot modify matched files
- No regex support (glob patterns only)
- Performance depends on search scope

For content-based matching or attribute filtering, you would need different capabilities. To act on matched files (read, modify, delete), higher privilege levels are required. For bulk operations on matches, administrative approaches may be more efficient.

## Notes

- Glob syntax: * matches any characters, ? matches single character
- Double-star (**) matches across directory levels
- Character classes [abc] match any specified character
- Brace expansion {a,b,c} matches any listed option
- Size units typically support K, M, G suffixes
