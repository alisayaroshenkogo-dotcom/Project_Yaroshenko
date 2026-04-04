# Даны средние значения температур за каждый месяц в году. 
# Найти минимальное и максимальное значения температур за год. 
# Вывести значения температур по временам года.

temperatures = [-5, -3, 2, 33, 16, 22, 25, 23, 17, 9, 3, -2]

print("Минимальная температура за год:", min(temperatures))
print("Максимальная температура за год:", max(temperatures))

print("Зима:", [temperatures[11], temperatures[0], temperatures[1]])
print("Весна:", temperatures[2:5])
print("Лето:", temperatures[5:8])
print("Осень:", temperatures[8:11])
