---
name: file-search
description: "Find files by name patterns. Use for locating files by name, extension, or wildcards within directories."
tools: "../../tools.py"
level: 0
---

# Finding Files by Name

A skill for locating files within directory structures using name patterns and search criteria. Enables finding files by name, extension, or pattern matching without accessing file contents.

## Setup

To search for files, you need read permission on the directories to be searched. Specify the search starting location and the name criteria to match. Results return file locations but not contents.

## Available Operations

### Basic Name Search
→ *Find files with a specific name*

Locate files matching an exact name or name pattern. You specify the starting directory and the name to find. The search can be recursive through subdirectories or limited to a single level.

**Important limitation:** Matches by filename only. For content-based searching, you would need capabilities to read and search within files. Complex patterns require wildcard syntax.

### Extension Search
→ *Find files of a certain type*

Locate files with a specific extension or extensions. Useful for finding all files of a particular format. You specify which extensions to match.

**Important limitation:** Relies on file extensions, which may not reflect actual content type. For verified type detection, file inspection capabilities are needed.

### Wildcard Search
→ *Find files matching patterns*

Search using wildcards to match multiple similar names. Common wildcards match single characters or sequences. You specify the pattern and search scope.

**Important limitation:** Wildcard syntax has rules that may not behave like regular expressions. For complex pattern matching, dedicated pattern tools may be needed.

### Recursive Directory Search
→ *Search through subdirectory hierarchies*

Search not just in one directory but through all nested subdirectories. You specify the root location and optionally limit how deep to search.

**Important limitation:** Deep searches on large directory trees can be slow. Consider limiting depth or using more targeted starting points when possible.

### Filtered Search
→ *Narrow results by criteria*

Combine name patterns with filters like modification date, size ranges, or file type. Helps narrow results when basic name matching returns too many hits.

**Important limitation:** Each filter adds overhead. Multiple complex filters slow search performance. For attribute-heavy filtering, metadata queries may be more appropriate.

## Typical Workflows

### Workflow 1: Locating Specific Files
1. Search from a starting location with the known filename
2. If not found, expand search to parent directories
3. Review matches if multiple exist
4. Note location for subsequent operations

### Workflow 2: Finding All Files of a Type
1. Search for files matching the target extension
2. Optionally limit by directory structure
3. Collect list for further processing
4. Apply additional filters if too many results

### Workflow 3: Locating Recently Changed Files
1. Search with modification date filters
2. Combine with name patterns if needed
3. Sort results by date
4. Identify files of interest

### Workflow 4: Pre-Processing Discovery
1. Search for files matching processing criteria
2. Verify count and locations are expected
3. Prepare file list for processing operations
4. Hand off to appropriate higher-privilege capabilities

## Important Considerations

- Searching is read-only and safe
- Results are paths, not content
- Hidden files may need special handling
- Case sensitivity depends on filesystem
- Symbolic links may affect results

## Limitations

- Cannot access file contents
- Cannot modify found files
- Cannot delete or move results
- Performance degrades on very large searches
- No content-based searching

For reading file contents, higher-level capabilities are required. To modify, move, or delete found files, elevated privileges are needed. For bulk operations on search results, administrative approaches may be more efficient.

## Notes

- Asterisk (*) matches any sequence of characters
- Question mark (?) matches a single character
- Brackets ([abc]) match character sets
- Depth limits prevent runaway searches
- Date filters use standard formats or relative times
