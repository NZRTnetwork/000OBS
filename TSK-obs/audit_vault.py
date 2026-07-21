r"""
audit_vault.py — OBS-TSK-003. Lightweight SAI structure check of the VLT-SAI vault.

Heuristic aid, not authoritative: walks C:\VLT-SAI and flags folders that hold NO markdown
summary file (a SAI node should carry one lowercase summary .md). Writes a CSV report into
ema's Shared/Dolibarr_EDM folder. Read-only against the vault. Prints one RESULT: line.

Usage:
    python audit_vault.py

Excludes tooling dirs (.git, node_modules, .obsidian, __pycache__).
"""
import csv
import os
import sys
from datetime import date

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VAULT = r"C:\VLT-SAI"
SHARED_EDM = r"C:\VLT-SAI\SYS\PLA\WIN\FRA\FAI\ORG\VLT-nzt\OPS\VLT-agt\SHA\Dolibarr_EDM"
SKIP = {".git", "node_modules", ".obsidian", "__pycache__", ".pytest_cache", "SHA"}


def main():
    flagged = []
    scanned = 0
    for root, dirs, files in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d not in SKIP]
        scanned += 1
        mds = [f for f in files if f.lower().endswith(".md")]
        # a leaf-ish folder with subfolders is a container; only flag folders that have
        # files but no markdown summary at all
        if files and not mds:
            flagged.append(os.path.relpath(root, VAULT))

    out = os.path.join(SHARED_EDM, f"vault-audit-{date.today()}.csv")
    os.makedirs(SHARED_EDM, exist_ok=True)
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["folder_without_markdown_summary"])
        for rel in flagged:
            w.writerow([rel])

    if not os.path.isfile(out):
        print(f"ERROR: report not written: {out}")
        sys.exit(5)
    print(f"RESULT: folders_scanned={scanned} flagged={len(flagged)} file={out}")


if __name__ == "__main__":
    main()
