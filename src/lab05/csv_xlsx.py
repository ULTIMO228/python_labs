import csv
from pathlib import Path
import openpyxl.utils
from openpyxl import Workbook


def csv2xlsx(csv_path: str, xlsx_path: str):
    p = Path(csv_path)
    if not p.exists():
        raise FileNotFoundError
    with p.open("r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
        if len(rows) == 0 or len((rows[0])) == 0:
            raise ValueError

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    for row in rows:
        ws.append(row)
    num_cols = len(rows[0])
    cols_w = [0] * num_cols
    for row in rows:
        for i, cell in enumerate(row):
            cols_w[i] = max(cols_w[i], len((str(cell))))
    for i, width in enumerate(cols_w, start=1):
        ws.column_dimensions[openpyxl.utils.get_column_letter(i)].width = max(8, width)
    wb.save(xlsx_path)


if __name__ == "__main__":
    try:
        csv2xlsx("data/people.csv", "data/people.xlsx")
    except Exception as e:
        print(f"Ошибка: {e}")
