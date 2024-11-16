import json
import matplotlib.pyplot as plt

# Завантаження даних з JSON-файлу
with open("teams.json", "r") as file:
    teams = json.load(file)

# Підготовка даних для кругової діаграми
team_names = [team["Name"] for team in teams]
team_points = [team["Points"] for team in teams]

# Побудова кругової діаграми
plt.figure(figsize=(10, 10))
plt.pie(team_points, labels=team_names, autopct='%1.1f%%', colors=plt.cm.Paired.colors)
plt.title('Розподіл очок серед футбольних команд', fontsize=16)

# Відображення діаграми
plt.show()
