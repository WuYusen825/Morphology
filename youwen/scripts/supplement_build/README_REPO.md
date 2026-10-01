# Repository copy of the supplement build folder

This folder is a copy of `v7_work/supplement_build/` of the shared project folder (made by the data thread, 2026-10-01) and
holds the sources and scripts that built the seven Online Resources in `youwen/manuscript/submission/supplement/`. It is
internal: do not upload it, and do not put it into an anonymised data copy (`package_check.py` contains the patterns of the
names it looks for). `README.md` here says in which order to rebuild.

The scripts were written for the shared folder: `esm_common.py` and the other scripts point at paths under
`/mnt/project-files/youwen/` and at the data thread's scratch folder, so a rebuild outside that environment needs those paths
changed first. The seven files in `submission/supplement/` are the result and are what the audit
(`youwen/scripts/yisheng_submission_audit.py v10 --rerun-esm7`) checks. The files here are unchanged from the shared copy.
