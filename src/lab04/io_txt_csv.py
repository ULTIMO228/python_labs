import csv
from pathlib import Path
from typing import Iterable, Sequence

def ensure_parent_dir(path: str | Path) -> None:
    p = Path(path)
    if p.parent != Path('.'):
        p.parent.mkdir(parents=True, exist_ok=True)

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    return p.read_text(encoding=encoding)

def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    ensure_parent_dir(path)
    rows = list(rows)
    if rows:
        first_row_len = len(rows[0])
        if not all(len(r) == first_row_len for r in rows):
            raise ValueError("Все строки должны иметь одинаковую длину")
    p = Path(path)
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)
