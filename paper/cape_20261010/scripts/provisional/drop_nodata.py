"""Remove every claim that has no data yet (PENDING boxes and undefined m:* keys)."""
import re

def edit(path, pairs, cut=()):
    s = open(path).read()
    for a, b in cut:
        i = s.index(a)
        j = s.index(b, i) + len(b)
        s = s[:i] + s[j:]
    for old, new in pairs:
        assert old in s, (path, old[:70])
        s = s.replace(old, new)
    open(path, 'w').write(s)

# --- background ---
edit('sections/background.tex', [
    ("\\section{Background and Measurement Study}", "\\section{Background}"),
    (" They span three model families, draft models from 270M to 2B parameters and draft speeds that differ by a factor of \\E{m:draftspeed:ratio}, which changes how expensive on-path drafting is relative to the round trip.",
     " They span three model families and draft models from 270M to 2B parameters."),
    (" This real path is fast but irregular: transport and HTTP overhead per request has a median of \\E{m:net:median}\\,ms, a 90th percentile of \\E{m:net:p90}\\,ms and a 99th percentile of \\E{m:net:p99}\\,ms, and exceeds 100\\,ms in \\E{m:net:over100} of rounds. To emulate wide-area round trips, the client injects an additional delay into every verification request on top of this real path (Section~\\ref{sec:eval}). The measurements in this section are taken from the synchronous and fixed-window requests of the main evaluation.",
     " This real path is fast but carries the jitter of both wireless links. To emulate wide-area round trips, the client injects an additional delay into every verification request on top of this real path (Section~\\ref{sec:eval})."),
], cut=[("\\begin{figure*}[t]\n\\centering\n\\PENDING{Regenerate figures/measurement", "\\subsection{Design implications}\n")])
edit('sections/background.tex', [
    ("The observations lead to four goals.",
     r"""\subsection{Where the cost of speculation falls}
Three properties of the edge--cloud loop shape our design. \emph{Fresh drafting is on the critical path:} the verifier cannot start before the last draft token of a round has arrived, so every token drafted after a verification returns delays the next one. \emph{Verification is priced per round:} a GPU target scores all draft positions of a round in one forward pass, so the cost of a draft token is paid on the device. \emph{Draft work has an energy price:} the board's energy per request is
\begin{equation}
E \approx P_0\, T + P_d\, B, \label{eq:energy}
\end{equation}
where $T$ is the request's wall time, $B$ the draft server's busy time, and $P_0$ and $P_d$ the base and draft-active power. Lookahead drafted during verification is free in $T$ but not in $B$, and a discarded block raises the energy bill without emitting a token.

These properties lead to four goals."""),
])

# --- introduction ---
edit('sections/introduction.tex', [
    (" Three observations shape our design (Section~\\ref{sec:measure}):", " The loop has a simple asymmetry (Section~\\ref{sec:measure}):"),
    (" It keeps strict greedy verification and requires no change to the cloud server, and it decides in about \\E{m:overhead:ms}\\,ms per round.",
     " It keeps strict greedy verification and requires no change to the cloud server."),
    ("\\item \\textbf{Measurement insight.} We show that speculative work in edge--cloud decoding is asymmetric: fresh drafting occupies the critical path, while drafting during verification is nearly free in time but not in energy. A board energy model ($R^2=\\E{m:energy:rsq}$) prices the difference (Section~\\ref{sec:measure}).",
     "\\item \\textbf{Cost asymmetry.} We identify that speculative work in edge--cloud decoding is asymmetric: fresh drafting occupies the critical path, while drafting during verification is nearly free in time but not in energy, and we price both with a board energy model of wall time and draft-busy time (Section~\\ref{sec:measure})."),
    ("Together, these observations suggest a simple principle. \\emph{Tokens", "\\emph{Tokens"),
], cut=[("\\begin{itemize}\n\\item \\textbf{Drafting sits", "\\end{itemize}\n")])

# --- design ---
edit('sections/design.tex', [
    (" In our evaluation, late-request estimates of $\\alpha_H$ average \\E{m:ctl:ahit}, against \\E{m:ctl:amiss} for $\\alpha_M$.", ""),
    (" These 64 candidates take about \\E{m:overhead:ms}\\,ms in Python on the Jetson CPU, a negligible share of a round.",
     " The 64 candidates are evaluated in closed form on the Jetson CPU, and this time is part of every measured wall time."),
])

# --- evaluation ---
edit('sections/evaluation.tex', [
    ("\\PENDING{Paired prompt-cluster bootstrap intervals (2,000 resamples) for all effects; current numbers are unpaired aggregates.}\n", ""),
    ("Fig.~\\ref{fig:tradeoff} places every method in the speed--energy plane.", "Table~\\ref{tab:dynamic} also places every method in the speed--energy plane."),
    (r"""Fig.~\ref{fig:controller} shows the decisions behind these results. They follow the text as well as the network: on Gemma-3, per-token acceptance ranges from \E{acc:gemmathree:mtbench} on MT-Bench to \E{acc:gemmathree:humaneval} on HumanEval, and \cape{} lengthens its windows where acceptance is high. \cape{} keeps the critical path short and sizes the lookahead to the round trip: its mean lookahead grows from \E{m:ctl:capes:low:h} tokens at 2\,ms to \E{m:ctl:capes:high:h} at 100\,ms, and \capee{}, which prices speculative work, grows it only from \E{m:ctl:capee:low:h} to \E{m:ctl:capee:high:h}. This behavior emerges from Eq.~\eqref{eq:objective} and the online estimates; no delay threshold is configured. The lookahead is also better used: \capee{} discards \E{m:capee:waste} draft tokens per 100 output tokens, against \E{m:fixed4:waste} for Fixed-4, which explains its energy saving through Eq.~\eqref{eq:energy}. Short lookahead""",
     r"""The text matters as much as the network: on Gemma-3, per-token acceptance ranges from \E{acc:gemmathree:mtbench} on MT-Bench to \E{acc:gemmathree:humaneval} on HumanEval, so no single window suits every workload, and \cape{} estimates acceptance online in each state. Short lookahead"""),
], cut=[("\\begin{figure*}[t]\n\\centering\n\\PENDING{New figures/tradeoff", "\\end{figure*}\n\n"),
        ("\\begin{figure}[t]\n\\centering\n\\PENDING{Regenerate figures/controller", "\\end{figure}\n\n"),
        ("\n\\subsection{Output fidelity and overhead}", "per round.")])

# --- discussion ---
edit('sections/discussion.tex', [
    ("The real Wi-Fi path already contributes heavy-tailed jitter, with \\E{m:net:over100} of rounds exceeding 100\\,ms of overhead, on top of the injected delays.",
     "The real Wi-Fi path already contributes jitter on top of the injected delays."),
])

left = []
for f in ['main.tex'] + ['sections/%s.tex' % n for n in
          ['abstract', 'introduction', 'background', 'design', 'implementation', 'evaluation', 'related', 'discussion', 'conclusion', 'appendix']]:
    t = open(f).read()
    left += [(f, m) for m in re.findall(r'\\E\{m:[^}]*\}|\\PENDING\{(?!#)', t)]
    left += [(f, m) for m in re.findall(r'\\ref\{(fig:measure|fig:tradeoff|fig:controller|sec:integrity)\}', t)]
print('left:', left)
