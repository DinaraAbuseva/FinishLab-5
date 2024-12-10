import re


EN = "task1-en.txt"
RU = "task1-ru.txt"


def for_en(en):
    ans_1_ne = re.findall(r"\b[0-9]\b", en)
    ans_1_we = re.findall(r"(([a-zA-Zа-яА-ЯёЁ]+\d+)|(\d+[a-zA-Zа-яА-ЯёЁ]+)[a-zA-Zа-яА-ЯёЁ\d]*)", en)
    return ans_1_ne, ans_1_we


def for_ru(ru):
    ans_1_nr = re.findall(r"\b[0-9]\b", ru)
    ans_1_wr = re.findall(r"(([a-zA-Zа]+\d+)|(\d+[a-zA-Zа-яА-ЯёЁ]+)[a-zA-Zа-яА-ЯёЁ\d]*)", ru)
    return ans_1_nr, ans_1_wr


print("Вариант 6:")


with open(EN, "r", encoding = 'utf-8') as file_en, open(RU, "r", encoding = 'utf-8') as file_ru:
    en = file_en.read()
    ru = file_ru.read()
    ans_1_nr, ans_1_wr = for_ru(ru)
    ans_1_ne, ans_1_we = for_en(en)
    print(
        "1) Для файла 'task1-ru.txt':\nчисла:\n"
          f"{ans_1_nr}\n"
          "сочетания:\n "
          f"{ans_1_wr}\n "
          "Для файла 'task1-en.txt':\nчисла:\n"
          f"{ans_1_ne}\n"
          "сочетания:\n"
          f"{ans_1_we}"
          )


