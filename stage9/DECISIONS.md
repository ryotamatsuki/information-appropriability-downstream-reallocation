# Stage 9 Decisions

Engineering only; no theory change.

1. Use Python 3.13.5 + `pip` + exact direct dependency pins.
2. Keep dependencies to SymPy and pytest; implement deterministic numerical maximization with the Python standard library.
3. Use seed `20260828` and 10,000 admissible regression draws.
4. Separate symbolic derivation from economic sign assumptions.
5. Commit deterministic text/CSV/JSON outputs and verify them by CI regeneration.
6. Use a minimal standard LaTeX `article` scaffold and `latexmk`.
7. Keep `references.bib` empty until metadata can be imported from the verified Stage-6 ledger.
8. Treat `stage8/**` as immutable and enforce this relative to the freeze SHA.
9. P1 stays regression/special-case only; no P4 analysis is implemented.
10. Do not begin Stage 10 prose in this branch.
