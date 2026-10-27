import sys
p = sys.argv[1]
s = open(p).read()

def sub(old, new):
    global s
    assert old in s, old[:70]
    s = s.replace(old, new)

start = s.index("\\begin{figure}[t]\n\\centering\n\\PENDING{Delay sweep")
end = s.index("\\label{fig:sweep}\n\\end{figure}") + len("\\label{fig:sweep}\n\\end{figure}")
s = s[:start] + r"""\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{figures/sweep.pdf}
\caption{Throughput against the added delay per verification (Gemma-3, the same 30 prompts at every delay). The best fixed window moves from Fixed-2 to Fixed-4 to Fixed-8 as the delay grows; \capes{} follows the upper envelope without being told the delay, and is faster than PEARL at every delay.}
\label{fig:sweep}
\end{figure}""" + s[end:]

sub(r"""\PENDING{Text from gemma3\_delay\_sweep (expected 19:00): where the best fixed window switches from Fixed-2 to Fixed-8, and how close \capes{} stays to the upper envelope at every delay.}""",
r"""Fig.~\ref{fig:sweep} extends the two fixed delays to six, from 2 to 200\,ms, on the Gemma-3 pair. No fixed window stays best: Fixed-2 wins at 2\,ms, Fixed-4 at 10 and 25\,ms and Fixed-8 from 50\,ms on. \capes{} follows this envelope with one configuration. It is within \E{s:low:S:sub} of the best fixed window at 2\,ms, matches it at 10\,ms (\E{s:d10:S}) and is faster from 25\,ms on: by \E{s:d25:S} at 25\,ms, \E{s:d50:S} \E{s:d50:S:ci} at 50\,ms, \E{s:high:S:sub} at 100\,ms and \E{s:d200:S} at 200\,ms. Its largest gains fall exactly where the best window changes, between 50 and 100\,ms: there \cape{} combines short fresh windows after misses with long lookahead after hits, which no single window can express. Over the four added delays, \capes{} also uses \E{s:pooled:S:g4:sv} \E{s:pooled:S:g4:svci} less energy per token than Fixed-4 and \E{s:pooled:S:g8:sv} less than Fixed-8.

PEARL, whose draft length is recalibrated for every delay, is slower than \capes{} at all six delays; at 25\,ms its calibrated length is too short and it falls \E{s:d25:pearl} behind the best fixed window. The lookahead cap of $\Gamma+1=9$ tokens is ample: at 200\,ms, where PEARL drafts 12 tokens per block, \capes{} is still the fastest method.""")

sub(r"""\PENDING{Ablation (gemma3\_ablation, Gemma-3, 30 prompts, low/high/dynamic; expected 21:00): Fixed-4 $\rightarrow$ adaptive lookahead only (fresh window fixed at 4) $\rightarrow$ full \capes{}; and median-only round-trip estimate vs.\ distributional estimate.}""",
r"""\begin{table}[t]
\centering
\caption{Ablation of \capes{} on Gemma-3 (30 prompts; 2\,ms, 100\,ms and dynamic pooled): change relative to Fixed-4 with 95\% prompt-cluster bootstrap intervals.}
\label{tab:ablation}
\footnotesize
\setlength{\tabcolsep}{3pt}
\begin{tabular}{@{}lll@{}}
\toprule
Variant & Throughput (\%) & J/token saving (\%)\\
\midrule
Adaptive lookahead only (fresh window 4) & $+5.8$ [3.8, 9.0] & $-1.7$ [$-$2.7, $-$0.2]\\
Full controller, median round trip & $+7.9$ [5.5, 10.7] & $+5.5$ [3.2, 7.9]\\
Full controller, distributional (\capes{}) & $+6.9$ [4.5, 9.9] & $+8.6$ [5.1, 11.5]\\
\bottomrule
\end{tabular}
\end{table}

Table~\ref{tab:ablation} isolates the components of \capes{} on the Gemma-3 pair, and each has a distinct job. \emph{Adaptive lookahead delivers the speed.} Keeping the fresh window at four tokens and letting only the lookahead follow the round trip already raises throughput by \E{a:fresh4:sp} \E{a:fresh4:spci} over Fixed-4, and by \E{a:fresh4:high:sp} at 100\,ms, where a complete-block lookahead leaves most of the round trip unused. \emph{The adaptive fresh window delivers the energy.} Choosing the fresh window as well keeps the speed (a further \E{a:fresh:sp}, within noise) and cuts J/token by another \E{a:fresh:sv} \E{a:fresh:svci}, and by \E{a:fresh:low:sv} at 2\,ms, where \cape{} drafts short blocks instead of speculating four tokens at a time. \emph{The distributional round-trip estimate prices jitter.} Compared with a median-only estimate, it runs at the same speed (within \E{a:dist:sp}) and lowers J/token by \E{a:dist:sv} \E{a:dist:svci}, and by \E{a:dist:high:sv} at 100\,ms: on a jittery path it stops buying lookahead that the shorter round trips cannot hide. The full controller is \E{a:full:sp} \E{a:full:spci} faster than Fixed-4 and \E{a:full:sv} \E{a:full:svci} more energy-efficient.""")

sub(r"""\item \textbf{PicoSpec}~\cite{picospec2026}: optimistic drafting of the next window during verification with early interruption on rejection, at the paper's default window of four tokens.""",
r"""\item \textbf{PicoSpec}~\cite{picospec2026}: optimistic drafting of the next window during verification with early interruption of background drafting on rejection, at the paper's default window of four tokens. Its fast pre-verification and probability compression require cloud changes or do not apply to greedy verification, and its truncation rule is not specified, so our implementation covers its edge-side pipeline. Under greedy drafting and verification, PicoSpec proposes and accepts exactly the tokens of Fixed-4 and differs from it only in timing, which makes it a clean measure of interruption.""")

sub(r"""Fig.~\ref{fig:controller} shows the decisions behind these results.""",
r"""Fig.~\ref{fig:controller} shows the decisions behind these results. They follow the text as well as the network: on Gemma-3, per-token acceptance ranges from \E{acc:gemmathree:mtbench} on MT-Bench to \E{acc:gemmathree:humaneval} on HumanEval, and \cape{} lengthens its windows where acceptance is high.""")

sub(r"""which explains its energy saving through Eq.~\eqref{eq:energy}.""",
r"""which explains its energy saving through Eq.~\eqref{eq:energy}. Short lookahead also limits waiting for background drafts that a rejection has made useless: at 2\,ms such waiting takes \E{wait:capes:low} of the wall time of \capes{}, against \E{wait:pico:low} for PicoSpec, which interrupts these drafts, and \E{wait:fixed4:low} for Fixed-4. Interruption is orthogonal to the choice of windows and composes with \cape{}.""")

open(p, 'w').write(s)
print('PENDING left:', s.count('PENDING'))
