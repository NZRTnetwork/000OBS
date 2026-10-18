r"""
obs-vlt-chk.py — OBS-TSK-003. Lightweight SAI structure check of the VLT-SAI vault.

Heuristic aid, not authoritative: walks C:\VLT-SAI and flags folders that hold NO markdown
summary file (a SAI node should carry one lowercase summary .md). Writes a CSV report to
%TEMP%\Dolibarr_EDM and, with --ticket-id, attaches it to that DOL ticket and deletes the local
copy. Read-only against the vault. Prints one RESULT: line.

Usage:
    python obs-vlt-chk.py --ticket-id 725

Excludes tooling dirs (.git, node_modules, .obsidian, __pycache__).
"""
import argparse
import csv
import os
import sys
import tempfile
from datetime import date

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, r"C:\RPO-SAI\SYS\PLA\WIN\FRA\FAI\ORG\RPO-NZT\OPS\RPO-agt")
try:
    from dotenv import load_dotenv
    load_dotenv(dotenv_path=r"C:\RPO-SAI\SYS\PLA\WIN\FRA\FAI\ORG\RPO-NZT\OPS\RPO-agt\.env")
except Exception:
    pass

from ITG.dol_ema import dol_attach_file

VAULT = r"C:\VLT-SAI"
SHARED_EDM = os.path.join(tempfile.gettempdir(), "Dolibarr_EDM")
SKIP = {".git", "node_modules", ".obsidian", "__pycache__", ".pytest_cache", "SHA"}


def main():
    ap = argparse.ArgumentParser(description="SAI vault structure check (OBS-TSK-003)")
    ap.add_argument("--ticket-id", type=int, help="DOL ticket id to attach the report to")
    args = ap.parse_args()

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

    where = f"file={out}"
    if args.ticket_id:
        key = os.environ.get("DOLIBARR_API_KEY") or os.environ.get("DOL_API_KEY")
        if not key:
            print("ERROR: DOLIBARR_API_KEY not set (shared .env)")
            sys.exit(3)
        res = dol_attach_file(key, "ticket", args.ticket_id, out)
        if res.get("status") != "ok":
            print(f"ERROR: attach to ticket {args.ticket_id} failed: {res.get('error')}")
            sys.exit(5)
        os.remove(out)
        where = f"file={os.path.basename(out)} ticket={args.ticket_id}"
    print(f"RESULT: folders_scanned={scanned} flagged={len(flagged)} {where}")


if __name__ == "__main__":
    main()
