fio_new = ""
flag1 = False
len_fio = 0
gpa = float
s = input().replace("(", "").replace(")", "").split(", ")
for i in s:
    if i == "":
        s.append("musor")
if len(s) == 3:
    fio_old = s[0].replace('''"''', "").split(" ")
    for i in fio_old:
        if i != "" and flag1 == False:
            fio_new += str(i.capitalize()) + " "
            len_fio += 1
            flag1 = True
        elif flag1 == True and i != "":
            fio_new += str(i.capitalize()[0]) + "."
            len_fio += 1
    group = s[1].replace('''"''', "")
    gpa = float(s[2])
    if 3 >= len_fio >= 2:
        print(f'''"{fio_new}, гр. {group}, GPA {gpa:.2f}"''')
    else:
        print("ValueError")
else:
    print("ValueError")
