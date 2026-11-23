# Changelog

All notable changes to **The Human C-Suite** are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- README: the results section now shows only the benchmark comparisons; the version-by-version results moved to `benchmarks/HISTORY.md`.

## [1.5.1] - 2026-11-22

### Added
- Head-to-head benchmark against another open-source CFO skill, `cfo-advisor` from alirezarezvani/claude-skills (`benchmarks/cfo-vs-c-level-advisor/`): 141 of 144 checks against 85 of 144 across Claude Sonnet and Opus, graded blind, with the caveats in the benchmark.
- Follow-up runs for this release (`benchmarks/cfo-vs-c-level-advisor/follow-ups/`).

### Changed
- `the-human-cfo`: the rule against the seat's own terms now covers the reply and every document (including "the playbook" and "the templates"); for cash, runway and covenant problems the seat builds the 13-week cash forecast with base and downside headroom itself; each cash flow is dated when it is paid and temporary measures stay out of run-rates; involuntary reductions come with a fair package and support from the day of notice.
- Shared fact sheet (all seats): explains the Dutch selection rule for redundancies (afspiegelingsbeginsel) per group of interchangeable jobs, with sources.

## [1.5.0] - 2026-11-20

### Added
- **`the-human-cfo` seat**: the fourth seat at the table. Models every saving net of its costs and by quarter, keeps adjusted and one-off figures honest, works non-job levers first, handles cash/runway/covenants with the bank, challenges buybacks before investment, and designs long-term incentives with leaders' pay first.
- Blind-graded CFO benchmarks across six finance cases (`benchmarks/cfo-v1.5/`), passing 126 of 144 checks vs. 113 for the CEO seat across four models.
- Four-seat animated preview GIF in the README.

### Changed
- Updated `the-human-ceo`, `the-human-cto`, and `the-human-cpto` to bring in the CFO's view when financial trade-offs arise.
- Refined CFO references (Bain's 12% transformation statistic and the SEC rule on non-recurring labels).
- Moved preview and install instructions to the top of the README.

## [1.4.0] - 2026-11-20

### Added
- **`company-types.md` shared reference**: adapts all seats to any kind of organisation — startups, family firms, listed or PE-owned groups, cooperatives, non-profits, public bodies, and frontline operations (retail, care, warehouses, factories).
- Dutch on-call and flex-work legal touchpoints.
- Six non-software evaluation cases and published benchmarks (`benchmarks/company-types-v1.4/`).

### Changed
- Made the company context brief sector-neutral across all seats.

## [1.3.3] - 2026-11-20

### Added
- **Clear direction guidance** in `good-leadership.md`: start from customer problems after a merger, rebrand, sale, or reorg rather than reorganising again.
- Two new evaluation cases and published benchmark results (`benchmarks/check-v1.3.3/`).

## [1.3.2] - 2026-11-20

### Added
- **Push back privately first** guidance when advising a single leader, plus published benchmark verification (`benchmarks/check-v1.3.2/`).

## [1.3.1] - 2026-11-20

### Changed
- Clarified the role and boundaries of the confidential adviser across shared references.

## [1.3.0] - 2026-11-20

### Added
- **Leadership toolkit** (`shared/leadership-toolkit.md`) and tighter, shorter replies when leaders are in a hurry.
- Published v1.3 blind benchmarks across Claude (`benchmarks/claude-v1.3/`) and Gemini through Antigravity (`benchmarks/gemini-v1.3/`).

## [1.2.1] - 2026-11-20

### Added
- **Leaders go first** guidance (including the Nintendo pay-cut example) so executive pay, bonuses, and perks are cut before frontline jobs.

## [1.2.0] - 2026-11-20

### Added
- **European and Nordic social practice** (`shared/european-and-nordic-practice.md`), covering works councils, Kurzarbeit, Sweden's job security councils, Finland's training duty, and the EU AI Act at work.
- Good leadership reference (`shared/good-leadership.md`) and recommended MCP data connectors.

## [1.1.0] - 2026-11-20

### Added
- **`the-human-cto` and `the-human-cpto` seats**, tested with blind grading on Claude Sonnet and Opus.
- Shared reference pipeline (`shared/` + `scripts/sync_shared.py`) so every skill folder stays self-contained without drifting.

## [1.0.0] - 2026-11-19

### Added
- Initial release of **`the-human-ceo`** skill, test cases (`skills/the-human-ceo/evals/`), and Claude Code plugin marketplace configuration.
