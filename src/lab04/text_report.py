import argparse
import sys
from collections import Counter
from pathlib import Path
from src.lab03.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv


def frequencies_from_text(text: str) -> dict[str, int]:
    norm_text = normalize(text, True, True)
    tokens = tokenize(norm_text)
    return count_freq(tokens)


def main():
    parser = argparse.ArgumentParser(description="Генерация частотного отчета.")
    parser.add_argument('--in', dest='in_files', nargs='+', required=True, help="Входные файлы")
    parser.add_argument('--out', dest='out_file', default='data/lab04/report.csv', help="Выходной файл")
    parser.add_argument('--encoding', default='utf-8', help="Кодировка")
    parser.add_argument('--per-file', dest='per_file_report', help="Отчет по каждому файлу")
    parser.add_argument('--total', dest='total_report', help="Сводный отчет")
    args = parser.parse_args()

    if len(args.in_files) == 1:
        process_single_file(args.in_files[0], args.out_file, args.encoding)
    else:
        if not args.per_file_report or not args.total_report:
            print("Ошибка: укажите --per-file и --total", file=sys.stderr)
            sys.exit(1)
        process_multiple_files(args.in_files, args.per_file_report, args.total_report, args.encoding)


def process_single_file(in_path: str, out_path: str, encoding: str):
    try:
        text = read_text(in_path, encoding=encoding)
    except (FileNotFoundError, UnicodeDecodeError) as e:
        print(f"Ошибка чтения '{in_path}': {e}", file=sys.stderr)
        sys.exit(1)
    freq = frequencies_from_text(text)
    sorted_rows = top_n(freq, len(freq))
    write_csv(sorted_rows, out_path, header=("word", "count"))
    print(f"Отчет по файлу: {in_path}")
    print(f"Сохранен в: {out_path}")
    print("-" * 20)
    print(f"Всего слов: {sum(freq.values())}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5 слов:")
    top5 = top_n(freq, 5)
    if not top5:
        print("(пусто)")
    else:
        for word, count in top5:
            print(f"{word}: {count}")


def process_multiple_files(in_paths: list[str], per_file_path: str, total_path: str, encoding: str):
    total_freq = Counter()
    per_file_rows = []

    for path_str in in_paths:
        try:
            text = read_text(path_str, encoding=encoding)
            file_name = Path(path_str).name
            freq = frequencies_from_text(text)
            total_freq.update(freq)
            sorted_file_freq = top_n(freq, len(freq))
            for word, count in sorted_file_freq:
                per_file_rows.append((file_name, word, count))

        except Exception as e:
            print(f"Пропуск файла {path_str}: {e}", file=sys.stderr)
            continue

    per_file_rows.sort(key=lambda x: (x[0], -x[2], x[1]))
    write_csv(per_file_rows, per_file_path, header=("file", "word", "count"))
    print(f"Детальный отчет: {per_file_path}")
    sorted_total = top_n(dict(total_freq), len(total_freq))
    write_csv(sorted_total, total_path, header=("word", "count"))
    print(f"Сводный отчет: {total_path}")


if __name__ == '__main__':
    main()