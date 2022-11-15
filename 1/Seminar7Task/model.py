import csv

info = ['Фамилия: ИВАНОВА', 'Имя и отчество: Елизавета Сергеевна', 'Номер телефона: 8 (495) 546-01-68', 'Комментарий: доб. 1331', '\n', 'Фамилия: РАСТОРГУЕВА', 'Имя и отчество: Дарья Юрьевна', 'Номер телефона: 8 (495) 546-01-68', 'Комментарий: доб. 1712',
        '\n', 'Фамилия: СПИРИДОНОВ', 'Имя и отчество: Олег Анатольевич', 'Номер телефона: 8 (495) 546-01-68', 'Комментарий: доб. 1972', '\n', 'Фамилия: ШЕРЕМЕТ', 'Имя и отчество: Эллина Константиновна', 'Номер телефона: 8 (495) 546-01-68', 'Комментарий: доб. 1872']


def importTxt():
    file1 = open("phonebook.txt", "r", encoding='utf-8')
    list = []
    while True:
        line = file1.readline()
        if not line:
            break

        list.append(line)
    print(list)

    file1.close


def importCsv():
    with open("phonebook.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=";")
        list = []
        for row in file_reader:
            list.append(row)
        print(list)


def exportTxt():
    MyFile = open('export.txt', 'w', encoding='utf-8')
    MyFile.writelines(info)
    MyFile.close()



def exportCsv():
    file = 'export.csv'
    with open(file, 'a', encoding='utf-8') as data:
        for i in info:
            if i != '\n':
                data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')


op_cod = "[IT IC ET EC]"
operations = {'IT': importTxt, 'IC': importCsv,
              'ET': exportTxt, 'EC': exportCsv}