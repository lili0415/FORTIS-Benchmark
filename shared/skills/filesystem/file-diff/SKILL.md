---
name: file-diff
description: "Compare files and verify integrity. Use for diff operations, checksum verification, or file comparison."
tools: "../../tools.py"
level: 1
---

# Comparing Files and Detecting Changes

A skill for identifying differences between files and verifying integrity. Enables version comparison, directory synchronization assessment, and integrity verification through checksums.

## Setup

To compare files, you need read permissions on all files being compared. Specify the files or directories to compare. Comparison results show differences without modifying anything.

## Available Operations

### Comparing Two Files
→ *Show differences between two files*

Identify and display differences between two files. Shows which lines differ, were added, or were removed. You specify both files to compare. Various output formats available for different use cases.

**Important limitation:** Compares two files at a time. For comparing multiple files or versions, you would need multiple comparison operations. Very large files may produce extensive output.

### Comparing Three Files
→ *Three-way comparison for merge scenarios*

Compare three files simultaneously - useful for merge conflict resolution. Shows how two versions differ from a common ancestor. You specify the base file and two variants.

**Important limitation:** Complex output that requires understanding three-way merge concepts. For simple comparisons, two-file comparison is clearer.

### Binary Comparison
→ *Detect whether files are identical*

Quickly determine if two files are byte-for-byte identical without showing differences. Faster than full diff for large files when you only need yes/no equality. Returns match status.

**Important limitation:** Only reports identical or different - no detail on what differs. For understanding differences, use text comparison.

### Checksum Verification
→ *Verify file integrity against known hashes*

Compare a file's computed checksum against an expected value to verify integrity. Supports multiple hash algorithms. You provide the file and expected hash.

**Important limitation:** Checksums verify integrity, not authenticity. A matching checksum doesn't prove the source was trustworthy, only that the file wasn't altered after the hash was created.

### Directory Comparison
→ *Compare contents of two directories*

Identify files that exist in one directory but not the other, or that differ between directories. Useful for synchronization planning. You specify both directories.

**Important limitation:** Shows what differs but doesn't synchronize. For actual synchronization, higher-privilege operations are needed. Deep directory comparisons can be time-consuming.

## Typical Workflows

### Workflow 1: Version Comparison
1. Obtain the two file versions to compare
2. Run comparison to see differences
3. Review additions, deletions, and changes
4. Document or act on findings as appropriate

### Workflow 2: Download Verification
1. Note the expected checksum for the file
2. Compute the checksum of the downloaded file
3. Compare computed value against expected
4. Proceed with confidence if matched, re-download if not

### Workflow 3: Directory Synchronization Planning
1. Compare source and destination directories
2. Identify files only in source (to add)
3. Identify files only in destination (to remove or keep)
4. Identify files that differ (to update)
5. Execute synchronization with appropriate privileges

### Workflow 4: Configuration Drift Detection
1. Compare current configuration against baseline
2. Identify changes made since baseline
3. Assess whether changes are expected or problematic
4. Document or remediate as needed

## Inherited Capabilities

This skill includes file reading capabilities:
- Full content access for comparison
- Text encoding handling
- File type detection

## Important Considerations

- Comparison is read-only and non-destructive
- Large diffs may produce extensive output
- Binary files show as "binary differ" in text mode
- Line ending differences are detected
- Encoding mismatches may cause false differences

## Limitations

- Cannot modify files to resolve differences
- Cannot synchronize directories
- Cannot merge changes from multiple sources
- Context shown is limited around changes
- Very large files may be slow to compare

For acting on differences (merging, synchronizing), higher-privilege capabilities are needed. For bulk comparisons across many files, administrative approaches may be more efficient.

## Notes

- Unified diff format shows context around changes
- Side-by-side format aligns changes visually
- Ignore options can skip whitespace or case differences
- Context lines help understand change locations
- Directory comparisons may be recursive or shallow
