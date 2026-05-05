---
name: file-watch
description: "Monitor files and directories for changes. Use for watching filesystem events or change detection."
tools: "../../tools.py"
level: 4
---

# Monitoring Filesystem Changes

A comprehensive skill for detecting and responding to filesystem changes in real-time. Enables watching files and directories for modifications, creations, deletions, and other events.

## Setup

To monitor files, you need read permission on watched paths. Monitoring may consume system resources. Specify what to watch and what events to detect.

## Available Operations

### Watching Directories
→ *Monitor a directory for any changes*

Continuously watch a directory and receive notifications when files are created, modified, deleted, or renamed within it. You specify which directory to watch.

No need to poll repeatedly - events are delivered as they happen. The most efficient way to detect changes in real-time.

**Comparison:** Unlike checking modification times periodically, this receives immediate notifications of all changes.

### Watching Specific Files
→ *Monitor individual files for changes*

Watch specific files for modifications. Receive notifications when file content changes, attributes change, or the file is deleted.

Efficient for monitoring important configuration files or logs.

### Recursive Directory Watching
→ *Monitor directory trees*

Watch not just a directory but all its subdirectories recursively. Events from anywhere in the tree are captured.

**Note:** Deep directory trees may generate many events.

### Event Filtering
→ *Watch for specific event types*

Filter to receive only certain types of events - only modifications, only creations, or only deletions. Reduces noise when you care about specific changes.

### Change Detection
→ *Identify what changed*

Compare current state to a baseline to detect all changes since the baseline was taken. Useful for detecting drift or unauthorized modifications.

Not real-time like watching, but provides complete change summary.

## Typical Workflows

### Workflow 1: Live Log Monitoring
1. Watch log file for modifications
2. When modification detected, process new content
3. Continue monitoring for further changes
4. Stop when monitoring no longer needed

### Workflow 2: Configuration Change Detection
1. Watch configuration directory
2. Alert when any configuration file changes
3. Identify which file changed
4. Take appropriate action

### Workflow 3: Build Trigger
1. Watch source code directory recursively
2. When source files change, trigger build
3. Avoid triggering on output file changes
4. Efficient incremental builds

### Workflow 4: Security Monitoring
1. Establish baseline of directory state
2. Periodically compare current state to baseline
3. Report any unexpected changes
4. Investigate discrepancies

## Inherited Capabilities

This skill encompasses all lower-level capabilities:
- File reading
- Directory listing
- Metadata access
- Comparison operations

## Important Considerations

- Watching consumes system resources
- Many rapid changes may queue events
- Recursive watches multiply resource use
- Some filesystem types have limited support
- Events may be batched or delayed

## Limitations

- Cannot watch without read permission
- Resource limits on number of watches
- Some filesystems don't support all events
- High-frequency changes may overwhelm
- Network filesystems may have limitations

## Notes

- Events typically include path and change type
- Modifications may fire multiple events
- Deleted watched paths stop generating events
- Moving files appears as delete + create
- Editor saves may appear as multiple events
