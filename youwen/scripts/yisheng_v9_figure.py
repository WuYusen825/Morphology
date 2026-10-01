#!/usr/bin/env python3
"""Figure 1 of the v9 paper: odds ratios for H5 (sound among related pairs) under the checks.

Reads the result files of the enlarged blind coding (nothing is recomputed here: yisheng_models_ext_coding.csv,
yisheng_models_ext_author_check.csv, yisheng_models_ext_second_answer.csv) and draws a forest plot: the label's odds ratio for "identical or departing-tone" among pairs coded related,
with 95% confidence intervals, for the main test and for the checks reported in Table 8 of the
paper. The dashed line at OR = 2 is the smallest effect of interest fixed in
ext_coding/analysis_plan.md before the enlarged coding.

Run from anywhere:  python3 youwen/scripts/yisheng_v9_figure.py
Output: youwen/manuscript/figures/fig1_h5_forest.png (300 dpi) and fig1_h5_forest_values.csv
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter, NullLocator
import pandas as pd

YOUWEN = Path(__file__).resolve().parents[1]
EXT = YOUWEN / "ext_coding"
OUT = YOUWEN / "manuscript" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

main = pd.read_csv(EXT / "yisheng_models_ext_coding.csv", encoding="utf-8-sig")
auth = pd.read_csv(EXT / "yisheng_models_ext_author_check.csv", encoding="utf-8-sig")
second = pd.read_csv(EXT / "yisheng_models_ext_second_answer.csv", encoding="utf-8-sig")


def pick(df, prefix, tier=None):
    rows = df[df["test"].str.startswith(prefix)]
    if tier is not None:
        rows = rows[rows["tier"] == tier]
    assert len(rows) == 1, (prefix, tier, len(rows))
    return rows.iloc[0]


def ci(text):
    lo, hi = str(text).split("-")
    return float(lo), float(hi)


# (label, source row, column set, marker kind)
#   kind: "pre" pre-specified test, "expl" exploratory (added after the results were seen),
#         "sens" sensitivity analysis with the authors' judgment, "mh" within-series estimate
SPEC = [
    ("All related pairs (main test, H5)", pick(main, "P1 "), "gee", "pre"),
    ("Identity only", pick(main, "S1 "), "gee", "pre"),
    ("Paronomastic glosses removed", pick(main, "S2 "), "gee", "pre"),
    ("Labels shared by both recensions", pick(main, "S3 "), "gee", "pre"),
    ("Second blind pass", pick(main, "S5 "), "gee", "pre"),
    ("Pairs on which the passes agree", pick(main, "S7 "), "gee", "pre"),
    ("Shared labels, no paronomastic gloss", pick(main, "X3 "), "gee", "expl"),
    ("Pairs coded E only", pick(main, "X1 "), "gee", "expl"),
    ("Adjusted for Y against E", pick(main, "X2 "), "gee", "expl"),
    ("The 677 new items only", pick(main, "X4 near"), "gee", "expl"),
    ("Second answers used in two batches", pick(second, "P1 ", "second_b3_b6"), "gee", "expl"),
    ("Authors' consolidated judgment, 126 codes", pick(auth, "P1 ", "author_adjudicated"), "gee", "sens"),
    ("Main test within series (MH, 37 phonetics)", pick(main, "P1 "), "mh", "mh"),
]

records = []
for label, row, which, kind in SPEC:
    if which == "gee":
        est, (lo, hi) = float(row["gee_OR"]), ci(row["gee_CI95"])
    else:
        est, (lo, hi) = float(row["mh_OR"]), ci(row["mh_CI95"])
    records.append(dict(label=label, kind=kind, OR=est, lo=lo, hi=hi,
                        hits1=int(row["group1_hits"]), n1=int(row["group1_n"]),
                        hits0=int(row["group0_hits"]), n0=int(row["group0_n"])))
vals = pd.DataFrame(records)
vals.to_csv(OUT / "fig1_h5_forest_values.csv", index=False)

# the values the paper quotes; stops the figure from drifting away from the text
EXPECT = {"All related pairs (main test, H5)": (2.35, 1.43, 3.86),
          "Authors' consolidated judgment, 126 codes": (2.73, 1.61, 4.65),
          "Main test within series (MH, 37 phonetics)": (2.01, 0.75, 5.39),
          "Second answers used in two batches": (2.39, 1.38, 4.14),
          "Shared labels, no paronomastic gloss": (1.80, 0.95, 3.42)}
for _, r in vals.iterrows():
    if r["label"] in EXPECT:
        assert (round(r["OR"], 2), round(r["lo"], 2), round(r["hi"], 2)) == EXPECT[r["label"]], r.to_dict()

style = {"pre": dict(marker="o", mfc="black", mec="black", ms=6),
         "expl": dict(marker="o", mfc="white", mec="black", ms=6),
         "sens": dict(marker="s", mfc="gray", mec="gray", ms=6),
         "mh": dict(marker="D", mfc="white", mec="black", ms=6)}

fig, ax = plt.subplots(figsize=(6.6, 5.2))
n = len(vals)
for i, r in vals.iterrows():
    y = n - 1 - i
    st = style[r["kind"]]
    color = st["mec"]
    ax.plot([r["lo"], r["hi"]], [y, y], color=color, lw=1.4, solid_capstyle="butt")
    ax.plot([r["OR"]], [y], linestyle="none", **st)
    ax.text(9.6, y, f"{r['OR']:.2f} [{r['lo']:.2f}, {r['hi']:.2f}]", va="center", ha="left", fontsize=7.5)
ax.axvline(1, color="black", lw=0.8)
ax.axvline(2, color="black", lw=0.8, ls="--")
ax.set_xscale("log")
ax.xaxis.set_minor_locator(NullLocator())
ax.xaxis.set_minor_formatter(NullFormatter())
ax.set_xlim(0.6, 9)
ax.set_xticks([0.75, 1, 2, 3, 4, 6, 8])
ax.set_xticklabels(["0.75", "1", "2", "3", "4", "6", "8"], fontsize=8)
ax.set_yticks(range(n))
ax.set_yticklabels(list(vals["label"])[::-1], fontsize=8)
ax.set_xlabel("Odds ratio, labelled vs ordinary pairs (95% CI; log scale)", fontsize=8.5)
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
ax.text(2.04, n - 0.35, "smallest effect\nof interest (2)", fontsize=7, ha="left", va="bottom")
ax.set_ylim(-0.7, n + 0.35)
handles = [plt.Line2D([], [], linestyle="none", **style[k]) for k in ("pre", "expl", "sens", "mh")]
ax.legend(handles, ["pre-specified", "exploratory", "authors' consolidated\njudgment (sensitivity)", "within series (MH)"],
          loc="upper center", fontsize=7, frameon=False, ncol=4, bbox_to_anchor=(0.45, -0.17), handletextpad=0.3,
          columnspacing=1.2)
fig.tight_layout()
fig.subplots_adjust(right=0.80)
path = OUT / "fig1_h5_forest.png"
fig.savefig(path, dpi=300)
print("wrote", path)
print(vals.round(2).to_string(index=False))
