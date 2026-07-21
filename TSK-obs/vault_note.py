r"""
vault_note.py — OBS-TSK-001. Create or revise a note/SOP in the VLT-SAI vault.

Writes UTF-8 markdown to a path under C:\VLT-SAI. 'create' refuses to overwrite; 'update'
requires the file to already exist. Self-verifies the file on disk; prints one RESULT: line.
Exit 0 ok / 2 bad args / non-zero fail.

Usage:
    python vault_note.py --action update --path SYS\...\win.md --content-file new.md
    python vault_note.py --action create --path SYS\...\newnote.md --content-file body.md
"""
import argparse
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VAULT = r"C:\VLT-SAI"


def fail(msg, code=1):
    print(f"ERROR: {msg}")
    sys.exit(code)


def main():
    ap = argparse.ArgumentParser(description="Write a VLT-SAI vault note (OBS-TSK-001)")
    ap.add_argument("--action", required=True, choices=["create", "update"])
    ap.add_argument("--path", required=True, help="path relative to C:\\VLT-SAI")
    ap.add_argument("--content-file", required=True)
    args = ap.parse_args()

    if not os.path.isfile(args.content_file):
        fail(f"content file not found: {args.content_file}", 2)
    target = os.path.join(VAULT, args.path)
    if not os.path.abspath(target).startswith(os.path.abspath(VAULT)):
        fail("path escapes the vault root", 2)

    exists = os.path.isfile(target)
    if args.action == "create" and exists:
        fail(f"already exists (use --action update): {target}", 2)
    if args.action == "update" and not exists:
        fail(f"does not exist (use --action create): {target}", 2)

    body = open(args.content_file, encoding="utf-8").read()
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(body)

    if not os.path.isfile(target) or os.path.getsize(target) == 0:
        fail(f"write did not land: {target}", 5)
    print(f"RESULT: {args.action} {target} ({os.path.getsize(target)} bytes)")


if __name__ == "__main__":
    main()
