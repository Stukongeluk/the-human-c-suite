# Contributing to The Human C-Suite

Pushback is the point. Every seat ends with *"what am I missing?"* — and the same applies to this repository. Issues, challenges, better evidence, and pull requests are welcome.

## High-value contributions

- **Pushback on advice patterns**: cases where a seat gave weak, unrealistic, or overly soft advice — include the prompt and what a sharp, humane leader should have done instead.
- **Better evidence**: peer-reviewed research, filings, or primary-source company examples (both positive and cautionary) with dated citations.
- **Local legal & social practice**: works council rules, consultation duties, short-time work schemes, or AI-at-work rules in countries not yet covered.
- **New seats at the table**: for example, a humane **CHRO**, **COO**, or **General Counsel** seat that follows the same principles and cross-seat pattern.

## Working with shared files

Each folder under `plugins/the-human-c-suite/skills/` is designed to work on its own (for single-skill zip installs). Files shared across multiple seats live once in `shared/` (and marked blocks in `shared/blocks/`), then get copied into each skill.

Always edit the canonical copy in `shared/`, then run:

```bash
python3 scripts/sync_shared.py     # copy shared files into every skill
python3 scripts/validate.py        # check sync, JSON, and skill frontmatter
```

CI runs `python3 scripts/validate.py` on every pull request and fails if any skill has drifted from `shared/` or if versions disagree across `SKILL.md` and `.claude-plugin/marketplace.json`.

## Evidence & writing standards

- **Cite your sources.** If you add a statistic, study, or company example, link to the primary source and note its year.
- **Keep it plainspoken and sharp.** Avoid corporate jargon and preachiness. Make the humane case with numbers, governance, and real operational detail.
- **Match the format.** Respect short-answer rules, read-only defaults, and privacy boundaries (aggregated people data only).

## Running evals

Before opening a pull request that changes skill behaviour, check that the relevant seat still passes its evals. With Claude Code (note: these are real, billed model runs):

```bash
python3 scripts/run_evals.py the-human-cto -- --allow-tools Write,Edit,Bash
```

The test cases live in `evals/<seat>/`, outside the plugin, so installs stay small and the plugin stays within the Claude plugin directory's file limits. The script copies the seat and its cases into `dist/eval-runs/<seat>/` and runs `claude plugin eval` there; add new cases to `evals/<seat>/`, never inside the skill folder.

You can also try prompts by hand from [examples/test-prompts.md](examples/test-prompts.md).

## Packaging & releases (maintainers)

To test the release zip archives locally (written to `dist/`, which is gitignored):

```bash
python3 scripts/package_skills.py
```

To cut a new release:
1. Bump `"version"` in `.claude-plugin/marketplace.json`, in `plugins/the-human-c-suite/.claude-plugin/plugin.json` and `metadata.version` in every `plugins/the-human-c-suite/skills/*/SKILL.md`.
2. Add a matching `## [X.Y.Z] - YYYY-MM-DD` section to [CHANGELOG.md](CHANGELOG.md).
3. Run `python3 scripts/validate.py --tag vX.Y.Z`.
4. Commit, tag `vX.Y.Z`, and push the tag — GitHub Actions automatically builds the clean `.zip` archives and publishes the GitHub Release.
