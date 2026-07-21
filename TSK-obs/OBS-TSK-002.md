SCRIPT — OBS-TSK-002 Create wiki note   (agent: ema)

INPUTS (from the ticket ASK):
  path          new note path relative to C:\VLT-SAI
  title         note title
  tags          comma-separated ref-code tags (e.g. nzrt,000DOL)
  content-file  local file with the note body

RUN:    python C:\RPO-SAI\SYS\PLA\WIN\FRA\FAI\ORG\RPO-NZT\WIK\RPO-app\RPO-obs\TSK-obs\create_wiki_note.py --path {path} --title "{title}" --tags {tags} --content-file {file}
VERIFY: exit 0 and a final line "RESULT: created {target} tags=[...]".
CLOSE:  dol_close_ticket note = the RESULT line → [RESOLVED]
ON FAIL: non-zero exit → leave open, paste the ERROR line. Exit 2 = note already exists.
