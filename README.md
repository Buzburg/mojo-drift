# Mojo Drift 🧭

**Asked for a bug fix. Got a redesign?**

Compare an agent's proposed action with the original goal and keep a local timeline of the results. Drift uses deterministic hashed word vectors and lexical overlap to flag actions that deserve a second look.

## Try it

Requires Python 3.11+. No runtime dependencies, API keys, or model download.

```sh
git clone https://github.com/Buzburg/mojo-drift.git
cd mojo-drift
python drift.py check --goal "Fix JWT token expiration" --action "Fix JWT token expiration"
python drift.py init --goal "Fix JWT token expiration"
python drift.py step --action "Redesign the checkout page colors"
python drift.py status
```

An alert exits 1. A missing session on `step` exits 2. Session history lives in `.mojo_drift/session.json` in the current directory; `init` starts a new history and replaces the previous one.

## A signal for review

The angle and `SAFE`/`WARN`/`DRIFT_ALERT` labels are **lexical heuristics**, not calibrated probabilities or reliable judgments of relevance. `SAFE` means the heuristic did not flag the text. Synonyms, short actions, and non-English text can produce misleading results. This tool does not intercept another agent automatically or prevent commands from running; a harness must explicitly consult it.

The supported CLI is Python. The separate `core.mojo` experiment compiles with Mojo 1.1.0 but is not loaded by the CLI. There is no measured end-to-end native speed guarantee.

## Verify

```sh
python -m unittest discover -v
# Optional native experiment:
mojo build core.mojo -o drift-native
```

Experimental advisory tool. [Release verification](RELEASE_VERIFICATION.md). MIT licensed. Built by Buzburg.
