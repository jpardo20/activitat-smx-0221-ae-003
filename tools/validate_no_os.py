#!/usr/bin/env python3
'''Scan repository files and warn if Operating System strings are present.
This helps enforce the "sense SO" requirement.'''
import re, sys, os
BLACKLIST = [
    r"windows\s*11", r"windows\s*10", r"windows\s*7",
    r"\bubuntu\b", r"\bdebian\b", r"\bfedora\b", r"\barch\b",
    r"\bmac\s*os\b", r"\bmacos\b", r"\bos\s*X\b", r"\bios\b",
    r"\bsistema\s*operatiu\b", r"\boperating\s*system\b", r"\bso\b",
    r"\blinux\b"
]

KEY_PATTERNS = [
    # Windows product key 5x5 (very rough)
    r"[A-Z0-9]{5}(-[A-Z0-9]{5}){4}"
]

def scan_file(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            data = f.read()
    except Exception:
        return []
    warnings = []
    for pat in BLACKLIST:
        if re.search(pat, data, flags=re.I):
            warnings.append(f"[OS] Possibles referències d'SO a: {path} :: patró {pat}")
    for pat in KEY_PATTERNS:
        if re.search(pat, data, flags=re.I):
            warnings.append(f"[KEY] Patró semblant a clau de producte a: {path}")
    return warnings

def main(root='.'):
    warn = []
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if fn.lower().endswith((".md",".html",".txt",".json",".csv",".yml",".yaml",".ini",".cfg",".ps1",".sh",".js",".css",".py")):
                p = os.path.join(dirpath, fn)
                if "tools/validate_no_os.py" in p:
                    continue
                warn.extend(scan_file(p))
    if warn:
        print("⚠ ALERTES:\n" + "\n".join(warn))
        sys.exit(1)
    else:
        print("✔ Cap referència d'SO detectada.")
        sys.exit(0)

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv)>1 else ".")