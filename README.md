# HW-2: Changelog → Release Notes

## Workflow
Takes raw developer changelog entries (commit messages, internal notes, ticket summaries) and produces polished, user-facing release notes grouped by category.

## User
Product managers, DevOps engineers, or developers responsible for communicating software releases to customers or stakeholders; anyone who needs to bridge the gap between internal dev language and user-friendly communication.

## Input
A block of raw changelog text: commit messages, bullet-pointed dev notes, or a mix of both. Optionally a version label (e.g. `v2.4.0`).

## Output
Formatted release notes with a one-sentence summary and categorized bullets (New Features, Improvements, Bug Fixes, Breaking Changes) written in plain language for end users.

## Why automate this?
Writing release notes is repetitive, time-consuming, and often deprioritized; leading to releases shipped with no communication or inconsistent tone. Automating the first draft lets the team focus on reviewing and refining rather than starting from scratch, reducing time-to-publish and improving release communication quality.

## Usage

```bash
# From a file
python app.py changelog.txt --version v2.4.0

# From stdin
echo "fixed login bug, added dark mode" | python app.py --version v1.2.0

# Save output to a file
python app.py changelog.txt --version v2.4.0 --output release_notes.md
```

Set your API key before running:
```bash
export ANTHROPIC_API_KEY=your_key_here
```

## Video Walkthrough
https://youtu.be/9gcXNCzlYBM
