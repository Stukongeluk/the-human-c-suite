# Changelog

All notable changes to **The Human C-Suite** are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Trigger test of the five descriptions (`benchmarks/triggers-v1.6/`): 90 messages against the seats and 22 competing skills on Sonnet and Opus. The CEO, CFO and CHRO were picked for 58 to 60 of their 60 requests, the CTO for 55 (and a seat for all 60), and no routine near-miss loaded a seat. The CPTO, at 45 of 60, got a new description; on a retest it rose from 30 to 40 of 52 with no new false loads.

### Changed
- The plugin now lives in its own folder, `plugins/the-human-c-suite/`, with a `.claude-plugin/plugin.json` manifest, a README, a licence and an icon, so it can be submitted to the Claude plugin directory. The marketplace points at that folder, so `/plugin install` works as before. To install the seats as plain skills, copy them from `plugins/the-human-c-suite/skills/`.
- The test cases moved from `skills/<seat>/evals/` to `evals/<seat>/`, outside the plugin. Installs now bring only the skills, and the plugin holds 90 files instead of almost 700, within the directory's limit of 512. `scripts/run_evals.py` runs a seat's cases with `claude plugin eval`.
- `the-human-cpto`: the description now names falling NPS, churn or adoption, so customer-outcome questions reach the CPTO instead of a generic metrics skill. To stay within 1,024 characters it no longer lists AI tooling and spend, which the CTO covers.
- `scripts/validate.py` also checks the plugin manifest against the marketplace (name, version and source) and the directory's file rules (README, licence, file count, file types and sizes, no test cases inside the plugin). CI also runs Claude Code's `claude plugin validate` on the marketplace and, with the directory profile, on the plugin.

## [1.6.0] - 2026-11-23

### Added
- **`the-human-chro` seat**: the fifth seat at the table, for people decisions. Judges the work instead of a curve or a counter, selects by the law and never by sick days, part-time hours or other proxies, tells people who are scored or selected and lets them object, fixes unexplained pay gaps on a dated plan measured in months, keeps dignity at every exit, treats layoffs as the last rung, writes announcements as proposals where works councils or unions must consent, and leads with the options that take nothing away from people: for a return to office, fixing the named problem directly and making home working good with funded team days, a home-working allowance and proper equipment. Covers reviews and ranking, layoff selection, return to office, pay gaps and the EU pay transparency rules, AI in hiring, monitoring, surveys and burnout, and contractors.
- Blind-graded CHRO benchmark on six people cases against the CEO seat, `chro-advisor` from alirezarezvani/claude-skills and no skill (`benchmarks/chro-v1.6/`): 34 of 36 checks on Sonnet against 27 for the CEO seat, 36 of 36 on Opus against 33, with the caveats in the benchmark and the follow-up reruns.
- Shared fact sheet (all seats): a Belgium section (works council thresholds, consultation on new technology under collective agreement No. 39, the 2012 pay gap law, discrimination lump sums and the pay transparency status).

### Changed
- `the-human-ceo`, `the-human-cfo`, `the-human-cto`, `the-human-cpto`: bring in the CHRO's check on fair process, pay equity and people law, and use `the-human-chro` when it is available.
- Shared fact sheet (all seats): Dutch works council consent on home-working policy, with the Caterpillar (2025) and Booking.com (2026) rulings; pay gap reporting dates set by national law and per legal entity (the Dutch bill: first reports in June 2028, on 2027); equal pay is already law (Article 157 TFEU); German dismissals are void when the mass-dismissal notification is missing or early (Federal Labour Court, 1 April 2026); ending agreed telework in Germany is a transfer that needs works council consent.
- The plugin description and keywords now include the CHRO seat, and the README preview shows all five seats.
- `scripts/validate.py` fails when a skill's description is longer than the 1,024 characters the Agent Skills format allows.

## [1.5.2] - 2026-11-23

### Added
- Benchmark of the CEO, CTO and CPTO seats against `ceo-advisor`, `cto-advisor` and `cpo-advisor` from alirezarezvani/claude-skills, plus a four-turn pushback test (with no-skill runs) and a test of which skill an agent loads when it sees all twelve (`benchmarks/c-suite-vs-claude-skills/`), with the caveats in the benchmark.
- Follow-up runs for this release, including a draft of the pushback rule that folded (`benchmarks/c-suite-vs-claude-skills/follow-ups/`).

### Changed
- All seats: under repeated pushback, each reply stays short, never hands over the declined part in another form, and still gives something new and usable that keeps every non-negotiable.
- All seats: the shortcut guidance names which moves are reversible and can start now, and which (layoffs, hiring stops, outsourcing) wait for data.
- `the-human-ceo`, `the-human-cto`, `the-human-cpto`: support from the day of notice goes in any plan in which roles might end; when a system scores, ranks, flags, schedules or selects people, they are told, can see their own data and can object, a person decides, and passing a flag to a subcontractor doesn't pass on the responsibility.
- Shared fact sheet (all seats): Swedish pay during notice and re-employment priority are legal rights, and the redundancy notice to Arbetsförmedlingen is confidential; Dutch dismissal for poor performance goes to the cantonal court.
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
