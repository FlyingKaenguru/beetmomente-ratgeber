#!/usr/bin/env python3
"""Prüft index.json und alle Beiträge (Regeln siehe README.md).

    python3 scripts/check.py
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAX_MINUTES = 3
WORDS_PER_MINUTE = 200
MAX_BYTES = 256 * 1024
MAX_ARTICLES = 50
FILE_PATTERN = re.compile(r"^[a-z0-9-]+\.md$")
FOOTER = "\n---\n"


def body_of(text: str) -> str:
    """Text ohne den Hinweis „Alle Angaben ohne Gewähr“ am Ende."""
    return text.rsplit(FOOTER, 1)[0]


def check_article(entry: dict) -> list[str]:
    errors = []
    name = entry.get("id", "?")
    for field in ("id", "title", "summary", "file", "updated"):
        if not entry.get(field):
            errors.append(f"{name}: Feld „{field}“ fehlt")
    file = entry.get("file", "")
    if not FILE_PATTERN.match(file):
        errors.append(f"{name}: ungültiger Dateiname „{file}“")
        return errors
    try:
        date.fromisoformat(entry.get("updated", ""))
    except ValueError:
        errors.append(f"{name}: „updated“ ist kein Datum JJJJ-MM-TT")
    path = ROOT / file
    if not path.exists():
        return errors + [f"{name}: Datei {file} fehlt"]
    if path.stat().st_size > MAX_BYTES:
        errors.append(f"{name}: größer als 256 KB")
    text = path.read_text(encoding="utf-8")
    if FOOTER not in text or "Alle Angaben ohne Gewähr" not in text:
        errors.append(f"{name}: Hinweis „Alle Angaben ohne Gewähr“ fehlt")
    body = body_of(text)
    if body.startswith("# "):
        errors.append(f"{name}: keine Überschrift erster Ebene, den Titel zeigt die App")
    if re.search(r"[!–—-]", body):
        errors.append(f"{name}: Ausrufezeichen, Binde- oder Gedankenstrich im Text")
    words = len(body.split())
    minutes = max(1, round(words / WORDS_PER_MINUTE))
    if minutes > MAX_MINUTES:
        errors.append(
            f"{name}: {words} Wörter, etwa {minutes} Minuten; "
            f"höchstens {MAX_MINUTES} Minuten"
        )
    if entry.get("reading_minutes") != minutes:
        errors.append(
            f"{name}: reading_minutes {entry.get('reading_minutes')}, "
            f"passend wären {minutes} ({words} Wörter)"
        )
    for month in entry.get("months", []):
        if not 1 <= month <= 12:
            errors.append(f"{name}: Monat {month} ungültig")
    return errors


def main() -> int:
    index = json.loads((ROOT / "index.json").read_text(encoding="utf-8"))
    articles = index.get("articles", [])
    errors = []
    if index.get("schema_version") != 1:
        errors.append("schema_version muss 1 sein")
    if len(articles) > MAX_ARTICLES:
        errors.append(f"mehr als {MAX_ARTICLES} Beiträge")
    ids = [a.get("id") for a in articles]
    if len(ids) != len(set(ids)):
        errors.append("doppelte id")
    for entry in articles:
        errors.extend(check_article(entry))
    listed = {a.get("file") for a in articles}
    for path in ROOT.glob("*.md"):
        if path.name not in listed and path.name != "README.md":
            errors.append(f"{path.name}: nicht in index.json eingetragen")
    for error in errors:
        print(f"Fehler: {error}")
    print(f"{len(articles)} Beiträge geprüft, {len(errors)} Fehler")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
