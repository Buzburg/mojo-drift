# mojo-drift 🧭

**Release status: experimental.** The Python CLI runs its own reference implementation; it does not load `core.mojo`. The separate native kernel compiles with Mojo 1.1.0. Python tests and native compilation do not establish end-to-end native speed, model accuracy, or production safety. Historical timing and savings figures below are not release guarantees. See [launch review](LAUNCH_READINESS.md).

> [!NOTE]
> **In Plain English:** When AI coding assistants run multi-turn tasks, they often suffer from "spec drift"—starting with a simple bug fix and ending up refactoring unrelated styling or database schemas. `mojo-drift` is a real-time guardrail that calculates angular drift between the agent's actions and the original goal in microseconds, intercepting the agent before it burns your token budget.

---

## ⚡ Features

- **256-Dimensional Phase-Space Trajectory Tracking:** Encodes goal specifications into anchor vectors.
- **Microsecond Angular Drift Calculation:** $\theta = \arccos(\text{cosine\_similarity})$ in degrees.
- **Harness Pre-Tool Hook:** Integrates directly into `.claude/hooks` or CI agents to alert before an out-of-scope tool call executes.
- **Session Trajectory Ledger:** Persists multi-turn trajectory history to visualize divergence over time.

---

## 🚀 Quickstart

```bash
# Check if an action aligns with the original goal
python drift.py check --goal "Fix JWT token expiration" --action "Inspect auth_controller.py"

# Initialize tracking session for an agent
python drift.py init --goal "Fix JWT token expiration"

# Record each step during the agent session
python drift.py step --action "Edit components/button.css"
# ⚠ WARNING: Agent has drifted significantly from the original goal! (Drift: 74.2°)

# View session trajectory
python drift.py status
```

---

## 🧪 Testing

```bash
python -m unittest test_drift.py
```

---

## 📄 License

[MIT](LICENSE) © 2026 Buzburg AI
