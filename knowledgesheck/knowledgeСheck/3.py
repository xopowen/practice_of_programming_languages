
file = open('words.txt','r')
maks_len = ''
while True:
    # считываем строку
    line = file.readline()
    maks_len  =  maks_len if len(maks_len)>len(line) else line
    # прерываем цикл, если строка пустая
    if not line:
        print(maks_len)
        break


# закрываем файл
file.close