#Составить генератор (yield), который преобразует все буквенные символы в заглавные

def to_upper(text):
    for ch in text:
        yield ch.upper()

text = input("Введите текст для изменения: ")

for i in to_upper(text):
    print(i, end="")
