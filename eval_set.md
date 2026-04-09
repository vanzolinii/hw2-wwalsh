# Evaluation Set

## Case 1: Normal Case: Standard feature release
**Input:**
```
- added dark mode toggle in user settings
- fixed crash when uploading files larger than 50mb
- improved dashboard load time by caching API responses
- new CSV export button on the reports page
- updated password reset email template
- fixed broken pagination on the users table
```

**What a good output should do:**
Group into Features, Improvements, and Bug Fixes. Use user-friendly language; e.g. "Added a dark mode option in settings" not "added dark mode toggle". Mention user benefit for the performance improvement. No jargon.

---

## Case 2: Normal Case: Minor patch / bug-fix only release
**Input:**
```
- fix null pointer exception in billing module when user has no payment method on file
- hotfix: session tokens not expiring correctly after logout
- corrected timezone offset bug in scheduled report emails
- removed duplicate notification sent on account creation
```

**What a good output should do:**
Produce a Bug Fixes-only release note. Summary should indicate this is a stability/fix release. Each bullet explains the user-visible impact (e.g. "Fixed an issue where logout did not properly end your session") without exposing internal details like "null pointer exception".

---

## Case 3: Normal Case: Major version with breaking changes
**Input:**
```
v3.0.0
- BREAKING: removed legacy v1 REST API endpoints (deprecated since 2023-06)
- BREAKING: auth tokens now expire after 24h instead of 30 days
- new GraphQL API now available at /api/graphql
- complete UI redesign using new design system
- added SSO support via SAML 2.0
- dropped support for IE11
```

**What a good output should do:**
Clearly flag breaking changes so users know action may be required. Introduce the new GraphQL API and SSO as headline features. Mention IE11 drop in a way that's informative but not alarming to users on modern browsers. Tone should be confident and forward-looking.

---

## Case 4: Edge Case: Cryptic / minimal commit messages
**Input:**
```
- wip
- fix tests
- PR #442
- refactor auth middleware
- bump lodash 4.17.19 -> 4.17.21
- misc cleanup
- typo
```

**What a good output should do:**
Recognize that most of these are internal/non-user-facing entries. Either produce very sparse release notes (acceptable) or note that there is nothing meaningful to surface to users. Should NOT hallucinate features or fixes not evidenced in the input. A good output might say something like "This release includes minor internal improvements and dependency updates."

---

## Case 5: Likely Failure / Hallucination / Requires Human Review
**Input:**
```
- JIRA-1045: finalize Q3 compliance work per legal review
- JIRA-1102: data retention policy update (see internal doc)
- JIRA-998: removed PII fields from analytics events per GDPR request
- JIRA-1110: updated terms of service (effective 2024-11-01)
- JIRA-1089: audit log now immutable per SOC2 requirement
```

**What a good output should do:**
This is a sensitive compliance/legal release. A good output surfaces the ToS update and GDPR/data changes in plain language since users need to know. It should NOT invent specifics about what the compliance changes entail. The JIRA IDs should be stripped. Requires human review before publishing; a grader should check whether the output accurately represents the legal implications without overstating or understating them.
