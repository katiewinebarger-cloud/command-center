#!/usr/bin/env python3
"""Scan local files and generate history.json for the Command Center dashboard."""

import json
import os
import hashlib
from datetime import datetime
from pathlib import Path

COWORK_DIR = Path(__file__).parent.resolve()
HOME_DIR = Path.home()
OUTPUT_FILE = COWORK_DIR / "history.json"

EXCLUDE_NAMES = {
    ".DS_Store", ".git", ".claude", "node_modules", "__pycache__",
    "index.html", "dashboard.html", "TASKS.md", "scan_history.py",
    "history.json",
}

EXCLUDE_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico", ".webp",
    ".mp4", ".mov", ".mp3", ".wav",
    ".py", ".js", ".ts", ".json", ".md", ".html", ".css",
    ".sh", ".yml", ".yaml", ".toml", ".lock", ".log",
}

COACHING_KEYWORDS = [
    "self-assessment", "coaching", "leadership", "feedback", "360",
    "coaching trends", "development study",
]

def make_id(filepath):
    return hashlib.md5(str(filepath).encode()).hexdigest()[:8]

def format_size(size_bytes):
    if size_bytes >= 1_000_000:
        return f"{size_bytes / 1_000_000:.1f} MB"
    elif size_bytes >= 1_000:
        return f"{size_bytes / 1_000:.0f} KB"
    return f"{size_bytes} B"

def format_date(ts):
    dt = datetime.fromtimestamp(ts)
    return dt.strftime("%b %-d, %Y"), dt.strftime("%Y-%m-%d")

def infer_badge(name):
    lower = name.lower()
    if "draft" in lower or "vdraft" in lower:
        return "draft", "Draft"
    if "autosaved" in lower:
        return "final", "Final"
    return "final", "Final"

def classify(filepath):
    name_lower = filepath.name.lower()
    ext = filepath.suffix.lower()

    # Executive Coaching: keyword match on .docx or .pdf
    if ext in (".docx", ".pdf"):
        for kw in COACHING_KEYWORDS:
            if kw in name_lower:
                badge, label = ("final", "Complete") if ext == ".pdf" else infer_badge(filepath.name)
                if ext == ".docx" and "self-assessment" in name_lower:
                    badge, label = "final", "Complete"
                return "Executive Coaching", badge, label

    # Slides: .pptx files
    if ext == ".pptx":
        badge, label = infer_badge(filepath.name)
        return "Slides", badge, label

    # Spreadsheets
    if ext in (".xlsx", ".csv", ".tsv"):
        badge, label = infer_badge(filepath.name)
        return "Spreadsheets", badge, label

    # PDF (remaining)
    if ext == ".pdf":
        badge, label = infer_badge(filepath.name)
        return "PDF", badge, label

    # Company Intel (remaining .docx)
    if ext == ".docx":
        badge, label = infer_badge(filepath.name)
        return "Company Intel", badge, label

    return None, None, None

def make_preview(filepath, skill, file_size):
    name = filepath.stem
    ext = filepath.suffix.upper().lstrip(".")
    size_str = format_size(file_size)
    folder = filepath.parent.name or "home"
    return (
        f'<div class="line"><span class="highlight">{name}</span></div>'
        f'<div class="line">{ext} file &middot; {size_str}</div>'
        f'<div class="line">&nbsp;</div>'
        f'<div class="line"><span class="muted">Source: ~/{folder}/{filepath.name}</span></div>'
    )

def should_exclude(filepath):
    if filepath.name in EXCLUDE_NAMES:
        return True
    if filepath.name.startswith("."):
        return True
    if filepath.name.startswith("~$"):
        return True
    if filepath.suffix.lower() in EXCLUDE_EXTENSIONS:
        return True
    if any(kw in filepath.name.lower() for kw in ["logo", "sponsor"]):
        return True
    return False

def scan_files():
    found = []

    # Scan Cowork directory recursively
    for root, dirs, files in os.walk(COWORK_DIR):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in EXCLUDE_NAMES and not d.startswith(".")]
        for fname in files:
            fp = Path(root) / fname
            if not should_exclude(fp):
                found.append(fp)

    # Scan home directory top-level only
    for item in HOME_DIR.iterdir():
        if item.is_file() and not should_exclude(item):
            found.append(item)

    return found

def main():
    # Load existing history if present (preserve session entries)
    existing_session_entries = []
    existing_scan_paths = set()

    if OUTPUT_FILE.exists():
        with open(OUTPUT_FILE) as f:
            data = json.load(f)
            for entry in data.get("entries", []):
                if entry.get("source") == "session":
                    existing_session_entries.append(entry)
                elif entry.get("source") == "scan":
                    existing_scan_paths.add(entry.get("filePath", ""))

    # Scan for files
    files = scan_files()
    scan_entries = []

    for fp in files:
        skill, badge, badge_label = classify(fp)
        if skill is None:
            continue

        stat = fp.stat()
        date_display, date_iso = format_date(stat.st_mtime)
        size = stat.st_size

        # Build human-friendly name from filename
        name = fp.stem
        # Clean up common patterns
        name = name.replace("_", " ")
        # Don't mangle dashes in dates like "2026-03-28"
        # Just clean up leading numbering like "3. "
        if name and name[0].isdigit() and ". " in name[:4]:
            name = name[name.index(". ") + 2:]

        scan_entries.append({
            "id": make_id(fp),
            "skill": skill,
            "name": name,
            "date": date_display,
            "dateISO": date_iso,
            "meta": f"{format_size(size)} · .{fp.suffix.lstrip('.')}",
            "badge": badge,
            "badgeLabel": badge_label,
            "preview": make_preview(fp, skill, size),
            "source": "scan",
            "filePath": str(fp),
        })

    # Combine: scan entries + preserved session entries
    all_entries = scan_entries + existing_session_entries

    # Sort by date descending
    all_entries.sort(key=lambda e: e.get("dateISO", ""), reverse=True)

    # Write output
    output = {
        "version": 1,
        "lastScan": datetime.now().isoformat(),
        "entries": all_entries,
    }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2)

    # Summary
    skills = {}
    for e in all_entries:
        skills[e["skill"]] = skills.get(e["skill"], 0) + 1

    print(f"Scanned {len(files)} files, classified {len(scan_entries)} entries.")
    print(f"Preserved {len(existing_session_entries)} session entries.")
    print(f"Total: {len(all_entries)} entries in history.json")
    print(f"By skill: {json.dumps(skills, indent=2)}")

if __name__ == "__main__":
    main()
