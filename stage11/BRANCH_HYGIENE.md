# Stage 11 Branch Hygiene

## Canonical base

- Starting post-Stage-10 `main`: `1564118776a225424e8efd040e68daf197ef023a`
- Stage 10 PR: `#3` — merged
- Stage 10 final HEAD: `0118d08ac0cedc4386d527cbb78a7be372951bfd`
- Stage 8 freeze SHA: `ef588465430f618b56cf84445681752702c161e1`
- Workflow v1.1 SHA: `488e5ab06c207909296a7564eaf9066f7f94319c`

## Remote branch classification

| Branch | HEAD | Ahead of main | Behind main | PR / state | Unique unmerged work | Classification | Action |
|---|---|---:|---:|---|---|---|---|
| `stage8/canonical-theory-freeze` | `ddf266e1191938c14d787abb05bf5e56c999a0dc` | 0 | 30 | historical Stage 8 / integrated | No | HISTORICAL — FULLY INTEGRATED | Leave untouched; never use as a new base |
| `stage9/reproducibility-setup` | `db202ddd3b9266a2f18bae2f6644cbb4b0d1a63c` | 0 | 24 | PR #2 merged | No | HISTORICAL — FULLY INTEGRATED | Leave untouched; never use as a new base |
| `stage9/reproducibility-setup-temp` | `c11a3628aa28515a3462f35c218a8bf2339cad5a` | 0 | 28 | abandoned intermediate | No | TEMPORARY — OBSOLETE | Leave untouched; explicitly excluded as a future base |
| `stage10/manuscript-drafting` | `0118d08ac0cedc4386d527cbb78a7be372951bfd` | 0 | 1 | PR #3 merged | No | HISTORICAL — FULLY INTEGRATED | Leave untouched; never use as a new base |

At Stage 11 initialization there were no open pull requests and no pre-existing Stage 11 branch. `stage11/referee-attack` was therefore created from the verified post-Stage-10 `main` SHA above.

## Safety attestation

No historical branch was deleted, merged, rebased, force-updated, or otherwise rewritten during Stage 11 initialization. No branch other than `stage11/referee-attack` is authorized as the Stage 11 working base.
