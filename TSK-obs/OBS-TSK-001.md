SCRIPT — OBS-TSK-001 Update SOPs   (agent: ema)

INPUTS (from the ticket ASK):
  action        create | update
  path          note path relative to C:\VLT-SAI
  content-file  local file with the new note body

RUN:    python C:\RPO-SAI\SYS\PLA\WIN\FRA\FAI\ORG\RPO-NZT\WIK\RPO-app\RPO-obs\TSK-obs\vault_note.py --action {action} --path {path} --content-file {file}
VERIFY: exit 0 and a final line "RESULT: {action} {target} ({bytes})".
CLOSE:  dol_close_ticket note = the RESULT line → [RESOLVED]
ON FAIL: non-zero exit → leave open, paste the ERROR line. Exit 2 = create-over-existing or update-missing.
