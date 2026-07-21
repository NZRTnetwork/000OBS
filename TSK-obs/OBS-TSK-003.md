SCRIPT — OBS-TSK-003 Audit vault structure   (agent: ema)

INPUTS (from the ticket ASK): none.

RUN:    python C:\RPO-SAI\SYS\PLA\WIN\FRA\FAI\ORG\RPO-NZT\WIK\RPO-app\RPO-obs\TSK-obs\audit_vault.py
VERIFY: exit 0 and a final line "RESULT: folders_scanned=... flagged=... file=...".
CLOSE:  dol_close_ticket note = the RESULT line (report in Shared/Dolibarr_EDM) → [RESOLVED]
ON FAIL: non-zero exit → leave open, paste the ERROR line.
Note: heuristic aid — flags folders with files but no markdown summary; xc reviews the CSV.
