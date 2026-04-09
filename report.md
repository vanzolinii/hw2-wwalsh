# Report: Changelog → Release Notes

## Business Use Case

Software teams ship releases frequently but often deprioritize writing release notes — the result is either no communication, or terse developer-language notes that confuse end users. This prototype automates the first draft of user-facing release notes from raw changelog input (commit messages, internal notes, or ticket summaries). The intended user is a product manager, DevOps engineer, or developer who is responsible for communicating releases to customers but lacks the time or bandwidth to rewrite internal changelogs from scratch. The system receives a block of raw changelog text and an optional version label, and produces structured, plain-language release notes grouped into sections (New Features, Improvements, Bug Fixes, Breaking Changes). Automating this task reduces time-to-publish, improves consistency across releases, and ensures users receive timely communication about what changed and why it matters to them.

## Model Choice

The prototype uses `claude-haiku-4-5-20251001`. Haiku was chosen because the task is well-defined and formulaic — it requires rewriting and categorizing short bullet points, not complex reasoning. Haiku is fast and low-cost, which matters for a workflow likely to run on every release. No other models were tested, but Sonnet or Opus would add latency and cost without meaningful benefit for this specific task. For a compliance-heavy organization that needs higher reliability on the human-review flag, upgrading to Sonnet could be justified.

## Baseline vs. Final Design

The initial prompt produced strong results on routine cases but had two meaningful failures. On Case 3 (major version with breaking changes), the auth token expiry change was placed under "Improvements" rather than flagged as breaking — a user who missed that would face unexpected logouts after upgrading. On Case 4 (cryptic commit messages), the model refused to produce any output and instead asked the user for more information, which breaks automation entirely. On Case 5 (compliance release), the model produced plausible-sounding notes without any signal that human review was needed.

Revision 1 added an explicit "Breaking Changes" section with a rule that any change removing functionality or requiring user action belongs there. It also added a fallback instruction directing the model to produce a minimal note for non-user-facing inputs rather than refusing. Both fixes worked as intended: Case 3 now correctly categorizes the auth token and IE11 changes as breaking, and Case 4 produces a usable one-line note. Revision 2 added a human-review flag triggered by compliance, legal, or privacy-related input. Case 5 now opens with a visible warning before the draft notes, correctly signaling that the output requires verification before publishing. Cases 1 and 2 were unaffected across all three versions.

## Where the Prototype Still Fails

The prototype handles well-labeled input reliably but struggles with ambiguity. If a changelog entry says "refactor auth middleware" without context, the model cannot know whether this affects users (e.g., changed session behavior) or is purely internal — and it will silently drop the entry. Similarly, the human-review flag depends on keywords like "GDPR" or "compliance" appearing in the input; a compliance change described in plain language without those terms would not trigger the flag. The system also has no memory of prior releases, so it cannot detect duplicate notes, track what was already communicated, or flag a change that contradicts a previous release. All outputs should be reviewed before publishing.

## Deployment Recommendation

This prototype is suitable for deployment as a draft-generation tool under human supervision. It should not be deployed as a fully automated publish pipeline. The recommended workflow is: run the script to generate a first draft, have the responsible product manager review and edit, then publish. This preserves the time savings of automation while keeping a human in the loop for accuracy. The compliance flag (added in Revision 2) is the most important safety control — any release triggering that flag should be reviewed by someone familiar with the relevant legal or regulatory context before notes go out. The system should not be used in contexts where compliance or legal accuracy is critical without that review step in place.
