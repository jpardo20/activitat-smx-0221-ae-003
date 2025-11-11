#!/usr/bin/env python3
'''Check for unfilled placeholders like {{...}} in templates or student files.'''
import os, re, sys

def has_placeholders(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            data = f.read()
    except Exception:
        return []
    issues = []
    if "{{" in data or "}}" in data:
        issues.append("Conté placeholders '{{...}}' sense omplir.")
    for token in ["OMPLEU", "PENDENT", "TODO"]:
        if re.search(rf"\b{token}\b", data, flags=re.I):
            issues.append(f"Conté marcador pendent: {token}")
    return issues

def main(root='.'):
    problems = []
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if fn.lower().endswith((".md",".html",".txt",".json",".csv",".ps1",".sh",".py")):
                p = os.path.join(dirpath, fn)
                if "tools/check_placeholders.py" in p:
                    continue
                issues = has_placeholders(p)
                if issues:
                    problems.append(f"{p}\n  - " + "\n  - ".join(issues))
    if problems:
        print("⚠ PLACEHOLDERS PENDENTS:\n" + "\n\n".join(problems))
        sys.exit(1)
    else:
        print("✔ No s'han detectat placeholders sense omplir.")
        sys.exit(0)

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv)>1 else ".")