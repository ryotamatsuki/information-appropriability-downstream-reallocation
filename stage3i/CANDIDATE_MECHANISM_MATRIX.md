# Stage 3-I — Candidate Mechanism Matrix

Scoring weights were fixed ex ante: proposition novelty 25, information essentiality 20, whole-game prior-art survival 20, mechanism clarity 10, tractability 10, welfare 5, institutional plausibility 5, empirical bridge 3, journal-family relevance 2.

Automatic caps from the Stage 3-I contract were applied where relevant.

| Candidate | Information-specific object | New strategic arrow | Generic effort reduction? | Closest prior | Expected theorem/result | Welfare | Tractability | Score | Verdict |
|---|---|---|---|---|---|---|---|---:|---|
| A Persistent reusable information stock | persistent nonrival stock `I_{t+1}` | effort -> stock -> future use | Yes unless nonrival reuse/rights add further structure | dynamic data/knowledge models; Wang–Wang 2026; service carry-over models | persistence/appropriability wedge | potentially strong | medium | 35 | KILL — GENERIC DYNAMIC INVESTMENT / PRIOR ART |
| B Endogenous upstream adoption | upstream implementation action `a` | information -> manufacturer adoption -> return to producer | Partly; adoption can be generic investment response | Hu et al. 2021; vertical R&D/quality investment | adoption threshold/nonmonotonic effort | moderate | high | 35 | KILL — PRIOR ART / MECHANICAL THRESHOLD RISK |
| C Ownership/access rights | excludable information asset/control | rights -> access -> ex-ante investment | No, but data/property-rights theory already contains it | Jones–Tonetti 2020; Wang–Wang 2026 | ownership changes investment/use | strong | medium | 33 | KILL — PRIOR ART |
| D Portability after reallocation | transferability across organizational boundary | portability -> future use -> current collection | No | Li–Zhang 2026 IJIO; Wang–Wang 2026 | portability changes collection and competition | strong | high | 32 | KILL — PRIOR ART |
| E Acquisition versus disclosure | separate acquisition and disclosure actions | acquisition -> signal -> disclosure -> upstream response | No | Guo–Iyer 2010; Jiang–Wu–Zhao 2026 | acquisition/sharing wedges | strong | high | 30 | KILL — PRIOR ART |
| F Bayesian precision / learning | endogenous posterior precision | effort -> precision -> upstream action | No | Guo 2009; Hu et al. 2021; rational-inattention / precision-acquisition work | precision choice and quality response | moderate | high | 34 | KILL — PRIOR ART |
| G Competing information producers | multiple strategic precision suppliers | each effort -> aggregate posterior -> other effort | Not generically, but close information-network games contain it | Li et al. 2020; Jiang et al. 2026; Myatt–Wallace 2019; Migrow–Squintani 2023 | strategic substitution/complementarity in acquisition | moderate | medium | 35 | KILL — CLOSE PRIOR / NO DISTINCT RESULT FROM H |
| H Diagnostic / informational diversity | multidimensional state + non-collinear signal loadings | reallocation -> source mix/effort -> posterior geometry -> upstream design -> returns | **No** | Xiong–Li–Lang 2025; Myatt–Wallace 2019; Migrow–Squintani 2023; Gao et al. 2015 | total effort can rise while design accuracy falls; low-volume source may merit retention for unique diagnostic direction | strong | medium-high | **83** | **PREFERRED** |
| I Post-exit reuse / intertemporal appropriability | persistent learning asset usable after separation | current investment -> post-exit use -> ex-ante return | Often collapses to specific investment/hold-up | Wang–Wang 2026; relationship-specific investment | post-exit continuation creates underinvestment | strong | medium | 30 | KILL — PRIOR ART |
| J Retention for learning option value | future signal-arrival option under uncertainty | retain -> learn -> adapt -> continuation value -> retain | No | Board–Meyer-ter-Vehn 2024; Gieczewski–Kosterina 2024 | commercially weak node retained for experimentation option | strong | low-medium | **68** | **TOP 3 (runner-up)** |

## Candidate dispositions

### A — KILL

A state equation such as `I_{t+1}=(1-delta)I_t+g(e_t)` does not by itself make the economics information-specific. Persistent service/customer capital or generic knowledge capital can generate the same dynamic investment logic. More information-specific versions require nonrival reuse, residual control or post-exit rights, but those additions move directly toward existing data/learning-asset literatures.

### B — KILL

Making the manufacturer choose an implementation/quality action after downstream information creates a strategic arrow, but a close version is already present in Hu et al. (2021): retailer information acquisition/sharing interacts with the manufacturer's quality decision. A binary adoption cost would primarily manufacture a threshold.

### C — KILL

Information ownership is genuinely information/data-specific, but it is not an open mechanism by itself. Jones and Tonetti establish the importance of property rights for nonrival data use, and 2026 learning-asset work directly studies residual control over a persistent jointly created informational asset.

### D — KILL

Li and Zhang (2026) already provide a two-period model where data collected in period 1 can be transferred to another firm in period 2, and portability changes firms' ex-ante data collection. This is too close to the proposed portability mechanism.

### E — KILL

The acquisition/disclosure distinction is central to Guo–Iyer and remains an active 2026 supply-chain literature. Reallocation vocabulary does not create a new game unless an additional interaction is supplied, which would violate the one-new-object discipline for this candidate.

### F — KILL

Signal precision is information-specific but not novel. The proposed architecture is a standard costly-information-acquisition module unless reallocation introduces an additional strategic interaction. That extra interaction is better isolated under H rather than F.

### G — KILL

Multiple information producers are not enough. The literature already studies multiple retailers with private signals and endogenous acquisition/sharing, as well as costly correlated signal acquisition in networks. The only potentially distinctive element found in G was heterogeneity in what the signals diagnose, which is exactly H; G is therefore not retained as a separate TOP candidate.

### H — PREFERRED

H changes the object from scalar information quantity to a posterior precision matrix generated by distinct diagnostic directions. The commercial network's composition can therefore change the quality of what can be learned even when total effort or total signal count does not fall. This is not reproducible by relabeling effort in Xu et al. (2022).

### I — KILL

Post-exit use is highly relevant institutionally but no longer plausibly new as a standalone theory object after Wang–Wang (2026), which explicitly separates cross-client reuse and post-exit continuity of a persistent learning asset.

### J — TOP 3 / runner-up

The option to preserve a node because it can generate future information is genuinely information-specific, and no exact vertical dealer-retention model was found in the inspected set. However, the architecture requires dynamic uncertainty, experimentation and an endogenous retention/stopping choice, and is exposed to a mature experimentation literature. It is materially less minimal than H.

## Ranking

1. **H — Diagnostic diversity under downstream concentration: 83/100 — PREFERRED**
2. **J — Retention for learning option value: 68/100 — TOP 3 / runner-up**

No third candidate is promoted. Selecting G together with H would amount to selecting two variants of the same information-aggregation family, contrary to the Stage 3 mechanism-diversity rule.