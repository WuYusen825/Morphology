#!/usr/bin/env python3
"""Counts quoted in the v9 paper that no result file prints directly.

Reads ext_coding/ext_codes_long.csv (one row per coded pair; code1 = pass 1 for the new items and
the original blind code for the 90 first-sample items in the frame, code2 = pass 2 likewise) and
ext_coding/ext_author_check_output.txt, prints each count with the place in the paper that cites
it, and stops with an AssertionError if a number in the paper would no longer match.

Run from anywhere:  python3 youwen/scripts/yisheng_v9_counts.py
"""
from pathlib import Path

import pandas as pd

EXT = Path(__file__).resolve().parents[1] / "ext_coding"
a = pd.read_csv(EXT / "ext_codes_long.csv", encoding="utf-8-sig")
ac = (EXT / "ext_author_check_output.txt").read_text(encoding="utf-8")


def check(label, got, want):
    print(f"{label}: {got}")
    assert got == want, (label, got, want)


# Table 2 and Section 3.4: the flow from coded pairs to the tests
lab, ordi = a[a.label == 1], a[a.label == 0]
check("coded pairs (labelled, ordinary, all)", (len(lab), len(ordi), len(a)), (212, 555, 767))
check("new items, first-sample items in the frame", (int((a.source == "extended").sum()),
                                                        int((a.source == "original_100").sum())), (677, 90))
check("labelled without an MC reading", int(lab.mc_relation.isna().sum()), 35)
check("labelled proper names with an MC reading", int(((lab.mc_relation.notna()) & (lab.code1 == "X")).sum()), 5)
check("ordinary proper names", int((ordi.code1 == "X").sum()), 93)
frame = a[(a.mc_relation.notna()) & (a.code1 != "X")]
check("pairs in the tests (labelled, ordinary)", (int((frame.label == 1).sum()), int((frame.label == 0).sum())), (172, 462))
check("phonetics in the tests", frame.phonetic.nunique(), 150)

# Section 4.3: disagreements between the two blind passes on the 677 new items
new = a[a.source == "extended"]
dis = new[new.code1 != new.code2].copy()
check("disagreements (all, labelled, ordinary)", (len(dis), int((dis.label == 1).sum()), int((dis.label == 0).sum())), (76, 33, 43))
check("share of the 677", round(100 * len(dis) / len(new), 1), 11.2)
dis["pair"] = ["/".join(sorted([x, y])) for x, y in zip(dis.code1, dis.code2)]
by = dis.groupby(["label", "pair"]).size()
check("labelled Y/E, E/N", (int(by[(1, "E/Y")]), int(by[(1, "E/N")])), (16, 15))
check("ordinary E/N, N/X", (int(by[(0, "E/N")]), int(by[(0, "N/X")])), (30, 10))
rel_n = dis[dis.pair.isin(["E/N", "N/Y"])].groupby("label").size()
check("related on one pass, N on the other (labelled, ordinary)", (int(rel_n[1]), int(rel_n[0])), (17, 31))
check("new items per group (labelled, ordinary)", (int((new.label == 1).sum()), int((new.label == 0).sum())), (177, 500))

# Section 4.3: the authors' check, as printed by the data thread's script
for needle in ["四类一致 45/50", "相关/不相关一致 47/50", "与第一次盲编相同 23，与第二次盲编相同 50，与两次都不同 3",
               "κ = 0.735 [0.603, 0.842]", "κ = 0.798 [0.666, 0.905]",
               "亦声对（45 条）： 不变 18，相关内 Y/E 之间 12，相关→不相关 10，不相关→相关 5",
               "普通对（81 条）： 不变 50，相关→不相关 13，不相关→相关 8"]:
    assert needle in ac, needle
print("author-check figures found in ext_author_check_output.txt")

# Table 3: the example pairs are items on which both passes agreed with confidence 3
ex = [("頃", "傾", "Y"), ("巽", "僎", "Y"), ("耳", "珥", "E"), ("米", "鬻", "E"), ("匡", "恇", "N"), ("亡", "良", "N"),
      ("善", "鄯", "X"), ("文", "汶", "X")]
for ph, ch, code in ex:
    r = a[(a.phonetic == ph) & (a.char == ch)]
    assert len(r) == 1 and r.iloc[0].code1 == r.iloc[0].code2 == code and r.iloc[0].conf1 == r.iloc[0].conf2 == 3, (ph, ch)
print("Table 3 examples: both passes agree with confidence 3")

# Table 9: relation types of the homophonous pairs, ordinary pairs restricted to the 172 phonetics of the frame
d = pd.read_csv(EXT.parent / "yisheng_dataset.csv", encoding="utf-8-sig")
d = d[d.in_analysis_set == True]  # noqa: E712
ph172 = set(d[d.relation == "亦聲"].phonetic)
hom = d[d.mc_relation == "identical"]
lab_t = hom[hom.relation == "亦聲"].identical_relation_type.value_counts().to_dict()
ord_t = hom[(hom.relation == "聲") & hom.phonetic.isin(ph172)].identical_relation_type.value_counts().to_dict()
check("homophonous labelled pairs by type", lab_t, {"F": 42, "L": 8, "C": 5, "U": 8})
check("homophonous ordinary pairs by type (172-phonetic frame)", ord_t, {"U": 73, "X": 42, "F": 15, "L": 3})
check("homophonous ordinary pairs (frame, all rows)", (sum(ord_t.values()), int((hom.relation == "聲").sum())), (133, 143))

# Section 4.4: what the ordinary rate would give among the 141 related labelled pairs
check("141 x 23/79", round(141 * 23 / 79), 41)
print("all v9 counts agree with the files")
