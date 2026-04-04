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




# ИЛИ
"""
temps = [-5, -3, 2, 8, 14, 18, 22, 20, 15, 9, 2, -2]

print(f"Min: {min(temps)}, Max: {max(temps)}")

seasons = {'Зима': [11,0,1], 'Весна': [2,3,4], 'Лето': [5,6,7], 'Осень': [8,9,10]}

for season, idx in seasons.items():
    print(f"{season}: {', '.join(map(str, [temps[i] for i in idx]))}")
"""
