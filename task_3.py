import re
import csv


file = "task3.txt"


def search(text):
    id = re.findall(r" \d+ ", text)
    surname = re.findall(r"\b[A-Z][a-zA-Z-]+\b", text)
    mail = re.findall(r"[\w'._+-]+@[\w'._+-]+", text)
    date = re.findall(r"\d{4}-\d\d-\d\d", text)
    url = re.findall(r"https?://[^s/$.?#].[^s]*", text)
    return id, surname, mail, date, url


keys = ["ID", "Surname", "E-mail", "Date", "Site"]


with open(file, "r", encoding = "utf-8") as text:
    text = text.read()
    id, surname, mail, date, site = search(text)

    new_text = zip(id, surname, mail, date, site)
    
    with open("Answer_task_3.csv", "w", newline = "", encoding = "utf-8") as ans:
        ans_file= csv.writer(ans)
        ans_file.writerow(["ID", "Surname", "E-mail", "Date", "Site"])
        ans_file.writerows(new_text)
