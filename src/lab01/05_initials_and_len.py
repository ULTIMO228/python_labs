fio = input("ФИО: ").split()
I = ''
for i in range(3):
    I += fio[i][0]
print(f"Инициалы: {I}.")
print(sum(len(i)+2 for i in fio))
