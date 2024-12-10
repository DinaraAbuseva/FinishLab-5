import re


file = "task2.html"


def search(text):
    ans = re.findall(r'\b(?:src|background)s*=s*[""]([^""]+.png)[""]', text)
    return ans


with open(file, "r", encoding = "utf-8") as open_file:
    text = open_file.read()
    ans = search(text)
    print(f"2) Ссылки на изображения:\n {ans}")

