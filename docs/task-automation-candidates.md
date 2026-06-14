# Task Automation Candidates

This is a record of some recurring IT tasks weighed for automation. Each is judged based on four
questions: how often it happens, how intensive it is by hand, whether it follows
clear rules or needs human judgment, and the blast radius if it goes wrong.

## Ticket #3 — Monthly user folder size report

**Verdict: Automate first.**

- **How often:** monthly, it would be nice to have come the first of each month.
- **How intensive:** intensively tedious, one by one for many, error prone,
  inefficient as well.
- **Rules vs. judgment:** folders over 10 GB should be considered for a cleanup.
- **Blast radius:** non-destructive, simply review folders suggested for cleanup.
- **Why first:** read-only, it can't break anything, the safest place to start.

## Ticket #2 — Daily critical log review

**Verdict: Automate with care.**

- **How often:** daily, this could be very rewarding.
- **How intensive:** moderately tedious, reading a log every morning looking
  for "critical" errors and alerting the team.
- **Rules vs. Judgement** most days it's nothing, but occasionally a real
  issue is buried in the logs.
- **Blast radius** hazarous, it could leave clients experiencing critical
  issues and the team in the dark about those issues.
- **The catch:** "critical" needs judgment, the rules must be defined carefully.
- **Rollout:** run in *shadow mode* alongside the manual process during a
  probation period, comparing results and grading it before trusting it.

## Ticket #1 — Weekly temp-file cleanup

**Verdict: Automate later, with guardrails.**

- **How often** roughly once a week, unspecific
- **How intensive** minimual, a routine task the team handles ad hoc.
- **Rules vs. Judgement** the rule is clear; delete files older than 7 days.
  the hard part isn't judgment, it's the risk (see below)
  which is why it needs guardrails
- **Blast radius** destructive, many variables to consider, could negetively
  affect multiple team members.
- **The risk:** it deletes, wide blast radius.
- **Guardrails needed:** dry-run mode, archive instead of delete, log every
  action, scope tightly to the one disposable folder.
- **Also consider:** the real fix may be upstream (the build server cleaning up
  after itself).

## Build order

1. **#3** — folder size report (safe, read-only)
2. **#1** — temp cleanup (teaches safe *destructive* automation)
3. **#2** — log review (needs judgment — revisit when we add a local AI model)
