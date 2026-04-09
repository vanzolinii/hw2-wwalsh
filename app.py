import os
import sys
import argparse
import anthropic

MODEL = "claude-haiku-4-5-20251001"

SYSTEM_PROMPT = """You are a technical writer who transforms raw developer changelogs into clear, user-facing release notes.

Your release notes must:
- Be written for end users, not developers; avoid internal jargon, ticket IDs, and implementation details
- Group changes into sections using only these labels (omit any section with no entries): New Features, Improvements, Bug Fixes, Breaking Changes
- Place any change that removes functionality, changes default behavior, or requires user action in Breaking Changes, not in Improvements
- Lead each bullet with a strong action verb (e.g. "Added", "Fixed", "Improved", "Removed")
- Highlight user benefit, not technical mechanism
- Keep each bullet to one sentence
- Use a warm but professional tone
- Include a one-sentence summary paragraph at the top describing the release overall

If the input contains only internal or non-user-facing entries (e.g. refactors, test fixes, dependency bumps, WIP notes), do not refuse. Instead produce a brief release note stating that this release contains minor internal improvements with no user-facing changes.

If the input contains compliance, legal, regulatory, or privacy-related changes (e.g. GDPR, SOC2, terms of service, data retention, audit requirements), include a prominent note at the top of the output: "⚠️ Human Review Required: This release contains compliance or legal changes. Please have a qualified reviewer verify the accuracy and completeness of these notes before publishing."

Do not include: commit hashes, branch names, internal ticket numbers (e.g. JIRA-123), or developer names unless they are the user-facing author.
Do not invent features or fixes not present in the input."""


def generate_release_notes(changelog_text: str, version: str = None) -> str:
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    version_line = f"Version: {version}\n\n" if version else ""
    user_message = f"{version_line}Changelog:\n{changelog_text}"

    message = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    )

    return message.content[0].text


def main():
    parser = argparse.ArgumentParser(description="Convert a changelog to release notes using Claude.")
    parser.add_argument("input", nargs="?", help="Path to changelog file (omit to read from stdin)")
    parser.add_argument("--version", "-v", help="Version label (e.g. v2.4.0)")
    parser.add_argument("--output", "-o", help="Path to save output (omit to print to stdout)")
    args = parser.parse_args()

    if args.input:
        with open(args.input, "r") as f:
            changelog_text = f.read()
    else:
        print("Paste your changelog below (Ctrl+D when done):", file=sys.stderr)
        changelog_text = sys.stdin.read()

    if not changelog_text.strip():
        print("Error: changelog input is empty.", file=sys.stderr)
        sys.exit(1)

    release_notes = generate_release_notes(changelog_text, version=args.version)

    if args.output:
        with open(args.output, "w") as f:
            f.write(release_notes)
        print(f"Release notes saved to {args.output}", file=sys.stderr)
    else:
        print(release_notes)


if __name__ == "__main__":
    main()
