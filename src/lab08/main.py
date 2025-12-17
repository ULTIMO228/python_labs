from pathlib import Path

from models import Student
from serialize import students_from_json, students_to_json


def main():
    students = [
        Student(
            fio="Пак Вячеслав Хз",
            birthdate="2007-10-12",
            group="BIVT-25-4",
            gpa=0.01,
        ),
        Student(
            fio="Алексеев Всеволод Сергеевич",
            birthdate="2007-05-26",
            group="BIVT-25-4",
            gpa=5.0,
        ),
        Student(
            fio="Муфазалов Эрик Мансурович",
            birthdate="2007-08-28",
            group="BIVT-25-4",
            gpa=4.7,
        ),
        Student(
            fio="Любимов Сашенька Ювелир",
            birthdate="2007-08-28",
            group="BIVT-25-4",
            gpa=2.0,
        )
    ]

    json_path = Path("data/students.json")

    students_to_json(students, json_path)
    print(f"→ JSON сохранён в {json_path}")

    loaded_students = students_from_json(json_path)
    print("→ Загружено студентов:", len(loaded_students))

    print("\nСтуденты из JSON")
    for s in loaded_students:
        print(s)
        print()


if __name__ == "__main__":
    main()