"""Create today's daily log: python scripts/new_day.py [YYYY-MM-DD]"""
import sys
from datetime import date

from _common import JOURNEY_START, day_number, render, week_dir, week_number


def main() -> None:
    day = date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else date.today()
    if day < JOURNEY_START:
        sys.exit(f"{day} is before the journey start ({JOURNEY_START}).")
    week = week_number(day)
    path = week_dir(week) / f"{day.isoformat()}.md"
    if path.exists():
        print(f"Already exists: {path}")
        return
    path.write_text(
        render("daily-log.md", date=day.isoformat(), week=week, day_number=day_number(day)),
        encoding="utf-8",
    )
    print(f"Created {path}")


if __name__ == "__main__":
    main()
