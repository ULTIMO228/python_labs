fio = input("ФИО: ").split()
I = ""
for i in range(3):
    I += fio[i][0]
print(f"Инициалы: {I}.")
print(sum(len(i) for i in fio) + 2)
