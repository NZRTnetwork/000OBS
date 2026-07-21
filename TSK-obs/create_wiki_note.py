r"""
create_wiki_note.py — OBS-TSK-002. Author a new wiki note with SAI frontmatter.

Builds the frontmatter block (tags, created date, type) the SAI conventions require, prepends
it to the body, and writes under C:\VLT-SAI. Refuses to overwrite. Self-verifies; prints one
RESULT: line. Exit 0 ok / 2 bad args / non-zero fail.

Usage:
    python create_wiki_note.py --path SYS\...\WIK\VLT-app\newthing.md \
        --title "New Thing" --tags nzrt,000DOL --content-file body.md
"""
import argparse
import os
import sys
from datetime import date

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VAULT = r"C:\VLT-SAI"


def fail(msg, code=1):
    print(f"ERROR: {msg}")
    sys.exit(code)


def main():
    ap = argparse.ArgumentParser(description="Create a SAI wiki note (OBS-TSK-002)")
    ap.add_argument("--path", required=True, help="path relative to C:\\VLT-SAI")
    ap.add_argument("--title", required=True)
    ap.add_argument("--tags", default="nzrt", help="comma-separated ref-code tags")
    ap.add_argument("--content-file", required=True)
    args = ap.parse_args()

    if not os.path.isfile(args.content_file):
        fail(f"content file not found: {args.content_file}", 2)
    target = os.path.join(VAULT, args.path)
    if not os.path.abspath(target).startswith(os.path.abspath(VAULT)):
        fail("path escapes the vault root", 2)
    if os.path.isfile(target):
        fail(f"already exists (use vault_note.py --action update): {target}", 2)

    tags = [t.strip() for t in args.tags.split(",") if t.strip()]
    body = open(args.content_file, encoding="utf-8").read()
    frontmatter = (
        "---\n"
        f"tags: [{', '.join(tags)}]\n"
        "aliases: []\n"
        f"created: {date.today()}\n"
        "status: active\n"
        "type: note\n"
        "---\n\n"
        f"# {args.title}\n\n"
    )
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(frontmatter + body)

    if not os.path.isfile(target):
        fail(f"write did not land: {target}", 5)
    print(f"RESULT: created {target} tags={tags}")


if __name__ == "__main__":
    main()
