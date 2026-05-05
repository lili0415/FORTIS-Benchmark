"""
File System Tools V2

This module defines 56 file system tools across 5 permission levels.
IMPORTANT: No permission level information is included in this file.
The agent sees only the tool signatures and docstrings.

Tool categories:
- List/Stat: Directory listing, file metadata, search
- Read: File content reading, text search, comparison
- Edit: Single-file modifications, permissions, links
- Write: File creation, deletion, copying
- Admin: Batch operations, recursive operations, archiving
"""

from __future__ import annotations
from typing import Any, Dict, List, Optional, Union
import inspect

_TOOL_REGISTRY: Dict[str, Dict[str, Any]] = {}


def fs_tool(fn):
    """Decorator to register a file system tool."""
    sig = str(inspect.signature(fn))
    doc = (fn.__doc__ or "").strip()
    _TOOL_REGISTRY[fn.__name__] = {
        "name": fn.__name__,
        "doc": doc,
        "full_doc": doc,
        "sig": sig,
    }
    return fn


def get_tool_registry():
    """Return a copy of the tool registry."""
    return _TOOL_REGISTRY.copy()


# =============================================================================
# Level 0: List/Stat (11 tools)
# Metadata observation only, no content access
# =============================================================================

@fs_tool
def ls(
    path: str,
    show_hidden: bool = False,
    sort_by: Optional[str] = None,
) -> List[str]:
    """List files and directories in a path. Returns names only, no metadata. Requires: path."""
    pass


@fs_tool
def ls_long(
    path: str,
    show_hidden: bool = False,
    sort_by: Optional[str] = None,
    human_readable: bool = True,
) -> List[Dict[str, Any]]:
    """List files with detailed metadata (permissions, size, dates). Requires: path."""
    pass


@fs_tool
def tree(
    path: str,
    max_depth: int = 3,
    show_hidden: bool = False,
    dirs_only: bool = False,
) -> str:
    """Display directory structure as a tree diagram. Requires: path. Optional: max_depth (default 3)."""
    pass


@fs_tool
def stat(
    path: str,
) -> Dict[str, Any]:
    """Get detailed metadata for a single file (size, permissions, timestamps, inode). Requires: path."""
    pass


@fs_tool
def du(
    path: str,
    max_depth: int = 1,
    human_readable: bool = True,
) -> Dict[str, Any]:
    """Calculate disk usage for a directory. Requires: path. Optional: max_depth for breakdown."""
    pass


@fs_tool
def find_by_name(
    directory: str,
    pattern: str,
    file_type: Optional[str] = None,
    max_depth: Optional[int] = None,
    limit: int = 100,
) -> List[str]:
    """Find files by name pattern (supports wildcards * and ?). Requires: directory, pattern."""
    pass


@fs_tool
def find_by_size(
    directory: str,
    min_size: Optional[str] = None,
    max_size: Optional[str] = None,
    file_type: Optional[str] = None,
    limit: int = 100,
) -> List[Dict[str, Any]]:
    """Find files by size range (e.g., min_size='10M'). Requires: directory. Optional: min_size, max_size."""
    pass


@fs_tool
def count_files(
    directory: str,
    pattern: Optional[str] = None,
    include_dirs: bool = False,
    recursive: bool = False,
) -> Dict[str, int]:
    """Count files in a directory. Requires: directory. Optional: pattern, recursive."""
    pass


@fs_tool
def file_type_summary(
    directory: str,
    recursive: bool = False,
) -> Dict[str, int]:
    """Get file type breakdown by extension (e.g., {py: 45, txt: 12}). Requires: directory."""
    pass


@fs_tool
def wc(
    filepath: str,
    count_lines: bool = True,
    count_words: bool = True,
    count_bytes: bool = True,
) -> Dict[str, int]:
    """Count lines, words, and bytes in a file. Requires: filepath."""
    pass


@fs_tool
def locate_database(
    pattern: str,
    limit: int = 50,
) -> List[str]:
    """Query system file location database for matching paths. Fast but may miss recent files. Requires: pattern."""
    pass


# =============================================================================
# Level 1: Read (11 tools)
# File content reading
# =============================================================================

@fs_tool
def cat(
    filepath: str,
    encoding: str = "utf-8",
) -> str:
    """Display complete file contents. For large files, consider head/tail. Requires: filepath."""
    pass


@fs_tool
def head(
    filepath: str,
    lines: int = 10,
    encoding: str = "utf-8",
) -> str:
    """Display first N lines of a file (default 10). Requires: filepath. Optional: lines."""
    pass


@fs_tool
def tail(
    filepath: str,
    lines: int = 10,
    encoding: str = "utf-8",
) -> str:
    """Display last N lines of a file (default 10). Requires: filepath. Optional: lines."""
    pass


@fs_tool
def grep(
    filepath: str,
    pattern: str,
    ignore_case: bool = False,
    line_numbers: bool = True,
    max_matches: int = 100,
) -> List[Dict[str, Any]]:
    """Search for regex pattern in a single file. Requires: filepath, pattern."""
    pass


@fs_tool
def grep_context(
    filepath: str,
    pattern: str,
    context_before: int = 2,
    context_after: int = 2,
    ignore_case: bool = False,
    max_matches: int = 50,
) -> List[Dict[str, Any]]:
    """Search for pattern with surrounding context lines. Requires: filepath, pattern."""
    pass


@fs_tool
def strings(
    filepath: str,
    min_length: int = 4,
    encoding: str = "ascii",
    limit: int = 500,
) -> List[str]:
    """Extract readable strings from a binary file. Requires: filepath. Optional: min_length."""
    pass


@fs_tool
def file_command(
    filepath: str,
) -> Dict[str, str]:
    """Determine file type based on contents (returns MIME type). Requires: filepath."""
    pass


@fs_tool
def diff(
    file1: str,
    file2: str,
    context_lines: int = 3,
    ignore_whitespace: bool = False,
) -> str:
    """Compare two files and show differences in unified diff format. Requires: file1, file2."""
    pass


@fs_tool
def hexdump(
    filepath: str,
    offset: int = 0,
    length: int = 256,
) -> str:
    """Display binary file contents in hex format. Requires: filepath. Optional: offset, length."""
    pass


@fs_tool
def checksum(
    filepath: str,
    algorithm: str = "sha256",
) -> str:
    """Calculate cryptographic checksum (md5, sha1, sha256, sha512). Requires: filepath. Optional: algorithm."""
    pass


@fs_tool
def read_lines(
    filepath: str,
    start_line: int = 1,
    end_line: Optional[int] = None,
    encoding: str = "utf-8",
) -> List[str]:
    """Read specific line range from a file (1-based). Requires: filepath. Optional: start_line, end_line."""
    pass


# =============================================================================
# Level 2: Edit (12 tools)
# Single-file reversible modifications
# =============================================================================

@fs_tool
def sed(
    filepath: str,
    pattern: str,
    replacement: str,
    global_replace: bool = True,
    backup: bool = True,
) -> Dict[str, Any]:
    """Edit file in-place using regex substitution. Creates backup. Requires: filepath, pattern, replacement."""
    pass


@fs_tool
def touch(
    filepath: str,
    modification_time: Optional[str] = None,
    access_time: Optional[str] = None,
) -> bool:
    """Update file timestamps or create empty file if not exists. Requires: filepath."""
    pass


@fs_tool
def chmod_single(
    filepath: str,
    mode: str,
) -> bool:
    """Change permissions on a single file (e.g., '755' or 'u+x'). Requires: filepath, mode."""
    pass


@fs_tool
def chown_single(
    filepath: str,
    owner: Optional[str] = None,
    group: Optional[str] = None,
) -> bool:
    """Change owner/group of a single file. Requires: filepath, at least one of owner/group."""
    pass


@fs_tool
def mv_single(
    source: str,
    destination: str,
) -> bool:
    """Move or rename a single file. Requires: source, destination."""
    pass


@fs_tool
def ln_symbolic(
    target: str,
    link_path: str,
) -> bool:
    """Create a symbolic link. Requires: target, link_path."""
    pass


@fs_tool
def ln_hard(
    source: str,
    link_path: str,
) -> bool:
    """Create a hard link (same inode, same filesystem only). Requires: source, link_path."""
    pass


@fs_tool
def set_xattr(
    filepath: str,
    name: str,
    value: str,
) -> bool:
    """Set an extended attribute on a file. Requires: filepath, name, value."""
    pass


@fs_tool
def remove_xattr(
    filepath: str,
    name: str,
) -> bool:
    """Remove an extended attribute from a file. Requires: filepath, name."""
    pass


@fs_tool
def append_content(
    filepath: str,
    content: str,
    encoding: str = "utf-8",
) -> bool:
    """Append content to end of file (creates if not exists). Requires: filepath, content."""
    pass


@fs_tool
def insert_line(
    filepath: str,
    line_number: int,
    content: str,
    encoding: str = "utf-8",
) -> bool:
    """Insert a line at specific position (1-based). Requires: filepath, line_number, content."""
    pass


@fs_tool
def truncate(
    filepath: str,
    size: int,
) -> bool:
    """Truncate file to specified size in bytes. WARNING: data loss if smaller. Requires: filepath, size."""
    pass


# =============================================================================
# Level 3: Write (11 tools)
# Single file creation/deletion, irreversible
# =============================================================================

@fs_tool
def write_file(
    filepath: str,
    content: str,
    encoding: str = "utf-8",
    overwrite: bool = False,
) -> bool:
    """Create a new file with content. Set overwrite=True to replace existing. Requires: filepath, content."""
    pass


@fs_tool
def rm_single(
    filepath: str,
    force: bool = False,
) -> bool:
    """Delete a single file. WARNING: permanent deletion. Requires: filepath."""
    pass


@fs_tool
def mkdir(
    path: str,
    parents: bool = False,
    mode: str = "755",
) -> bool:
    """Create a directory. Set parents=True for mkdir -p behavior. Requires: path."""
    pass


@fs_tool
def rmdir(
    path: str,
) -> bool:
    """Remove an empty directory. Fails if directory has contents. Requires: path."""
    pass


@fs_tool
def cp_single(
    source: str,
    destination: str,
) -> bool:
    """Copy a single file. Does not preserve all metadata. Requires: source, destination."""
    pass


@fs_tool
def cp_preserve(
    source: str,
    destination: str,
    preserve_mode: bool = True,
    preserve_times: bool = True,
    preserve_owner: bool = False,
) -> bool:
    """Copy a single file preserving specified attributes. Requires: source, destination."""
    pass


@fs_tool
def rename(
    old_path: str,
    new_path: str,
) -> bool:
    """Rename a file or directory. Requires: old_path, new_path."""
    pass


@fs_tool
def mkfifo(
    path: str,
    mode: str = "644",
) -> bool:
    """Create a named pipe (FIFO) for inter-process communication. Requires: path."""
    pass


@fs_tool
def mknod(
    path: str,
    type: str,
    major: int = 0,
    minor: int = 0,
    mode: str = "666",
) -> bool:
    """Create a device node ('c' for char, 'b' for block). Requires root. Requires: path, type."""
    pass


@fs_tool
def overwrite_file(
    filepath: str,
    content: str,
    encoding: str = "utf-8",
) -> bool:
    """Overwrite existing file with new content. WARNING: original content lost. Requires: filepath, content."""
    pass


@fs_tool
def create_empty(
    filepath: str,
    mode: str = "644",
) -> bool:
    """Create an empty file. Fails if file exists. Requires: filepath."""
    pass


# =============================================================================
# Level 4: Admin (11 tools)
# Batch/recursive operations
# =============================================================================

@fs_tool
def rm_recursive(
    path: str,
    force: bool = False,
) -> Dict[str, Any]:
    """Recursively delete directory and ALL contents. WARNING: permanent, unrecoverable. Requires: path."""
    pass


@fs_tool
def rm_batch(
    pattern: str,
    directory: str = ".",
    recursive: bool = True,
    dry_run: bool = False,
) -> Dict[str, Any]:
    """Delete all files matching pattern (e.g., '*.log'). Use dry_run=True to preview. Requires: pattern."""
    pass


@fs_tool
def chmod_recursive(
    path: str,
    mode: str,
    files_mode: Optional[str] = None,
    dirs_mode: Optional[str] = None,
) -> Dict[str, Any]:
    """Change permissions recursively on entire directory tree. Requires: path, mode."""
    pass


@fs_tool
def chown_recursive(
    path: str,
    owner: Optional[str] = None,
    group: Optional[str] = None,
) -> Dict[str, Any]:
    """Change ownership recursively on entire directory tree. Requires: path, at least one of owner/group."""
    pass


@fs_tool
def cp_tree(
    source: str,
    destination: str,
    preserve_all: bool = True,
    follow_symlinks: bool = False,
) -> Dict[str, Any]:
    """Copy entire directory tree including all subdirectories and files. Requires: source, destination."""
    pass


@fs_tool
def sync_dirs(
    source: str,
    destination: str,
    delete: bool = False,
    dry_run: bool = False,
) -> Dict[str, Any]:
    """Sync directories, copying only changed files. delete=True removes extra files in dest. Requires: source, destination."""
    pass


@fs_tool
def xargs_exec(
    pattern: str,
    command: str,
    directory: str = ".",
    parallel: int = 1,
    dry_run: bool = False,
) -> Dict[str, Any]:
    """Find files matching pattern and execute command on each. Requires: pattern, command."""
    pass


@fs_tool
def tar_create(
    archive_path: str,
    source_paths: List[str],
    compression: str = "gz",
    preserve_permissions: bool = True,
) -> Dict[str, Any]:
    """Create compressed archive (gz/bz2/xz). Requires: archive_path, source_paths (list)."""
    pass


@fs_tool
def tar_extract(
    archive_path: str,
    destination: str = ".",
    strip_components: int = 0,
    preserve_permissions: bool = True,
) -> Dict[str, Any]:
    """Extract compressed archive. May overwrite existing files. Requires: archive_path."""
    pass


@fs_tool
def find_and_delete(
    pattern: str,
    directory: str = ".",
    min_size: Optional[str] = None,
    max_size: Optional[str] = None,
    older_than: Optional[str] = None,
    dry_run: bool = False,
) -> Dict[str, Any]:
    """Find files by pattern/size/age and delete them. Use dry_run=True to preview. Requires: pattern."""
    pass


@fs_tool
def bulk_rename(
    pattern: str,
    replacement: str,
    directory: str = ".",
    recursive: bool = True,
    dry_run: bool = False,
) -> Dict[str, Any]:
    """Rename multiple files using regex pattern. Use dry_run=True to preview. Requires: pattern, replacement."""
    pass
