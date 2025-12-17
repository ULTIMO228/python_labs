from pathlib import Path
import json
import csv
from typing import List, Dict, Any


def check_file_found(path: str) -> Path:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return p


def load_json(path: str) -> List[Dict[str, Any]]:
    p = check_file_found(path)
    text = p.read_text(encoding="utf-8")
    if text.strip() == "":
        raise ValueError
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        raise ValueError
    if (
        not isinstance(data, list)
        or len(data) == 0
        or not all(isinstance(item, dict) for item in data)
    ):
        raise ValueError
    return data


def json_to_csv(json_path: str, csv_path: str) -> None:
    data = load_json(json_path)
    fieldnames = list(data[0].keys())
    csv_file = Path(csv_path)
    with csv_file.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in data:
            writer.writerow({k: row.get(k, "") for k in fieldnames})


def csv_to_json(csv_path: str, json_path: str) -> None:
    p = check_file_found(csv_path)
    with p.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError
        data = [dict(row) for row in reader]
    out = Path(json_path)
    with out.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    try:
        json_to_csv("data/people.json", "data/people.csv")
    except Exception as e:
        print("Ошибка:", e)
