"""Shared helpers for the log scripts."""
from datetime import date
from pathlib import Path

JOURNEY_START = date(2026, 10, 26)  # Monday of Week 1, edit if you start later
ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "docs" / "templates"
LOGS = ROOT / "logs"


def week_number(day: date) -> int:
    return (day - JOURNEY_START).days // 7 + 1


def day_number(day: date) -> int:
    return (day - JOURNEY_START).days + 1


def week_dir(week: int) -> Path:
    path = LOGS / f"week-{week:02d}"
    path.mkdir(parents=True, exist_ok=True)
    return path


def render(template_name: str, **values: object) -> str:
    text = (TEMPLATES / template_name).read_text(encoding="utf-8")
    for key, value in values.items():
        text = text.replace("{" + key + "}", str(value))
    return text
