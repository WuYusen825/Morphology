#!/usr/bin/env python3
"""Fig. 1 of the v10 paper in the form Morphology (Springer) asks for: odds ratios for H5 under the checks.

Same data and same values as Figure 1 of v9 (scripts/yisheng_v9_figure.py; nothing is recomputed, the numbers are read from
ext_coding/yisheng_models_ext_coding.csv, yisheng_models_ext_author_check.csv and yisheng_models_ext_second_answer.csv), redrawn
at the final size so that the lettering is 8 pt where it is printed:
  - 119 mm wide (the "small journal" column of Springer's artwork guidelines; at most 195 mm high), Arial-compatible
    Liberation Sans, all lettering 8 pt, no title or caption inside the figure, lines at least 0.5 pt, black and white
    with the groups told apart by marker shape and fill, not by colour;
  - three files named as Springer asks ("Fig1" and the extension): Fig1.eps (vector, fonts embedded), Fig1.tif (600 dpi,
    LZW, RGB) and Fig1.png (600 dpi, 2811 pixels wide, which is also above Snapp's minimum of 1500 x 1200 pixels; this is
    the file embedded in the Word manuscript).
Graphics program: Python 3 with matplotlib.

Run from anywhere:  python3 youwen/scripts/yisheng_v10_figure.py
Output: youwen/manuscript/submission/Fig1.png, Fig1.eps, Fig1.tif and youwen/manuscript/figures/fig1_h5_forest_values.csv
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.ticker import NullFormatter, NullLocator
import pandas as pd
from PIL import Image

YOUWEN = Path(__file__).resolve().parents[1]
EXT = YOUWEN / "ext_coding"
FIGS = YOUWEN / "manuscript" / "figures"
OUT = YOUWEN / "manuscript" / "submission"
FIGS.mkdir(parents=True, exist_ok=True)
OUT.mkdir(parents=True, exist_ok=True)

WIDTH_MM = 119
WIDTH_IN = WIDTH_MM / 25.4
FONT = 8
DPI = 600

families = {f.name for f in font_manager.fontManager.ttflist}
for fam in ("Arial", "Helvetica", "Liberation Sans"):
    if fam in families:
        break
else:
    raise SystemExit("no Arial-compatible font (Arial, Helvetica, Liberation Sans) is installed")
plt.rcParams.update({"font.family": fam, "font.size": FONT, "pdf.fonttype": 42, "ps.fonttype": 42,
                     "axes.linewidth": 0.6, "xtick.major.width": 0.6, "ytick.major.width": 0.6,
                     "xtick.major.size": 3, "ytick.major.size": 3})

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


# (label as printed, label in the values file, source row, estimate, marker kind)
#   kind: "pre" pre-specified test, "expl" exploratory (added after the results were seen),
#         "sens" sensitivity analysis with the authors' judgment, "mh" within-series estimate
SPEC = [
    ("All related pairs (main test)", "All related pairs (main test, H5)", pick(main, "P1 "), "gee", "pre"),
    ("Identity only", "Identity only", pick(main, "S1 "), "gee", "pre"),
    ("Paronomastic glosses removed", "Paronomastic glosses removed", pick(main, "S2 "), "gee", "pre"),
    ("Labels in both recensions", "Labels shared by both recensions", pick(main, "S3 "), "gee", "pre"),
    ("Second blind pass", "Second blind pass", pick(main, "S5 "), "gee", "pre"),
    ("Pairs where the passes agree", "Pairs on which the passes agree", pick(main, "S7 "), "gee", "pre"),
    ("Shared, no paronomastic gloss", "Shared labels, no paronomastic gloss", pick(main, "X3 "), "gee", "expl"),
    ("Pairs coded E only", "Pairs coded E only", pick(main, "X1 "), "gee", "expl"),
    ("Adjusted for Y against E", "Adjusted for Y against E", pick(main, "X2 "), "gee", "expl"),
    ("The 677 new items only", "The 677 new items only", pick(main, "X4 near"), "gee", "expl"),
    ("Second answers (two batches)", "Second answers used in two batches", pick(second, "P1 ", "second_b3_b6"), "gee", "expl"),
    ("Authors' judgment, 126 codes", "Authors' consolidated judgment, 126 codes", pick(auth, "P1 ", "author_adjudicated"), "gee", "sens"),
    ("Main test within series (MH)", "Main test within series (MH, 37 phonetics)", pick(main, "P1 "), "mh", "mh"),
]

records = []
for label, long_label, row, which, kind in SPEC:
    if which == "gee":
        est, (lo, hi) = float(row["gee_OR"]), ci(row["gee_CI95"])
    else:
        est, (lo, hi) = float(row["mh_OR"]), ci(row["mh_CI95"])
    records.append(dict(label=long_label, kind=kind, OR=est, lo=lo, hi=hi,
                        hits1=int(row["group1_hits"]), n1=int(row["group1_n"]),
                        hits0=int(row["group0_hits"]), n0=int(row["group0_n"])))
vals = pd.DataFrame(records)
vals.to_csv(FIGS / "fig1_h5_forest_values.csv", index=False)

# the values the paper quotes; stops the figure from drifting away from the text
EXPECT = {"All related pairs (main test, H5)": (2.35, 1.43, 3.86),
          "Authors' consolidated judgment, 126 codes": (2.73, 1.61, 4.65),
          "Main test within series (MH, 37 phonetics)": (2.01, 0.75, 5.39),
          "Second answers used in two batches": (2.39, 1.38, 4.14),
          "Shared labels, no paronomastic gloss": (1.80, 0.95, 3.42)}
for _, r in vals.iterrows():
    if r["label"] in EXPECT:
        assert (round(r["OR"], 2), round(r["lo"], 2), round(r["hi"], 2)) == EXPECT[r["label"]], r.to_dict()

MS = 4.6
style = {"pre": dict(marker="o", mfc="black", mec="black", ms=MS, mew=0.8),
         "expl": dict(marker="o", mfc="white", mec="black", ms=MS, mew=0.8),
         "sens": dict(marker="s", mfc="#555555", mec="#555555", ms=MS, mew=0.8),
         "mh": dict(marker="D", mfc="white", mec="black", ms=MS - 0.4, mew=0.8)}

HEIGHT_IN = 4.15
assert HEIGHT_IN * 25.4 <= 195
fig = plt.figure(figsize=(WIDTH_IN, HEIGHT_IN))
# axes box in figure fractions: room on the left for the row labels, on the right for the numbers
ax = fig.add_axes([0.375, 0.215, 0.405, 0.725])
n = len(vals)
for i, r in vals.iterrows():
    y = n - 1 - i
    st = style[r["kind"]]
    ax.plot([r["lo"], r["hi"]], [y, y], color=st["mec"], lw=1.0, solid_capstyle="butt", zorder=2)
    ax.plot([r["OR"]], [y], linestyle="none", zorder=3, **st)
    ax.text(10.5, y, f"{r['OR']:.2f} [{r['lo']:.2f}, {r['hi']:.2f}]", va="center", ha="left", fontsize=FONT,
            clip_on=False)
ax.axvline(1, color="black", lw=0.7, zorder=1)
ax.axvline(2, color="black", lw=0.7, ls=(0, (3, 2)), zorder=1)
ax.set_xscale("log")
ax.xaxis.set_minor_locator(NullLocator())
ax.xaxis.set_minor_formatter(NullFormatter())
ax.set_xlim(0.6, 9)
ax.set_xticks([1, 2, 4, 8])
ax.set_xticklabels(["1", "2", "4", "8"])
ax.set_yticks(range(n))
ax.set_yticklabels([s[0] for s in SPEC][::-1])
ax.set_xlabel("Odds ratio, labelled vs ordinary pairs (95% CI; log scale)")
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
ax.text(2.06, n - 0.4, "smallest effect\nof interest (2)", ha="left", va="bottom", linespacing=1.0)
ax.set_ylim(-0.7, n + 0.55)
fig.text(0.805, 0.215 + 0.725 * (n - 1 - (-0.7) + 0.0) / (n + 0.55 + 0.7) + 0.034, "OR [95% CI]", ha="left", va="bottom")
handles = [plt.Line2D([], [], linestyle="none", **style[k]) for k in ("pre", "expl", "sens", "mh")]
fig.legend(handles, ["pre-specified", "exploratory", "authors' judgment (sensitivity)", "within series (MH)"],
           loc="lower left", frameon=False, ncol=2, bbox_to_anchor=(0.02, 0.0), handletextpad=0.3,
           columnspacing=1.6, labelspacing=0.5, borderaxespad=0.2)

png = OUT / "Fig1.png"
fig.savefig(png, dpi=DPI, facecolor="white")
fig.savefig(OUT / "Fig1.eps", facecolor="white")
plt.close(fig)

im = Image.open(png).convert("RGB")
im.save(png, dpi=(DPI, DPI))
im.save(OUT / "Fig1.tif", dpi=(DPI, DPI), compression="tiff_lzw")
w, h = im.size
assert w >= 1500 and h >= 1200, (w, h)
print(f"wrote Fig1.png/.eps/.tif in {OUT}: {w} x {h} px at {DPI} dpi = {w / DPI * 25.4:.0f} x {h / DPI * 25.4:.0f} mm; font {fam} {FONT} pt")
print(vals.round(2).to_string(index=False))
