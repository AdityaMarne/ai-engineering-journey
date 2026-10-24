"""Create this week's review: python scripts/new_week.py [YYYY-MM-DD]"""
import sys
from datetime import date

from _common import render, week_dir, week_number


def main() -> None:
    day = date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else date.today()
    week = week_number(day)
    path = week_dir(week) / "review.md"
    if path.exists():
        print(f"Already exists: {path}")
        return
    text = render("weekly-review.md", week=f"{week:02d}", date=day.isoformat())
    path.write_text(text, encoding="utf-8")
    print(f"Created {path}")


if __name__ == "__main__":
    main()
