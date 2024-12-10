import re

file = "task_add.txt"

def search(text):
    date = re.findall(r"\d{4}-\d\d-\d\d", text)
    date_1 = re.findall(r"\d\d.\d\d.\d{4}", text)
    date_2 = re.findall(r"\d{4}/\d\d/\d\d", text)

    for num in date_1:
        date.append(num)
    for num in date_2:
        date.append(num)

    mail = re.findall(r" [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+[.][a-zA-Z]{2,}", text)
    url = re.findall(r" https?://[^s/$.?#].[^0-9%{]*", text)
    return date, mail, url

with open(file, "r", encoding = "utf-8") as open_file:
    text = open_file.read()
    date, mail, url = search(text)
    print(f"Даты: {date}\n Адреса эл. почт: {mail}\n Ссылки: {url}")